from qqbot import qqbotsched
import pymysql
    
def onQQMessage(bot, contact, member, content):
	global chatdetail
	if contact.ctype == 'group':
		if '集资查询:' in content or '集资查询：' in content:
			querryId(bot, contact, member, content)  

def querryId(bot, contact, member, content):
	gl = bot.List('group', '费沁源的冰糖草莓们')
	if gl is not None:
		for group in gl:
			querryId = content[5:]
			if querryId == '沉迷学习的奥特虾':
				msg = '非法请求！'
				bot.SendTo(contact,msg)
			else:
				mysql_conn = {'host': 'localhost',
				'port': 3306,
				'user': 'root',
				'password': '*******',
				'db': 'SNH48',
				'charset': 'utf8'}
				                    
				db = pymysql.connect(**mysql_conn)
				cursor = db.cursor()

				try:	
					sql = "SELECT SUM(num) FROM fqyjzdata WHERE ID like '%s'" % (querryId)
					cursor.execute(sql)
					msg = '%s聚聚已累计为源源投入了：' % (querryId)
					results = cursor.fetchall()
					for row in results:
						price = row[0]
					msg = msg+str(price)+'元'
					db.close()
					bot.SendTo(contact,msg)
				except:	
					msg = '查询失败'
					db.close()
					bot.SendTo(contact,msg)
