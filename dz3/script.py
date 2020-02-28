#!/usr/bin/env python

import json
import csv

myList = []
tmpDict = {}
books_list = []


with open("books.csv", "r") as books_file:
    next(csv.reader(books_file))

    for row in csv.reader(books_file):
        tmpDict['title'] = row[0]
        tmpDict['autohor'] = row[1]
        tmpDict['height'] = row[3]
        books_list.append(tmpDict.copy())

tmpDict.clear()

with open("users.json", "r") as users_file:
    i = 0
    users_data = json.load(users_file)
    for user in users_data:
        tmpDict["gender"] = user["gender"]
        tmpDict["name"] = user["name"]
        tmpDict["address"] = user["address"]
        tmpDict["books"] = []
        tmpDict["books"].append(books_list[i])
        myList.append(tmpDict.copy())
        i += 1
print myList

with open("new.json", "w") as my_file:
    json.dump(myList, my_file)
