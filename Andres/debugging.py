def divisors(num):
    return [i for i in range(1, num+1) if num%i==0]


def main():
    
    try:
        num = int(input("Type a number: "))
        if num <= 0:
            raise Exception("Use only numbers higher than 0")
        print(divisors(num))
        print("Program finished")
    except ValueError:
        print('Just numbers are accepted as input')
    except Exception as ex:
        print(ex)



if __name__ == "__main__":
    main()