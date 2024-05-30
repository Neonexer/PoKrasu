from django.shortcuts import render
import json
from .models import Restaurant

# Create your views here.
def restaurants(request):

    # file = "/Users/max/PycharmProjects/Project/restaurants/static/restaurants/result.json"
    #
    # data2 = []
    #
    # with open(file, mode='r') as file:
    #     data = json.load(file)
    #
    # for el in data:
    #     # print(el)
    #
    #     try:
    #         address = el.get("address")
    #     except Exception as e:
    #         print(e)
    #         street = ""
    #         home = ""
    #         continue
    #
    #     name = el.get("name")
    #     type = el.get("type")
    #
    #     try:
    #         rating = el.get("raiting").replace(",", ".")
    #         rating = str(rating)
    #     except Exception as e:
    #         print(e)
    #         continue
    #     try:
    #         image = el.get("img")[1]
    #     except:
    #         continue
    #     # print(name)
    #     # print(type)
    #     # print(rating)
    #     # # print(address)
    #     # print(street)
    #     # print(home)
    #     # print(image)
    #     data2.append({
    #         "name": name,
    #         "address": address,
    #         "type": type,
    #         "image": image,
    #         "rating": rating
    #     })
    #
    #     # print(street, home)
    #     address = Address(address=address)
    #     restaurant = Restaurant(name=name, type=type, address=address, rating=rating, image=image)
    #     address.save()
    #     restaurant.save()
    #
    # print(len(data))


    # return render(request,"restaurants/rest.html", context={"data":data2})

    restaurants = Restaurant.objects.all()


    return render(request,"restaurants/rest.html", {"restaurants":restaurants, "count":restaurants.count()})