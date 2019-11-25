import requests
from bs4 import BeautifulSoup
search_term=input("Enter Search Term : ")
request_data=requests.get("https://www.google.co.in/search?sxsrf=ACYBGNQlAJTI0BE8rSD7xzkE1O7-5UhD-w%3A1574615235505&source=hp&ei=w7jaXenAHKCe4-EPi9ezqA0&q="+search_term+"&oq="+search_term+"&gs_l=psy-ab.3..35i39l2j0i67l8.231723.235740..236136...2.0..0.409.2720.0j1j4j3j1......0....1..gws-wiz.....10..35i362i39j0i131j0.eCKyY3hHvFY&ved=0ahUKEwiprpLuqoPmAhUgzzgGHYvrDNUQ4dUDCAY&uact=5")
soup = BeautifulSoup(request_data.text, 'html.parser')

for div in soup.find_all(attrs={"class": "ZINbbc"}):
	#print(div)
	title=div.find(attrs={"class":"vvjwJb"})
	desc=div.find(attrs={"class":"s3v9rd"})
	link=div.find("a")
	if title!=None:
		print("Title : "+title.get_text())
		print("Description : "+desc.get_text())
		print("Link : "+str(link.get('href')).replace("/url?q=",""))
		print("\n=============================\n")

#now let's scrap more website
request_data2=requests.get("https://finance.yahoo.com/commodities")
soup2 = BeautifulSoup(request_data2.text, 'html.parser')
file=open("scarp_2.html","w")
file.write(soup2.prettify())
file.close()
#print(soup2.prettify())
for tr in soup2.find_all(attrs={"class":"BdT"}):
	symbol=tr.find(attrs={"class":"Fw(b)"})
	name=tr.find(attrs={"class":"data-col1"})
	price=tr.find(attrs={"class":"data-col2"})
	print("Symbol : "+symbol.get_text())
	print("Name : "+name.get_text())
	print("Last Price : "+price.get_text())
	print("\n=====================\n")
	#break