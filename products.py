import sqlite3

connection = sqlite3.connect("product.db")
cursor = connection.cursor()

cursor.execute("create table if not exists products (id_product integer , name_product text, price_product integer, category text)")

products = [
    (1, 'ZEbr0', 611, 'bottom'),
    (2, 'Kit-CAT', 46, 'top'),
    (3, 'Leader-coat', 644, 'jacket'),
    (4, 'Social-credit Calculator', 56, 'accessorie'),
    (5, 'Commun-CARD', 151, 'gift-card')

]

cursor.executemany("insert into products values (?,?,?,?)", products)

for row in cursor.execute("select * from products"):
    print(row)
cursor.close()