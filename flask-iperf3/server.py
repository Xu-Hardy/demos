import os
import iperf3

# 确保 libiperf 可以被找到
os.environ["DYLD_LIBRARY_PATH"] = "/opt/homebrew/lib:" + os.environ.get("DYLD_LIBRARY_PATH", "")

def start_iperf_server(port=5201):
    """最基础的 iPerf3 服务器"""
    server = iperf3.Server()
    server.port = port  # 监听端口

    print(f"🚀 iPerf3 服务器已启动，监听端口: {port}")

    try:
        while True:
            result = server.run()

            if result.error:
                print(f"⚠️ 错误: {result.error}")
            else:
                print(f"✅ 测试完成: {result}")
    except KeyboardInterrupt:
        print("\n❌ 服务器已停止")

if __name__ == "__main__":
    start_iperf_server(port=5201)  # 监听默认 5201 端口
