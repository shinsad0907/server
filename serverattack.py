import asyncio
import websockets

clients = set()  # Set để lưu trữ tất cả các client kết nối

async def handler(websocket, path):
    print("📡 Client connected!")
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"📩 Received: {message}")
            # Gửi lại cho tất cả các client khác
            for client in clients:
                if client != websocket:
                    await client.send(f"🛠️ Server: {message}")
            await websocket.send(f"🛠️ Server: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("❌ Client disconnected!")
    finally:
        clients.remove(websocket)

start_server = websockets.serve(handler, "0.0.0.0", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
