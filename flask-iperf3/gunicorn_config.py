import os

# 获取环境变量 GUNICORN_PORT，默认为 5200
PORT = os.getenv("GUNICORN_PORT", "5200")

# 绑定到 0.0.0.0 并监听指定端口
bind = f"0.0.0.0:{PORT}"

# 进程 & 线程配置（适用于生产环境）
workers = 4  # 4 个 worker 进程
threads = 2  # 每个 worker 2 个线程
timeout = 120  # 120 秒超时，适用于长时间测速
keepalive = 5  # 连接保持 5 秒，提升并发性能

# 日志设置
loglevel = "info"  # 日志级别
accesslog = "-"  # 访问日志输出到控制台
errorlog = "-"  # 错误日志输出到控制台

# 预加载应用，提高性能（可选）
preload_app = True
