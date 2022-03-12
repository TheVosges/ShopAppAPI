import unittest
import requests
import App

BASE = "http://127.0.0.1:5000/"

class MyTestCase(unittest.TestCase):

    def testClearDatabase(self):
        response = requests.post(BASE + "all", {"name": 'test', "amount": 0, "type": "CLEAR"})
        self.assertEqual(203, response.status_code)

    def testEmptyJson(self):
        response = requests.get(BASE + "all")
        self.assertEqual(None, print(response))

    def testAddItems(self):
        response = requests.post(BASE + "all", {"name": 'test', "amount": 0, "type": "CLEAR"})
        response = requests.post(BASE + "all", {"name": 'apple', "amount": 2, "type": "PUT"})
        response1 = requests.post(BASE + "all", {"name": 'apple', "amount": 5, "type": "PUT"})
        response2 = requests.post(BASE + "all", {"name": 'orange', "amount": 8, "type": "PUT"})
        self.assertEqual(201, response.status_code)

    def testAppleAmount(self):
        response = requests.get(BASE + "all")
        objJson = response.json()
        apples = objJson["1"]
        self.assertEqual(7,apples['amount'])

    def testOrderItems(self):
        response1 = requests.post(BASE + "all", {"name": 'orange', "amount": 8, "type": "PUT"})
        response2 = requests.post(BASE + "all", {"name": 'orange', "amount": 2, "type": "TAKE"})
        response = requests.get(BASE + "all")
        objJson = response.json()
        oranges = objJson["1"]
        self.assertEqual(6, oranges['amount'])



if __name__ == '__main__':
    unittest.main()
