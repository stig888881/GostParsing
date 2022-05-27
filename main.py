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
    print(gost.text)
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
print('done')
print(result4)
print(result2)

import sqlite3

conn = sqlite3.connect("sqlite.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
lens=len(result2)
text_gost=['ГОСТ 8.1-2000','ГОСТ 8.2-2003']
#cursor.execute("""CREATE TABLE tablegost
#                  (gost text)
#               """)

for i in range(lens):
    resgost=result2[i]
    cursor.execute("INSERT INTO tablegost VALUES (?)", [resgost])
    conn.commit()
sql = "SELECT * FROM tablegost"
cursor.execute(sql)
print(cursor.fetchall())
print('done')
fat=cursor.fetchone()
print('done2')
