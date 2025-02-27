# flask-iperf3

## 🚀 简介
`flask-iperf3` 是一个基于 Flask 和 iPerf3 的网络测速应用，使用 Gunicorn 作为 WSGI 服务器，并支持 Docker 部署。项目包含：
- **iPerf3 服务器 API（5201 端口）**：用于处理网络测速请求
- **Flask Web UI（5200 端口）**：提供前端界面，可视化测速
- **Docker 容器化**：支持轻量级 `python:3.12-slim` 镜像

## 📁 目录结构
```
flask-iperf3/
│── static/              # 前端静态文件
│── templates/           # HTML 模板文件
│   └── index.html       # 主界面
│── app.py               # Flask Web UI (Gunicorn 端口 5200)
│── server.py            # iPerf3 服务器 API (Gunicorn 端口 5201)
│── Dockerfile           # Docker 构建文件
│── entrypoint.sh        # 启动脚本 (控制 -s / -c 逻辑)
│── requirements.txt     # Python 依赖
│── gunicorn_config.py   # Gunicorn 配置 (可选)
```

## 📦 依赖安装
### 1️⃣ 本地运行
```sh
pip install -r requirements.txt
```

### 2️⃣ 使用 Docker
```sh
docker build -t flask-iperf3 .
```

## 🔥 运行方式
### **🎯 启动 iPerf3 服务器（端口 5201）**
```sh
# 使用 Flask API 服务器
docker run -p 5201:5201 flask-iperf3 -s

# 或者使用原生 iPerf3 服务器
iperf3  -s
```

### **🎯 启动 Flask Web UI（端口 5200）**
```sh
docker run -p 5200:5200 flask-iperf3 -c
```

## ⚙️ 配置
### **Gunicorn 生产模式**
如果需要更详细的 Gunicorn 配置，可以修改 `gunicorn_config.py`：
```python
bind = "0.0.0.0:5200"  # 监听所有 IP
workers = 4  # 4 个 worker 进程
threads = 2  # 每个 worker 2 个线程
timeout = 120  # 超时时间
loglevel = "info"  # 日志级别
```

## 🛠️ 开发调试
### **手动启动 Flask（开发模式）**
```sh
python server.py  # 启动 iPerf3 服务器 (5201)
python app.py     # 启动 Flask UI (5200)
```

## 🎯 适用场景
- **内部网络测速**：在数据中心、公司局域网中测试吞吐量
- **自动化测试**：集成 iPerf3 到 API 测试环境
- **可视化网络状态**：提供直观的 Web UI 进行测速

## 📜 许可证
MIT License

