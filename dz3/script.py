import json
import csv

myList = []
tmpDict = {}
with open("users.json", "r") as users_file:
    users_data = json.load(users_file)
    for i in users_data:
        tmpDict["gender"] = i["gender"]
        tmpDict["name"] = i["name"]
        tmpDict["address"] = i["address"]
        myList.append(tmpDict)


print myList
# with open("books.csv", "r") as books_file:
#     books_data = csv.reader(books_file)
#     for row in books_data:
#         print row
#         print type(row)
#         break

