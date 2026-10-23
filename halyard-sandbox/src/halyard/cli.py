"""Halyard command-line interface."""

import argparse

from halyard.config import DEFAULTS


def build_parser():
    parser = argparse.ArgumentParser(prog="halyard")
    sub = parser.add_subparsers(dest="command")

    scan = sub.add_parser("scan", help="Scan a directory for hardcoded secrets")
    scan.add_argument("--path", default=".", help="Directory to scan")
    scan.add_argument("--format", default=DEFAULTS["format"], choices=DEFAULTS["formats"])
    scan.add_argument("--timeout", type=int, default=DEFAULTS["timeout"])
    scan.add_argument("--min-severity", default=DEFAULTS["min_severity"])
    scan.add_argument("--exclude", action="append", help="Glob pattern to skip")

    sub.add_parser("version", help="Print the Halyard version")
    return parser


def main():
    args = build_parser().parse_args()
    if args.command == "scan":
        print(f"Scanning {args.path} (format={args.format}, timeout={args.timeout}s)")
    elif args.command == "version":
        print("halyard 1.4.0")


if __name__ == "__main__":
    main()
