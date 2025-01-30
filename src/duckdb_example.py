import duckdb

con = duckdb.connect()
con.execute("CREATE TABLE users (id INTEGER, name TEXT, age INTEGER)")
con.execute("INSERT INTO users VALUES (1, 'Alice', 25), (2, 'Bob', 30)")