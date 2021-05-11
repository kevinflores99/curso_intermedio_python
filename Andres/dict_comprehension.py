def main():
    # dict_nums={}
    # for i in range(1,101):
    #     dict_nums[i] = i**3
    # print(dict_nums)

    dic = { i:i**3 for i in range(1,101)}
    print(dic)

if __name__ == "__main__":
    main()