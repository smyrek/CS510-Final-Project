import sqlite3

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.execute('''SELECT COUNT(from_id), new_rank, url 
     FROM Pages JOIN Links ON Pages.id = Links.to_id
     WHERE html IS NOT NULL
     GROUP BY id ORDER BY new_rank DESC''')

n = 0
count = int(input('How many pages would you like to display?: '))
for row in cur :
    if n < count : print(row)
    n += 1
print(count, 'rows')
cur.close()
