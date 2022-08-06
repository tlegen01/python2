import psycopg2

conn = psycopg2.connect(dbname='new1_postgres_db', user='postgres', password='Qwerty123', host='localhost')
cursor = conn.cursor()
cursor.execute("""
SELECT * FROM public.new_postgres_tb1
where age > 20
ORDER BY age ASC""")
records = cursor.fetchall()
print(records)
print(type(records))
...
cursor.close()
conn.close()

conn = psycopg2.connect(dbname='new1_postgres_db', user='postgres', password='Qwerty123', host='localhost')
cursor = conn.cursor()
new_arr = [
    [37, 'true', 'Tlegen'],
    [38, 'true', 'Alibek'],
]
for i in new_arr:
    query_string = f"""
    INSERT INTO public.new_postgres_tb1 (age, is_have_money, name) 
    VALUES ('{i[0]}', '{i[1]}', '{i[2]}')"""
    cursor.execute(query_string)
conn.commit()
cursor.close()
conn.close()