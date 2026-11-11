from functions import add, sub, mult, div
from operations import get_number, get_operation


def main():
    while True:
        a = get_number("Введіть перше число: ")
        op = get_operation()
        b = get_number("Введіть друге число: ")

        match op:
            case "+":
                print("Результат:", add(a, b))
            case "-":
                print("Результат:", sub(a, b))
            case "*":
                print("Результат:", mult(a, b))
            case "/":
                res = div(a, b)
                if res is not None:
                    print("Результат:", res)

        choice = input("\nБажаєте продовжити? ('q' для виходу, Enter — продовжити): ").strip()
        if choice.lower() == "q":
            print("Роботу калькулятора завершено.")
            break


if __name__ == "__main__":
    main()