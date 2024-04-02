import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SALAH.BERRET.0",
    database="company_management"
)

# Function to fetch all employee records from the database
def fetch_employee():
    cur = mydb.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    cur.close()
    return rows

# Function to insert a new employee record into the database
def insert_employee(emp_id, first_name, last_name, birth_day, sex, salary, super_id, branch_id):
    cur = mydb.cursor()
    # Execute SQL INSERT statement
    cur.execute("INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (emp_id, first_name, last_name, birth_day, sex, salary, super_id, branch_id))
    # Commit the transaction
    mydb.commit()
    cur.close()

# Function to delete an employee record from the database
def delete_employee(emp_id):
    cur = mydb.cursor()
    # Execute SQL DELETE statement
    cur.execute("DELETE FROM employee WHERE emp_id=%s", (emp_id,))
    # Commit the transaction
    mydb.commit()
    cur.close()

# Function to update an employee record in the database
def update_employee(new_fname, new_lname, new_birth_day, new_sex, new_salary, new_super_id, new_branch, emp_id):
    cur = mydb.cursor()
    # Execute SQL UPDATE statement
    cur.execute("UPDATE employee SET first_name = %s, last_name = %s, birth_day = %s, sex = %s, salary = %s, super_id = %s, branch_id = %s WHERE emp_id = %s", (new_fname, new_lname, new_birth_day, new_sex, new_salary, new_super_id, new_branch, emp_id))
    # Commit the transaction
    mydb.commit()
    cur.close()

# Function to check if an employee with the given ID exists in the database
def id_exists(emp_id):
    cur = mydb.cursor()
    # Execute SQL SELECT statement to count the number of rows with the given ID
    cur.execute("SELECT COUNT(*) FROM employee WHERE emp_id = %s", (emp_id,))
    count = cur.fetchone()[0]
    cur.close()
    # Return True if count is greater than 0, indicating the ID exists; otherwise, return False
    return count > 0
