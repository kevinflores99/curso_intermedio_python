def divisors(num):
    try:
        if num <= 0:
            raise ValueError("Use only numbers higher than 0")
        return [i for i in range(1, num+1) if num%i==0]

    except ValueError as ve:
        print(ve)
        return


def main():
    
    try:
        num = int(input("Type a number: "))
        print(divisors(num))
        print("Program finished")
    except ValueError:
        print('Just numbers are accepted as input')



if __name__ == "__main__":
    main()