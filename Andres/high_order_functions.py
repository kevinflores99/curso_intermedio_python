def main():
    #? Lambda function
    is_odd = lambda x: x%2 != 0

    #* FILTER
    print("------------FILTER------------")
    print("Filter the odd numbers")
    my_list = [1,4,5,6,7,13,17,19,21]
    odds = list(filter(is_odd, my_list))
    print(odds)

    #* MAP
    print("------------MAP------------")
    print("Get the squares of the odd numbers")
    squares = list(map(lambda x: x**2, odds))
    print(squares)

    #* REDUCE
    from functools import reduce
    print("------------REDUCE------------")
    print("Get the multiplicacion of all numbers in the list above")
    final_result = reduce(lambda a,b: a*b, squares)
    print(final_result)

if __name__ == "__main__":
    main()