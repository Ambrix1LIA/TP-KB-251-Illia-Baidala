from functions import add, sub, mult, div
from operations import get_number, get_operation


def log_action(a, op, b, result):
    with open("calc_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Числа: {a}, {b} | Операція: '{op}' | Результат: {result}\n")


def main():
    while True:
        a = get_number("Введіть перше число: ")
        op = get_operation()
        b = get_number("Введіть друге число: ")

        res = None
        match op:
            case "+":
                res = add(a, b)
            case "-":
                res = sub(a, b)
            case "*":
                res = mult(a, b)
            case "/":
                res = div(a, b)

        if res is not None:
            print("Результат:", res)
            log_action(a, op, b, res)
        else:
            log_action(a, op, b, "Помилка (ділення на 0)")

        choice = input("\nПродовжити? ('q' для виходу, Enter — далі): ").strip()
        if choice.lower() == "q":
            print("Роботу завершено.")
            break


if __name__ == "__main__":
    main()