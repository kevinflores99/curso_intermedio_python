def run():
    # my_dict = {}
    # for i in in range(1, 101):
    #     my_dict[i] = i**3

    # print(my_dict)

    # dic = {i: i**3 for i in range(1, 101)}
    # print(dic)

    dic = {i: i for i in range(1, 101) if i % 3 != 0}
    print(dic)


if __name__ == "__main__":
    run()
