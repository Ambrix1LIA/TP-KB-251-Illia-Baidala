def main() -> None:
    lst = [5, 2, 8]
    print(f"Початковий список: {lst}")

    lst.append(10)
    print(f"append(10): {lst}")

    lst.extend([1, 7])
    print(f"extend([1, 7]): {lst}")

    lst.insert(2, 99)
    print(f"insert(2, 99): {lst}")

    lst.remove(2)
    print(f"remove(2): {lst}")

    lst.sort()
    print(f"sort(): {lst}")

    lst.reverse()
    print(f"reverse(): {lst}")

    lst_copy = lst.copy()
    print(f"copy(): {lst_copy}")

    lst.clear()
    print(f"clear(): {lst}")


if __name__ == "__main__":
    main()