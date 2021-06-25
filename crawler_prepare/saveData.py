# -*- codeing = utf-8 -*-
# @Time: 2021/6/18 0018 9:22
# @Author: Delon
# @File: saveData.py
# @software: PyCharm

# 生成exel表的
import xlwt


def saveData(data_list,save_path="豆瓣电影Top250.xls"):
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
        for i in range(len(data_list)):
            for j in range(len(data_list[i])):
                worksheet.write(i+1, j, data_list[i][j])
        workbook.save(save_path)
    except Exception as e:
        print("保存失败 :-(", "\n", e)
