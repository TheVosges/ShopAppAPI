import ShopApi
import requests
import json

BASE = "http://127.0.0.1:5000/"


if __name__ == '__main__':
    # with open('data.json') as json_file:
    #     jsonFile = json.load(json_file)
    # jsonFile["products"][0]["amount"] = 5
    # print(jsonFile)

    response = requests.get(BASE + "all")
    print(response.json())
    # #
    # response = requests.post(BASE + "all",{"name": "apple", "amount" : 1, "type" : "PUT"})
    # print(response.json())
    # print("PO")
    # response = requests.get(BASE + "all")
    # print(response.json())
    # requests.post(BASE + "all",{"name": "apple", "amount" : 1, "type" : "CLEAR"})
    # response = requests.get(BASE)
    # print(response.json())
