# -*- codeing = utf-8 -*-
# @Time: 2021/6/4 0004 9:38
# @Author: Delon
# @File: game.py
# @software: PyCharm

from random import randint
print('我们来玩个游戏吧！')
toBegin = True


def justify(userinput, num):
    """用户赢了输出True，计算机赢了输出False，平手输出0"""
    lit = ['石头', '剪刀', '布']
    if userinput not in lit:
        print('输入不正确，请重新输入...')
        return -1
    if lit[num] == userinput:
        print('您出的是\t%s，电脑出的也是\t%s，所以平手啦' % (userinput, lit[num]))
        return 0
    elif num == 0:
        if userinput == '剪刀':
            print('您出的是\t%s，电脑出的是\t%s，很遗憾，你输啦' % (userinput, lit[num]))
            return False
        else:
            print('您出的是\t%s，电脑出的是\t%s，太棒啦，你赢了' % (userinput, lit[num]))
            return True
    elif num == 1:
        if userinput == '石头':
            print('您出的是\t%s，电脑出是\t%s，太棒啦，你赢了' % (userinput, lit[num]))
            return True
        else:
            print('您出的是\t%s，电脑出的是\t%s，很遗憾，你输啦' % (userinput, lit[num]))
            return False
    elif num == 2:
        if userinput == '石头':
            print('您出的是\t%s，电脑出的是\t%s，很遗憾，你输啦' % (userinput, lit[num]))
            return False
        else:
            print('您出的是\t%s，电脑出的是\t%s，太棒啦，你赢了' % (userinput, lit[num]))
            return True


while toBegin:
    clientResult = input("请输入：石头、剪刀或者布")
    serveResult = randint(0, 2)
    result = justify(clientResult, serveResult)
    if result == -1:
        continue
    ifgoon = input('继续玩吗？输入任意键继续游戏，输入N退出游戏：')
    if ifgoon == 'n' or ifgoon == 'N':
        print('拜~下次再和你玩')
        break
