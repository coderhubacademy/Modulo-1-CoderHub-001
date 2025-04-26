import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn
  
conexion = create_connection("./db/northwind.db")
cursor = conexion.cursor()

employees = cursor.execute("SELECT EmployeeID, FirstName, Lastname FROM employees ORDER BY LastName DESC LIMIT 5").fetchall()

for employee in employees:
    print(employee)

# con = sqlite3.connect("prueba.db")
# cur = con.cursor()

# # Create a table

# cur.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL, 
#         email TEXT NOT NULL UNIQUE
#     )
# ''')

# # Insert a record

# # cur.execute('''
# #             INSERT INTO users (name, age, email) 
# #             VALUES ('Pablo', 25, 'Pablo@prueba.com')
# #            ''')

# # con.commit()

# user = cur.execute("SELECT * FROM users ORDER BY name ASC LIMIT 1").fetchone()
# print(user)