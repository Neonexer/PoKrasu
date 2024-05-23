import json
from models import Address, Restaurant

filename = "result.json"
# filename = "result5_entertainment.json"

with open(filename, mode='r') as file:
    data = json.load(file)


for el in data:
    print(el)
    street = ""
    home = ""

    name = el.get("name")
    type = ""
    address = ""
    rating = ""
    image = ""
    print(name)

print(len(data))