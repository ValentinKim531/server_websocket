import asyncio
import websockets
import json


async def send_message():
    async with websockets.connect("ws://localhost:8000") as websocket:
        message = {
            "input": "hello"
        }
        await websocket.send(json.dumps(message))
        print(f"Sent message: {message}")

        response = await websocket.recv()
        print(f"Received response: {response}")

if __name__ == "__main__":
    asyncio.run(send_message())
