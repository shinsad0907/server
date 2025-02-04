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
    # Chạy server WebSocket trên Railway URL
    start_server = websockets.serve(handler, "0.0.0.0", 5000)
    await start_server
    print("Server started on port 5000.")
    await asyncio.Future()  # Giữ server chạy mãi

# Khởi động vòng lặp sự kiện
if __name__ == "__main__":
    asyncio.run(main())
