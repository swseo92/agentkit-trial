import sys

from src.cli_args import parse


def run(argv: list[str]) -> str:
    a = parse(argv)
    if a["count"]:
        return str(len(a["text"].split()))
    return a["text"].upper() if a["upper"] else a["text"]


if __name__ == "__main__":
    print(run(sys.argv[1:]))
