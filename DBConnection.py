from pymongo import MongoClient

client = MongoClient('localhost',27017).get_database("Waze")
#client = MongoClient('mongodb://admin:cnat2203@localhost:27017').get_database("Waze")
#print("teststststts")