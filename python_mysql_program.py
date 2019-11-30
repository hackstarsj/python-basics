import mysql.connector

class DBOperation:

	def __init__(self):
		self.db=mysql.connector.connect(host="localhost",user="python_tut",passwd="python_password",database="user_details")


	def showMenu(self):
		print("============================")
		print("||     1. Add Users       ||")
		print("||     2. Show Users      ||")
		print("||     3. Update User     ||")
		print("||     4. Delete User     ||")
		print("||     5. Exit Program    ||")
		print("============================")
		data=input("Enter Your Choice : ")
		return data

	def addUsers(self):
		cursor=self.db.cursor()
		name=input("Enter Name : ")
		email=input("Enter Email : ")
		age=input("Enter Age : ")
		work=input("Enter Work : ")

		data=(name,email,age,work)
		sql="INSERT into users (name,email,age,work) values (%s,%s,%s,%s)"
		cursor.execute(sql,data)
		self.db.commit()

	def showUsers(self):
		cursor=self.db.cursor()
		sql="select * from users"
		cursor.execute(sql)
		result=cursor.fetchall()

		print("=============USER DATA==========")
		print("||  ID  ||   NAME   ||      EMAIL    ||    AGE   ||    WORK   ||")
		for row in result:
			print("|| ",row[0]," || ",row[1]," || ",row[2]," || ",row[3]," || ",row[4]," ||")
		print("================================")		

	def updateUser(self):
		cursor=self.db.cursor()
		ids=input("Enter User ID : ")
		sql="select * from users where id='"+ids+"'"
		cursor.execute(sql)
		user_data=cursor.fetchone()
		name=input("Old Name is : "+user_data[1]+" New Name : ")
		email=input("Old Email is : "+user_data[2]+" New Email : ")
		age=input("Old Age is : "+user_data[3]+" New Age : ")
		work=input("Old Work is : "+user_data[4]+" New Work : ")
		sql="UPDATE users set name='"+name+"',email='"+email+"',age='"+age+"',work='"+work+"' where id='"+ids+"'"

		cursor.execute(sql)
		self.db.commit()

	def DeleteuseData(self):
		cursor=self.db.cursor()
		ids=input("Enter ID ")
		sql="DELETE from users where id='"+ids+"'"
		cursor.execute(sql)
		self.db.commit()

dbOper=DBOperation()
print("=========Program Start============")
exit=False

while exit!=True:

	input_data=dbOper.showMenu()

	if input_data=="1":
		dbOper.addUsers()

	if input_data=="2":
		dbOper.showUsers()	
	
	if input_data=="3":
		dbOper.updateUser()
	
	if input_data=="4":
		dbOper.DeleteuseData()		
	
	if input_data=="5":
		exit=True


