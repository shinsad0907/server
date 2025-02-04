import asyncio
import websockets
import logging

# Cấu hình log chi tiết để theo dõi lỗi
logging.basicConfig(level=logging.DEBUG)

async def handler(websocket, path):
    """Xử lý kết nối WebSocket và gửi/nhận dữ liệu"""
    print("📡 Client connected!")
    try:
        while True:
            # Lắng nghe tin nhắn từ client
            message = await websocket.recv()
            print(f"📩 Received: {message}")

            # Gửi phản hồi lại cho client
            await websocket.send(f"🛠️ Server received: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("❌ Client disconnected!")

async def main():
    """Chạy server WebSocket"""
    uri = "wss://web-production-fa2d.up.railway.app/"  # Địa chỉ WebSocket của bạn trên Railway
    port = 8080  # Railway thường sử dụng cổng này, nhưng có thể thay đổi
    start_server = websockets.serve(handler, "0.0.0.0", port)
    
    # Khởi động server
    await start_server
    print(f"Server started on wss://your-app-name.up.railway.app:{port}")
    await asyncio.Future()  # Giữ server chạy mãi

# Khởi động vòng lặp sự kiện
if __name__ == "__main__":
    asyncio.run(main())
