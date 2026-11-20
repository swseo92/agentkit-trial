"""리스트의 중앙값."""


def median(values: list[float]) -> float:
    if not values:
        raise ValueError("median of empty list")
    s = sorted(values)
    return s[(len(s) - 1) // 2]
