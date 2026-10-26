
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------------- MYSQL CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")
cursor.execute("USE studentdb")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    mobile VARCHAR(15),
    email VARCHAR(100)
)
""")

# ---------------- TKINTER WINDOW ----------------
root = tk.Tk()
root.title("Student CRUD Application")
root.geometry("900x550")

selected_id = None

# ---------------- FUNCTIONS ----------------
def clear_fields():
    global selected_id
    firstname_entry.delete(0, tk.END)
    lastname_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    selected_id = None
    tree.selection_remove(tree.selection())


def display_data():
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


def insert_data():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()

    if firstname == "" or lastname == "":
        messagebox.showerror(
            "Error",
            "Please enter First Name and Last Name"
        )
        return

    query = """
    INSERT INTO students
    (firstname, lastname, mobile, email)
    VALUES (%s, %s, %s, %s)
    """

    values = (firstname, lastname, mobile, email)

    cursor.execute(query, values)
    conn.commit()

    messagebox.showinfo("Success", "Student Added Successfully")
    clear_fields()
    display_data()


def select_data(event):
    global selected_id

    selected = tree.focus()

    if selected:
        values = tree.item(selected, "values")
        selected_id = values[0]

        firstname_entry.delete(0, tk.END)
        lastname_entry.delete(0, tk.END)
        mobile_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        firstname_entry.insert(0, values[1])
        lastname_entry.insert(0, values[2])
        mobile_entry.insert(0, values[3])
        email_entry.insert(0, values[4])


def update_data():
    global selected_id

    if selected_id is None:
        messagebox.showerror("Error", "Please select a student")
        return

    query = """
    UPDATE students
    SET firstname=%s,
        lastname=%s,
        mobile=%s,
        email=%s
    WHERE id=%s
    """

    values = (
        firstname_entry.get(),
        lastname_entry.get(),
        mobile_entry.get(),
        email_entry.get(),
        selected_id
    )

    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Student Updated Successfully")
    else:
        messagebox.showinfo("Info", "No changes were made.")

    clear_fields()
    display_data()


def delete_data():
    global selected_id

    if selected_id is None:
        messagebox.showerror("Error", "Please select a student")
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Do you want to delete this student?"
    )

    if confirm:
        cursor.execute(
            "DELETE FROM students WHERE id=%s",
            (selected_id,)
        )
        conn.commit()

        messagebox.showinfo("Success", "Student Deleted Successfully")
        clear_fields()
        display_data()


# ---------------- FORM ----------------
tk.Label(root, text="First Name").place(x=50, y=50)
firstname_entry = tk.Entry(root, width=30)
firstname_entry.place(x=180, y=50)

tk.Label(root, text="Last Name").place(x=50, y=100)
lastname_entry = tk.Entry(root, width=30)
lastname_entry.place(x=180, y=100)

tk.Label(root, text="Mobile").place(x=50, y=150)
mobile_entry = tk.Entry(root, width=30)
mobile_entry.place(x=180, y=150)

tk.Label(root, text="Email").place(x=50, y=200)
email_entry = tk.Entry(root, width=30)
email_entry.place(x=180, y=200)

# ---------------- BUTTONS ----------------
tk.Button(root, text="Add", command=insert_data).place(x=180, y=250)
tk.Button(root, text="Update", command=update_data).place(x=250, y=250)
tk.Button(root, text="Delete", command=delete_data).place(x=330, y=250)
tk.Button(root, text="Clear", command=clear_fields).place(x=410, y=250)

# ---------------- TREEVIEW ----------------
columns = ("ID", "First Name", "Last Name", "Mobile", "Email")

tree = ttk.Treeview(root, columns=columns, show="headings")

for column in columns:
    tree.heading(column, text=column)

tree.column("ID", width=50)
tree.place(x=400, y=50, width=480, height=400)

tree.bind("<ButtonRelease-1>", select_data)

# ---------------- LOAD DATA ----------------
display_data()

# ---------------- RUN ----------------
try:
    root.mainloop()
finally:
    cursor.close()
    conn.close()
