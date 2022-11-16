# @Time    : 2022-11-16 20:50
# @Author  : Peisong Li
# @FileName: Websocket_server.py

import asyncio
from websockets import serve


async def echo(websocket, path):
    name = await websocket.recv()
    print(f"{name}")

    greeting = f"Hello {name}!"
    await websocket.send(greeting)
    print(f" {greeting}")


async def main():
    async with serve(echo, "0.0.0.0", 4001):
        await asyncio.Future()  # run forever


asyncio.run(main())