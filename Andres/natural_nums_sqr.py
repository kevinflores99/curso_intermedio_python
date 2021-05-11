def main():
    squared_nums = [ x**2 for x in range(1,101) if x%3 != 0]
    print(squared_nums)

if __name__ == "__main__":
    main()