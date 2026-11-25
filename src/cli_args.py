def parse(argv: list[str]) -> dict:
    """`--upper`, `--count` 플래그와 나머지 낱말(text)을 나눈다. 모르는 `--x`는 ValueError."""
    out = {"upper": False, "count": False, "text": ""}
    words = []
    for a in argv:
        if a in ("--upper", "--count"):
            out[a[2:]] = True
        elif a.startswith("--"):
            raise ValueError(f"unknown flag: {a}")
        else:
            words.append(a)
    out["text"] = " ".join(words)
    return out
