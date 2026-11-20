"""리스트의 중앙값."""


def median(values: list[float]) -> float:
    if not values:
        raise ValueError("median of empty list")
    s = sorted(values)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
