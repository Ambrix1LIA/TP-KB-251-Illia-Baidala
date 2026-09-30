import math


def discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4 * a * c


def find_roots(a: float, b: float, c: float) -> tuple[float | None, float | None]:
    if a == 0:
        return None, None

    d = discriminant(a, b, c)

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x, None
    else:
        return None, None


def main() -> None:
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    d = discriminant(a, b, c)
    print(f"D = {d}")

    x1, x2 = find_roots(a, b, c)

    if x1 is not None and x2 is not None:
        print(f"x1 = {x1}, x2 = {x2}")
    elif x1 is not None:
        print(f"x = {x1}")
    else:
        print("Немає дійсних коренів")


if __name__ == "__main__":
    main()