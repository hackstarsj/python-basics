print("Hello World in Python")

a=5
b=10
sum=a+b
print(sum)

#let's see in string

a="5"
b="10"
sum=a+b
print(sum)

#convert string into integer
sum=int(a)+int(b)
print(sum)

string="Hello Python String"
print(string)

a=10.5
b=11.15
sum=a+b
print(sum)

string_esc='Hello Esacpe\'s String'
print(string_esc)

string_next_line="Hello \n Next Line \n String"
print(string_next_line)

string_tab_string="Hello \t Tab String"
print(string_tab_string)

string_1="Hello "
string_2="Python"
string_join=string_1+string_2
print(string_join)

string_1="This Item "
string_2="Cost is "
integer_1=10
string_3=" RS"
print(string_1+string_2+str(integer_1)+string_3)

string_data="Hello World in Python"
string_to_array=string_data.split(" ")
print(string_to_array)

#boolean datatypes

print(1==1)
print(1==2)
print(True == True)
print(True == "True")
print(str(True) == "True")
print(1 is 1)
print(1 is 2)

#list in python
list_data=["Rahul","Sanjeev","Vishal"]
print(list_data)
print("My Name is : "+list_data[0])
print("My Name is : "+list_data[1])
print("My Name is : "+list_data[2])

#dictionary

dict_data={"name":"Rahul","age":"25","Interest":"Coding"}
print(dict_data)
print("Name is : "+dict_data["name"])
print("Age is : "+dict_data["age"])
print("Interest is : "+dict_data["Interest"])


#inbuilt function

print("Print is Used for Print Data in Console")
int_data=5
#str convert int to string
print(str(int_data))

list_data=["Rahul","Sanjeev","Vishal"]
#len print length of list
print(len(list_data))

list_data=[42,423,42,52,594,35,54,52]
#sorted sort the list
print(sorted(list_data))

list_data=["BA","AA","JK","DD","ED"]
print(sorted(list_data))

#create own function
def myFirstFunction():
	print("My First Function Call")


myFirstFunction()	
myFirstFunction()	
myFirstFunction()	

#create parameter function
def mySecondFunctionWithParam(data1,data2):
	print("This is First "+data1)
	print("This is Second "+data2)

mySecondFunctionWithParam("Data 1","Data 2")
mySecondFunctionWithParam("Hello","World")


#default Argument(Parameter) function

def myDefaultArgumentFunction(name="Unknown",work="Unknown Work"):
	print("Name is :"+name)
	print("Work is :"+work)


myDefaultArgumentFunction()
myDefaultArgumentFunction("Rahul","Coder")		
myDefaultArgumentFunction("Rahul")

#pass data with keyword argument
myDefaultArgumentFunction(work="coding")
myDefaultArgumentFunction(work="Coding",name="Aman")
myDefaultArgumentFunction(name="Vishal",work="Coding")

#function with return data

def multiply_no(num_1,num_2):
	return num_1*num_2

def add_no(num_1,num_2):
	return num_1+num_2	

def subtract_no(num_1,num_2):
	return num_1-num_2

def divide_no(num_1,num_2):
	return num_1/num_2	

print(multiply_no(10,4))
print(add_no(4,5))
print(subtract_no(10,5))
print(divide_no(20,5))	

#if statement
check_cond=True

if check_cond==True:
	print("This is True Statement")

check_cond=False

#else statement
if check_cond==True:
	print("This is True Statement")
else:
	print("This is False Statement")

#elif

check_cond=False

if check_cond==True:
	print("This is True Statement")
elif check_cond==False:
	print("This is False Statement")
elif check_cond=="Hello":
	print("This is a Word Hello")
elif check_cond=="World":
	print("This is a Word World")	


#some operator
#for check greater than ">"
#for check smaller than "<"
#for check equal to "=="
#for check not equal to "!="
#for check greater than equal ">="
#for smaller than equal to "<="
a=10
b=20

if a==b:
	print("A and B Equal")

if a!=b:
	print("A not Equal to B")

if a>=b:
	print("A is Greater than Equal to B")

if a<=b:
	print("A is Smaller than Equal to B")

if a>b:
	print("A is Greater to B")

if a<b:
	print("A is Smaller to B")


#for loop

#range is a function for running loop in a range
for x in range(5):
	print(x)

#loop inside loop nested loop
for x in range(5):
	for y in range(10): 
		print(str(x)+"."+str(y))

#now stop loop in middle using break
#it run until 5 break stop the loop
for x in range(10):
	if x==6:
		break
	print(x)

#now skip some item in loop using continue
#in this it skip 5 and 6
for x in range(10):
	if x==5:
		continue

	if x==6:
		continue

	print(x)

#for each loop for printing each item in list

data_list=["Rahul","Aman","Sanjeev","Vishal"]
 
for item in data_list:
	print("My name is "+item)

data_list=[1,2,3,4,5,6,7]
 
for item in data_list:
	print("My name is "+str(item))

#while loop

a=10
b=0

while b!=a:
	print("Value of B is "+str(b))
	b=b+1

check_cond=True
i=0

while check_cond!=False:
	print("Value of I is : "+str(i))

	if(i==10):
		check_cond=False

	i=i+1							