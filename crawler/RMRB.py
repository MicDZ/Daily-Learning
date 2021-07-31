import time
import os
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf

fp = open(os.getcwd() + "/crawler/file/RMRB.txt", "w+")

time_now = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
timetext = time_now.strftime('%Y-%m-%d')
timetext_site = time_now.strftime('%Y-%m/%d/')

RMRB_Pre_Base_Url = "http://paper.people.com.cn/rmrb/html/" + timetext_site
RMRB_Suf_Base_Url = "/nbs.D110000renmrb_"

Weekday = time_now.weekday() + 1

RMRB_Article_Url = []


def remove_duplicate(list):
    tmp = []
    for item in list:
        if item not in tmp:
            tmp.append(item)


def fetch_article_weekends():
    for i in range(2, 5):
        RMRB_Article_Url.append(
            RMRB_Pre_Base_Url + "nw.D110000renmrb_" + time_now.strftime('%Y%m%d_') + '1-0' + str(i) + '.htm')


def fetch_article_weekdays():
    tag = RMRB_Homepage_Obj.find_all('a', id='pageLink', href=True)
    page_id = []

    for site in tag:
        if '评论' in site.string:
            length = len(site['href'])
            page_id = site['href'][length - 6:length - 4]

    for i in range(1, 4):
        RMRB_Article_Url.append(
            RMRB_Pre_Base_Url + "nw.D110000renmrb_" + time_now.strftime('%Y%m%d_') + str(i) + '-' + page_id + '.htm')


def crawl_article():
    for article in RMRB_Article_Url:
        article_page = urlopen(article)
        article_Obj = bf(article_page.read(), 'html.parser')

        print('<h1 class=\"print\">', article_Obj.find_all('h1')[0].string, '</h1>', file=fp)
        print('<hr>', file=fp)
        # author
        # print(article_Obj.find_all('p',class_='sec')[0])
        print("<a class=\"no-print\" href=\"", article, "\">", "原文链接", "</a>", "\n\n", file=fp)

        for i in article_Obj.find_all('p', class_=False):
            if i.string:
                if i.string != 'ios版' and i.string != 'android版' and i.string != '微信小程序':
                    print(i, file=fp)
        time.sleep(0.12)


if __name__ == '__main__':
    # print(RMRB_Pre_Base_Url + timetext_site + RMRB_Suf_Base_Url + "01.html")

    RMRB_Homepage = urlopen(RMRB_Pre_Base_Url + RMRB_Suf_Base_Url + "01.htm")
    RMRB_Homepage_Obj = bf(RMRB_Homepage.read(), 'html.parser')

    if Weekday == 6 or Weekday == 7:
        fetch_article_weekends()
    else:
        fetch_article_weekdays()

    remove_duplicate(RMRB_Article_Url)
    crawl_article()

    print("RMRB completed")
# PO_Aricle_Url=[]
# PO_Aricle_Url_qc=[]
#
# for i in PO_Homepage_Obj.find_all('a',href=True):
#     if(i.parent.get('class') and len(i.parent.get('class'))!=0):
#         if(i.parent.get('class')[0]=='t14l14'):
#             PO_Aricle_Url.append(PO_Base+i['href'])
#
#
#
# def Get_Article_PO(PO_Article_Url):
#     PO_Aricle=urlopen(PO_Article_Url)
#
#     PO_Aricle_Obj=bf(PO_Aricle.read().decode('GB2312','ignore'),'html.parser')
#
#     print('<h1 class=\"print\">',PO_Aricle_Obj.find_all('h1')[1].string,'</h1>',file=fp)
#     print('<hr>',file=fp)
#     print("<div class=\"author no-print\">",PO_Aricle_Obj.find('div',class_='author cf').string,"</div>","\n\n",file=fp)
#     print("<a class=\"no-print\" href=\"",PO_Article_Url,"\">","原文链接","</a>","\n\n",file=fp)
#
#
#     for i in PO_Aricle_Obj.find_all('p'):
#         if(i.string):
#             print(i,file=fp)
#     print('<br>',file=fp)
#
#
# for i in range(0,3):
#     Get_Article_PO(PO_Aricle_Url[i])
#
# print("PO completed")
