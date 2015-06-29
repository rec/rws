#!/usr/bin/env python3

# Requires https://pypi.python.org/pypi/websockets

import asyncio
import json
import websockets

from rws_args import parse_args

ARGS = parse_args('rws: ripple websocket test.')
PROTOCOL = 'wss' if ARGS.secure else 'ws'
ADDRESS = '%s://%s:%d/' % (PROTOCOL, ARGS.address, ARGS.port)

COMMANDS = {
    'quit': lambda: True,
}

KEYS = sorted(COMMANDS.keys())
PROMPT = 'Choose command from ' + ', '.join(KEYS)

def execute_one_input(prompt=''):
    prompt = prompt or PROMPT

    while True:
        data = input(prompt + ': ').strip().split()
        if data:
            try:
                command = COMMANDS.get(data[0])
                if not command:
                    raise ValueError('Don\'t understand command ' + data[0])
                return command(*data[1:])
            except Exception as e:
                print('ERROR:', e)


def client():
    @asyncio.coroutine
    def coroutine():
        websocket = yield from websockets.connect(ADDRESS)
        name = input('')
        yield from websocket.send(name)
        print("> {}".format(name))
        greeting = yield from websocket.recv()
        print("< {}".format(greeting))

    asyncio.get_event_loop().run_until_complete(coroutine())

if __name__ == '__main__':
    client()
