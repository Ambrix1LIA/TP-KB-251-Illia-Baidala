def discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4 * a * c


def main() -> None:
    try:
        a = float(input("Введіть a: "))
        b = float(input("Введіть b: "))
        c = float(input("Введіть c: "))

        d = discriminant(a, b, c)
        print(f"Дискримінант D = {d}")

    except ValueError:
        print("Помилка: введіть числа.")


if __name__ == "__main__":
    main()