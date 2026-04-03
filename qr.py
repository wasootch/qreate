#!/usr/bin/env python3
import sys
import qrcode


def main():
    if len(sys.argv) < 2:
        print("Usage: qr <text>", file=sys.stderr)
        sys.exit(1)

    qr = qrcode.QRCode()
    qr.add_data(" ".join(sys.argv[1:]))
    qr.make()
    qr.print_ascii(invert=True)


if __name__ == "__main__":
    main()
