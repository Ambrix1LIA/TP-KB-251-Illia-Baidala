def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float | str:
    if b == 0:
        return "Помилка (ділення на 0)"
    return a / b


def main() -> None:
    a = float(input("a: "))
    b = float(input("b: "))
    op = input("op: ")

    match op:
        case "+":
            print(add(a, b))
        case "-":
            print(subtract(a, b))
        case "*":
            print(multiply(a, b))
        case "/":
            print(divide(a, b))
        case _:
            print("Невідома дія")


if __name__ == "__main__":
    main()