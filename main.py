import requests
import numpy as np
from bs4 import BeautifulSoup
import re
aprove=[]
url= f'https://гост-снип-рд.рф/Data1/Index1/24.htm'
q=requests.get(url)
result=q.content

soup=BeautifulSoup(result,'lxml')
i=0
itext=[]
gost=soup.find_all('table', {'id': 'main'})
for gost in gost:
    gost_title=gost.get('title')
    #aprove=gost.text
    #print(gost.text)
    aprove.append(gost.text)
result4=re.findall(r"ГОСТ Р \d{5}-\d{4}",aprove[0])
result2=re.findall(r"ГОСТ Р \d{5}-\d{2}",aprove[0])
m=[]
for i in range(len(result2)):
    g=result2[i].split('-')
    m.append(g[0])
    m.append(g[1])
a=np.array(m)
b=a.reshape(-1,2)
c=np.array(b).tolist()
#print('done')
#print(result4)
#print(result2)

import sqlite3

conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()
#cursor.execute("DROP TABLE tablegost2")
# cursor.execute("""CREATE TABLE tablegost2
#                   (gost text)
#                """)
#
# cursor.execute("""CREATE TABLE tablegost4
#                   (gost text)
#                """)
#
# for i in range(len(result2)):
#     resgost=result2[i]
#     cursor.execute("INSERT INTO tablegost2 VALUES (?)", [resgost])
#     conn.commit()
# cursor.execute("""CREATE TABLE tablegost2
#                   (gost text)
#                """)
#
# for i in range(len(result4)):
#     resgost=result4[i]
#     cursor.execute("INSERT INTO tablegost4 VALUES (?)", [resgost])
#     conn.commit()
#sql = "SELECT * FROM tablegost"
p=[]
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
p = c.execute('SELECT * FROM tablegost2').fetchall()
print(cursor.fetchall())
print('done')
