import requests
import time
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

file_req=requests.get("https://www.google.co.in/search?q=python&sxsrf=ACYBGNRehqcWkSEcZ4c13bo_p3GomRgS_g:1574615472757&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj2haXfq4PmAhVaILcAHcT9DZ8Q_AUoAXoECGgQAw&biw=1536&bih=674&dpr=1.25")
file=open("file_scrap.html","w")
data=file_req.text
file.write(data)
file.close()
soup=BeautifulSoup(data,"html.parser")
for img in soup.find_all("img"):
	print("Src ",img.get("src"))
	req2=requests.get(img.get("src"))
	img_file=Image.open(BytesIO(req2.content))
	ts = time.time()
	img_file.save("images/"+"img_"+str(ts)+"."+img_file.format)
