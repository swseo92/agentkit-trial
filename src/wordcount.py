"""표준 입력을 읽어 줄·낱말·글자 수를 한 줄로 찍는다."""
import sys


def count(text):
    """(줄, 낱말, 글자) 수. 줄은 개행 문자 수, wc와 같다."""
    return text.count("\n"), len(text.split()), len(text)


def main():
    lines, words, chars = count(sys.stdin.read())
    print(f"{lines} {words} {chars}")


if __name__ == "__main__":
    main()
