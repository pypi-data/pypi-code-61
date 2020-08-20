import io

ASCII = b'.' * 32 + bytes(range(32, 127)) + b'.' * 129


def dump(data, n=16, base=0):
    data = bytes(data)
    res = io.StringIO()
    for i in range(0, len(data), n):
        row = data[i : i + n].hex() + '  ' * n
        left = ' '.join(row[k : k + 2] for k in range(0, n, 2))
        right = ' '.join(row[k : k + 2] for k in range(n, n * 2, 2))
        text = data[i : i + 16].translate(ASCII).decode()
        res.write(f'{base + i:016x} | {left} | {right} | {text}\n')
    return res.getvalue()


def memprint(data, n=16, base=0, file=None):
    print(dump(data, n, base), file=file)


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser('memdump')
    parser.add_argument('--address', type=lambda x: int(x, 0), default=0)
    parser.add_argument('--offset', type=lambda x: int(x, 0), default=0)
    parser.add_argument('--size', type=lambda x: int(x, 0), default=None)
    parser.add_argument('filename')
    args = parser.parse_args()

    fd = sys.stdin.buffer if args.filename == '-' else open(args.filename, 'rb')

    with fd:
        if args.offset:
            fd.seek(args.offset)
        data = fd.read(args.size)
        memprint(data, base=args.address)
