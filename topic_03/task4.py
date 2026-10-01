def find_insert_position(lst: list, val: int | float) -> int:
    for i, item in enumerate(lst):
        if val <= item:
            return i
    return len(lst)


def main() -> None:
    numbers = [10, 20, 30, 40, 50]
    val = int(input("val: "))

    pos = find_insert_position(numbers, val)
    print(pos)

    numbers.insert(pos, val)
    print(numbers)


if __name__ == "__main__":
    main()