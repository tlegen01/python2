import requests
import psycopg2
from openpyxl import Workbook
import numpy as np
from openpyxl.utils import get_column_letter

url = "https://jsonplaceholder.typicode.com/posts"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
status = response.status_code
content = response.json()
# print(content)
######################################################
conn = psycopg2.connect(dbname='new1_postgres_db', user='postgres', password='Qwerty123', host='localhost')
cursor = conn.cursor()
for i in content:
    # print(i['title'])
    query_string = f'''
    INSERT INTO public.new1_postgres_tb (userId, id, title, body)
    VALUES ('{i['userId']}', '{i['id']}', '{i['title']}', '{i['body']}')
    '''
    cursor.execute(query_string)
conn.commit()
cursor.close()
conn.close()
######################################################
conn = psycopg2.connect(dbname='new1_postgres_db', user='postgres', password='Qwerty123', host='localhost')
cursor = conn.cursor()
cursor.execute("""SELECT * FROM public.new1_postgres_tb
where userid > 3
ORDER BY id ASC""")
records = cursor.fetchall()
# print(records[0])
# print(type(records[0]))
...
cursor.close()
conn.close()
#######################################################
workbook = Workbook()
worksheet = workbook.active
for i in records:
    worksheet.append(i)
workbook.save("home_work_sql.xlsx")

