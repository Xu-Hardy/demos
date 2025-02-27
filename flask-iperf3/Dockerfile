# 使用更小的 Python 3.12 Slim 版本
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖 & iperf3
RUN apt-get update && apt-get install -y --no-install-recommends \
    iperf3 \
    && rm -rf /var/lib/apt/lists/*

# 复制代码到容器
COPY . .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 赋予 entrypoint.sh 执行权限
RUN chmod +x /app/entrypoint.sh

# 暴露端口（Flask 5200, 服务器 API 5201）
EXPOSE 5200 5201

# 入口脚本，控制启动 server.py 或 app.py
ENTRYPOINT ["/app/entrypoint.sh"]


