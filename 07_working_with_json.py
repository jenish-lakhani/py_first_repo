book = {}
book["tom"] = {"name": "tom", "address": "1, red street, NY", "phone": 74136985}
book["bob"] = {"name": "bob", "address": "1, green street, NY", "phone": 76514558}

import json

s = json.dumps(book)
# print(s)

with open("c://Python_AI//book.txt", "w") as f:
    f.write(s)

f = open("c://Python_AI//book.txt", "r")
s = f.read()
print(s)

book = json.loads(s)
# print(book)
# print(type(book))


print(book["bob"])
print(book["bob"]["phone"])

for person in book:
    print(book[person])
