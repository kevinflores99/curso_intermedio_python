def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding='UTF-8') as f:
        [numbers.append(int(line)) for line in f]

    print(numbers)


def write():
    names = ['Maria', 'Fernanda']
    with open("./files/names.txt", "a", encoding='UTF-8') as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    # read()
    write()


if __name__ == '__main__':
    run()
