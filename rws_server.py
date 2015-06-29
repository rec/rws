#!/usr/bin/env python3

import asyncio
import websockets

from rws_args import parse_args

ARGS = parse_args('rws: websocket test server.')

def server():
    @asyncio.coroutine
    def coroutine(websocket, path):
        name = yield from websocket.recv()
        print("< {}".format(name))
        greeting = "Hello {}!".format(name)
        yield from websocket.send(greeting)
        print("> {}".format(greeting))

    print('Starting server %s:%s' % (ARGS.address, ARGS.port))
    start_server = websockets.serve(coroutine, ARGS.address, ARGS.port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    server()
