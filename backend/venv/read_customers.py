import psycopg

connection = psycopg.connect(
    host = "localhost",
    port = 5432,
    dbname = "finserve",
    user = "user",
    password = ""
)

try: 
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, email, phone FROM customers WHERE name LIKE 'C%'") 

        customers = cursor.fetchall()

        for customer in customers:
            print(customer)

finally:
    connection.close()