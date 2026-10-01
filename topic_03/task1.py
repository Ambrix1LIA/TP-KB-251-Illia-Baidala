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
    while True:
        op = input("op (+, -, *, /, exit): ").strip()
        if op == "exit":
            break

        if op not in ("+", "-", "*", "/"):
            print("Невідома дія")
            continue

        try:
            a = float(input("a: "))
            b = float(input("b: "))
        except ValueError:
            print("Помилка введення числа")
            continue

        match op:
            case "+":
                print(add(a, b))
            case "-":
                print(subtract(a, b))
            case "*":
                print(multiply(a, b))
            case "/":
                print(divide(a, b))


if __name__ == "__main__":
    main()