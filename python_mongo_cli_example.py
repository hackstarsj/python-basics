from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client['demo_database']

#insert data
user=db.users
#user_data={"name":"rahul","age":"28","work":"programmer"}
#user.insert_one(user_data)


#fetch data
for user_one in user.find():
	print(user_one['name'])

#update data

user.update_many({"name":"rahul"},{"$set":{"age":"29"}})	

for user_one in user.find():
	print(user_one)


#single delete
user.delete_one({"name":"rahul"})

#multi delete
user.delete_many({"name":"rahul"})