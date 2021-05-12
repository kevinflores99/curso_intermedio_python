def divisors(num):
    try:
        return [i for i in range(1, num+1) if num % i == 0]

    except ValueError as ve:
        print(ve)
        return


def run():
    while True:
        try:
            num = int(input('Enter a number: '))
            if num < 0:
                print('Insert a positive number')
                break
            else:
                print(divisors(num))
                print('Finish')
                break
        except ValueError:
            print('You have to write a number')


if __name__ == '__main__':
    run()
