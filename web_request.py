import requests
data=requests.get("https://www.google.co.in/")
file=open("response.html","w")
file.write(data.text)
file.close()


#python with get param
user_input=input("Enter Input")
data=requests.get("https://www.google.co.in/search?sxsrf=ACYBGNQlAJTI0BE8rSD7xzkE1O7-5UhD-w%3A1574615235505&source=hp&ei=w7jaXenAHKCe4-EPi9ezqA0&q="+str(user_input)+"&oq="+str(user_input)+"&gs_l=psy-ab.3..35i39l2j0i67l8.231723.235740..236136...2.0..0.409.2720.0j1j4j3j1......0....1..gws-wiz.....10..35i362i39j0i131j0.eCKyY3hHvFY&ved=0ahUKEwiprpLuqoPmAhUgzzgGHYvrDNUQ4dUDCAY&uact=5")
file2=open("response_with_getparam.html","w")
file2.write(data.text)
file2.close()

#python with post example
post_data={"Name":"Rahul","Age":"28"}
post_req=requests.post("https://postman-echo.com/post",post_data)
print(post_req.text)
#let print headers also
print("Header "+" : "+str(post_req.headers))


#python post with headers
name=input("Enter Name")
age=input("Enter Name")
post_data={"Name":name,"Age":age}
headers={"AuthToken":"ABCAUTH","Authorization":"XYZAUTH"}
post_req=requests.post("https://postman-echo.com/post",post_data,headers=headers)
print(post_req.text)
print("Headers : "+str(post_req.headers))

#upload file using request
files={"file1":open("csv_file.csv","r"),"file2":open("demo_data.txt")}
some_data={"data1":"value1","data2":"value2"}
post_upload=requests.post("https://postman-echo.com/post",some_data,files=files)
print(post_upload.text)
