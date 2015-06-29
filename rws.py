#!/usr/env/python3

import argparse
import asyncio
import websockets

import argparse

parser = argparse.ArgumentParser(
    description='rws: ripple websocket test.',
)

parser.add_argument(
    '--port', '-p',
    default=8765,
    type=int,
    help='Websocket port.',
)

parser.add_argument(
    '--address', '-a',
    default='localhost',
    type=str,
    help='Websocket server address.',
)

parser.add_argument(
    '--secure', '-s',
    action='store_true',
    help='Use secure websockets.')

parser.add_argument(
    '--server',
    action='store_true',
    help='Act as a websocket server.')

ARGS = parser.parse_args()

PROTOCOL = 'wss' if ARGS.secure else 'ws'
ADDRESS = '%s://%s:%d/' % (PROTOCOL, ARGS.address, ARGS.port)

def server():
    @asyncio.coroutine
    def coroutine(websocket, path):
        name = yield from websocket.recv()
        print("< {}".format(name))
        greeting = "Hello {}!".format(name)
        yield from websocket.send(greeting)
        print("> {}".format(greeting))

    start_server = websockets.serve(coroutine, ARGS.address, ARGS.port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

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
    if ARGS.server:
        server()
    else:
        client()
