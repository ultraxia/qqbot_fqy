# -*- coding: utf-8 -*-
import setting
from qqbot import qqbotsched
import weibo
import copy
import modian
import time


global weibo_id_array
global firstcheck_weibo

weibo_id_array = []
firstcheck_weibo = 1

groupid = setting.groupid()


# 关键字回复
def onQQMessage(bot, contact, member, content):
    if contact.ctype == 'group' and contact.nick == groupid:
        if content == '打卡':
            jz = ''
            jz = jz + setting.wds_name() + '\n' + setting.wds_url()
            bot.SendTo(contact, str(jz))
        elif content == 'wds20' or content == 'rank':
            bot.SendTo(contact, modian.rank(1))
        elif content == 'dkb' or content == '打卡榜':
            bot.SendTo(contact, modian.rank(2))
        elif content == "独占":
            duzhan = "独占请集资" + '\n' + setting.wds_name() + '\n' + setting.wds_url()
            bot.SendTo(contact, duzhan)
        elif content == "help":
            help = '''Nemo操作手册：\n摩点相关\n1.“打卡”：返回集资地址"\n2.“rank”或“wds20”：返回集资金额榜单\n3.“打卡榜”或“dkb”：返回打卡天数榜单\n\n查询类\n1."集资查询+ID"返回某一ID的集资总额（数据每个月更新一次）\n2."我的2017+ID"返回2017年度账单\n3."微博故事+费沁源（或UID)"返回微博故事下载链接\n(注：所有查询类请求格式均为"命令+冒号+参数（ID）)'''
            bot.SendTo(contact, help)


# 定时任务。每五分钟获取一次微博数据，如果有新的微博，自动发送到群。
# 可修改定时任务时间来提高查询频率，其他无需修改
@qqbotsched(hour='0-23', minute='0-59/1')
def mytask3(bot):
    global weibo_id_array
    global firstcheck_weibo
    wbcontent = ""
    gl = bot.List('group', groupid)
    if gl is not None:
        for group in gl:
            idcount = -1
            if (firstcheck_weibo == 1):
                weibo_id_array = copy.copy(weibo.getidarray())
                firstcheck_weibo = 0
            checkwbid = copy.copy(weibo.get_5_idarray())
            if (firstcheck_weibo == 0):
                for cardid in checkwbid:
                    idcount += 1
                    if int(cardid) == 0:
                        continue
                    if cardid not in weibo_id_array:
                        weibo_id_array.append(cardid)
                        retweet = weibo.checkretweet(idcount)
                        wbpic = weibo.checkpic(idcount)
                        wbscheme = weibo.getscheme(idcount)
                        if (retweet):
                            wbcontent = "源源刚刚[转发]了一条微博：" + '\n' + '\n' + weibo.getretweetweibo(idcount) + '\n'
                            wbcontent = wbcontent + '\n' + "传送门：" + wbscheme
                        else:
                            wbcontent = "源源刚刚发了一条新微博：" + '\n' + '\n' + weibo.getweibo(idcount) + '\n'
                            if (wbpic):
                                wbcontent = wbcontent + weibo.getpic(idcount)
                            wbcontent = wbcontent + '\n' + "传送门：" + wbscheme
                        bot.SendTo(group, wbcontent)


# 定时任务。每1分钟获取一次微打赏数据，如果有新的集资评论，自动发送到群。
# 可修改定时任务时间来提高查询频率，其他无需修改
# 若修改了查询频率，一定要修改下方newOrder方法的第二个参数
@qqbotsched(hour='0-23', minute='0-59')
def mytask(bot):
    gl = bot.List('group', groupid)
    if gl is not None:
        for group in gl:
            # 获取当前unix时间（10位，单位为秒）
            stampTime = int(time.time())
            # 调用modian.py的newOrder方法
            # 第二个参数是查询时间段：60即查询当前时间前60s得新集资
            # 若修改了查询频率，则一定要修改第二个参数
            msgDict = modian.newOrder(stampTime, 60)
            # 返回了一个字典
            if msgDict:
                for msg in msgDict['msg']:
                    msg += msgDict['end']
                    bot.SendTo(group, msg)
