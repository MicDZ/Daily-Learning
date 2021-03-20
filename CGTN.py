import time

from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
CGTN_Homepage=urlopen("https://www.cgtn.com/")
CGTN_Homepage_Obj=bf(CGTN_Homepage.read(),'html.parser')

fp=open("./"+time.strftime("%Y-%m-%d", time.localtime())+".md","w+")

CGTN_Aricle_Url_qc=[]


for i in CGTN_Homepage_Obj.find_all('a',{"data-action":"News_Click"},href=True):
    if(not i['href'] in CGTN_Aricle_Url_qc):
        if(len(i.get('class'))==0 and i['href'].find("special")==-1 and i['href'].find("event")==-1):
            CGTN_Aricle_Url_qc.append(i['href'])


for article_id in range(0,2):
    
    CGTN_Aricle_Url=CGTN_Aricle_Url_qc[article_id]
    CGTN_Article=urlopen(CGTN_Aricle_Url)

    CGTN_Article_Obj=bf(CGTN_Article.read(),'html.parser')
    
    CGTN_Article_Titlle=CGTN_Article_Obj.find('div',class_="news-title").string

    print('### ',CGTN_Article_Titlle,file=fp)

    print(CGTN_Aricle_Url,file=fp)

    
    CGTN_Article_qc=[]

    for i in CGTN_Article_Obj.find_all('p',_class=False):
        if not i.string in CGTN_Article_qc:
            CGTN_Article_qc.append(i.string)


    for a in CGTN_Article_qc:
        if(a): 
            if(a!=' Share ' and a!='Copied'):
                print(a,"\n",file=fp)



fp.close()



