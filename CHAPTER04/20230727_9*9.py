def multiplication_table():
    print("九九の結果表:")
    for i in range(1, 10):
        for j in range(1, 10):
            result = i * j
            print(f"{result:2}", end="  ")
        print()


multiplication_table()
