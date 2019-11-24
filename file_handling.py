import os
import json
import csv
#writing data in file
#in this all data of file will be remove and new contents will be overwritten 
file=open("demo_data.txt","w")

#writing data in file
file.write("This is Some Demo Content Writing in file")

#closing file
file.close()

#read file content
file1=open("demo_data.txt","r")

#printing data of file
print("Data is : "+file1.read())
file1.close()

#appending data in file
#in this method it just add extra contents at the end of file 
file2=open("demo_data.txt","a")
file2.write("\nThis is Extra Data appending in file")
file2.write("\n This is Again Extra Data appending in file")
file2.write("\nThis is Again and Again Extra Data appending in file")
file2.close()

#again printing data
file3=open("demo_data.txt","r")
print("New Data is : "+file3.read())
file3.close()

#now reading some content of file
file4=open("demo_data.txt","r")
print(file4.read(15))
file4.close()

#now reading file content line by line
file5=open("demo_data.txt","r")

#printing content from line by line
print(file5.readline())
print(file5.readline())
print(file5.readline())
print(file5.readline())
file5.close()

#printing content by for loop
file6=open("demo_data.txt","r")
i=1
for line in file6:
	#printing content line by line
	print("Line : "+str(i)+" : "+line)
	i=i+1
file6.close()


#delete file also check file exist
if os.path.exists("demo_data.txt"):
	print("File Exist")
	#deleting file
	#os.remove("demo_data.txt")
else:
	print("File Not Exist")	


person_dict={"name":"Rahul","age":"28","work":"Programmer"}

#converting dict to json
json_file=open("json_data.json","w")
json_data=json.dumps(person_dict)
json_file.write(json_data)
json_file.close()

#now let's read json data from file and convert into dict
json_read=open("json_data.json","r")
json_data_read=json_read.read()

#convert json into dict
json_dict=json.loads(json_data_read)
print(json_dict['name'])

#writing list into json file
lang_list=["Python","PHP","C","C++","Java"]
json_list=open("json_list.json","w")
json_list.write(json.dumps(lang_list))
json_list.close()

#reading json list data now and convert into list

json_read_list=open("json_list.json","r")
json_list_data=json_read_list.read()

#convert json into list
data_list=json.loads(json_list_data)
print(data_list[1])


#let's see example of csv
#writing a data in csv file
#if you don't add newline="" it will add extra line always
with open("csv_file.csv","w",newline="") as csv_file:
	writer=csv.writer(csv_file)
	list_1=["Name","Age","Work","Exp"]
	list_2=["Rahul","27","Python","4"]
	list_3=["Vishal","24","PHP","2"]
	list_4=["Aman","23","JAVA","1"]
	list_5=["Ankit","25","C","3"]

	#now writing into file
	writer.writerow(list_1)	
	writer.writerow(list_2)
	writer.writerow(list_3)
	writer.writerow(list_4)
	writer.writerow(list_5)

#reading csv file
with open("csv_file.csv","r") as csv_file_read:
	csv_reader=csv.reader(csv_file_read)
	for line in csv_reader:
		print(line)
