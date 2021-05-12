def divisors(num):
    return [i for i in range(1, num+1) if num%i==0]


def main():
    num = int(input("Type a number: "))
    print(divisors(num))
    print("Program finished")


if __name__ == "__main__":
    main()