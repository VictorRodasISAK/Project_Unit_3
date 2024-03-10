# Unit 3: Application Development for the Company 'Mantis Rackets'


![Logo.png](..%2FProject_Images%2FLogo.png)


*Fig.1:* Logo of the Company


# Criteria A: Planning


## Problem Definition


My client, a Salesman guy who is establishing a company dedicated to the creation of ping pong rackets, is having problems
with the record of sales, inventory, clients and purchases. He is using a spreadsheet in a MacBook Air (2017) to keep track of this information, 
making it hard and time-consuming to find and track the information of purchases and sales. Also, when trying to update the materials to produce the rackets,
he has to check the availability of the materials, but sometimes, the information that he gets is incorrect. Moreover, most of the time
he wants to keep the information of his customers in a table to offer future promotions  , but he does not have a system to remember the customers.
He has a large company, and he has a lot of employees. Sometimes he needs the assistance of his employees to solve some problems,
but he does not have a way to track the schedule of his employees. Finally, because there is confidential information, he wants to have a system
that is secure and only the employees can access the information by using a username and a password.


## Proposed Solution


I'm proposing to develop an application that will help the salesman to keep track of the sales, inventory, clients, purchases, and employees.
I'll make the application with a Graphical User Interface (GUI) that will be developed in Python with Kivymd. GUIs are generally more user-friendly than command-line interfaces. They use visual elements such as windows, icons, and menus to represent and manipulate data, making it easier for users to interact with the system.[^1]
 GUIs can improve efficiency by allowing users to perform tasks more quickly and easily. For example, they often provide drag-and-drop functionality, which can be much faster than typing commands. [^2]
Python is a high-level, interpreted, and general-purpose dynamic programming 
language that focuses on code readability. Python is a powerful, flexible, and easy-to-use language. In addition, the Python 
community is very active. It is used in many organizations as it supports multiple programming paradigms. It also performs automatic memory management.[^3] I'm using
Kivymd because The Kivy is defined as a python library that is available as a free, open-source library used for building the cross-platform applications that include Windows, Linux, iOS, 
Android and other platforms, and the look and feel of each application will be different from each other. It is important as it helps to develop multi-touch applications written in a python programming language that is very fast and robust.
The Kv language is used for writing the Kivy based program and helps to write the class, widgets and easy to configure.[^4] Kivy comes with a large set of UI controls, including buttons, sliders, and text inputs. [^5] Moreover, for the databases
I will use SQLite, which is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.[^6] SQLite is used extensively in various industries and for a multitude of applications. It's used in software testing, web browsers, embedded systems, and more. [^7]
SQLite is in the public domain, which means you can use it for any purpose, commercial or private. [^8]
Finally, to have a clear record of transactions, a button will be available to print the information in a PDF file.


[^1]: “Graphical User Interface (GUI).” Techopedia, Techopedia Inc., 1 Nov. 2023, www.techopedia.com/definition/4822/graphical-user-interface-gui.


[^2]: “Why Are Graphical User Interfaces Better Than Command Line Interfaces?” Quora, Quora, 1 Nov. 2023, www.quora.com/Why-are-Graphical-User-Interfaces-better-than-Command-Line-Interfaces.


[^3]: “Python Language Advantages and Applications.” GeeksforGeeks, GeeksforGeeks, 1 Nov. 2023, www.geeksforgeeks.org/python-language-advantages-applications/. 


[^4]: “What Is Kivy?: Need and Importance: Advantages and Disadvantages.” EDUCBA, 3 Apr. 2023, www.educba.com/what-is-kivy/. 


[^5]: “Kivy: Cross-platform Python Framework for NUI Development.” Kivy, kivy.org/#home.


[^6]: “SQLite.” Wikipedia, Wikimedia Foundation, 1 Nov. 2023, en.wikipedia.org/wiki/SQLite.


[^7]: “Appropriate Uses For SQLite.” SQLite, sqlite.org/appropriateuses.html.


[^8]: “SQLite: Small. Fast. Reliable. Choose Any Three.” SQLite, sqlite.org/index.html.


### Design Statement


I will design an application where both customers and the salesman can interact. The application will be run by a Graphical
User Interface (GUI) that will be developed in Python with Kivymd. It will take approximately 4 weeks to develop the application.
and will be evaluated with the success criteria shown below.


## Success Criteria


s TT a [issue tackled: "Finally, because there is confidential information, he wants to have a system
that is secure and only the employees can access the information by using an username and a password."]
2) The application will have a system to keep track of the sales, inventory, clients, purchases, and employees. [issue tackled: "having problems
with the record of sales, inventory, clients and purchases."]
3) The application will have a system to update the materials to produce the rackets, and check the availability of the materials. [issue tackled: "when trying to update the materials to produce the rackets,
he has to check the availability of the materials, but sometimes, the information that he gets is incorrect."]
4) The application will have a system to keep track of the schedule of the employees. [issue tackled: "Sometimes he needs the assistance of his employees to solve some problems,
but he does not have a way to track the schedule of his employees."]
5) The application will have a system to keep updated the data of the customers and the new customers to offer future promotions. [issue tackled: "Moreover, most of the time
he wants to keep the information of his customers in a table to offer future promotions, but he does not have a system to remember the customers."]
6) The application will have a button to print the information of Purchases and Orders Table. [issue tackled: "He is using a spreadsheet in a MacBook Air (2017) to keep track of this information, 
making it hard and time-consuming to find and track the information of purchases and sales"]
7) The application will have a screen where the user can produce the racket with the material and the color that the customer wants. [issue tackled: "Also, when trying to update the materials to produce the rackets,
he has to check the availability of the materials, but sometimes, the information that he gets is incorrect."]


### Introducing Success Criteria to the Client


![Email_sent.png](..%2FProject_Images%2FEmail_sent.png)


*Fig.2:* Email sent to the client with the success criteria


### Approval of the Success Criteria


![Approval.png](..%2FProject_Images%2FApproval.png)


*Fig.3:* Approval of the success criteria by the client


### Feedback from the Client


![Feedback.png](..%2FProject_Images%2FFeedback.png)


*Fig.4:* Feedback from the client


### Application Finished


![ApplicationComplete.png](..%2FProject_Images%2FApplicationComplete.png)


*Fig.5:* Application finished


# Criteria B: Design


## System Diagram


![SystemDiagramImage.png](..%2FProject_Images%2FSystemDiagramImage.png)


*Fig.6:* System Diagram for Project Unit 3


The system diagram in the `Project_Unit_3` provides a high-level overview of how the different components of the system interact with each other. It includes the user, the application, and the database.


**User**: The user interacts with the application through a Graphical User Interface (GUI). The user can perform various actions such as logging in, registering a new account, viewing and managing tables, placing orders, purchasing materials, and more.

**Application**: The application is the main component that facilitates all the operations. It's developed using Python and KivyMD for the GUI. It handles all the user inputs and processes them accordingly. For example, it validates user inputs, performs necessary calculations, and updates the GUI.

**Database**: The database is where all the data is stored and retrieved from. It's managed using SQLite. The application interacts with the database to perform operations such as inserting new records, updating existing records, and fetching data. For example, when a user places an order, the application inserts a new record in the 'orders' table in the database.


The arrows in the diagram represent the direction of interaction. For example, the user interacts with the application, and the application interacts with the database. The application also interacts with the user by displaying data and feedback on the GUI.


## Wireframe Diagram


![Wireframe_Diagram.png](..%2FProject_Images%2FWireframe_Diagram.png)


*Fig.7:* Wireframe Diagram for Project Unit 3


The Wireframe Diagram provides a visual representation of the user interface of the application. It outlines the structure and layout of the different screens, and how the user can navigate between them.
Each screen is designed to be intuitive and user-friendly, with clear labels and instructions. The user can easily navigate between the screens using the buttons provided. The Wireframe Diagram helps in understanding the flow and interaction of the application from the user's perspective.


## ER Diagram


![ER_Diagram.png](..%2FProject_Images%2FER_Diagram.png)


*Fig.8:* ER Diagram for Project Unit 3


The ER Diagram provides a visual representation of the data model for the application's database. It shows the entities (tables) in the database, the attributes (columns) of these entities, and the relationships between these entities.
The relationships between the entities are: Many users have many customers. Many Users make many purchases. One user has many orders. One order contains one material. One material is in one order.


## UML Diagram


![UML_Diagram_Part1.png](..%2FProject_Images%2FUML_Diagram_Part1.png)


*Fig.9:* UML Diagram(Part 1) for Project Unit 3


![UML_Diagram_Part2.png](..%2FProject_Images%2FUML_Diagram_Part2.png)


*Fig.10:* UML Diagram(Part 2) for Project Unit 3


The UML diagram for the Project_Unit_3 provides a visual representation of the classes used in the application, their attributes, methods, and the relationships between them.


## Flow Diagrams


![Place_Order_Function.png](..%2FProject_Images%2FPlace_Order_Function.png)


*Fig.11:* Flow Diagram for Place Order Function


![Purchase_Material_Function.png](..%2FProject_Images%2FPurchase_Material_Function.png)


*Fig.12:* Flow Diagram for Purchase Material Function


![Try_Register_Function.png](..%2FProject_Images%2FTry_Register_Function.png)


*Fig.13:* Flow Diagram for Try Register Function


## Test Plan


| Test No. | Test Type                                                                                                                                                                                                                                                                                                                           | Date   | Procedure                                                                                                                                                                                                                                                                                                    | Expected Outcome                                                                                                                                                                                                                                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Functional: Testing if the SignUp Screen successfully saves the data in the database and gives the errors when the input does not fulfill the policy, this with the function 'try_register'                                                                                                                                         | Feb 23 | By running Company_Application.py and clicking on the text button 'Don't have an account? Sign Up here' redirects to the Screen SignUp.  Then insert the values of name, email, password, confirm password,  manager code and the schedule and click the button'CREATE ACCOUNT' and  it goes to the MainPage | Saves every value given into the database  in the next order: given_name, password (the password must be hashed), schedule and email. After saving the data it redirects to the MainPage. If a policy is not successfully fulfilled, must give some errors in the TextField. |
| 2        | Functional: Testing if the Login Screen successfully connects with the database and enters without problem to the application, the function 'Try_login' should work properly.                                                                                                                                                       | Feb 23 | By running Company_Application.py and trying to SignIn with the values entered previously. Testing if the errors are working properly.                                                                                                                                                                       | If everything is correct, it must go to the MainPage. If a problem is presented, must give the errors in the TextField, giving the opportunity to enter another value.                                                                                                       |
| 3        | Functional: Testing if the Buttons can properly redirect to the assigned Screens                                                                                                                                                                                                                                                    | Feb 25 | By running Company_Application.py and making the proper changes in CompanyApp.kv the buttons must go to the assigned page.                                                                                                                                                                                   | Every button must go to the assigned page. Moreover, every page has a button 'return' which must get back to the MainPage.                                                                                                                                                   |
| 4        | Functional: Testing if the Update_Material screen works properly with the function 'purchase_popup' and 'purchase_material'                                                                                                                                                                                                         | Feb 26 | By running Company_Application.py and with the GUI developed in CompanyApp.kv and by clicking in the icon with the '+' inside the image of the material that I want to buy should show a popup message. Where an amount is required to buy the material.                                                     | After clicking on the icon '+' that every item has, and after putting the amount, it should save everything in the table 'Purchases' with the information of material_id, quantity, total_price and date. After that it should update the table of 'Materials'               |
| 5        | Functional: Testing if the Custom Screen works properly to make a new custom object. This with the function 'place_order'                                                                                                                                                                                                           | Feb 29 | By running Company_Application.py and clicking on the button 'Custom Orders' which redirects to the screen 'Custom' and then giving some values to test the  functionality of the code                                                                                                                       | Saves every value given into the table 'orders' in the next order: 'customer_id', 'material_id', 'color', 'quantity' and 'total_price'. When finished a the button 'CREATE OBJECT' pressed, should show a popup screen saying the success of the order.                      |
| 6        | Functional: Testing if the DropDownItem in the screen 'Custom' works properly to make the experience better for the user                                                                                                                                                                                                            | Mar 02 | By running Company_Application.py and clicking on the button 'Custom Orders' which will show the options, in this case there are two options with a dropdown table, that is to select the customer who is buying the project and the next one is to set the material of the racket                           | Displays the DropDownItem without problem, shows the possible options to select and when selected the value, shows the id of the customer who is requesting the object and the id of the material selected.                                                                  |
| 7        | Functional: Testing if the Tables that needs to be shown are working properly, updating every change. Some of them with the possibility to delete rows or enter a new value or make a PDF with the data. This with the functions 'on_pre_enter', 'update', 'row_pressed', 'check_box_pressed', 'delete', 'download_pdf', and 'save' | Mar 05 | By running Company_Application.py and clicking on the button 'Tables' will show different buttons to go to the different tables, the plan is to go through each one and use every button of each one to see if it works properly                                                                             | If a button is pressed, should go to the screen assigned and it will show the table with the information updated. Some of them have the opportunity to delete rows, add something new or save the information in a PDF it should work without problem.                       |
| 8        | Functional: Testing if the schedule of each employee can be chosen by displaying a popup screen where the time can be chosen.                                                                                                                                                                                                       | Mar 06 | By running Company_Application.py and clicking on the text button 'Don't have an account? Sign Up here' redirects to the Screen SignUp. Then clicking on the text button 'Pick your schedule'.                                                                                                               | After pressing the button a popup button should be pressed. With the functions show_time_picker and get_time should work, and the text showed in the screen should change to the time selected.                                                                              |
| 9        | Functional: Testing if the LogOut button in the 'MainPage' works properly. This with the function 'try_log_out'                                                                                                                                                                                                                     | Mar 07 | By running Company_Application.py and Signing In normally, then pressing the button 'Log Out'.                                                                                                                                                                                                               | When pressing Log Out should show a popup message which asks if the user wants to log out. If yes it should return to the SignIn page with every value restored. If no, is gonna close the popup message.                                                                    |
| 10       | Functional: Testing the complete functionality of the application with the customer                                                                                                                                                                                                                                                 | Mar 9  | By running Company_Application.py and going through every button and function. Trying to input values that can give an error and see if there are some gaps in the code.                                                                                                                                     | Every functionality should work without problem and the user can have the best experience possible. Not having problems when working on it                                                                                                                                   |

## Record Of Tasks


| Task No. | Planned Action                                               | Planned Outcome                                                                                          | Time Estimate | Completion Date | Criterion  |
|----------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------|-----------------|------------|
| 1        | First meeting with client                                    | To understand what the client requires                                                                   | 1 hour        | Feb 15          | A          |
| 2        | Working on the proposed solution                             | To give a clear idea to my client of what I can do to help him                                           | 25 min        | Feb 16          | A          |
| 3        | Working on the design statement and success criteria         | To give my client the features and the different methods my client can have when running the application | 1 hour        | Feb 17          | A          |
| 4        | Working on the System Diagram                                | Develop a clear idea of the hardware and software  requirements for the proposed solution                | 15 min        | Feb 18          | B          |
| 5        | Working on the possible Wireframe Diagram                    | To have a clear idea of what the application that I'm developing will have                               | 1 hour        | Feb 19          | B          |
| 6        | Thinking on the tables for the database that I will be using | To start doing the connections between them                                                              | 1 hour        | Feb 20          | B          |
| 7        | Start working on the SignUp screen                           | To see the functions that I need to use to save the values and state the policy for the SignUp Screen    | 2 hours       | Feb 21          | C          |
| 8        | Start working on the SingIn screen                           | To see the functions that I need to properly LogIn into the application                                  | 1 hour        | Feb 22          | C          |
| 9        | Working on the Functions try_login, try_register             | To give the proper functionality to the screen SignIn and SignUp                                         | 1 hour 30 min | Feb 23          | C          |
| 10       | Working on the MainPage                                      | To see the functions that I need for the MainPage and the screens that I need to add                     | 1 hour        | Feb 24          | C          |
| 11       | Adding the Screens missing such as the screens of the Tables | To have a better overview of my application                                                              | 1 hour        | Feb 25          | C          |
| 12       | Sending the report to my client                              | To check functionality and make possible changes or things that I can improve in my code                 | 15 min        | Feb 25          | A, B       |
| 13       | Getting feedback from my client                              | To improve the code. With the feedback implement the new changes                                         | 30 min        | Feb 26          | A, B       |
| 14       | Working on the changes of design                             | To make the application as the client requires                                                           | 2 hours       | Feb 27          | C          |
| 15       | Working on the UML Diagram                                   | To check how the classes are working, and see if I can improve something from it                         | 1 hour        | Feb 28          | B          |
| 16       | Working on the ER Diagram                                    | To check how the tables are working with a possibility to make something better                          | 30 min        | Feb 29          | B          |
| 17       | Working on the Flow Diagram for place_order                  | To check how the code works and find possible gaps in the code                                           | 30 min        | Mar 01          | B          |
| 18       | Working on the Flow Diagram  for purchase_material           | To check how the code works and find possible gaps in the code                                           | 30 min        | Mar 02          | B          |
| 19       | Working on the Flow Diagram for try_register                 | To check how the code works and find possible gaps in the code                                           | 30 min        | Mar 03          | B          |
| 20       | Working on the GUI of the code                               | To make the visual part of the application better                                                        | 2 hours       | Mar 04          | C          |
| 21       | Adding the button to create PDF Files from the tables        | Therefore my client can have a better management of the transactions                                     | 1 hour        | Mar 05          | C          |
| 22       | Adding the function time_picker when adding a new employee   | To know the schedule of the employee and keep it known for the client                                    | 30 min        | Mar 06          | C          |
| 23       | Going through the python code                                | To see if I can make something better, therefore less lines of code are used                             | 1 hour        | Mar 07          | C          |
| 24       | Going through the kiyvmd code                                | To see if I can make more buttons that can be used to make the code with less lines                      | 1 hour        | Mar 07          | C          |
| 25       | Finishing my test plans                                      | To see if there is no gaps in the code and the application runs properly                                 | 1 hour        | Mar 07          | B          |
| 26       | Sending the application to my customer                       | To see if the application fulfilled the customer requirements                                            | 15 min        | Mar 08          | A, B       |
| 27       | Getting the answer from my customer                          | The criteria given is completely fulfilled                                                               | 15 min        | Mar 08          | A, B       |
| 28       | Finishing criteria C                                         | Explaining every part of my code to make the things clear                                                | 2 hours       | Mar 09          | C          |
| 29       | Working on the video                                         | To see the different functions that my code has                                                          | 1 hour        | Mar 10          | D          |
| 30       | Uploading everything to github                               | To have the code stored somewhere and get feedback from Dr. Ruben                                        | 15 min        | Mar 11          | A, B, C, D |



# Criteria C: Development


## Existing Tools


| Software/Development Tools |
|----------------------------|
| Python                     |
| PyCharm                    |
| KivyMD                     |
| SQLite                     |


| Libraries |
|-----------|
| Kivymd    |
| Kivy      |
| Reportlab |
| SQLite    |
| Passlib   |


## List of Techniques used in the code


1. **Object-Oriented Programming (OOP)**: The code is structured around objects rather than actions and data rather than logic. This is evident from the use of classes such as `SignUp`, `MainPage`, and `CompanyApp`.

2. **Database Management**: SQLite is used for database management. The code includes SQL queries for data insertion, retrieval, and search operations.

3. **GUI Development**: The KivyMD library is used for creating the graphical user interface of the application. This includes creating screens, dialog boxes, and handling user input.

4. **Event-Driven Programming**: The code responds to user actions (events) such as button clicks and text input.

5. **Error Handling**: The code includes checks for potential errors, such as invalid user input during registration and login.

6. **Password Hashing**: For security, passwords are hashed before being stored in the database.

7. **Time Management**: The code includes functionality for picking and managing time schedules.

8. **Data Validation**: The code includes checks for validating user input, such as checking if an email contains "@" or if a password meets certain criteria.

9. **Use of External Libraries**: The code uses external libraries such as KivyMD for GUI and SQLite for database management.

10. **Code Modularity and Reusability**: The code is divided into functions and methods, each performing a specific task. This makes the code more readable, maintainable, and reusable.

11. **Data Binding**: The code uses data binding to link the GUI with the underlying data structures. For example, the `MDTimePicker` is bound to the `get_time` function.


## Development of the Application


## Python Code


### DatabaseWorker Class


```.python
class DatabaseWorker:
    def __init__(self, name):
        self.name_db = name
        self.connection = sqlite3.connect(self.name_db)
        self.cursor = self.connection.cursor()

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def insert(self, query):
        self.run_query(query)

    def search(self, query, multiple=False):
        results = self.cursor.execute(query)
        if multiple:
            return results.fetchall()
        return results.fetchone()


    def create_tables(self):
        #Users table
        query_users_table = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        given_name TEXT NOT NULL,
        password TEXT NOT NULL,
        schedule TEXT NOT NULL,
        email TEXT NOT NULL
        )"""

        query_materials_table = """CREATE TABLE IF NOT EXISTS materials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        material_name TEXT NOT NULL,
        material_price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        required_quantity INTEGER NOT NULL
        )"""

        query_customer_table = """CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uname TEXT NOT NULL,
        email TEXT NOT NULL
        )"""

        query_orders_table = """CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        material_id INTEGER NOT NULL,
        color TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        total_price REAL NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
        FOREIGN KEY (material_id) REFERENCES materials(id)
        )"""

        query_purchases_table = """CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        material_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        total_price REAL NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (material_id) REFERENCES materials(id)
        )"""

        # self.run_query(query_users_table)
        # self.run_query(query_materials_table)
        # self.run_query(query_customer_table)
        # self.run_query(query_orders_table)
        # self.run_query(query_purchases_table)


    def close(self):
        self.connection.close()
```
The `__init__` method initializes the class with a database name and establishes a connection to the database. The `run_query` method executes a given SQL query and commits the changes to the database. The `insert` method is a wrapper for `run_query` intended specifically for insert operations. The `search` method executes a given SQL query and returns either all results (if `multiple` is `True`) or the first result (if `multiple` is `False`). The `create_tables` method defines SQL queries for creating several tables ('users', 'materials', 'customers', 'orders', 'purchases'). The `close` method closes the connection to the database.


### Sign In Functionality (**Success Criteria 1**)


```.python
def try_login(self):
    uname = self.ids.user.text
    passwd = self.ids.password.text
    user = CompanyApp.db.search(f"SELECT * FROM users WHERE given_name = '{uname}'")
    if user:
        if check_hash(passwd, user[2]):
            self.parent.current = "Third"
        else:
            self.ids.password.error = True
            self.ids.password.helper_text = "Invalid password."
    else:
        self.ids.user.error = True
        self.ids.user.helper_text = "User not found."
```
This part of the code is a function named `try_login` that is used to authenticate a user in the application.


`uname = self.ids.user.text`: This line retrieves the username entered by the user in the GUI.
`passwd = self.ids.password.text`: This line retrieves the password entered by the user in the GUI.
`user = CompanyApp.db.search(f"SELECT * FROM users WHERE given_name = '{uname}'")`: This line queries the database to find a user with the given username. If a user with the given username exists, it returns the user's details; otherwise, it returns `None`.
`if user:`: This checks if a user was found in the database. If a user was found, it proceeds to the next step; otherwise, it sets an error message on the username field in the GUI.
`if check_hash(passwd, user[2]):`: This checks if the entered password, when hashed, matches the hashed password stored in the database for the found user. If the passwords match, it proceeds to the next step; otherwise, it sets an error message on the password field in the GUI.
`self.parent.current = "Third"`: If the passwords match, this line changes the current screen of the application to the screen with the name "Third".
`self.ids.password.error = True` and `self.ids.password.helper_text = "Invalid password."`: If the passwords do not match, these lines set an error state and error message on the password field in the GUI.
`self.ids.user.error = True` and `self.ids.user.helper_text = "User not found."`: If no user was found in the database, these lines set an error state and error message on the username field in the GUI.


### Tables Overview Functionality (**Success Criteria 2**)


```.python
def on_pre_enter(self, *args):
    column_names = [('ID', 20), ('Username', 30), ('Password', 100), ('Schedule', 40), ('Email', 40)]
    self.data_tables = MDDataTable(
        size_hint=(0.9, 0.5),
        pos_hint={'center_x': 0.5, 'center_y': 0.6},
        use_pagination=False,
        check=True,
        column_data=column_names,
    )
    self.data_tables.bind(on_row_press=self.row_pressed)
    self.data_tables.bind(on_check_press=self.checkbox_pressed)
    self.add_widget(self.data_tables)
    self.update()

def update(self):
    data = CompanyApp.db.search('SELECT * FROM users', multiple=True)
    self.data_tables.update_row_data(
        None, data
    )

def row_pressed(self, table, cell):
    print(f"Values Clicked {cell.text}")

def checkbox_pressed(self, table, current_row):
    print(f"Record Checked {current_row}")
    if current_row in self.selected_rows:
        self.selected_rows.remove(current_row)
    else:
        self.selected_rows.append(current_row)
```
`on_pre_enter(self, *args)`: This function is called before the screen is displayed. It sets up a data table with specific column names and binds certain events (row press and check press) to their respective handler functions. It also adds the data table as a widget to the screen and calls the `update` function to populate the table with data.


`update(self)`: This function retrieves data from the database (all users in this case) and updates the data table with this data.


`row_pressed(self, table, cell)`: This function is the event handler for when a row in the data table is pressed. It prints the text of the cell that was clicked.


`checkbox_pressed(self, table, current_row)`: This function is the event handler for when a checkbox in the data table is pressed. It prints the row that was checked. If the row was already in the `selected_rows` list, it removes it; otherwise, it adds it. This allows for the selection and deselection of rows in the data table.


### Purchase Materials Functionality (**Success Criteria 3**)


```.python
def purchase_popup(self, material_id):
    self.material_id = material_id
    self.dialog = MDDialog(
        title="Purchase Material",
        type="custom",
        content_cls=PurchaseContent(),
        buttons=[
            MDFlatButton(
                text="CANCEL", on_release=self.close_dialog
            ),
            MDFlatButton(
                text="PURCHASE", on_release=self.purchase_material
            ),
        ],
    )
    self.dialog.open()

def purchase_material(self, *args):
    quantity = self.dialog.content_cls.ids.quantity.text
    if quantity:
        total_price = int(quantity) * 10
        CompanyApp.db.insert(f"INSERT INTO purchases (material_id, quantity, total_price, date) VALUES ({self.material_id}, {quantity}, {total_price}, '{datetime.now()}')")
        material = CompanyApp.db.search(f"SELECT * FROM materials WHERE id = {self.material_id}")
        new_quantity = material[3] + int(quantity)
        CompanyApp.db.update(f"UPDATE materials SET quantity = {new_quantity} WHERE id = {self.material_id}")
        self.dialog.dismiss()
    else:
        self.dialog.content_cls.ids.quantity.error = True
        self.dialog.content_cls.ids.quantity.helper_text = "Quantity is required."
```
This part of the code is related to the purchasing of materials in the application.


`purchase_popup(self, material_id)`: This function is used to open a dialog box for purchasing materials. It takes the `material_id` as an argument which is the ID of the material to be purchased. The function creates a dialog box with the title "Purchase Material" and two buttons "CANCEL" and "PURCHASE". The "CANCEL" button closes the dialog box and the "PURCHASE" button triggers the `purchase_material` function.


`purchase_material(self, *args)`: This function is used to handle the purchase of materials. It retrieves the quantity of the material to be purchased from the dialog box. If a quantity is provided, it calculates the total price (assuming the price of each unit is 10), inserts the purchase record into the 'purchases' table in the database, updates the quantity of the material in the 'materials' table, and then dismisses the dialog box. If no quantity is provided, it sets an error state and error message on the quantity field in the dialog box.


### Entering a New Employee Functionality (**Success Criteria 4**)


```.python
def try_register(self):

    # define local variables
    name = self.ids.uname.text
    email = self.ids.email.text
    passwd = self.ids.password.text
    passwd_check = self.ids.confirm_password.text
    secret_code = self.ids.code_manager.text
    schedule_time = self.ids.time.text

    if len(name) == 0 or " " in name:
        if len(name) == 0:
            self.ids.uname.error = True
            self.ids.uname.helper_text = "This field is required."
        return

    # Email policy
    # If email does not have @, has 0 characters or already exists in database, show error
    name_validation = CompanyApp.db.search(f"Select * from users where given_name = '{name}'")
    if name_validation:
        self.ids.uname.error = True
        self.ids.uname.helper_text = "A user already exists with this name"
        return

    email_validation = CompanyApp.db.search(f"SELECT * FROM users WHERE email = '{email}'")

    if "@" not in email or len(email) == 0 or email_validation:
        if "@" not in email:
            self.ids.email.error = True
            self.ids.email.helper_text = "Invalid email. Needs to include @ sign."
        if len(email) == 0:
            self.ids.email.error = True
            self.ids.email.helper_text = "This field is required."
        if email_validation:
            self.ids.email.error = True
            self.ids.email.helper_text = "A user already exists with this email."
        return

    # Password policy
    # If username has 0 characters, space, is not equal to passw check or has less tha 4 charc, show error
    if len(passwd) < 4 or " " in passwd or passwd != passwd_check or len(passwd) == 0:
        if len(passwd) < 4:
            self.ids.password.error = True
            self.ids.password.helper_text = "Password must be longer than 4 characters."
        if passwd != passwd_check:
            self.ids.confirm_password.error = True
            self.ids.password.error = True
            self.ids.confirm_password.helper_text = "Passwords do not match."
            self.ids.password.helper_text = "Passwords do not match."
        if len(passwd) == 0:
            self.ids.password.error = True
            self.ids.password.helper_text = "This field is required."
        return

    if secret_code != "1234":
        self.ids.code_manager.error = True
        self.ids.code_manager.helper_text = "Invalid code."
        return

    # Password check policy
    # If check password has 0 characters, show error
    if len(passwd_check) == 0:
        self.ids.confirm_password.error = True
        self.ids.confirm_password.helper_text = "This field is required."
        return

    else:
        CompanyApp.db.insert(f"INSERT INTO users (given_name, password, schedule, email) VALUES ('{name}', '{make_hash(passwd)}', '{schedule_time}','{email}')")
        Dialog = MDDialog(title="Success!", text="You have been registered!")
        Dialog.open()
        self.parent.current = "Third"

def show_time_picker(self):
    time_dialog = MDTimePicker()
    time_dialog.bind(time=self.get_time)
    time_dialog.open()

def get_time(self, instance, time):
    self.ids.time.text = str(time)
```

The `try_register` function is used to register a new user in the application. It first retrieves the user input from the GUI, including the username, email, password, password confirmation, secret code, and schedule time. It then validates this input according to various policies. For example, it checks if the username is empty or contains a space, if the email is valid and unique, if the password meets certain criteria and matches the password confirmation, and if the secret code is correct. If any of these checks fail, it sets an error state and error message on the corresponding field in the GUI. If all checks pass, it inserts the new user into the database, displays a success dialog, and navigates to the "Third" screen. The `show_time_picker` function opens a time picker dialog and binds the selected time to the `get_time` function, which sets the text of the time field in the GUI to the selected time.


### Customers Updated Functionality (**Success Criteria 5**)
    
```.python
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.data_tables = None
    self.selected_rows = []

def on_pre_enter(self, *args):
    column_names = [('ID', 40), ('Username', 40), ('Email', 40)]
    self.data_tables = MDDataTable(
        size_hint=(0.5, 0.5),
        pos_hint={'center_x': 0.5, 'center_y': 0.7},
        use_pagination=False,
        check=True,
        column_data=column_names,
    )
    self.data_tables.bind(on_row_press=self.row_pressed)
    self.data_tables.bind(on_check_press=self.checkbox_pressed)
    self.add_widget(self.data_tables)
    self.update()

def update(self):
    data = CompanyApp.db.search('SELECT * FROM customers', multiple=True)
    self.data_tables.update_row_data(
        None, data
    )

def row_pressed(self, table, cell):
    print(f"Values Clicked {cell.text}")

def checkbox_pressed(self, table, current_row):
    print(f"Record Checked {current_row}")
    if current_row in self.selected_rows:
        self.selected_rows.remove(current_row)
    else:
        self.selected_rows.append(current_row)

def save(self):
    uname = self.ids.name.text
    email = self.ids.email.text
    save_query = f"""INSERT INTO customers (uname, email) 
                    VALUES ('{uname}', '{email}')"""
    CompanyApp.db.insert(save_query)
    self.update()
    Dialog = MDDialog(title="Success!", text="Customer has been added!")
    Dialog.open()
    self.ids.name.text = ""
    self.ids.email.text = ""

def delete(self):
    for row in self.selected_rows:
        CompanyApp.db.run_query(f"DELETE FROM customers WHERE id = {row[0]}")
    self.update()

def delete_all(self):
    CompanyApp.db.run_query("DELETE FROM customers")
    self.update()
```

The `__init__` method initializes the class with `data_tables` and `selected_rows` attributes. The `on_pre_enter` method sets up a data table with specific column names and binds row press and check press events to their respective handler functions. The `update` method fetches all customers from the database and updates the data table. The `row_pressed` and `checkbox_pressed` methods handle row press and check press events respectively, with the latter also managing the selection of rows. The `save` method retrieves user input from the GUI, inserts a new customer into the database, updates the data table, and displays a success dialog. The `delete` method deletes selected customers from the database and updates the data table. The `delete_all` method deletes all customers from the database and updates the data table.


### PDF Button Functionality (**Success Criteria 6**)

```.python
def fetch_data(self):
    conn = sqlite3.connect('Project3Data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM purchases")
    data = cursor.fetchall()
    conn.close()
    return data

def generate_pdf(self, data):
    doc = SimpleDocTemplate("purchases.pdf", pagesize=letter)

    # Create a Table with the data
    table = Table(data)

    # Create a TableStyle and add it to the Table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    # Add the Table to the elements to be added to the PDFr
    elements = []
    elements.append(table)

    # Build the PDF
    doc.build(elements)

def download_pdf(self):
    data = self.fetch_data()
    self.generate_pdf(data)
    Dialog = MDDialog(title="Success!", text="PDF has been downloaded!")
    Dialog.open()
```

The code is related to fetching data from a SQLite database and generating a PDF document from that data.


`fetch_data(self)`: This function connects to a SQLite database named 'Project3Data.db', executes a SQL query to select all records from the 'purchases' table, fetches all the rows returned by the query, closes the database connection, and returns the fetched data.


`generate_pdf(self, data)`: This function takes the data fetched from the database as an argument and generates a PDF document named 'purchases.pdf' using the ReportLab library. It creates a table with the data, applies a style to the table (including alignment, font, color, and grid settings), and adds the table to the PDF document.


`download_pdf(self)`: This function calls the `fetch_data` function to get the data from the database, passes this data to the `generate_pdf` function to create the PDF, and then displays a success dialog to inform the user that the PDF has been downloaded. This function is called twice in the application.


### Creating the Racket Functionality (**Success Criteria 7**)

```.python
def drop_item(self, drop_item_element):
    users = CompanyApp.db.search("SELECT uname, email FROM customers", multiple=True)
    self.menu_items = [f"{user[0]} {user[1]}" for user in users]
    buttons_menu =[]
    for item in self.menu_items:
        buttons_menu.append(
            {"text": item,
             "on_release": lambda x=item: self.button_pressed(x, drop_item_element),
             "viewclass": "OneLineListItem",
             }
        )
    self.menu = MDDropdownMenu(caller=drop_item_element, items=buttons_menu, width_mult=2)
    self.menu.open()

def button_pressed(self, x, drop_item_element):
    first, last = x.split(" ")
    user_id = CompanyApp.db.search(f"SELECT id FROM customers WHERE uname = '{first}' AND email = '{last}'")
    drop_item_element.text = str(user_id[0])
    self.menu.dismiss()

def drop_material(self, drop_item_element):
    materials = CompanyApp.db.search("SELECT material_name FROM materials", multiple=True)
    self.menu_items = [f"{material[0]}" for material in materials]
    buttons_menu =[]
    for item in self.menu_items:
        buttons_menu.append(
            {"text": item,
             "on_release": lambda x=item: self.button_pressed_material(x, drop_item_element),
             "viewclass": "OneLineListItem",
             }
        )
    self.menu = MDDropdownMenu(caller=drop_item_element, items=buttons_menu, width_mult=2)
    self.menu.open()

def button_pressed_material(self, x, drop_item_element):
    material_id = CompanyApp.db.search(f"SELECT id FROM materials WHERE material_name = '{x}'")
    drop_item_element.text = str(material_id[0])
    self.menu.dismiss()

def place_order(self):
    customer_id = self.ids.customer_id.text
    material_id = self.ids.material_id.text
    color = self.ids.color.text
    quantity = self.ids.quantity.text
    # Check if the quantity is available
    if int(quantity) > CompanyApp.db.search(f"SELECT quantity FROM materials WHERE id = {material_id}")[0]:
        Dialog = MDDialog(title="Error!", text="Not enough quantity available.")
        Dialog.open()
        return
    total_price = CompanyApp.db.search(f"SELECT material_price FROM materials WHERE id = {material_id}")
    final_price = float(total_price[0]) * int(quantity)
    save_query = f"""INSERT INTO orders (customer_id, material_id, color, quantity, total_price) 
                    VALUES ({customer_id}, {material_id}, '{color}', {quantity}, {final_price})"""
    CompanyApp.db.insert(save_query)
    Dialog = MDDialog(title="Success!", text="Order has been placed!")
    Dialog.open()
    self.ids.customer_id.text = ""
    self.ids.material_id.text = ""
    self.ids.color.text = ""
    self.ids.quantity.text = ""
    #update the values in the table materials specifically with quantity availability

    current_quantity = CompanyApp.db.search(f"SELECT quantity FROM materials WHERE id = {material_id}")[0]
    required_quantity = CompanyApp.db.search(f"SELECT required_quantity FROM materials WHERE id = {material_id}")[0]
    new_quantity = current_quantity - (int(quantity) * int(required_quantity))
    CompanyApp.db.run_query(f"UPDATE materials SET quantity = {new_quantity} WHERE id = {material_id}")

def restart_order(self):
    self.ids.customer_id.text = ""
    self.ids.material_id.text = ""
    self.ids.color.text = ""
    self.ids.quantity.text = ""
```
The `drop_item` and `drop_material` methods are used to create dropdown menus for selecting a customer and a material, respectively. They fetch the relevant data from the database, create a list of menu items, and then create a dropdown menu with these items. The `button_pressed` and `button_pressed_material` methods are event handlers for when a menu item is selected. They update the text of the dropdown menu caller (the button that opened the dropdown menu) with the ID of the selected customer or material, and then dismiss the dropdown menu.


The `place_order` method is used to place an order. It first retrieves the selected customer ID, material ID, color, and quantity from the GUI. It then checks if the requested quantity of the material is available. If not, it displays an error dialog and returns. If the quantity is available, it calculates the total price of the order, inserts the order into the 'orders' table in the database, displays a success dialog, and clears the input fields in the GUI. Finally, it updates the quantity of the selected material in the 'materials' table in the database to reflect the quantity used in the order.


The `restart_order` method is used to clear the input fields in the GUI, effectively resetting the order form.


## KivyMD Code


### Screens


```.python
ScreenManager:
    LoginScreen:
        name: "First"
    SignUp:
        name: "Second"
    MainPage:
        name: "Third"
    Table_Order:
        name: "Forth"
    Update_Material:
        name: "Fifth"
    Custom:
        name: "Sixth"
    Customers:
        name: "Seventh"
    Tables:
        name: "Eighth"
    Employees:
        name: "Ninth"
    Materials:
        name: "Tenth"
    Purchases:
        name: "Eleventh"
```


This part of the KivyMD code defines a `ScreenManager` and several `Screen` objects. The `ScreenManager` is a widget dedicated to managing multiple screens for your application. It is used to switch between different `Screen` objects, which represent different pages or states of your application.
Each `Screen` has a `name` property, which is a string that uniquely identifies the screen. This name is used to switch between screens.
Here's a brief explanation of each screen:


1. `LoginScreen`: This screen is used for user authentication. It's named "First".
2. `SignUp`: This screen is used for user registration. It's named "Second".
3. `MainPage`: This is likely the main or home screen of the application. It's named "Third".
4. `Table_Order`: This screen is used for displaying or managing orders. It's named "Forth".
5. `Update_Material`: This screen is used for updating material information. It's named "Fifth".
6. `Custom`: The purpose of this screen is to create the custom rackets. It's named "Sixth".
7. `Customers`: This screen is used for displaying or managing customer information. It's named "Seventh".
8. `Tables`: This screen is like another main screen, where shows different buttons that will display the information of the button selected. It's named "Eighth".
9. `Employees`: This screen is used for displaying or managing employee information. It's named "Ninth".
10. `Materials`: This screen is used for displaying or managing material information. It's named "Tenth".
11. `Purchases`: This screen is used for displaying or managing purchase information. It's named "Eleventh".


# Criteria D: Functionality


## Youtube Link for the Video


[Click Here For The Video] (https://youtu.be/6NPSfyVYBbE)
