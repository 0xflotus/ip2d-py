from ipy2d import *
from ip2dpy import __version__
import argparse


def main():
    parser = argparse.ArgumentParser(description="Convert some IPs to integers")
    parser.add_argument(
        "-v", action="version", version=f"{__version__}", help="IP to convert"
    )
    parser.add_argument("ip", help="IP to convert")
    parser.add_argument("-i", action="store_true", help="Integer to convert")
    parser.add_argument("--hex", action="store_true", help="IPv6 Mode")
    parser.add_argument("-c", action="store_true", help="Compress IPv6 addresses")
    parser.add_argument(
        "-o", type=str, required=False, help="Output format: (b)in, (o)ct or (h)ex"
    )
    parser.add_argument("-P", action="store_true", help="Output format without prefix")
    args = parser.parse_args()

    try:
        if args.hex:
            if args.i and args.c:
                try:
                    print(to_6(int(args.ip), compressed=True))
                except ValueError:
                    try:
                        print(to_6(int(args.ip, 0x10), compressed=True))
                    except ValueError:
                        print(to_6(int(args.ip, 0o10), compressed=True))
            elif args.i:
                try:
                    print(to_6(int(args.ip)))
                except ValueError:
                    try:
                        print(to_6(int(args.ip, 0x10)))
                    except ValueError:
                        print(to_6(int(args.ip, 0o10)))
            else:
                output = from_6(args.ip)
                if args.o in ["o", "oct"]:
                    output = (
                        oct(from_6(args.ip))
                        if not args.P
                        else oct(from_6(args.ip))[0x02:]
                    )
                elif args.o in ["h", "x", "hex"]:
                    output = (
                        hex(from_6(args.ip))
                        if not args.P
                        else hex(from_6(args.ip))[0x02:]
                    )
                elif args.o in ["b", "bin"]:
                    output = (
                        bin(from_6(args.ip))
                        if not args.P
                        else bin(from_6(args.ip))[0x02:]
                    )
                print(output)
        else:
            if args.i:
                try:
                    print(to_4(int(args.ip)))
                except ValueError:
                    try:
                        print(to_4(int(args.ip, 0x10)))
                    except ValueError:
                        print(to_4(int(args.ip, 0o10)))
            else:
                output = from_4(args.ip)
                if args.o in ["o", "oct"]:
                    output = (
                        oct(from_4(args.ip))
                        if not args.P
                        else oct(from_4(args.ip))[0x02:]
                    )
                elif args.o in ["h", "x", "hex"]:
                    output = (
                        hex(from_4(args.ip))
                        if not args.P
                        else hex(from_4(args.ip))[0x02:]
                    )
                elif args.o in ["b", "bin"]:
                    output = (
                        bin(from_4(args.ip))
                        if not args.P
                        else bin(from_4(args.ip))[0x02:]
                    )
                print(output)
    except IndexError:
        parser.print_help()


if __name__ == "__main__":
    main()
