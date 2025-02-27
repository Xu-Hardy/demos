# import os
#
# # 直接设置 DYLD_LIBRARY_PATH
# os.environ["DYLD_LIBRARY_PATH"] = "/opt/homebrew/lib:" + os.environ.get("DYLD_LIBRARY_PATH", "")
#
# import iperf3
# from flask import Flask, render_template, request, jsonify
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/test_speed', methods=['POST'])
# def test_speed():
#     server_host = request.form.get('server_host', '127.0.0.1')
#     duration = int(request.form.get('duration', 10))
#     protocol = request.form.get('protocol', 'tcp')
#
#     client = iperf3.Client()
#     client.server_hostname = server_host
#     client.duration = duration
#     client.protocol = protocol
#
#     result = client.run()
#
#     if result.error:
#         return jsonify({'error': result.error})
#
#     return jsonify({
#         'sent_mbps': result.sent_Mbps,
#         'received_mbps': result.received_Mbps,
#         'sent_bytes': result.sent_bytes,
#         'received_bytes': result.received_bytes
#     })
#
# if __name__ == '__main__':
#     app.run(debug=True)
import os

# 直接设置 DYLD_LIBRARY_PATH
os.environ["DYLD_LIBRARY_PATH"] = "/opt/homebrew/lib:" + os.environ.get("DYLD_LIBRARY_PATH", "")

import iperf3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def format_bytes(size):
    """将字节转换为人类可读格式"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_speed', methods=['POST'])
def test_speed():
    server_host = request.form.get('server_host', '127.0.0.1')
    duration = int(request.form.get('duration', 10))
    protocol = request.form.get('protocol', 'tcp')

    client = iperf3.Client()
    client.server_hostname = server_host
    client.duration = duration
    client.protocol = protocol

    result = client.run()

    if result.error:
        return jsonify({'error': result.error})

    return jsonify({
        'sent_mbps': f"{result.sent_Mbps:.2f} Mbps",
        'received_mbps': f"{result.received_Mbps:.2f} Mbps",
        'sent_bytes': format_bytes(result.sent_bytes),
        'received_bytes': format_bytes(result.received_bytes)
    })

if __name__ == '__main__':
    app.run(debug=True)
