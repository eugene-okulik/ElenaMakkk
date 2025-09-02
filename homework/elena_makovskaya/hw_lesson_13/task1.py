# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt
#
# Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл,
# находит в нём даты и делает с этими датами то, что после них написано. Опирайтесь на то,
# что структура каждой строки одинакова: сначала идет номер, потом дата, потом дефис и после него текст.
# У вас должен получиться код, который находит даты и для даты под номером один в коде должно быть реализовано то
# действие, которое написано в файле после этой даты. Ну и так далее для каждой даты.


import os
from datetime import datetime, timedelta
import re


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(eugene_file_path) as data_file:
        return data_file.readlines()


def get_data_from_line(line):
    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+", line)
    if match:
        date_str = match.group()
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    return None


def update_dates():
    lines = read_file()
    for line in lines:
        new_line = line.lstrip()
        if new_line.startswith('1'):
            date = get_data_from_line(line)
            if date:
                new_date = date + timedelta(days=7)
                print(f'1. Дата на неделю позже: {new_date}\n')
        elif new_line.startswith('2'):
            date = get_data_from_line(line)
            if date:
                print(f'2. День недели: {date.strftime("%A")}\n')
        elif new_line.startswith('3'):
            date = get_data_from_line(line)
            if date:
                now_date = datetime.now()
                delta_days = (now_date - date).days
                print(f'3. Дней назад: {delta_days}\n')


update_dates()
