from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
def restaurants(request):

    file = "/Users/max/PycharmProjects/Project/restaurants/static/restaurants/result.json"

    data2 = []

    with open(file, mode='r') as file:
        data = json.load(file)

    for el in data:
        print(el)

        try:
            address = el.get("address").split(", ")
            street = address[0]
            home = address[1]
        except Exception as e:
            street = ""
            home = ""
            continue

        name = el.get("name")
        type = el.get("type")

        raiting = el.get("raiting")
        try:
            image = el.get("img")[1]
        except:
            continue
        print(name)
        print(type)
        print(raiting)
        # print(address)
        print(street)
        print(home)
        print(image)
        data2.append({
            "name": name,
            "street": street,
            "type": type,
            "home": home,
            "image": image,
            "raiting": raiting
        })

    print(len(data))


    return render(request,"restaurants/rest.html", context={"data":data2})