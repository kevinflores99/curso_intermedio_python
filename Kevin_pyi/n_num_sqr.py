def run():
    # num_n = []
    # for num in range(1,11):
    #     if num % 3 != 0:
    #         num_n.append(num**2)

    # print(num_n)

    # squares = [i**2 for i in range(1,101) if i % 3 != 0]
    # print(squares)

    mult = [i for i in range(1, 100000) if i %
            4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(mult)


if __name__ == '__main__':
    run()
