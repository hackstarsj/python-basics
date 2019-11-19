#importing library
import re
program_run=True
previous=0
print("Enter Equation Type Quit for Exit the Program")
while program_run!=False:

	if previous==0:
		data=input("Enter Math Equation : ")
		data=re.sub('[a-zA-Z,:()" "]','',data)

	else:
		data=input(previous)
		data=re.sub('[a-zA-Z,:()" "]','',data)
		data=str(previous)+str(data)
	if data=="quit":
		program_run=False
	
	#using eval function to do calculation
	previous=eval(data)


