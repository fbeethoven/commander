import argparse

from .config import config, log_error, log_debug
from .commander import Commander  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser(
        prog = "Commander",
        description = "Cli tool to keep track of common comands",
    )

    parser.add_argument("-c", "--config", default=config.PATH)
    parser.add_argument("-o", "--out", default=config.PATH)
    parser.add_argument("-a", "--add", nargs="+")
    parser.add_argument("-d", "--delete")
    parser.add_argument("key", nargs="?")

    args = parser.parse_args()

    if args.config == None:
        log_error(
            "Cannot find config file. To set config file run commander -c <path-to-config>"
        )

    if args.out == None:
        log_error(
            "Cannot find output path. Run 'commander -o <path-to-output>"
        )

    com = Commander(args.config, args.out)

    if args.out != config.PATH:
        com.add_command("load", args.out)
    else:
        args.out = com.get_command("load")

    if args.key:
        com.handle_command(args.key)

    elif args.add and len(args.add) >= 2:
        com.add_command(args.add[0], args.add[1:])

    elif args.delete:
        com.delete_command(args.delete)


if __name__ == "__main__":
    main()

