from calculator import Calculator
from operations import get_number, get_operation


def main():
    calc = Calculator()

    while True:
        a = get_number("Введіть перше число: ")
        op = get_operation()
        b = get_number("Введіть друге число: ")

        match op:
            case "+":
                print("Результат:", calc.add(a, b))
            case "-":
                print("Результат:", calc.sub(a, b))
            case "*":
                print("Результат:", calc.mult(a, b))
            case "/":
                res = calc.div(a, b)
                if res is not None:
                    print("Результат:", res)

        choice = input("\nПродовжити? ('q' для виходу, Enter — далі): ").strip()
        if choice.lower() == "q":
            print("Роботу калькулятора завершено.")
            break


if __name__ == "__main__":
    main()