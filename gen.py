import time
import os
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
timenow = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)) 
timetext = timenow.strftime('%Y-%m-%d')

os.system("touch "+os.getcwd()+"/Daily-Learning-Site/"+timetext+".html")

Site_index=open(os.getcwd()+"/Daily-Learning-Site/index.html","w+") # 主页
History=open(os.getcwd()+"/Daily-Learning-Site/history.html","w+") # 往期主页
Site=open(os.getcwd()+"/Daily-Learning-Site/"+timetext+".html","w+") # 往期

def print_time(site):
    print("<br><p class=\"right\">更新日期",timetext,"</p></div>",file=site)


# 搜索爬虫目录下的所有爬虫
crawler=[]

def search(source,list):
    files = os.listdir(source)
    for i in files:
        # print(i)
        filename,extension=os.path.splitext(i)
        fullname=os.path.join(source,filename)
        if(filename!='.DS_Store' and filename!="file"):
            list.append(filename)

search(os.getcwd()+"/crawler",crawler)

crawler.sort()

# 运行所有的爬虫

for file in crawler:
    os.system("python3 "+os.getcwd()+"/crawler/"+file+".py")


# 输出主页
head=open(os.getcwd()+"/src/head.txt", "r").read()
tail=open(os.getcwd()+"/src/tail.txt", "r").read()


print(head,file=Site_index)

for file in crawler:
    file_data=open(os.getcwd()+"/crawler/file/"+file+".txt")
    print(file_data.read(),file=Site_index)
print_time(Site_index)
print(tail,file=Site_index)

# 输出往期
head_son=open(os.getcwd()+"/src/head_son.txt", "r").read()

print(head_son,file=Site)

for file in crawler:
    file_data=open(os.getcwd()+"/crawler/file/"+file+".txt")
    print(file_data.read(),file=Site)
print_time(Site)

print(tail,file=Site)

# 输出往期主页

history_page=[]

search(os.getcwd()+"/Daily-Learning-Site/source/",history_page)

print(head,file=History)

Site_Url_Base="https://learn.micdz.cn/source/"

history_page.sort()
for site in history_page:
    print("\t\t\t<li>","<a href=\"",Site_Url_Base+site,"\">",site,"</a>","</li>",file=History)

print_time(History)

print(tail,file=History)


# 复制文件

# os.system("rm "+os.getcwd()+"/Daily-Learning-Site/index.html")
# os.system("rm "+os.getcwd()+"/Daily-Learning-Site/history.html")

# print("cp "+os.getcwd()+"/.temp/index.html "+os.getcwd()+"/Daily-Learning-Site/index.html")

# os.system("cp "+os.getcwd()+"/.temp/index.html "+os.getcwd()+"/Daily-Learning-Site/index.html")
# os.system("cp "+os.getcwd()+"/.temp/"+timetext+".html "+os.getcwd()+"/Daily-Learning-Site/source/"+timetext+".html")



# os.system("cp "+os.getcwd()+"/.temp/history.html "+os.getcwd()+"/Daily-Learning-Site/history.html")