import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoob"]
mycol = mydb["runoob"]

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

for x in mycol.find():
  print(x)