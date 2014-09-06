import unirest as Unirest
import MySQLdb
import random
import time

db = MySQLdb.connect("localhost","root","ta","thoughtapp" )
user = [89,105,46,110]

cursor = db.cursor()

for i in xrange(1000):
	
	response = Unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/cat=Famous",
  	headers={"X-Mashape-Key": "vKnhtLRALPmshqzfe9isQkpBfP8Pp1x97OjjsnglQngrZwZn46"}
	)

	body = response.body

	category = body.get('category')	

	if(category != 'Movies'):
		content = body.get('quote')
		sql = 'INSERT INTO api_thought(user_id, content, lat, lng, category_id, is_anon, created, updated) VALUES(%d, "%s", %f, %f, %d, %d, "%s", "%s")' %(user[random.randint(0,3)], content, random.random()*100, random.random()*100, random.randint(1,11), random.randint(0,1), time.strftime("%Y-%m-%d %H:%M:%S"), time.strftime("%Y-%m-%d %H:%M:%S"))
		print sql
		#cursor.execute(sql)
		#db.commit()

db.close()
