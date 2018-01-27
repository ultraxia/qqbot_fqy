from qqbot import qqbotsched
import pymysql
    
def onQQMessage(bot, contact, member, content):
    global chatdetail
    if contact.ctype == 'group':
        if '我的2017:' in content or '我的2017：' in content:
            querryId(bot, contact, member, content)  

def querryId(bot, contact, member, content):
    gl = bot.List('group', '费沁源的冰糖草莓们')
    if gl is not None:
        for group in gl:
            querryId = content[7:]
            if querryId == '沉迷学习的奥特虾':
                msg = '非法请求！'
                bot.SendTo(contact,msg)
            else:
                mysql_conn = {'host': 'localhost',
                'port': 3306,
                'user': 'root',
                'password': '******',
                'db': 'test',
                'charset': 'utf8'}
                                    
                db = pymysql.connect(**mysql_conn)
                cursor = db.cursor()

                try:    
                    sql = "SELECT SUM(num) FROM wds2017 WHERE userid like '%s'" % (querryId)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                        price = row[0]
                
                    sql = "SELECT count(num) FROM wds2017 WHERE userid like '%s'" % (querryId)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                       count = row[0]
                
                    sql = "SELECT rank from rank2017 WHERE userid like '%s'" % (querryId)
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    for row in results:
                        rank = row[0]
                    percent = format((1300-float(rank))/1300, '.2%')
                    if querryId =='沙皮兔QQ':
                    	percent = '100%'
                    msg =  '%s聚聚在2017年共支持了源源%s次，累计投入了%s元，年度排名第%s名，击败了全国%s的源推，2018年也一起为源源应援吧！' % (querryId,count,price,rank,percent)
                    db.close()
                    bot.SendTo(contact,msg)
                except: 
                    msg = '查询失败，请检查ID输入是否正确'
                    db.close()
                    bot.SendTo(contact,msg)


