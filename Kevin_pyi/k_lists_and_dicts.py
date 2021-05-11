def run():
    my_list = [1,'Helo',True,4.5]
    my_dict = {"First Name": "Facundo", "Lastname":"Garcia"}

    super_list = [
        {"First Name": "Facundo", "Lastname":"Garcia"},
        {"First Name": "Kevin", "Lastname":"Flores"},
        {"First Name": "Andres", "Lastname":"Vargas"},
        {"First Name": "Belen", "Lastname":"Rodriguez"},
        {"First Name": "Lizzi", "Lastname":"Rodriguez"}
    ]

    super_dict = {
        "natural_num": [1,2,3,4,5],
        "integer_num": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }


    for key,value in super_dict.items():
        print(key, "-" ,value) 


    for dic in super_list:
        for key, value in dic.items():
            print(key, ":",value,)


if __name__ == '__main__':
    run()