# -*- codeing = utf-8 -*-
# @Time: 2021/6/9 0009 9:53
# @Author: Delon
# @File: parseHTML.py
# @software: PyCharm

# 网页分析
from bs4 import BeautifulSoup
import re


def parse(html):
    # with open("./pages/douBanMovieTop250.html", "rb") as f:
    #     file = f.read().decode("utf-8")
    #     bs = BeautifulSoup(file, "html.parser")
    #     # result = bs.a.string
    #     result = bs.head.content

    # re练习 START
    # pat = re.compile("(?<!z)food")
    # result = pat.search("zfoodfoodfod")

    # result = re.search("AA", "dsagsAA")

    # result = re.findall("a", "afsffAfdswgaaaa")
    # result = re.findall("[A-Z]", "djsIkdofLeOewVEasfeYOU")

    # result = re.sub(r"replace\w*", "REPLACED", "sfkpreplacesfjioir")
    # END

    result_list = []
    titles_rege = r'class="title".*>(.*)</span>'
    other_rege = r'class="other".*>(.*)</span>'
    movie_about_rege = re.compile(r'<p class="">(.*)</p>', re.S)
    rating_num_rege = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    judge_num_rege = r'<span>(\d*)人评价</span>'
    inq_rege = r'<span class="inq">(.*)</span>'
    soup = BeautifulSoup(html, "html.parser")
    # result_list = soup.find_all("div", class_="item")
    for item in soup.find_all("div", class_="item"):
        data = []
        # 详情的链接
        data.append(item.a['href'] or None)
        # 封面图的地址
        data.append(item.img['src'] or None)

        item = str(item)
        titles = re.findall(titles_rege, item)
        data.append(titles[0])
        data.append(re.sub(r'\s*\/\s*', "", titles[1]) if len(titles) == 2 else None)

        other = re.findall(other_rege, item)[0]
        data.append(other or None)
        # 评分
        rating_num = re.findall(rating_num_rege, item)[0]
        data.append(rating_num)

        judge_num = re.findall(judge_num_rege, item)[0]
        data.append(judge_num)

        inq_num = re.findall(inq_rege, item)
        if len(inq_num) == 0:
            data.append(None)
        else:
            data.append(inq_num[0])
        # 电影相关
        movie_about = re.findall(movie_about_rege, item)[0]
        movie_about = re.sub(r"<br\s*\/>\s*", "", movie_about)
        movie_about = re.sub(r"\s*<\/p>(\s|.)*$", "", movie_about)
        data.append(movie_about.strip())
        result_list.append(data)

    return result_list
