import time
import os
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf

timenow = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
timetext = timenow.strftime('%Y-%m-%d')

fp = open(os.getcwd() + "/crawler/file/CGTN.txt", "w+")

CGTN_Homepage = urlopen("https://www.cgtn.com/")
CGTN_Homepage_Obj = bf(CGTN_Homepage.read(), 'html.parser')

CGTN_Aricle_Url_qc = []

for i in CGTN_Homepage_Obj.find_all('a', {"data-action": "News_Click"}, href=True):
    if not i['href'] in CGTN_Aricle_Url_qc:
        if len(i.get('class')) == 0 and i['href'].find("special") == -1 and i['href'].find("event") == -1:
            CGTN_Aricle_Url_qc.append(i['href'])


def Get_Article_CGTN(CGTN_Aricle_Url):
    CGTN_Article = urlopen(CGTN_Aricle_Url)

    CGTN_Article_Obj = bf(CGTN_Article.read(), 'html.parser')

    CGTN_Article_Titlle = CGTN_Article_Obj.find('div', class_="news-title").string

    print('<h1 class=\"print\">', CGTN_Article_Titlle, '</h1>', file=fp)
    print('<hr>', file=fp)
    print("<a class=\"no-print\" href=\"", CGTN_Aricle_Url, "\">", "原文链接", "</a>", "\n\n", file=fp)

    CGTN_Article_qc = []

    for i in CGTN_Article_Obj.find_all('p', _class=False):
        if not i.string in CGTN_Article_qc:
            CGTN_Article_qc.append(i)

    for a in CGTN_Article_qc:
        if (a):
            if a.string != ' Share ' and a.string != 'Copied' and not a.get('class'):
                print(a, "\n", file=fp)
    print('<br>', file=fp)


for article_id in range(0, 2):
    Get_Article_CGTN(CGTN_Aricle_Url_qc[article_id])

print("CGTN completed")
