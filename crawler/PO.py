import time
import os
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
timenow = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)) 
timetext = timenow.strftime('%Y-%m-%d')

fp=open(os.getcwd()+"/crawler/file/PO.txt","w+")


PO_Homepage=urlopen("http://opinion.people.com.cn/GB/8213/49160/index.html")
PO_Homepage_Obj=bf(PO_Homepage.read(),'html.parser')
PO_Base='http://opinion.people.com.cn'

PO_Aricle_Url=[]
PO_Aricle_Url_qc=[]

for i in PO_Homepage_Obj.find_all('a',href=True):
    if(i.parent.get('class') and len(i.parent.get('class'))!=0):
        if(i.parent.get('class')[0]=='t14l14'):
            PO_Aricle_Url.append(PO_Base+i['href'])



def Get_Article_PO(PO_Article_Url):
    PO_Aricle=urlopen(PO_Article_Url)

    PO_Aricle_Obj=bf(PO_Aricle.read().decode('GB2312','ignore'),'html.parser')

    print('<h1 class=\"print\">',PO_Aricle_Obj.find_all('h1')[1].string,'</h1>',file=fp)
    print('<hr>',file=fp)
    print("<div class=\"author no-print\">",PO_Aricle_Obj.find('div',class_='author cf').string,"</div>","\n\n",file=fp)
    print("<a class=\"no-print\" href=\"",PO_Article_Url,"\">","原文链接","</a>","\n\n",file=fp)


    for i in PO_Aricle_Obj.find_all('p'):
        if(i.string):
            print(i,file=fp)
    print('<br>',file=fp)


for i in range(0,3):
    Get_Article_PO(PO_Aricle_Url[i])

print("PO completed")