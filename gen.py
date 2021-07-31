import time
import os
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf

timenow = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
timetext = timenow.strftime('%Y-%m-%d')

print(os.getcwd())

Home_page = os.getcwd() + "/Daily-Learning-Site/index.html"  # 主页
History_page = os.getcwd() + "/Daily-Learning-Site/history.html"  # 往期主页
Stored_page = os.getcwd() + "/Daily-Learning-Site/source/" + timetext + ".html"  # 往期

os.system("touch " + Home_page)

Home = open(Home_page, "w+")  # 主页
History = open(History_page, "w+")  # 往期主页
Stored = open(Stored_page, "w+")  # 往期


def print_time(site):
    print("<br><p class=\"right\">更新日期", timetext, "</p></div>", file=site)


# 搜索爬虫目录下的所有爬虫
crawler = []


def search(source, list, ex):
    files = os.listdir(source)
    for i in files:

        filename, extension = os.path.splitext(i)
        # print(extension)
        if extension == ex:
            list.append(filename)


search(os.getcwd() + "/crawler", crawler, '.py')

crawler.sort()

# 运行所有的爬虫

for file in crawler:
    os.system("python3 " + os.getcwd() + "/crawler/" + file + ".py")

# 输出主页
head = open(os.getcwd() + "/src/head.txt", "r").read()
tail = open(os.getcwd() + "/src/tail.txt", "r").read()
head_son = open(os.getcwd() + "/src/head_son.txt", "r").read()
tail_history = open(os.getcwd() + "/src/tail_history.txt", "r").read()

print(head, file=Home)

for file in crawler:
    file_data = open(os.getcwd() + "/crawler/file/" + file + ".txt")
    print(file_data.read(), file=Home)
print_time(Home)
print(tail, file=Home)

# 输出往期

print(head_son, file=Stored)

for file in crawler:
    file_data = open(os.getcwd() + "/crawler/file/" + file + ".txt")
    print(file_data.read(), file=Stored)
print_time(Stored)

print(tail, file=Stored)

# 输出往期主页

Stored_list = []

search(os.getcwd() + "/Daily-Learning-Site/source/", Stored_list, '.html')

print(head, file=History)

Site_Url_Base = "https://learn.micdz.cn/source/"

Stored_list.sort()
for site in Stored_list:
    print("\t\t\t<li>", "<a href=\"", Site_Url_Base + site, "\">", site, "</a>", "</li>", file=History)

print_time(History)

print(tail_history, file=History)

# 复制文件

# os.system("rm "+os.getcwd()+"/Daily-Learning-Site/index.html")
# os.system("rm "+os.getcwd()+"/Daily-Learning-Site/history.html")

# print("cp "+os.getcwd()+"/.temp/index.html "+os.getcwd()+"/Daily-Learning-Site/index.html")

# os.system("cp "+os.getcwd()+"/.temp/index.html "+os.getcwd()+"/Daily-Learning-Site/index.html")
# os.system("cp "+os.getcwd()+"/.temp/"+timetext+".html "+os.getcwd()+"/Daily-Learning-Site/source/"+timetext+".html")


# os.system("cp "+os.getcwd()+"/.temp/history.html "+os.getcwd()+"/Daily-Learning-Site/history.html")
