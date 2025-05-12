import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS student (
                roll INTEGER PRIMARY KEY,
                name TEXT,
                course TEXT,
                marks INTEGER,
                contact TEXT)''')
conn.commit()

# Functions
def add_student():
    roll = int(input("Roll No: "))
    name = input("Name: ")
    course = input("Course: ")
    marks = int(input("Marks: "))
    contact = input("Contact: ")
    
    c.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?)",
              (roll, name, course, marks, contact))
    conn.commit()
    print("✅ Student added successfully.")

def view_students():
    c.execute("SELECT * FROM student")
    rows = c.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(row)

def update_marks():
    roll = int(input("Enter roll number to update: "))
    new_marks = int(input("Enter new marks: "))
    c.execute("UPDATE student SET marks = ? WHERE roll = ?", (new_marks, roll))
    conn.commit()
    print("✅ Marks updated.")

def delete_student():
    roll = int(input("Enter roll number to delete: "))
    c.execute("DELETE FROM student WHERE roll = ?", (roll,))
    conn.commit()
    print("❌ Student deleted.")

# Main menu
while True:
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_marks()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("❗Invalid choice. Try again.")

conn.close()
