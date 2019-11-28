from pymongo import MongoClient
from bson import ObjectId

class DBOperation:

	def __init__(self):
		self.client=MongoClient("mongodb://localhost:27017/")
		self.db=self.client['demo_database']


	def showMenu(self):
		print("==============================")
		print("||    1. Show User Data     ||")
		print("||    2. Add User           ||")
		print("||    3. Update User        ||")
		print("||    4. Delete User        ||")
		print("||    5. Exit               ||")
		print("==============================")
		data=input("Enter Choice : ")
		return data

	def addUser(self):
		user=self.db.user
		name=input("Enter Name : ")
		age=input("Enter Age : ")
		work=input("Enter Work : ")
		user_data={"name":name,"age":age,"work":work}
		user.insert_one(user_data)

	def ShowData(self):
		print("===============USER DATA===========")
		print("||            ID          ||     Name    ||  AGE  ||   Work ||")
		for user in self.db.user.find():
			print("|| ",user['_id']," || ",user['name']," || ",user['age']," || ",user['work']," ||")
		print("================================")

	def UpdateUser(self):
		input_id=input("Enter User ID : ")
		user=self.db.user.find_one({"_id":ObjectId(input_id)})
		name=input(" Old Name : "+user['name']+" Enter New Name : ")
		age=input(" Old Age : "+user['age']+" Enter New Age : ")
		work=input(" Old Work : "+user['work']+" Enter New Work : ")

		user_data={"name":name,"age":age,"work":work}

		self.db.user.update_one({"_id":ObjectId(input_id)},{"$set":user_data})

	def DeleteUser(self):
		input_id=input("Enter User ID ")
		self.db.user.delete_one({"_id":ObjectId(input_id)})					



dboper=DBOperation()
exit=False
while exit!=True:
	input_data=dboper.showMenu()

	if input_data=="1":
		dboper.ShowData()

	if input_data=="2":
		dboper.addUser()

	if input_data=="3":
		dboper.UpdateUser()

	if input_data=="4":
		dboper.DeleteUser()

	if input_data=="5":
		exit=True		
