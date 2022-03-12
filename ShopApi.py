from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
import json
import requests

BASE = "http://127.0.0.1:5000/"

app = Flask(__name__)
api = Api(app)
shopApiParser = reqparse.RequestParser()
shopApiParser.add_argument("name", type=str, help="Name of product", required = True)
shopApiParser.add_argument("amount", type=int, help="Amount of products", required = True)
shopApiParser.add_argument("type", type=str, help="Type of request (PUT,TAKE, CLEAR)", required = True)

class ShopApi(Resource):

    def get(self, productID):

        f = open('data.json')
        data = json.load(f)
        # return self.data["products"][productID]
        if productID == "all":
            try:
                return data
            except json.decoder.JSONDecodeError:
                return "Unexceped error (probably no data foudnd)",408
        else:
            try:
                return data[productID]
            except KeyError:
                return "No item for this ID", 407



    def post(self, productID):
        args = shopApiParser.parse_args()
        wasInStock = False
        response = requests.get(BASE + "all")
        jsonObj = response.json()
        if (args['type'] == "PUT"):


            for item in jsonObj.values():
                 if args['name'] == item['name']:
                    wasInStock = True
                    item['amount'] = item['amount'] + args['amount']
                    with open('data.json', 'w') as outfile:
                        json.dump(jsonObj, outfile)
                    break

            lastID = "0"
            try:
                for item in jsonObj:
                    lastID = item
            except UnboundLocalError:
                lastID == "1"

            if (not wasInStock):
                newID = (int(lastID) + 1)
                dict = {"name" : args['name'], "amount" : args['amount']}
                jsonObj[str(newID)] = dict
                with open('data.json', 'w') as outfile:
                    json.dump(jsonObj, outfile)
            return "Operation sucessfuly added", 201

        #ORDER A PRODUCT
        elif(args['type'] == "TAKE"):
            for item in jsonObj.values():
                 if args['name'] == item['name']:
                    wasInStock = True
                    if (item['amount'] >= args['amount']):
                        item['amount'] = item['amount'] - args['amount']
                    else:
                        return "Not enough in stock (In stock: " + str(item['amount']) + ")", 406
                    with open('data.json', 'w') as outfile:
                        json.dump(jsonObj, outfile)
                    break
            if (not wasInStock):
                return "Item isn't in stock", 407
            return "Operation sucessfuly ordered", 202

        elif (args['type'] == "CLEAR"):
            try:
                dict = {}
                with open('data.json', 'w') as outfile:
                    json.dump(dict, outfile)
                return "Database cleard sucessfuly", 203
            except json.decoder.JSONDecodeError:
                return "Unexceped error (probably no data foudnd)"



        # jsonReq = request.get_json()
        # with open("data.json", "w") as outfile:
        #     json.dump(jsonReq, outfile)
        # return 'You posted this data: ' + str(jsonReq), 201

api.add_resource(ShopApi, '/<string:productID>')

if __name__ == '__main__':
    app.run(debug=True)

#curl -H "Content-Type: application/json" -X POST -d "{ \"name\":\"xyz\", \"address\":\"address_xyz\" }"  http://127.0.0.1:5000
