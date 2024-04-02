import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter  # Assuming this contains your custom widgets
import database  # Assuming this contains your database operations

# Create the main window
win = tk.Tk()
win.geometry("1200x650")  # Set window size
win.title("Company Management")  # Set window title
win.config(bg='#161C25')  # Set window background color
win.resizable(False, False)  # Disable window resizing

# Define fonts for the GUI
font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

# Function to fetch employees from the database and populate the Treeview
def add_to_treeview():
    employees = database.fetch_employee()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert("", tk.END, values=employee)

# Function to insert a new employee record into the database
def insert():
    # Get values from entry fields
    id = id_entry.get()
    fname = fname_entry.get()
    lname = lname_entry.get()
    bday = birth_entry.get()
    sex = var1.get()
    salary = salary_entry.get()
    super_id = super_entry.get()
    branch_id = var2.get()
    # Validate input
    if not (id and fname and lname and bday and sex and salary and super_id and branch_id):
        messagebox.showerror("Error", "Please fill in all fields")
    elif  database.id_exists(id):
        messagebox.showerror("Error", "Employee ID already exists")
    else:
        # Insert employee record into the database
        database.insert_employee(id, fname, lname, bday, sex, salary, super_id, branch_id)
        # Update the Treeview
        add_to_treeview()
        messagebox.showinfo("Success", "Employee added successfully")

# Function to display data of the selected employee in the entry fields
def display_data(event):
    selected_item = tree.focus()
    if selected_item :
        row = tree.item(selected_item)['values']
        clear()
        # Insert data into entry fields
        id_entry.insert(0, row[0])
        fname_entry.insert(0, row[1])
        lname_entry.insert(0, row[2])
        birth_entry.insert(0, row[3])
        var1.set(row[4])
        salary_entry.insert(0, row[5])
        super_entry.insert(0, row[6])
        var2.set(row[7])
    else :
        pass

# Function to clear entry fields
def clear(*clicked):
    if clicked :
        tree.selection_remove(tree.focus())
    id_entry.delete(0, tk.END)
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    birth_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    super_entry.delete(0, tk.END)

# Function to delete selected employee record from the database
def delete():
    id = id_entry.get()
    if not id:
        messagebox.showerror("Error", "Please enter an employee ID")
    elif not database.id_exists(id):
        messagebox.showerror("Error", "Employee ID does not exist")
    else:
        # Delete employee record from the database
        database.delete_employee(id)
        # Update the Treeview
        add_to_treeview()
        clear()
        messagebox.showinfo("Success", "Employee deleted successfully")

# Function to update selected employee record in the database
def update():
    id = id_entry.get()
    fname = fname_entry.get()
    lname = lname_entry.get()
    bday = birth_entry.get()
    sex = var1.get()
    salary = salary_entry.get()
    super_id = super_entry.get()
    branch_id = var2.get()
    if not id:
        messagebox.showerror("Error", "Please enter an employee ID")
    elif not database.id_exists(id):
        messagebox.showerror("Error", "Employee ID does not exist")
    else:
        # Update employee record in the database
        database.update_employee(fname, lname, bday, sex, salary, super_id, branch_id, id)
        # Update the Treeview
        add_to_treeview()
        clear()
        messagebox.showinfo("Success", "Employee updated successfully")

# Employee ID Label
id_label = customtkinter.CTkLabel(win, text="emp ID:", font=font1, bg_color='#161C25', fg_color='#161C25')
id_label.place(x=10, y=10)

# Employee ID Entry Field
id_entry = customtkinter.CTkEntry(win, font=font1, text_color='#000',bg_color='#161C25', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
id_entry.place(x=112, y=10)

# First Name Label
fname_label = customtkinter.CTkLabel(win, text="first name:",  font=font1, bg_color='#161C25', fg_color='#161C25')
fname_label.place(x=10, y=80)

# First Name Entry Field
fname_entry = customtkinter.CTkEntry(win, font=font1, text_color='#000',bg_color='#161C25', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
fname_entry.place(x=112, y=80)

# Last Name Label
lname_label = customtkinter.CTkLabel(win, text="last name:", font=font1, bg_color='#161C25', fg_color='#161C25')
lname_label.place(x=10, y=150)

# Last Name Entry Field
lname_entry = customtkinter.CTkEntry(win, font=font1, text_color='#000',bg_color='#161C25', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
lname_entry.place(x=112, y=150)

# Birth Date Label
birth_label = customtkinter.CTkLabel(win, text="birth date:", font=font1, bg_color='#161C25', fg_color='#161C25')
birth_label.place(x=10, y=220)

# Birth Date Entry Field
birth_entry = customtkinter.CTkEntry(win, font=font1, text_color='#000',bg_color='#161C25', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
birth_entry.place(x=112, y=220)

# Gender Label
gender_label = customtkinter.CTkLabel(win, text="gender:", font=font1, bg_color='#161C25', fg_color='#161C25')
gender_label.place(x=10, y=290)

# Gender Options
options = ["M", "F"]
var1 = tk.StringVar()

# Gender ComboBox
gender_option = customtkinter.CTkComboBox(win, variable=var1, values=options, font=font1, text_color='#000',bg_color='#161C25', fg_color='#fff', border_color='#0C9295', border_width=2, width=180, state="readonly")
gender_option.set("M")
gender_option.place(x=112, y=290)

# Salary Label
salary_label = customtkinter.CTkLabel(win, text="salary:", font=font1, bg_color='#161C25', fg_color='#161C25')
salary_label.place(x=10, y=360)

# Salary Entry Field
salary_entry = customtkinter.CTkEntry(win, font=font1, text_color='#000',bg_color='#161C25', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
salary_entry.place(x=112, y=360)

# Super ID Label
super_label = customtkinter.CTkLabel(win, text="super ID:", font=font1, bg_color='#161C25', fg_color='#161C25')
super_label.place(x=10, y=430)

# Super ID Entry Field
super_entry = customtkinter.CTkEntry(win, font=font1, text_color='#000',bg_color='#161C25', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
super_entry.place(x=112, y=430)

# Branch ID Label
branch_label = customtkinter.CTkLabel(win, text="branch ID:", font=font1, bg_color='#161C25', fg_color='#161C25')
branch_label.place(x=10, y=500)

# Branch ID Options
options2 = ['1', '2', '3']
var2 = tk.IntVar()

# Branch ID ComboBox
branch_option = customtkinter.CTkComboBox(win, variable=var2, values=options2, font=font1, text_color='#000',bg_color='#161C25', fg_color='#fff', border_color='#0C9295', border_width=2, width=180, state="readonly")
branch_option.set(1)
branch_option.place(x=112, y=500)

# Add Employee Button
add_button = customtkinter.CTkButton(win, text="add Employee", command=insert, font=font2, text_color='#fff',bg_color='#161C25', fg_color='#0C9295', border_color='#0C9295', border_width=2, width=250)
add_button.place(x=10, y=570)

# Clear Entry Fields Button
clear_button = customtkinter.CTkButton(win, text="New Employee", command=lambda:clear(True), font=font2, text_color='#fff',bg_color='#161C25', fg_color='#0C9295', border_color='#0C9295', border_width=2, width=250)
clear_button.place(x=300, y=570)

# Update Employee Button
update_button = customtkinter.CTkButton(win, text="update Employee", command=update, font=font2, text_color='#fff',bg_color='#161C25', fg_color='#0C9295', border_color='#0C9295', border_width=2, width=250)
update_button.place(x=600, y=570)

# Delete Employee Button
delete_button = customtkinter.CTkButton(win, text="delete Employee", command=delete, font=font2, text_color='#fff',bg_color='#161C25', fg_color='#0C9295', border_color='#0C9295', border_width=2, width=250)
delete_button.place(x=900, y=570)

# Styling for Treeview Widget
style = ttk.Style(win)
style.theme_use("clam")
style.configure("Treeview", rowheight=30, font=font2, background="#161C25", foreground="#fff", fieldbackground="#161C25")
style.map("Treeview", background=[("selected", "#0C9295")])

# Treeview Widget: Display Employee Data
tree = ttk.Treeview(win, height=17)

# Define columns for the Treeview
tree["columns"] = ("emp_id", "first_name", "last_name", "birth_day", "sex", "salary", "super_id", "branch_id")

# Configure columns of the Treeview
tree.column("#0", width=0, stretch=tk.NO)
tree.column("emp_id", anchor=tk.CENTER, width=100)
tree.column("first_name", anchor=tk.CENTER, width=100)
tree.column("last_name", anchor=tk.CENTER, width=100)
tree.column("birth_day", anchor=tk.CENTER, width=100)
tree.column("sex", anchor=tk.CENTER, width=100)
tree.column("salary", anchor=tk.CENTER, width=100)
tree.column("super_id", anchor=tk.CENTER, width=100)
tree.column("branch_id", anchor=tk.CENTER, width=100)

# Define and configure headings for each column
tree.heading("emp_id", text="emp_id")
tree.heading("first_name", text="first_name")
tree.heading("last_name", text="last_name")
tree.heading("birth_day", text="birth_day")
tree.heading("sex", text="sex")
tree.heading("salary", text="salary")
tree.heading("super_id", text="super_id")
tree.heading("branch_id", text="branch_id")

# Place the Treeview on the window
tree.place(x=300, y=10)

# Bind a function to the Treeview's click event to display data of the selected employee
tree.bind("<ButtonRelease>", display_data)

# Populate the Treeview with employee data
add_to_treeview()

# Start the main event loop
win.mainloop()
