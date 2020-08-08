from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import cssutils
import re
# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
#we create the driver specifying the origin of chrome browser
driver = webdriver.Chrome("C:/Scraping/chromedriver.exe", chrome_options=option)
driver.get("https://soundcloud.com/ironmaidenmusic/albums")
driver.maximize_window()
time.sleep(1)
#We make a slow scroll to the end of the page
iter=1
while True:
        scrollHeight = driver.execute_script("return document.documentElement.scrollHeight")
        Height=250*iter
        driver.execute_script("window.scrollTo(0, " + str(Height) + ");")
        if Height > scrollHeight:
            print('End of page')
            break
        time.sleep(1)
        iter+=1
#we get the internal html code of the body        
body = driver.execute_script("return document.body")
source = body.get_attribute('innerHTML') 
#we create a flat file and write the header
file1 = open("C:\\Scraping\\Files\\Albums.txt","w", encoding='utf-8') 
file1.write("Album,Cover,Published"+'\n')
#we iterate through the different albums with beautifulsoup and load the data into the flat file
soup = BeautifulSoup(source, "html.parser")
for album in soup.find_all("li", "soundList__item"):
    album_title = album.find("a", class_="sound__coverArt")
    album_link = album_title['href']
    title = album_title.div.span['aria-label']
    style = album_title.div.span['style']
    styles = cssutils.parseStyle(style)
    url = styles['background-image']
    opacity = styles['opacity']
    album_date = album.find("div", class_="soundTitle__usernameTitleContainer")
    date = album_date.find("span", class_="releaseDateCompact sc-type-light sc-font-light").span.text
    if opacity == '1':
        file1.write(title+','+url[4:-1]+','+'https://soundcloud.com'+album_link+','+date+'\n')
#finally we close the file and the driver
file1.close()
driver.close()