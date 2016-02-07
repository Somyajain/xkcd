import requests #requests module imported
import bs4 #importing beautifulsoup module
import os # importing os module
from tqdm import * #importing all functions from tqdm module
start=input('Enter the first chapter:') #taking input from user
end=input('Enter the last chapter:')
os.chdir('C:\Users\sony\Desktop')
if not os.path.exists("C:\Users\sony\Desktop\\xkcd comics"):
    os.mkdir('xkcd comics')
os.chdir('C:\Users\sony\Desktop\\xkcd comics')

for x in tqdm(range(start,end+1)):
    r = requests.get("https://xkcd.com/"+str(x)+'/')
    soup=bs4.BeautifulSoup(r.content,"lxml")
    comic=soup.find(id='comic')
    title=soup.find(id='ctitle')
    name=title.get_text()
    imgsrc=comic.img.get('src')
    
    comic= open(name +'.jpeg',"wb+")
    comic2=requests.get('https:'+imgsrc)
    comic.write(comic2.content)
    comic.close()
