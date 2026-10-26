
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="company"
)

cursorObject = dataBase.cursor()

# Create Student table
cursorObject.execute("""
CREATE TABLE IF NOT EXISTS Student (
    Roll_no INT PRIMARY KEY,
    Name VARCHAR(50)
)
""")

# Create StudentDetails table
cursorObject.execute("""
CREATE TABLE IF NOT EXISTS StudentDetails (
    Roll_no INT PRIMARY KEY,
    Branch VARCHAR(30),
    Section VARCHAR(10)
)
""")

# Insert sample records
cursorObject.execute("""
INSERT IGNORE INTO Student VALUES
(1, 'Raj'),
(2, 'Amit'),
(3, 'Priya')
""")

cursorObject.execute("""
INSERT IGNORE INTO StudentDetails VALUES
(1, 'BCA', 'A'),
(2, 'BBA', 'B'),
(4, 'BCA', 'A')
""")

dataBase.commit()

# INNER JOIN
print("\nINNER JOIN:")
cursorObject.execute("""
SELECT Student.Name, StudentDetails.Branch
FROM Student
INNER JOIN StudentDetails
ON Student.Roll_no = StudentDetails.Roll_no
""")

for row in cursorObject.fetchall():
    print(row)

# LEFT JOIN
print("\nLEFT JOIN:")
cursorObject.execute("""
SELECT Student.Name, StudentDetails.Branch
FROM Student
LEFT JOIN StudentDetails
ON Student.Roll_no = StudentDetails.Roll_no
""")

for row in cursorObject.fetchall():
    print(row)

# RIGHT JOIN
print("\nRIGHT JOIN:")
cursorObject.execute("""
SELECT Student.Name, StudentDetails.Branch
FROM Student
RIGHT JOIN StudentDetails
ON Student.Roll_no = StudentDetails.Roll_no
""")

for row in cursorObject.fetchall():
    print(row)

dataBase.close()
