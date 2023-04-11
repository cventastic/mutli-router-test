#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, '0.0.0.0', 420):
        await asyncio.Future()  # run forever

asyncio.run(main())
