import argparse

def parse_args(desc):
    parser = argparse.ArgumentParser(description=desc)
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

    return parser.parse_args()
