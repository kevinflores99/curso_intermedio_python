def main():
    squared_nums = [ x**2 for x in range(1,101) if x%3 != 0]
    print(squared_nums)

    print("======================================================")
    # List of nums multiples of 4,6,9 
    multiples = [ x for x in range(1,10000) if x%4==0 and x%6==0 and x%9==0]
    print(multiples)

if __name__ == "__main__":
    main()