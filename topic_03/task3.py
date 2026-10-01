def main() -> None:
    data = {"a": 1, "b": 2}
    print(data)

    data.update({"c": 3, "d": 4})
    print(data)

    print(list(data.keys()))
    print(list(data.values()))
    print(list(data.items()))

    del data["b"]
    print(data)

    data.clear()
    print(data)


if __name__ == "__main__":
    main()