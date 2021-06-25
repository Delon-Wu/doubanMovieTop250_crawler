# -*- codeing = utf-8 -*-
# @Time: 2021/6/9 0009 10:03
# @Author: Delon
# @File: getHTML.py
# @software: PyCharm
import urllib.request, urllib.error, urllib.parse      # 制定url，获取数据，初步认为是发请求的


def get_html(url="http://httpbin.org", data={}, method="GET"):
    # wd = urllib.parse.urlencode({"wd": "钢铁侠"}).encode('utf-8')
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    req = {}
    if len(data.keys()) > 0 and method.lower() == 'post':
        data = urllib.parse.urlencode(data)
        req = urllib.request.Request(url, data, headers=head, method=method)
    else:
        req = urllib.request.Request(url, headers=head, method=method)
    print('-'*30, data, method)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        # print('-'*20)
        # print("PAGE HTML：", html)
        # with open("pages/douBanMovieTop250.html", "w") as f:
        #     f.write(html)
        #     print("已写到pages/douBanMovieTop250.html")
        return html
    except Exception as e:
        print("urlopen出错：", e)
        return False
