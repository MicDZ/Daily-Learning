import time

from urllib.request import urlopen
from bs4 import BeautifulSoup as bf


CGTN_Homepage=urlopen("https://www.cgtn.com/")
CGTN_Homepage_Obj=bf(CGTN_Homepage.read(),'html.parser')

fp=open("./source/"+time.strftime("%Y-%m-%d", time.localtime())+".html","w+")
cu=open("./index.html","w+")


print("<!DOCTYPE html>",file=fp)
print("<html>",file=fp)
print("<head>",file=fp)
print("\t<meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" /><title>Template</title><meta name=\"author\" content=\"MicDZ\"><link rel=\"stylesheet\" href=\"css/index.css\" /><script src=\"js/index.js\"></script>",file=fp)
print("</head>",file=fp)
print("<body>",file=fp)
print("\t<div class=\"container\">",file=fp)

print("<!DOCTYPE html>",file=cu)
print("<html>",file=cu)
print("<head>",file=cu)
print("\t<meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" /><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" /><title>Template</title><meta name=\"author\" content=\"MicDZ\"><link rel=\"stylesheet\" href=\"css/index.css\" /><script src=\"js/index.js\"></script>",file=cu)
print("</head>",file=cu)
print("<body>",file=cu)
print("\t<div class=\"container\">",file=cu)

CGTN_Aricle_Url_qc=[]

for i in CGTN_Homepage_Obj.find_all('a',{"data-action":"News_Click"},href=True):
    if(not i['href'] in CGTN_Aricle_Url_qc):
        if(len(i.get('class'))==0 and i['href'].find("special")==-1 and i['href'].find("event")==-1):
            CGTN_Aricle_Url_qc.append(i['href'])


def Get_Article_CGTN(CGTN_Aricle_Url):
    CGTN_Article=urlopen(CGTN_Aricle_Url)

    CGTN_Article_Obj=bf(CGTN_Article.read(),'html.parser')
    
    CGTN_Article_Titlle=CGTN_Article_Obj.find('div',class_="news-title").string

    print('<h1>',CGTN_Article_Titlle,'</h1>',file=fp)
    print('<hr>',file=fp)
    print("<a href=\"",CGTN_Aricle_Url,"\">",CGTN_Aricle_Url,"</a>","\n\n",file=fp)

    print('<h1>',CGTN_Article_Titlle,'</h1>',file=cu)
    print('<hr>',file=cu)
    print("<a href=\"",CGTN_Aricle_Url,"\">",CGTN_Aricle_Url,"</a>","\n\n",file=cu)
    
    CGTN_Article_qc=[]

    for i in CGTN_Article_Obj.find_all('p',_class=False):
        if not i.string in CGTN_Article_qc:
            CGTN_Article_qc.append(i)


    for a in CGTN_Article_qc:
        if(a): 
            if(a.string!=' Share ' and a.string!='Copied' and not a.get('class')):
                print(a,"\n",file=fp)
                print(a,"\n",file=cu)
    print('<br>',file=fp)
    print('<br>',file=cu)

for article_id in range(0,2):
    Get_Article_CGTN(CGTN_Aricle_Url_qc[article_id])
    





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

    print('<h1>',PO_Aricle_Obj.find_all('h1')[1].string,'</h1>',file=fp)
    print('<hr>',file=fp)
    print("<div class=\"author\">",PO_Aricle_Obj.find('div',class_='author cf').string,"</div>","\n\n",file=fp)
    print("<a href=\"",PO_Article_Url,"\">",PO_Article_Url,"</a>","\n\n",file=fp)

    print('<h1>',PO_Aricle_Obj.find_all('h1')[1].string,'</h1>',file=cu)
    print('<hr>',file=cu)
    print("<div class=\"author\">",PO_Aricle_Obj.find('div',class_='author cf').string,"</div>","\n\n",file=cu)
    print("<a href=\"",PO_Article_Url,"\">",PO_Article_Url,"</a>","\n\n",file=cu)

    for i in PO_Aricle_Obj.find_all('p'):
        if(i.string):
            print(i,file=fp)
            print(i,file=cu)
    print('<br>',file=fp)
    print('<br>',file=cu)

for i in range(0,3):
    Get_Article_PO(PO_Aricle_Url[i])

print("\t\t</div>",file=fp)
print("</body>",file=fp)
print("</html>",file=fp)

print("\t\t</div>",file=cu)
print("</body>",file=cu)
print("</html>",file=cu)
fp.close()