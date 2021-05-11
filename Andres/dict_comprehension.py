from math import sqrt


def main():
    # dict_nums={}
    # for i in range(1,101):
    #     dict_nums[i] = i**3
    # print(dict_nums)

    dic = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(dic)

    print("+++++++++++++++++++++++++++++++++++++++++++++")
    dic_sqrt = {n: round(sqrt(n), 3) for n in range(1, 1000)}
    print(dic_sqrt)


if __name__ == "__main__":
    main()
