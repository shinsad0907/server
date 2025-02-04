import asyncio
import websockets
import logging

# Cấu hình logging để ghi nhận lỗi
logging.basicConfig(level=logging.DEBUG)

async def handler(websocket, path):
    logging.info("📡 Client connected!")
    try:
        while True:
            # Lắng nghe tin nhắn từ client
            message = await websocket.recv()
            logging.info(f"📩 Received: {message}")
            
            # Gửi phản hồi lại cho client
            await websocket.send(f"🛠️ Server received: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        logging.error(f"❌ Connection closed: {e}")
    except Exception as e:
        logging.error(f"❌ Unexpected error: {e}")

async def main():
    # Chạy WebSocket server trên địa chỉ và cổng cụ thể
    start_server = websockets.serve(handler, "0.0.0.0", 8080)
    await start_server
    logging.info("Server started on port 5000.")
    await asyncio.Future()  # Giữ server chạy mãi

if __name__ == "__main__":
    asyncio.run(main())
