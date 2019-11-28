from pymongo import MongoClient
from bson import ObjectId
client=MongoClient('mongodb://localhost:27017/')
db=client['test']

users=db.users
#user1={"name":"Aman","age":"29","work":"DEV"}
#users.insert_one(user1)

for user in users.find():
	print(user)
	print("|| ID ",user['_id'],"|| Name : ",user['name'],"|| Age ",user['age'],"|| Work ",user['work'],"||")

users.update_one({"age":"29"},{'$set':{'age':'30'}})

for user in users.find():
	print("|| ID ",user['_id'],"|| Name : ",user['name'],"|| Age ",user['age'],"|| Work ",user['work'],"||")


users.delete_many({'_id':ObjectId('5ddcf23c9616abf1db7dae10')})