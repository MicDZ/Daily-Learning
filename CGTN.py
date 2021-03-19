from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
CGTN_Homepage = urlopen("https://www.cgtn.com/china")
CGTN_Homepage_Obj = bf(CGTN_Homepage.read(),'html.parser')

CGTN_Aricle_Url=CGTN_Homepage_Obj.find_all('a',{"data-action":"News_Click"},href=True)[3]['href']

CGTN_Article=urlopen(CGTN_Aricle_Url)

CGTN_Article_Obj=bf(CGTN_Article.read(),'html.parser')

fp=open("./data.txt","w")


for a in CGTN_Article_Obj.find_all('p',_class=False):
    if(a.string): 
        print(a.string,file=fp)

fp.close()



