# 每日语料积累

- [X]  每日爬取人民日报文章
- [X] 每日爬取CGTN文章
- [X] 每日自动发布到 [Daily-Learning-Site](https://www.github.com/MicDZ/Daily-Learning-Site)


# 参与项目
## 运行
0. 依赖

python3、beautifulsoup4

```
pip install beautifulsoup4 
```

1. 将项目克隆到本地

```
git clone https://www.gituhb.com/MicDZ/Daily-Learning.git
```

2. 进入项目后将[Daily-Learning-Site](https://www.github.com/MicDZ/Daily-Learning-Site)克隆到根目录

```
cd Daily-Learning
git clone https://www.gituhb.com/MicDZ/Daily-Learning-Site.git
```

3. 运行gen.py

```
python gen.py
```
## 添加爬虫

* 生成文章的临时目录为`/crawler/file`。指定地址的格式为`open(os.getcwd() + "/crawler/file/Site_Name.txt", "w+")`。
* 生成HTML代码。
* 不在最终打印结果中出现的内容，标签的`class`设为`no-print`。
* 将爬虫放入 `crawler`，检查无误后提交PR。

