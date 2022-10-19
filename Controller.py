import csv
import json
import uFile_IO
import re
from pathlib import Path


def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee

def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())

employees  = read_csv()

def write_json(employees: list):
    with open('database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')

def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee

#
def add_line():
    id = str(input('Введите следущий id: '))
    last_name = str(input('Введите фамилию: '))
    first_name = str(input('Введите имя: '))
    position = str(input('Введите доллность: '))
    phone_number = str(input('Введите телефон: '))
    salary = str(input('Введите зарплату: '))
    return (f'{id},{last_name},{first_name},{position},{phone_number},{salary}')

def re_new():
    with open('database.csv', 'r', encoding='utf-8') as f:
        old_data = f.read()
    change_str = input('Введите что необходимо откорректировать: ')
    what_change = input('Введите на что необходимо заменить: ')
    new_data = old_data.replace(change_str, what_change)

    with open('database.csv', 'w', encoding='utf-8') as f:
        f.write(new_data)


#Находим по ключу!
def find_employees_by_name(last_name):
    for employ in employees:
        if employ['last_name'] == last_name:
            return employ


def find_employees_by_position(position):
    for employ in employees:
        if employ['position'] == position:
            return employ

def find_employees_by_salary_range(employees: list) -> list:
    result = []
    lo = float(input('Введите наименьший оклад: '))
    hi = float(input('Введите наибольший оклад: '))
    for employee in employees:
        if lo <= employee["salary"] <= hi:
            result.append(employee)
    return result


def remove_line(delete_request):

    with open('database.csv', encoding='utf-8') as f:
        lines = f.readlines()

    str = delete_request
    pattern = re.compile(re.escape(str))
    with open('database.csv', 'w', encoding='utf-8') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)





# uFile_IO.Input_data_file('database.csv', add_line(), 'a')
# print(find_employees_by_salary_range(employees))


# print(find_employees_by_name('Иванов'))
# print(find_employees_by_position('менеджер'))
