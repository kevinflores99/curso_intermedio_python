DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    print("========All python devs===========")
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    ho_all_python_devs=list(filter(lambda worker: worker["language"]=="python", DATA))
    ho_all_python_devs=list(map(lambda worker: worker["name"], ho_all_python_devs))
    print(all_python_devs)
    print(ho_all_python_devs)

    print("========All Platzi workers===========")
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    ho_all_python_devs=list(filter(lambda worker: worker["organization"]=="Platzi", DATA))
    ho_all_platzi_workers=list(map(lambda worker: worker["name"], ho_all_python_devs))
    print(all_platzi_workers)
    print(ho_all_platzi_workers)

    print("========All aldults===========")
    all_adults = [worker["name"] for worker in DATA if worker["age"]>=18]
    ho_all_adults = list(filter(lambda worker: worker["age"]>=18,DATA))
    ho_all_adults = list(map(lambda worker: worker["name"], ho_all_adults))
    print(all_adults)
    print(ho_all_adults)

    print("========Old people===========")
    old_people = [worker["name"] for worker in DATA if worker["age"]>70]
    ho_old_people = list(filter(lambda worker: worker["age"]>70,DATA))
    ho_old_people = list(map(lambda worker: worker["name"], ho_old_people))
    print(old_people)
    print(ho_old_people)

    print()
    print("========Old people add 'old' key===========")
    people_old = list(map(lambda worker: worker | {"old" : worker["age"]>70} , DATA))
    list_comprenhension_people_old = [worker | {"old": worker["age"] > 70} for worker in DATA]
    print(people_old)
    print(list_comprenhension_people_old)
if __name__ == "__main__":
    main()