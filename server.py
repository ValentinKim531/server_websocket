import asyncio
import websockets
import json

async def handle_connection(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        data = json.loads(message)
        response = {
            "response": f"Hello from server, you said: {data['input']}"
        }
        await websocket.send(json.dumps(response))

async def main():
    server = await websockets.serve(handle_connection, "0.0.0.0", 8000)
    print("Server started on ws://localhost:8000")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
