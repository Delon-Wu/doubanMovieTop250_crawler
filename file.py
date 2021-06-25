# -*- codeing = utf-8 -*-
# @Time: 2021/6/7 0007 14:32
# @Author: Delon
# @File: file.py
# @software: PyCharm

# try:
#     print("让我瞧瞧这代码有错没 ->_->")
#     with open('test123.text', 'r') as f:
#         '''
#         f.write("""I'm TEST FILE!
#             This is first line without.
#             This is second line.""")
#         f.write("This is third line without.\nThis is fourth line.")
#         '''
#         # content = f.read(10) # 读一行后指针指向下一行
#
#         content = f.readlines()
#
#         # content = f.readline()
#         # print(content)
#         # content = f.readline()
#         # print(content)
#         # content = f.readline()
#
#         print(content)
# except Exception as result:
#     print('啊哦，果然有错：', result)
import os
import time

try:
    with open('早发白帝城.text', 'r') as f:
        content = f.read()
        print('此情此刻我想吟诗一首！献上《早发白帝城》')
        time.sleep(1)
        for i in content:
            print(i, end="")
            time.sleep(0.35)
        print("谢谢！")
except Exception as result:
    print(result)
    with open('早发白帝城.text', 'w') as f:
        f.write("""【作者】李白 【朝代】唐
朝辞白帝彩云间，千里江陵一日还。
两岸猿声啼不住，轻舟已过万重山。
        """)