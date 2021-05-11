def main():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"first_name": "Andrés", "last_name": "Vargas"}

    super_list = [
        {"first_name": "Andrés", "last_name": "Vargas"},
        {"first_name": "Josue", "last_name": "Cobos"},
        {"first_name": "Kevin", "last_name": "Flores"},
        {"first_name": "Rafa", "last_name": "Rojas"},
        {"first_name": "Ernesto", "last_name": "Vargas"},
        {"first_name": "Jack", "last_name": "Vargas"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5,6],
        "integer_nums": [-2,-1,0,1,2],
        "floatin_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)

    for dic in super_list:
        print(dic)

if __name__ == "__main__":
    main()