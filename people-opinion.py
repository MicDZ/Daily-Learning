import time
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
PO_Homepage=urlopen("http://opinion.people.com.cn/GB/8213/49160/index.html")
PO_Homepage_Obj=bf(PO_Homepage.read(),'html.parser')
PO_Base='http://opinion.people.com.cn'

PO_Aricle_Url=[]
PO_Aricle_Url_qc=[]

for i in PO_Homepage_Obj.find_all('a',href=True):
    if(i.parent.get('class') and len(i.parent.get('class'))!=0):
        if(i.parent.get('class')[0]=='t14l14'):
            PO_Aricle_Url.append(PO_Base+i['href'])


fp=open("./src/"+time.strftime("%Y-%m-%d-PO", time.localtime())+".md","w+")

def Get_Article_PO(PO_Article_Url):
    PO_Aricle=urlopen(PO_Article_Url)

    PO_Aricle_Obj=bf(PO_Aricle.read().decode('GB2312','ignore'),'html.parser')

    print("### "+PO_Aricle_Obj.find_all('h1')[1].string,file=fp)

    print(PO_Aricle_Obj.find('div',class_='author cf').string,file=fp)

    print(PO_Article_Url,file=fp)

    for i in PO_Aricle_Obj.find_all('p'):
        if(i.string):
            print(i.string.replace('\t',''),file=fp)


for i in range(0,3):
    Get_Article_PO(PO_Aricle_Url[i])

fp.close()