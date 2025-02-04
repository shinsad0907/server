import asyncio
import websockets

async def handler(websocket, path):
    print("📡 Client connected!")
    try:
        while True:
            message = await websocket.recv()
            print(f"📩 Received: {message}")
            await websocket.send(f"🛠️ Server received: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"❌ Client disconnected: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

async def main():
    try:
        start_server = websockets.serve(handler, "0.0.0.0", 8080)
        await start_server
        print("Server started on port 8080.")
        await asyncio.Future()  # Giữ server chạy mãi
    except Exception as e:
        print(f"❌ Server failed to start: {e}")

if __name__ == "__main__":
    asyncio.run(main())
