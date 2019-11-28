from pymongo import MongoClient
from bson import ObjectId
class DbOperation:

	def __init__(self):
		self.client=MongoClient('mongodb://localhost:27017/')
		self.db=self.client['test']

	def PrintUsers(self):
		print("=============================USER TABLE============================")
		print("||       	id            ||   Name  || AGE  ||    Work      ||")
		for user in self.db.users.find():
			print("|| ",user['_id']," || ",user['name']," || ",user['age']," || ",user['work']," ||")
		print("===================================================================")

	def AddUsers(self):
		name=input("Enter Name : ")
		age=input("Enter Age : ")
		work=input("Enter Work : ")	
		user1={"name":name,"age":age,"work":work}
		self.db.users.insert_one(user1)						

	def UpdateUsers(self):
		ids=input('Enter ID : ')
		user=self.db.users.find_one({'_id':ObjectId(ids)});
		name=input("OLD Name is : "+user['name']+" Enter New Name : ")
		age=input("OLD Age is : "+user['age']+" Enter Age Name : ")
		work=input("OLD Work is : "+user['work']+" Enter Work Name : ")
		user1={"name":name,"age":age,"work":work}
		self.db.users.update_one({'_id':ObjectId(ids)},{'$set':user1})						

	def deleteData(self):
		ids=input('Enter ID : ')
		user=self.db.users.delete_one({'_id':ObjectId(ids)});


	def showMenu(self):
		print("============================SELECT OPERATION=======================")
		print("||			1. SHOW DATA 				 ||")
		print("||			2. ADD DATA 				 ||")
		print("||			3. UPDATE DATA 				 ||")
		print("||			4. DELETE DATA 		 		 ||")
		print("||			5. EXIT 		 		 ||")
		print("===================================================================")
		data=input("Enter Choice : ")
		return data



dboper=DbOperation()
exit=False
while exit!=True:
	input_d=dboper.showMenu()

	if(input_d=="1"):
		dboper.PrintUsers()	

	if(input_d=="2"):
		dboper.AddUsers()	

	if(input_d=="3"):
		dboper.UpdateUsers()	

	if(input_d=="4"):
		dboper.deleteData()	


	if(input_d=="5"):
		exit=True	


#user1={"name":"Aman","age":"29","work":"DEV"}
#users.insert_one(user1)

