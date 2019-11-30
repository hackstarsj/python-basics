import mysql.connector

db=mysql.connector.connect(host="localhost",user="python_tut",passwd="python_password",database="user_details")

#insert data
cursor=db.cursor()
sql="INSERT into users (name,email,age,work) values (%s,%s,%s,%s)"
value=("Rahul","rahul@gmail.com","25","Dev")

#cursor.execute(sql,value)
#db.commit()

#inserting multiple data
sql="INSERT into users (name,email,age,work) values (%s,%s,%s,%s)"
value=[("Rahul","rahul@gmail.com","25","Dev"),("Aman","aman@gmail.com","27","Tester")]

#cursor.executemany(sql,value)
#db.commit()

#fetching all data
cursor.execute("select * from users")
result=cursor.fetchall()

for data in result:
	print(data)


#update data
sql="update users set age='30' where name='Rahul'"
cursor.execute(sql)
db.commit()

#delete data

sql="DELETE from users where name='Rahul'"
cursor.execute(sql)
db.commit()