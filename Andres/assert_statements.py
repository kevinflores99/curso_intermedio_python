def divisors(num):
    return [i for i in range(1, num+1) if num%i==0]


def main():
    num = input("Type a number: ")
    assert "-" not in num, "Only positive numbers please"
    assert num.isnumeric(), "Just numbers are accepted as input"
    print(divisors(int(num)))
    print("Program finished")



if __name__ == "__main__":
    main()