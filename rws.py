#!/usr/bin/env python3

import asyncio
import websockets

from rws_args import parse_args

ARGS = parse_args('rws: ripple websocket test.')
PROTOCOL = 'wss' if ARGS.secure else 'ws'
ADDRESS = '%s://%s:%d/' % (PROTOCOL, ARGS.address, ARGS.port)

def client():
    @asyncio.coroutine
    def coroutine():
        websocket = yield from websockets.connect(ADDRESS)
        name = input("What's your name? ")
        yield from websocket.send(name)
        print("> {}".format(name))
        greeting = yield from websocket.recv()
        print("< {}".format(greeting))

    asyncio.get_event_loop().run_until_complete(coroutine())

if __name__ == '__main__':
    client()
