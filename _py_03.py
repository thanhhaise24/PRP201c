import sqlite3

conn = sqlite3.connect('Wage.sqlite')
c = conn.cursor()

# create table
sql_create_table = """
    DROP TABLE IF EXISTS Wage;

    CREATE TABLE Wage
    (
        Name TEXT,
        Hours FLOAT,
        Rate FLOAT,
        Total FLOAT,
        Tax FLOAT
    );
"""
try:
    c.executescript(sql_create_table)
    conn.commit()
except:
    print('Query error!')

# Load data
data = open('Database.txt')

num_line = 0
names = []
hours = []
rates = []

for line in data:
    num_line += 1
    if num_line == 1 or num_line == 2:
        continue
    data_piece = line.strip().split()
    names.append(data_piece[0].strip())
    hours.append(float(data_piece[1].strip()))
    rates.append(float(data_piece[2].strip()))

df = list(zip(names, hours, rates))

# Insert data
for item in df:
    total  = item[1] * item[2]
    tax = total/10 if total >= 2000000 else 0
    c.execute("""INSERT INTO Wage(Name,Hours,Rate,Total,Tax)
    VALUES (?, ?, ?, ?, ?)""", (item[0],item[1],item[2],total,tax))
    conn.commit()

show_data = "SELECT * FROM Wage WHERE Hours > 5 ORDER BY Hours"
c.execute(show_data)
data_row = c.fetchall()
print('Lecturer List:')
print("{:<15}{:<15}{:<15}{:<15}{:<15}".format('Name','Hours','Rate','Total','Tax'))
for row in data_row:
    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(row[0],row[1],row[2],row[3],row[4]))

conn.close()