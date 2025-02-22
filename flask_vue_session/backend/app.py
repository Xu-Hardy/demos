from flask import Flask, redirect, request, session, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置一个安全的密钥
CORS(app, supports_credentials=True)  # 允许跨域请求

# GitHub OAuth 配置
GITHUB_CLIENT_ID = 'xxxx'  # 替换为你的 GitHub Client ID
GITHUB_CLIENT_SECRET = 'xxxxx'  # 替换为你的 GitHub Client Secret
GITHUB_REDIRECT_URI = 'http://localhost:8000/auth/github/callback'

# GitHub OAuth URLs
GITHUB_AUTH_URL = 'https://github.com/login/oauth/authorize'
GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_USER_URL = 'https://api.github.com/user'

@app.route('/')
def index():
    return "Flask backend is running!"

@app.route('/login')
def login():
    # 重定向用户到 GitHub 进行授权
    return redirect(f'{GITHUB_AUTH_URL}?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_REDIRECT_URI}')

@app.route('/auth/github/callback')
def github_callback():
    # 获取授权码
    code = request.args.get('code')
    if not code:
        return 'Error: No code provided', 400

    # 使用授权码获取 access_token
    data = {
        'client_id': GITHUB_CLIENT_ID,
        'client_secret': GITHUB_CLIENT_SECRET,
        'code': code,
        'redirect_uri': GITHUB_REDIRECT_URI
    }
    headers = {'Accept': 'application/json'}
    response = requests.post(GITHUB_TOKEN_URL, data=data, headers=headers)
    token_json = response.json()
    access_token = token_json.get('access_token')

    if not access_token:
        return 'Error: Failed to obtain access token', 400

    # 使用 access_token 获取用户信息
    headers = {'Authorization': f'token {access_token}', 'Accept': 'application/json'}
    user_response = requests.get(GITHUB_USER_URL, headers=headers)
    user_json = user_response.json()

    # 获取用户的邮箱（需要额外请求）
    email_response = requests.get('https://api.github.com/user/emails', headers=headers)
    print(f"Email Response Status Code: {email_response.status_code}")
    print(f"Email Response Content: {email_response.text}")

    if email_response.status_code == 200:
        email_json = email_response.json()
        print(f"Email JSON: {email_json}")  # 打印邮箱数据
        primary_email = next((email['email'] for email in email_json if email['primary']), None)
    else:
        print(f"Failed to fetch emails: {email_response.text}")
        primary_email = None

    # 保存用户信息和 token 到 session
    session['github_token'] = access_token
    session['github_user'] = {
        'username': user_json.get('login'),
        'avatar_url': user_json.get('avatar_url'),
        'name': user_json.get('name'),
        'email': primary_email
    }

    # 重定向到前端页面
    return redirect('http://localhost:5173')
@app.route('/api/check_login')
def check_login():
    # 检查用户是否已登录
    if 'github_token' in session:
        return jsonify({
            'logged_in': True,
            'user': session['github_user']
        })
    return jsonify({'logged_in': False})

@app.route('/logout')
def logout():
    # 清除 session
    session.pop('github_token', None)
    session.pop('github_user', None)
    return jsonify({'status': 'logged out'})

if __name__ == '__main__':
    app.run(port=8000, debug=True)