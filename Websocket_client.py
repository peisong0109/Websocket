# @Time    : 2022-11-16 20:50
# @Author  : Peisong Li
# @FileName: Websocket_client.py

from websockets import connect
import asyncio



async def hello(uri):
    async with connect(uri) as websocket:
        name = 'Test'

        await websocket.send(name)
        print(f" {name}")

        greeting = await websocket.recv()
        print(f" {greeting}")

asyncio.run(hello("ws://82.156.79.199:4001"))