import argparse

import config
from config import log_error, log_debug
from commander import Commander


parser = argparse.ArgumentParser(
    prog = "Commander",
    description = "Cli tool to keep track of common comands",
)

parser.add_argument("-c", "--config", default=config.PATH)
parser.add_argument("-o", "--out", default=config.PATH)
parser.add_argument("-a", "--add", nargs="+")
parser.add_argument("-d", "--delete")

args = parser.parse_args()
print(args)

# Namespace(add=None, config='config/config.json', delete=None, out=None)
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

print(len(args.add))

