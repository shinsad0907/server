# server.py
import os
import asyncio
import websockets

async def handler(websocket, path):
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
    # Lấy cổng từ Railway hoặc mặc định là 5000
    port = int(os.environ.get("PORT", 5000))
    start_server = websockets.serve(handler, "0.0.0.0", port)
    await start_server
    print(f"Server started on port {port}.")
    await asyncio.Future()  # Giữ server chạy mãi

# Khởi động vòng lặp sự kiện
if __name__ == "__main__":
    asyncio.run(main())
