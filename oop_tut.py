#parent class
class Person:

	def __init__(self,name,gender):
		self.name=name
		self.gender=gender

	def setName(self,name):
		self.name=name

	def setGender(self,gender):
		self.gender=gender

	def getName(self):
		return self.name

	def getGender(self):
		return self.gender
#child class
class Employee(Person):
	def __init__(self,name,gender,salary,is_boss):
		self.is_boss=is_boss
		self.salary=salary
		Person.__init__(self,name,gender)

	def getIsBoss(self):
		return self.is_boss	

	def getSalary(self):
		return self.salary	


# pers=Person()

# pers.setName("Rahul")
# pers.setGender("Male")

# pers2=Person()

# pers2.setName("Vishal")
# pers2.setGender("Male")

# pers3=Person()

# pers3.setName("Sheetal")
# pers3.setGender("FeMale")



# print("Name is : "+pers.getName())
# print("Gender is : "+pers.getGender())	

# print("Name is : "+pers2.getName())
# print("Gender is : "+pers2.getGender())				

# print("Name is : "+pers3.getName())
# print("Gender is : "+pers3.getGender())	

pers=Person("Rahul","Male")
print("Name is : "+pers.getName())
print("Gender is : "+pers.getGender())

emp=Employee("Rahul","Male","10000",False)
emp1=Employee("Vishal","Male","100000",True)
print("Name is : "+emp.getName())
print("Gender is : "+emp.getGender())
print("Salary is : "+emp.getSalary())
if emp.getIsBoss():
	print("Boss is : Yes")
else:	
	print("Boss is : No")

print("Name is : "+emp1.getName())
print("Gender is : "+emp1.getGender())
print("Salary is : "+emp1.getSalary())
if emp1.getIsBoss():
	print("Boss is : Yes")
else:	
	print("Boss is : No")	


class calculator:
	def __init__(self,value1,value2):
		self.value1=value1
		self.value2=value2

	def addNumber(self):
		return self.value1+self.value2

	def MultiPlyNumber(self):
		return self.value1*self.value2

	def subNumber(self):
		return self.value1-self.value2

	def divideNumber(self):
		return self.value1/self.value2

calc=calculator(10,20)
print("Addition : "+str(calc.addNumber()))
print("Multiplication : "+str(calc.MultiPlyNumber()))
print("Subtraction : "+str(calc.subNumber()))
print("Divide : "+str(calc.divideNumber()))
