#!/bin/bash

if [[ "$1" == "-s" ]]; then
    echo "🚀 以生产模式启动 iPerf3 服务器 API (Gunicorn) 端口 5201..."
    export GUNICORN_PORT=5201
    python server.py
elif [[ "$1" == "-c" ]]; then
    echo "🚀 以生产模式启动 Flask Web UI (Gunicorn) 端口 5200..."
    export GUNICORN_PORT=5200
    gunicorn -c gunicorn_config.py app:app
else
    echo "❌ 参数错误！请使用 -s（启动 iPerf3 服务器）或 -c（启动 Flask 客户端）"
    exit 1
fi
