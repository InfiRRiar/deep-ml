def min_max(x: list[float]) -> list[float]:
    mx, mn = max(x), min(x)
    for idx, num in enumerate(x):
        x[idx] = (num - mn) / (mx - mn)
    return x