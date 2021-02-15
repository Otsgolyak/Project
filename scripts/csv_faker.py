import csv
import random
from faker import Faker



fake = Faker()
data = [['Name', 'E-mail', 'Phone', 'Country', 'City', 'Age']]


def lst_maker(number):
    data = [['Name', 'E-mail', 'Phone', 'Country', 'City', 'Age']]
    for i in range(number):
        lst = []
        lst.append(fake.name())
        lst.append(fake.email())
        lst.append(str(fake.country_calling_code())+str(fake.pyint(min_value=999999999, max_value=9999999999, step=1)))
        lst.append(fake.country())
        lst.append(fake.city())
        lst.append(random.randint(18, 60))
        data.append(lst)
    return data


def lst_maker_russian(number):
    data = [['Имя', 'Имейл', 'Телефон', 'Страна', 'Город', 'Возраст']]
    for i in range(number):
        lst = []
        lst.append(fake.name())
        lst.append(fake.email())
        lst.append(str(fake.country_calling_code())+str(fake.pyint(min_value=999999999, max_value=9999999999, step=1)))
        lst.append(fake.country())
        lst.append(fake.city())
        lst.append(random.randint(18, 60))
        data.append(lst)
    return data


def lst_with_doubles_maker(number):
    data = [['Name', 'E-mail', 'Phone', 'Country', 'City', 'Age']]
    for i in range(number):
        if i % 10 == 0:
            lst = []
            lst.append(fake.name())
            lst.append(fake.email())
            lst.append(
                str(fake.country_calling_code())+str(fake.pyint(min_value=999999999, max_value=9999999999, step=1)))
            lst.append(fake.country())
            lst.append(fake.city())
            lst.append(random.randint(18, 60))
            data.append(lst)
            data.append(lst)
        else:
            lst = []
            lst.append(fake.name())
            lst.append(fake.email())
            lst.append(
                str(fake.country_calling_code()) + str(fake.pyint(min_value=999999999, max_value=9999999999, step=1)))
            lst.append(fake.country())
            lst.append(fake.city())
            lst.append(random.randint(18, 60))
            data.append(lst)
    return data


def lst_with_empty_fields_maker(number):
    data = [['Name', 'E-mail', 'Phone', 'Country', 'City', 'Age']]
    for i in range(number):
        if i % 10 == 0:
            lst = []
            lst.append(fake.name())
            lst.append(fake.email())
            lst.append('')
            lst.append(fake.country())
            lst.append(fake.city())
            lst.append(random.randint(18, 60))
            data.append(lst)

        elif i % 10 == 2:
            lst = []
            lst.append(fake.name())
            lst.append(fake.email())
            lst.append(
                str(fake.country_calling_code()) + str(fake.pyint(min_value=999999999, max_value=9999999999, step=1)))
            lst.append(fake.country())
            lst.append('')
            lst.append(random.randint(18, 60))
            data.append(lst)
        else:
            lst = []
            lst.append(fake.name())
            lst.append(fake.email())
            lst.append(
                str(fake.country_calling_code()) + str(fake.pyint(min_value=999999999, max_value=9999999999, step=1)))
            lst.append(fake.country())
            lst.append(fake.city())
            lst.append(random.randint(18, 60))
            data.append(lst)
    return data

def faker_csv():
    fake = Faker()
    data = [['Name', 'E-mail', 'Phone', 'Country', 'City', 'Age']]
    print("               ****         ")
    print("Файл: 200k.csv создаётся")
    with open('200k.csv', 'w', encoding='utf8') as myFile:
        writer = csv.writer(myFile, delimiter=';', lineterminator='\n')
        writer.writerows(lst_maker(200000))
        print("Файл: 200k.csv создан")
    print("               ****         ")
    print("Файл: 100.csv создаётся")
    with open('100.csv', 'w', encoding='utf8') as myFile:
        writer = csv.writer(myFile, delimiter=';', lineterminator='\n')
        writer.writerows(lst_maker(100))
        print("Файл: 100.csv создаётся")
    print("               ****         ")
    print("Файл: 100_with_doubles_in_file.csv создаётся")
    with open('100_with_doubles_in_file.csv', 'w', encoding='utf8') as myFile:
        writer = csv.writer(myFile, delimiter=';', lineterminator='\n')
        writer.writerows(lst_with_doubles_maker(100))
        print("Файл: 100_with_doubles_in_file.csv создан")
    print("               ****         ")
    print("Файл: 100_with_empty_fields.csv создаётся")
    with open('100_with_empty_fields.csv', 'w', encoding='utf8') as myFile:
        writer = csv.writer(myFile, delimiter=';', lineterminator='\n')
        writer.writerows(lst_with_empty_fields_maker(100))
        print("Файл: 100_with_empty_fields.csv создан")
    print("               ****         ")
    print("Файл: delimetr_coma.csv создаётся")
    with open('delimetr_coma.csv', 'w', encoding='utf8') as myFile:
        writer = csv.writer(myFile, delimiter=',', lineterminator='\n')
        writer.writerows(lst_maker(100))
        print("Файл: delimetr_coma.csv создан")
    print("               ****         ")
    print("Файл: russian_fields.csv создаётся")
    with open('russian_fields.csv', 'w', encoding='utf8') as myFile:
        writer = csv.writer(myFile, delimiter=';', lineterminator='\n')
        writer.writerows(lst_maker_russian(100))
        print("Файл: russian_fields.csv создан")
    print("               ****         ")
    for i in range(1, 11):
        print("Файл: {} создаётся".format(i))
        with open('{}.csv'.format(i), 'w', encoding='utf8') as myFile:
            writer = csv.writer(myFile, delimiter=';', lineterminator='\n')
            writer.writerows(lst_maker(100000))
            print("Файл: {} создан".format(i))
            print("               ****         ")
    print("********************************")
    print("            Конец               ")
    print("********************************")
