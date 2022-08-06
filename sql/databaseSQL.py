import psycopg2

# READ
#############################################################
conn = psycopg2.connect(dbname='example', user='postgres', password='Qwerty123', host='localhost')
cursor = conn.cursor()
# cursor.execute('SELECT * FROM public.table1')
cursor.execute("""SELECT * FROM public.table1
where age > 19
ORDER BY age ASC, credits DESC""")
records = cursor.fetchall()
print(records)
print(type(records))
for i in records:
    print(i)
    print(type(i))
...
cursor.close()
conn.close()

###############################################################
conn = psycopg2.connect(dbname='example', user='postgres', password='Qwerty123', host='localhost')
cursor = conn.cursor()
new_arr = [
    ['w', 25, 'true', 2500.6, 3],
    ['b', 50, 'false', 30.6, 3],
    ['y', 25, 'true', 2500.6, 3],
    ['r', 75, 'false', 500.6, 0],
    ['u', 88, 'true', 2500.6, 3],
    ['3', 25, 'true', 305.6, 0],
]
index = 40
for i in new_arr:
    query_string = f"""
    INSERT INTO public.table1 (username, age, married, credits, id) 
    VALUES ('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}', '{index}')"""
    index += 1
    cursor.execute(query_string)
conn.commit()
cursor.close()
conn.close()

