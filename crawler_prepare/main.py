# -*- codeing = utf-8 -*-
# @Time: 2021/6/8 0008 11:06
# @Author: Delon
# @File: main.py
# @software: PyCharm

# 正则
import re
import sqlite3
from getHTML import get_html
from parseHTML import parse as parse_html
from saveData import saveData


def main():
    print('Runing mian program...')
    base_url = "https://movie.douban.com/top250?start="
    result_list = []
    for i in range(0, 10):
        html = get_html(base_url+str(i*25))
        result_list.extend(parse_html(html))
        # print('parse_result%d::'%i, parse_result)
    saveData(result_list)

    # try:
    #     lest_html_len = len(html)
    #     count = 1
    #     with open("./pages/douBanMovieTop250.html", "a") as f:
    #         while lest_html_len > 0:
    #             f.write(html[(count - 1) * 10000:count * 10000])
    #             count += 1
    #             lest_html_len -= 10000
    #             print("HTML写入成功！", lest_html_len,  count)
    # except Exception as e:
    #     print("写入html文件出错：", e)


# 当程序执行时
if __name__ == "__main__":
    main()
    print('hi,pycharm!')
