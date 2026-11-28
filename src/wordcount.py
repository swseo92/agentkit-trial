"""표준 입력을 읽어 줄·낱말·글자 수를 한 줄로 찍는다."""
import argparse
import sys


def count(text):
    """(줄, 낱말, 글자) 수. 줄은 개행 문자 수, wc와 같다."""
    return text.count("\n"), len(text.split()), len(text)


def main(argv=()):
    parser = argparse.ArgumentParser(prog="wordcount")
    parser.add_argument("--chars-only", action="store_true", help="글자 수만 찍는다")
    parser.add_argument("--lines-only", action="store_true", help="줄 수만 찍는다")
    parser.add_argument("--words-only", action="store_true", help="낱말 수만 찍는다")
    parser.add_argument("--bytes-only", action="store_true", help="UTF-8 바이트 수만 찍는다")
    args = parser.parse_args(list(argv))
    text = sys.stdin.read()
    lines, words, chars = count(text)
    if args.chars_only:
        print(chars)
    elif args.lines_only:
        print(lines)
    elif args.words_only:
        print(words)
    elif args.bytes_only:
        print(len(text.encode("utf-8")))
    else:
        print(f"{lines} {words} {chars}")


if __name__ == "__main__":
    main(sys.argv[1:])
