# -*- codeing = utf-8 -*-
# @Time: 2021/6/18 0018 9:22
# @Author: Delon
# @File: saveData.py
# @software: PyCharm

# 生成exel表的
import xlwt
import sqlite3
import datetime


def save_data(data_list, save_path="豆瓣电影Top250.xls"):
    connection = sqlite3.connect('doubanMoviesTop250.db')
    cursor = connection.cursor()

    init_table("doubanMoviesTop250.db")

    for report in data_list:
        report.append(None)
        cursor.execute('''INSERT INTO doubanMovie  values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', tuple(report))
    connection.commit()
    connection.close()

    try:
        workbook = xlwt.Workbook('utf-8')
        worksheet = workbook.add_sheet("sheet1")
        # 练习九九乘法表 START
        # for i in range(0, 9):
        #     for j in range(0, 9):
        #         if j<i:
        #             continue
        #         worksheet.write(j, i, "%d x %d = %d"%(i+1, j+1,(i+1)*(j+1)))
        # END
        head = ("详情链接", "封面图地址", "电影名称", "电影名称（英文）", "其他信息", "电影评分", "评分人数", "经典评论", "电影相关")
        for i in range(len(head)):
            worksheet.write(0, i, head[i])

        workbook.save(save_path)
    except Exception as e:
        print("保存失败 :-(", "\n", e)


def init_table(db_path=str(datetime.datetime.now())+'.db'):
    table_sql = '''CREATE TABLE doubanMovie 
        (detail_link text,
        cover_url text,
        movie_name text(50),
        movie_name_foreign text(50),
        other text(200),
        rating text(5),
        judge_num text(20),
        comment text(300),
        movie_about text(200),
        id integer PRIMARY KEY AUTOINCREMENT)
        '''
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    try:
        cursor.execute(table_sql)
    except sqlite3.OperationalError as e:
        print(e, '该表可能已存在,正在删除该表重新创建...')
        cursor.execute('''DROP TABLE doubanMovie''')
        cursor.execute(table_sql)
    print("成功建表 :-)")
