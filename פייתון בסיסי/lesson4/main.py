# 1
def num_of_words(file):
    count = 0
    with open(file, 'r') as file_read:
        for line in file_read:
            count += 1
            count += line.count(' ')
    return count


with open('file.txt', 'w') as file:
    file.write("hello world\nhello Yehudit hhh")

# print(num_of_words('file.txt'))

# 2
import csv


def ex2(list_of_lists):
    with open('file_user', 'w') as f:
        writer = csv.writer(f)
        for l in list_of_lists:
            writer.writerow(l)


lists = [["Hana", "Cohen", 32, "Modi'in"], ["Sara", "Cohen", 34, "Modi'in"]]
ex2(lists)

# 3

import json


def ex3(dict):
    with open('data.json', 'w') as f:
        json.dump(dict, f)
    with open('data.json', 'r') as f:
        data = json.load(f)
        print(data)


dict = {"name": "Sara", "age": 43}
ex3(dict)
