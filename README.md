a GUI application using Tkinter for the front end and MySQL for the back end to manage employee data for a company. Here's a breakdown of what each part of the code does:

1. Tkinter GUI Setup:
   - Imports Tkinter and sets up the main window (`win`).
   - Defines fonts and sets the window size, title, and background color.
   - Creates labels, entry fields, combo boxes, and buttons for user input.

2. Database Operations:
   - Imports the `mysql.connector` module.
   - Establishes a connection to a MySQL database named `company_management`.
   - Defines functions to interact with the database, such as fetching employees, inserting, deleting, and updating employee records, and checking if an employee ID exists in the database.

3. GUI Functions:
   - `add_to_treeview()`: Fetches employees from the database and populates a Treeview widget with their data.
   - `insert()`: Inserts a new employee record into the database based on user input.
   - `display_data(event)`: Displays the data of the selected employee in the entry fields for editing.
   - `clear(*clicked)`: Clears the entry fields and optionally deselects the currently selected item in the Treeview widget.
   - `delete()`: Deletes the selected employee record from the database.
   - `update()`: Updates the selected employee record in the database with the new data entered by the user.

4. Treeview Widget:
   - Creates a Treeview widget to display the list of employees with columns for different attributes such as employee ID, first name, last name, etc.
   - Binds the `display_data` function to the `<ButtonRelease>` event to update the entry fields with the selected employee's data when clicked.

5. Styling:
   - Sets up custom styles for the Treeview widget to change its appearance.

6. Mainloop:
   - Starts the main event loop to run the application.


  database.py : This Python script connects to a MySQL database and provides several functions to interact with an "employee" table in the "company_management" database. Let's break down the script step by step:

1. Importing Libraries: The script imports the `mysql.connector` library to interact with MySQL databases.

2. Database Connection: It establishes a connection to the MySQL database hosted on the local machine. The connection parameters include the hostname ("localhost"), username ("root"), password ("SALAH.BERRET.0"), and the name of the database ("company_management").

3. Fetch Employee Function: The `fetch_employee()` function retrieves all rows from the "employee" table. It executes a SELECT query to fetch all columns from the "employee" table and returns the result as a list of rows.

4. Insert Employee Function: The `insert_employee()` function inserts a new employee record into the "employee" table. It takes various parameters such as employee ID, first name, last name, birth day, sex, salary, supervisor ID, and branch ID. It executes an INSERT query to add a new row to the table with the provided data.

5. Delete Employee Function: The `delete_employee()` function deletes an employee record from the "employee" table based on the provided employee ID. It executes a DELETE query to remove the employee record corresponding to the given employee ID.

6. Update Employee Function: The `update_employee()` function updates an existing employee record in the "employee" table. It takes new values for first name, last name, birth day, sex, salary, supervisor ID, branch ID, and the employee ID to be updated. It executes an UPDATE query to modify the existing record with the new values.

7. ID Exists Function: The `id_exists()` function checks if a given employee ID exists in the "employee" table. It executes a SELECT COUNT(*) query to count the number of rows with the specified employee ID. If the count is greater than 0, it returns True, indicating that the ID exists; otherwise, it returns False.

Each function utilizes a cursor to execute SQL queries and interacts with the MySQL database. After executing INSERT, UPDATE, or DELETE queries, the `mydb.commit()` statement is used to commit the transaction to the database. Finally, the cursor is closed to release the database resources.
