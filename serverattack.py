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

async def start_server():
    server = await websockets.serve(handler, "0.0.0.0", 5000)
    await server.wait_closed()

# Thay vì sử dụng `asyncio.get_event_loop()`, hãy dùng `asyncio.run()`
asyncio.run(start_server())
