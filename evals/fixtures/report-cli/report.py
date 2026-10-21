"""Synthetic baseline for evaluating an agent's CLI feature implementation."""

import argparse


def nonnegative(value):
    try:
        count = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("count must be an integer") from exc
    if count < 0:
        raise argparse.ArgumentTypeError("count must be nonnegative")
    return count


def main():
    parser = argparse.ArgumentParser(description="Report an item count.")
    parser.add_argument("--count", type=nonnegative, default=0)
    args = parser.parse_args()
    print(f"Items: {args.count}")


if __name__ == "__main__":
    main()
