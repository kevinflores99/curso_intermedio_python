def divisors(num):
    return [i for i in range(1, num+1) if num % i == 0]


def run():
    num = input('Enter a number: ')
    assert "-" not in num, 'Just positive numbers'
    assert num.isnumeric(), 'Debes ingresar un numero'
    print(divisors(int(num)))
    print('Finish')


if __name__ == '__main__':
    run()
