# 每日语料积累

- [X]  每日爬取人民日报文章
- [X] 每日爬取CGTN文章
- [X] 每日自动发布到 [Daily-Learning-Site](https://www.github.com/MicDZ/Daily-Learning-Site)
- [ ] 实现基于语意识别的文章爬取

# 参与项目
## 运行
### 依赖

python3、beautifulsoup4

```
pip install beautifulsoup4 
```

### 将项目克隆到本地

```
git clone https://www.gituhb.com/MicDZ/Daily-Learning.git
```

### 导入部署项目

进入项目后将[Daily-Learning-Site](https://www.github.com/MicDZ/Daily-Learning-Site)克隆到根目录

```
cd Daily-Learning
git clone https://www.gituhb.com/MicDZ/Daily-Learning-Site.git
```

### 运行

```
python gen.py
```
## 添加爬虫

* 生成文章的临时目录为`/crawler/file`。指定地址的代码为
  ```py
  open(os.getcwd() + "/crawler/file/Site_Name.txt", "w+")
  ```

* 以HTML标签的格式保存文章。
* 不在最终打印结果中出现的内容，标签的`class`设为`no-print`。
* 将爬虫放入 `crawler`，检查无误后提交PR。

