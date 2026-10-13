import psycopg

connection = psycopg.connect(
    host = "localhost",
    port = 5432,
    dbname = finserve,
    user = "user",
    password = ""
)