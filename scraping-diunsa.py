import time
from selenium import webdriver
from bs4 import BeautifulSoup

#print("Ingrese ek parametro correcto")
#nombre = input()
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
browser = webdriver.Chrome("C:/Scraping/chromedriver.exe", chrome_options=option)
#browser.get("https://www.diunsa.hn/es/belleza-y-salud/bioseguridad?O=OrderByReleaseDateDESC".format(nombre))
browser.get("https://www.diunsa.hn/es/belleza-y-salud/bioseguridad?O=OrderByReleaseDateDESC")
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=True
while(match):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=False

source_data = browser.page_source
soup = BeautifulSoup(source_data,"html.parser")
if(soup.findAll(['script', 'style'])):
    [x.extract() for x in soup.findAll(['script', 'style'])]

if(soup.findAll(['meta'])):
    [y.extract() for y in soup.findAll(['meta'])]

if(soup.findAll(['noscript'])):
    [z.extract() for z in soup.findAll(['noscript'])]

if(soup.findAll(['link'])):
    [a.extract() for a in soup.findAll(['link'])]

response = []
#for item in soup.select('div#ResultItems_12247047  >div >ul >li >div'):
for item in soup.find_all("div", "contentShelve globalShelves checked"):
    result={}
    #result['nombre']=item.select_one("div#ResultItems_12247047 >div >ul >li >div > div.productName >a").title.strip()
    #result['precio']=item.select_one("div#ResultItems_12247047 >div >ul >li >div > div.priceProduct >a >span ").text.strip()
    result['nombre']="hola"
    response.append(result)

print(response)
print(len(response))
browser.close()
