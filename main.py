from psycopg2 import connect
conn = connect('postgresql://olgichumak:olgichumak@localhost:5432/olgichumak')
with conn.cursor() as cursor:
    with open('categories.sql', 'r', encoding='utf-8') as file:
        cursor.execute(file.read())
        conn.commit()
    with open('users.sql', 'r', encoding='utf-8') as file:
        cursor.execute(file.read())
        conn.commit()
    with open('statuses.sql', 'r', encoding='utf-8') as file:
        cursor.execute(file.read())
        conn.commit()

    with open('orders.sql', 'r', encoding='utf-8') as file:
        cursor.execute(file.read())
        conn.commit()
    with open('products.sql', 'r', encoding='utf-8') as file:
        cursor.execute(file.read())
        conn.commit()
    with open('order_items.sql', 'r', encoding='utf-8') as file:
        cursor.execute(file.read())
        conn.commit()
