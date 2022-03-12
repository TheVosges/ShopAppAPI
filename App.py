import requests


class ShopAPIFunctions:

    def __init__(self):
        self.BASE = "http://127.0.0.1:5000/"

    def showStock(self):
        response = requests.get(self.BASE + "all")
        objJson = response.json()
        for item in objJson:
            values = objJson[item]
            print("ID: " + str(item) + ", Name: " + str(values['name']) + ", Amount: " + str(values['amount']))
        # print(response.json())

    def showStockForID(self, ID):
        response = requests.get(self.BASE + ID)
        objJson = response.json()
        print("ID: " + str(ID) + ", Name: " + str(objJson['name']) + ", Amount: " + str(objJson['amount']))
        # print(response.json())

    def addItemToStock(self, productName, amount):
        response = requests.post(self.BASE + "all",{"name": productName, "amount" : int(amount), "type" : "PUT"})

    def orderItemFromStock(self, productName, amount):
        response = requests.post(self.BASE + "all",{"name": productName, "amount" : int(amount), "type" : "TAKE"})

    def changeBase(self, baseLink):
        self.BASE = baseLink


#Simple console app
if __name__ == '__main__':
    shopAPI = ShopAPIFunctions()
    print("Welcome to Shop REST API!\n"
          + "Please select what you want to do:\n"
          + "1. Show current stock\n"
          + "2. Show stock for specific item ID\n"
          + "3. Add\Create item to stock\n"
          + "4. Order an item from stock\n"
          + "5. Change link to API\n"
          + "6. Exit\n")
    running = True
    while running:
        option = input("Type 1/2/3/4/5: ")
        if (option == "1"):
            shopAPI.showStock()
        elif (option == "2"):
            ID = input("Please provide item ID: ")
            shopAPI.showStockForID(ID)
        elif (option == "3"):
            productName = input("Please provide item name: ")
            stock = input("Please provide amount: ")
            shopAPI.addItemToStock(productName, stock)
        elif (option == "4"):
            productName = input("Please provide item name: ")
            stock = input("Please provide amount: ")
            shopAPI.orderItemFromStock(productName, stock)
        elif (option == "5"):
            BASE = input("Please provide API link: ")
            shopAPI.changeBase(BASE)
        elif (option=="6"):
            running = False





