import asyncio
import websockets

async def handler(websocket, path):
    print("📡 Client connected!")
    try:
        async for message in websocket:
            print(f"📩 Received: {message}")
            await websocket.send(f"🛠️ Server: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("❌ Client disconnected!")

async def main():
    start_server = websockets.serve(handler, "0.0.0.0", 5000)
    await start_server
    print("Server started on port 5000.")
    await asyncio.Future()  # Keep the server running

# Sử dụng asyncio.run() để bắt đầu vòng lặp sự kiện
if __name__ == "__main__":
    asyncio.run(main())
