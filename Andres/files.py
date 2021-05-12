def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line.strip()))
        print(numbers)

def write():
    names = ["Andrés", "Joshua", "Pepe", "Pedro"]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name + "\n")

def main():
    write()

if __name__ == "__main__":
    main()