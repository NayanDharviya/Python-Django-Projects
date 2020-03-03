
import pymysql
con=pymysql.connect('localhost','root','','project')
cursor=con.cursor()
i='''insert into admin values(%s,%s);'''
v=(input('enter username'),input('enter password'))
result=cursor.execute(i,v)
print('data successfully add')
con.commit()
d='''select * from admin'''
cursor.execute(d)
ans=cursor.fetchall()
print('name\tpassword')
for i in ans:            
    print('{}\t{}'.format(i[0],i[1]))

        
con.close()
