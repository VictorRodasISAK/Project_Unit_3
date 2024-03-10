from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDTimePicker
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField

from Library import DatabaseWorker, make_hash, check_hash
import datetime

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import sqlite3


class Employees(MDScreen):

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

    def delete(self):
        for row in self.selected_rows:
            CompanyApp.db.run_query(f"DELETE FROM users WHERE id = {row[0]}")
        self.update()

class Materials(MDScreen):

    def on_pre_enter(self, *args):
        column_names = [('ID', 40), ('Material', 40), ('Price', 40), ('Quantity', 40), ('Required Quantity', 40)]
        self.data_tables = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            use_pagination=False,
            check=True,
            column_data=column_names,
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = CompanyApp.db.search('SELECT * FROM materials', multiple=True)
        self.data_tables.update_row_data(
            None, data
        )

    def row_pressed(self, table, cell):
        print(f"Values Clicked {cell.text}")

    def checkbox_pressed(self, table, current_row):
        print(f"Record Checked {current_row}")


class Tables(MDScreen):
    pass

class Purchases(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []

    def on_pre_enter(self, *args):
        column_names = [('ID', 40), ('Material', 40), ('Quantity', 40), ('Total Price', 40), ('Date', 40)]
        self.data_tables = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            use_pagination=False,
            check=True,
            column_data=column_names,
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = CompanyApp.db.search('SELECT * FROM purchases', multiple=True)
        self.data_tables.update_row_data(
            None, data
        )

    def row_pressed(self, table, cell):
        print(f"Values Clicked {cell.text}")

    def checkbox_pressed(self, table, current_row):
        print(f"Record Checked {current_row}")

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




class Table_Order(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_tables = None
        self.selected_rows = []

    def on_pre_enter(self, *args):
        column_names = [('ID', 40), ('Customer', 30), ('Material', 30), ('Color', 40), ('Quantity', 25), ('Total Price', 50)]
        self.data_tables = MDDataTable(
            size_hint=(0.8, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            use_pagination=False,
            check=True,
            column_data=column_names,
        )
        self.data_tables.bind(on_row_press=self.row_pressed)
        self.data_tables.bind(on_check_press=self.checkbox_pressed)
        self.add_widget(self.data_tables)
        self.update()

    def update(self):
        data = CompanyApp.db.search('SELECT * FROM orders', multiple=True)
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

    def delete_selected(self):
        for row in self.selected_rows:
            CompanyApp.db.run_query(f"DELETE FROM orders WHERE id = {row[0]}")
        self.update()


    def fetch_data(self):
        conn = sqlite3.connect('Project3Data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        data = cursor.fetchall()
        conn.close()
        return data

    def generate_pdf(self, data):
        doc = SimpleDocTemplate("orders.pdf", pagesize=letter)

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

        # Add the Table to the elements to be added to the PDF
        elements = []
        elements.append(table)

        # Build the PDF
        doc.build(elements)

    def download_pdf(self):
        data = self.fetch_data()
        self.generate_pdf(data)
        Dialog = MDDialog(title="Success!", text="PDF has been downloaded!")
        Dialog.open()



class Customers(MDScreen):
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

class Update_Material(MDScreen):
    def purchase_popup(self, material_name):
        self.quantity_field = MDTextField(
            hint_text="Enter quantity",
            helper_text="This will determine how much material you want to buy",
            helper_text_mode="on_focus",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint_x=None,
            width=200
        )
        self.purchase_popup = MDDialog(
            title="Purchase Material",
            type="custom",
            content_cls=self.quantity_field,
            buttons=[
                MDFlatButton(
                    text="CANCEL", on_release=lambda x: self.purchase_popup.dismiss()
                ),
                MDFlatButton(
                    text="BUY", on_release=lambda x: self.purchase_material(material_name)
                )
            ],
        )
        self.purchase_popup.open()

    def purchase_material(self, material_name):
        quantity = self.quantity_field.text
        self.purchase_popup.dismiss()
        # update the values in the table materials specifically with quantity availability
        current_quantity = CompanyApp.db.search(f"SELECT quantity FROM materials WHERE material_name = '{material_name}'")[0]
        new_quantity = current_quantity + int(quantity)
        CompanyApp.db.run_query(f"UPDATE materials SET quantity = {new_quantity} WHERE material_name = '{material_name}'")
        Dialog = MDDialog(title="Success!", text="Material has been purchased!")
        Dialog.open()
        # update the values in the table purchases just with the id, the quantity bought, the data and the total paid
        date = datetime.datetime.now()
        material_id = CompanyApp.db.search(f"SELECT id FROM materials WHERE material_name = '{material_name}'")[0]
        total_price = float(quantity) * (CompanyApp.db.search(f"SELECT material_price FROM materials WHERE material_name = '{material_name}'")[0])
        CompanyApp.db.insert(f"INSERT INTO purchases (material_id, quantity, total_price, date) VALUES ({material_id}, {quantity}, {total_price}, '{date}')")

class Custom(MDScreen):
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


class MyButton5(MDLabel):
    pass
class MyButton4(MDIconButton):
    pass

class MyButton3(FitImage):
    pass
class MyButton2(MDFlatButton):
    pass
class MyButton(Button):
    pass
class LoginScreen(MDScreen):
    def clear(self):
        self.ids.user.text = ""
        self.ids.password.text = ""

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

class SignUp(MDScreen):
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



class MainPage(MDScreen):
    def try_logout(self):
        self.sign_out_confirmation_dialog = MDDialog(
            title="Sign Out",
            text="Are you sure you want to sign out?",
            buttons=[
                MyButton2(
                    text="CANCEL", on_release=lambda x: self.sign_out_confirmation_dialog.dismiss()
                ),
                MyButton2(
                    text="YES", on_release=self.log_out
                ),
            ],
        )

        self.sign_out_confirmation_dialog.open()

    def log_out(self, *args):
        self.sign_out_confirmation_dialog.dismiss()
        self.parent.current = "First"
        self.parent.get_screen("First").clear()





class CompanyApp(MDApp):
    db = DatabaseWorker("Project3Data.db")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        Window.size = (1250, 1000)



test = CompanyApp()
test.db.create_tables()
test.run()


