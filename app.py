# from tkinter import *

# def get_user_input():
#     user_input = entry.get()
#     print(f'User entered: {user_input}')
#     user_age=age.get()
#     print(f'User age:{user_age}')
# window = Tk()

# window.geometry('400x300')

# label=Label(window,text='Enter your name')
# label.pack()

# entry=Entry(window)
# entry.pack()

# label_age=Label(window,text='Enter Age')
# label_age.pack()

# age=Entry(window)
# age.pack()



# button = Button(window,text="Submit",command=get_user_input)
# button.pack()

# window.mainloop()

# from tkinter import *

# def display_result():
#     name=name_input.get()
#     print(name)


# window=Tk()

# window.geometry('400x300')

# name_label=Label(window,text='Name:')
# name_label.grid(row=0,column=0)
# name_input = Entry(window)
# name_input.grid(row=0,column=1)

# submit_button = Button(window,text='Submit',command=display_result)
# submit_button.grid(row=0,column=2)

# window.mainloop()

# import mysql.connector
# from tkinter import *

# def connect_db():
#     conn = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='mydatabase'
#     )
#     return conn

# def fetch_data():
#     conn = connect_db()
#     cursor=conn.cursor()
#     cursor.execute('select * from users')
#     results=cursor.fetchall()
#     conn.close()
#     for result in results:
#         label=Label(window,text=result[1])
#         label.pack()


# window = Tk()

# window.geometry('400x300')

# fetch_button=Button(window,text='Fetch Data',command=fetch_data)
# fetch_button.pack()
    
# window.mainloop()




# from tkinter import *
# import mysql.connector

# def connect_db():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",       # Your MySQL username
#         password="root", # Your MySQL password
#         database="mydatabase" # Database name
#     )
#     return conn

# def saveData():
#     name=nameInput.get()
#     age=ageInput.get()
#     print(name,age)
#     if name and age:
#         conn = connect_db()
#         cursor=conn.cursor()
#         cursor.execute('insert into users (name,age) values(%s,%s)',(name,age))
#         conn.commit()
#         conn.close()
#         successLabel.config(text='Data Inserted Successfully',fg='green')
#     else:
#         successLabel.config(text='Please fill both the fields',fg='red')

# window=Tk()

# window.geometry('400x300')

# nameLabel=Label(window,text='Name: ')
# nameLabel.grid(row=0,column=0)

# nameInput = Entry(window,width=18)
# nameInput.grid(row=0,column=1)

# ageLabel=Label(window,text='Age: ')
# ageLabel.grid(row=0,column=2)

# ageInput = Entry(window,width=18)
# ageInput.grid(row=0,column=3)


# submitButton=Button(window,text='Submit',width=18,command=saveData)
# submitButton.grid(row=0,column=4)

# successLabel = Label(window,text='')
# successLabel.grid(row=1,column=0)



# window.mainloop()



# from tkinter import *
# import mysql.connector

# def connect_db():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",       # Your MySQL username
#         password="root", # Your MySQL password
#         database="mydatabase" # Database name
#     )
#     return conn

# def upDateData():
#     name=nameInput.get()
#     age=ageInput.get()
#     id = idInput.get()
#     print(name,age)
#     if name and age and id:
#         conn = connect_db()
#         cursor=conn.cursor()
#         cursor.execute('update users set name=%s, age= %s where id=%s',(name,age,id))
#         conn.commit()
#         conn.close()
#         successLabel.config(text='Data Updated Successfully',fg='green')
#     else:
#         successLabel.config(text='Please fill both the fields',fg='red')

# window=Tk()

# window.geometry('600x300')

# updateMsg = Label(window,text="Please enter details to update")
# updateMsg.grid(row=3,column=0)

# idLabel=Label(window,text="Enter id: ")
# idLabel.grid(row=4,column=0)

# idInput=Entry(window,width=18)
# idInput.grid(row=4,column=1)

# nameLabel=Label(window,text='Name: ')
# nameLabel.grid(row=0,column=0)

# nameInput = Entry(window,width=18)
# nameInput.grid(row=0,column=1)

# ageLabel=Label(window,text='Age: ')
# ageLabel.grid(row=0,column=2)

# ageInput = Entry(window,width=18)
# ageInput.grid(row=0,column=3)


# submitButton=Button(window,text='Submit',width=18,command=upDateData)
# submitButton.grid(row=0,column=4)

# successLabel = Label(window,text='')
# successLabel.grid(row=1,column=0)

# window.mainloop()


# from tkinter import *
# import mysql.connector

# def connect_db():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",       # Your MySQL username
#         password="root", # Your MySQL password
#         database="mydatabase" # Database name
#     )
#     return conn

# def deleteRecord():
#     id=idInput.get()
#     if id:
#         conn = connect_db()
#         cursor=conn.cursor()
#         cursor.execute('delete from users where id=%s',(id,))
#         conn.commit()
#         conn.close()
#         successLabel.config(text='Data deleted Successfully',fg='green')
#     else:
#         successLabel.config(text='Unable to delete, Please try with correct id',fg='red')

# window=Tk()

# window.geometry('400x300')

# idLabel=Label(window,text='id:')
# idLabel.grid(row=0,column=0)

# idInput = Entry(window,width=18)
# idInput.grid(row=0,column=1)

# successLabel = Label(window,text='')
# successLabel.grid(row=1,column=0)

# submitButton=Button(window,text='Submit',width=18,command=deleteRecord)
# submitButton.grid(row=0,column=4)

# window.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector

# # Connect to MySQL Database
# def connect_db():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root",
#         database="mydatabase"
#     )
#     return conn

# # Function to delete data with confirmation
# def delete_data():
#     user_id = id_entry.get()

#     if not user_id:  # Ensure ID is entered
#         status_label.config(text="Please enter an ID.", fg="red")
#         return

#     conn = connect_db()
#     cursor = conn.cursor()

#     # Check if ID exists
#     cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
#     result = cursor.fetchone()

#     if result is None:
#         status_label.config(text="ID not found.", fg="red")
#     else:
#         # Show confirmation dialog
#         confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete ID {user_id}?")
        
#         if confirm:
#             cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
#             conn.commit()
#             status_label.config(text="Data Deleted Successfully!", fg="green")
#         else:
#             status_label.config(text="Deletion Canceled.", fg="blue")

#     conn.close()

# # Setting up the Tkinter window
# window = tk.Tk()
# window.geometry("400x250")

# id_label = tk.Label(window, text="Enter ID to Delete:")
# id_label.pack()
# id_entry = tk.Entry(window)
# id_entry.pack()

# delete_button = tk.Button(window, text="Delete Data", command=delete_data)
# delete_button.pack()

# status_label = tk.Label(window, text="")
# status_label.pack()

# window.mainloop()


# import tkinter as tk
# from tkinter import ttk, messagebox
# import mysql.connector

# # Function to connect to MySQL
# def connect_db():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",  
#         password="root",  
#         database="mydatabase"
#     )
#     return conn

# # Function to insert data
# def insert_data():
#     name = name_entry.get()
#     age = age_entry.get()

#     if name and age:
#         conn = connect_db()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
#         conn.commit()
#         conn.close()
#         fetch_data()  # Refresh data
#         name_entry.delete(0, tk.END)
#         age_entry.delete(0, tk.END)
#         messagebox.showinfo("Success", "Data Inserted Successfully!")
#     else:
#         messagebox.showerror("Error", "Please enter both Name and Age.")

# # Function to fetch data from database and display in treeview
# def fetch_data():
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users")
#     rows = cursor.fetchall()
#     conn.close()
    
#     # Clear previous data in treeview
#     for item in tree.get_children():
#         tree.delete(item)

#     # Insert new data into treeview
#     for row in rows:
#         tree.insert("", "end", values=row)

# # Function to update data
# def update_data():
#     selected_item = tree.focus()
#     if not selected_item:
#         messagebox.showerror("Error", "Please select a record to update.")
#         return

#     user_id = tree.item(selected_item)["values"][0]  # Get ID of selected row
#     new_name = name_entry.get()
#     new_age = age_entry.get()

#     if new_name or new_age:
#         conn = connect_db()
#         cursor = conn.cursor()
        
#         if new_name and new_age:
#             cursor.execute("UPDATE users SET name=%s, age=%s WHERE id=%s", (new_name, new_age, user_id))
#         elif new_name:
#             cursor.execute("UPDATE users SET name=%s WHERE id=%s", (new_name, user_id))
#         elif new_age:
#             cursor.execute("UPDATE users SET age=%s WHERE id=%s", (new_age, user_id))

#         conn.commit()
#         conn.close()
#         fetch_data()  # Refresh data
#         messagebox.showinfo("Success", "Data Updated Successfully!")
#     else:
#         messagebox.showerror("Error", "Please enter new Name or Age.")

# # Function to delete data
# def delete_data():
#     selected_item = tree.focus()
#     if not selected_item:
#         messagebox.showerror("Error", "Please select a record to delete.")
#         return

#     user_id = tree.item(selected_item)["values"][0]  # Get ID of selected row
#     confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete ID {user_id}?")
    
#     if confirm:
#         conn = connect_db()
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
#         conn.commit()
#         conn.close()
#         fetch_data()  # Refresh data
#         messagebox.showinfo("Success", "Data Deleted Successfully!")

# # Function to select data from treeview and display in input fields
# def select_record(event):
#     selected_item = tree.focus()
#     if selected_item:
#         values = tree.item(selected_item)["values"]
#         name_entry.delete(0, tk.END)
#         age_entry.delete(0, tk.END)
#         name_entry.insert(0, values[1])  # Insert name
#         age_entry.insert(0, values[2])  # Insert age

# # Creating main Tkinter window
# root = tk.Tk()
# root.title("CRUD Tkinter with MySQL")
# root.geometry("600x400")

# # Labels and Entry Fields
# tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
# name_entry = tk.Entry(root)
# name_entry.grid(row=0, column=1, padx=10, pady=10)

# tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10)
# age_entry = tk.Entry(root)
# age_entry.grid(row=1, column=1, padx=10, pady=10)

# # Buttons for CRUD Operations
# insert_btn = tk.Button(root, text="Insert", command=insert_data)
# insert_btn.grid(row=0, column=2, padx=10, pady=10)

# update_btn = tk.Button(root, text="Update", command=update_data)
# update_btn.grid(row=1, column=2, padx=10, pady=10)

# delete_btn = tk.Button(root, text="Delete", command=delete_data)
# delete_btn.grid(row=2, column=2, padx=10, pady=10)

# # Treeview Table to Display Data
# tree = ttk.Treeview(root, columns=("ID", "Name", "Age"), show="headings")
# tree.heading("ID", text="ID")
# tree.heading("Name", text="Name")
# tree.heading("Age", text="Age")
# tree.bind("<ButtonRelease-1>", select_record)  # Select record on click
# tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# # Fetch data on startup
# fetch_data()

# # Run the Tkinter event loop
# root.mainloop()






# from tkinter import *
# from tkinter import ttk


# def select_record(event):
#     selected_item=tree.focus()
#     if selected_item:
#         values=tree.item(selected_item)["values"]
#         print('Selected Data: ',values)

# window=Tk()

# window.geometry('600x400')

# window.title('Treeview in tkinter')

# tree = ttk.Treeview(window,columns=('Id','Name','Age'),show='headings')

# tree.heading('Id',text='ID')
# tree.heading('Name',text='Name')
# tree.heading('Age',text="Age")

# tree.pack(expand=True,fill='both')

# tree.insert('', 'end', values=(1, 'Alice', 25))  # Added at the end
# tree.insert('', 0, values=(2, 'Bob', 30))        # Added at the start
# tree.insert('', 1, values=(3, 'Charlie', 22))    # Inserted at index 1

# # btn=Button(window,text='Get Selected',command=select_record)
# # btn.pack()

# tree.bind('<ButtonRelease-1>',select_record)

# window.mainloop()



# import tkinter as tk
# from tkinter import ttk, messagebox

# # Function to select record and display in entry fields
# def select_record(event):
#     selected_item = tree.focus() 
#     if selected_item:
#         values = tree.item(selected_item)["values"]
#         if values:  # Avoid errors if selection is empty
#             id_entry.delete(0, tk.END)
#             name_entry.delete(0, tk.END)
#             age_entry.delete(0, tk.END)
            
#             id_entry.insert(0, values[0])  # Insert ID
#             name_entry.insert(0, values[1])  # Insert Name
#             age_entry.insert(0, values[2])  # Insert Age

# # Function to add a new record
# def add_record():
#     id_value = id_entry.get()
#     name_value = name_entry.get()
#     age_value = age_entry.get()

#     if id_value and name_value and age_value:
#         tree.insert('', 'end', values=(id_value, name_value, age_value))
#         clear_entries()
#     else:
#         messagebox.showwarning("Warning", "All fields are required!")

# # Function to update the selected record
# def update_record():
#     selected_item = tree.focus()
#     if selected_item:
#         tree.item(selected_item, values=(id_entry.get(), name_entry.get(), age_entry.get()))
#         clear_entries()
#     else:
#         messagebox.showerror("Error", "No record selected to update!")

# # Function to delete the selected record
# def delete_record():
#     selected_item = tree.focus()
#     if selected_item:
#         tree.delete(selected_item)
#         clear_entries()
#     else:
#         messagebox.showerror("Error", "No record selected to delete!")

# # Function to clear entry fields
# def clear_entries():
#     id_entry.delete(0, tk.END)
#     name_entry.delete(0, tk.END)
#     age_entry.delete(0, tk.END)

# # Creating main Tkinter window
# root = tk.Tk()
# root.title("Treeview CRUD Example")
# root.geometry("600x400")

# # Labels and Entry Fields
# tk.Label(root, text="ID:").pack()
# id_entry = tk.Entry(root)
# id_entry.pack()

# tk.Label(root, text="Name:").pack()
# name_entry = tk.Entry(root)
# name_entry.pack()

# tk.Label(root, text="Age:").pack()
# age_entry = tk.Entry(root)
# age_entry.pack()

# # Create Buttons for CRUD operations
# btn_frame = tk.Frame(root)
# btn_frame.pack(pady=10)

# add_btn = tk.Button(btn_frame, text="Add", command=add_record, width=10)
# add_btn.grid(row=0, column=0, padx=5)

# update_btn = tk.Button(btn_frame, text="Update", command=update_record, width=10)
# update_btn.grid(row=0, column=1, padx=5)

# delete_btn = tk.Button(btn_frame, text="Delete", command=delete_record, width=10)
# delete_btn.grid(row=0, column=2, padx=5)

# clear_btn = tk.Button(btn_frame, text="Clear", command=clear_entries, width=10)
# clear_btn.grid(row=0, column=3, padx=5)

# # Create Treeview
# tree = ttk.Treeview(root, columns=("ID", "Name", "Age"), show="headings")
# tree.heading("ID", text="ID")
# tree.heading("Name", text="Name")
# tree.heading("Age", text="Age")

# # Bind Treeview Click Event to `select_record`
# tree.bind("<ButtonRelease-1>", select_record)

# # Display Treeview
# tree.pack(expand=True, fill="both")

# root.mainloop()


# from tkinter import *
# from tkinter import ttk,messagebox

# # function to insert record in the tree table
# def insert_Record():
#     id=idInput.get()
#     name=nameInput.get()
#     age=ageInput.get()
#     if id and name and age:
#         treeviewTable.insert('','end',values=(id,name,age))
#         clear_Record()
#     else:
#         messagebox.showwarning('Error','All fields are required!')

# # function to clear input fields        
# def clear_Record():
#     idInput.delete(0,END)
#     nameInput.delete(0,END)
#     ageInput.delete(0,END)

# def delete_Record():
#     selected_record=treeviewTable.focus()
#     if selected_record:
#         treeviewTable.delete(selected_record)
#         clear_Record()
#     else:
#         messagebox.showerror('Error','No record selected to delete')

# # function to update records 
# def update_Record():
#     selected_record=treeviewTable.focus()
#     if selected_record:
#         treeviewTable.item(selected_record,values=(idInput.get(),nameInput.get(),ageInput.get()))
#         clear_Record()
#     else:
#         messagebox.showerror('Error','No records selected to update')

# def select_record(event):
#     select_record=treeviewTable.focus()
#     if select_record:
#         record_values=treeviewTable.item(select_record)["values"]
#         if record_values:
#             # removing existing values from form fields if exists 
#             idInput.delete(0,END)
#             nameInput.delete(0,END)
#             ageInput.delete(0,END)

#             # displaying selected record values from table to form fields
#             idInput.insert(0,record_values[0])
#             nameInput.insert(0,record_values[1])
#             ageInput.insert(0,record_values[2])


# window=Tk()

# window.title('Crud Operation in tkinter')
# window.geometry('600x400')

# # making form 
# # for id 
# idLabel = Label(window,text='ID')
# idLabel.pack()
# idInput=Entry(window)
# idInput.pack()

# # for name 
# nameLabel=Label(window,text='Name')
# nameLabel.pack()
# nameInput=Entry(window)
# nameInput.pack()

# # for age 
# ageLabel=Label(window,text='Age')
# ageLabel.pack()
# ageInput=Entry(window)
# ageInput.pack()


# # creating frame for adjusting buttons in a line
# btn_frame=Frame(window)
# btn_frame.pack(pady=10)

# # creating buttons under frame 
# addButton = Button(btn_frame,text="Add",command=insert_Record)
# addButton.grid(row=0,column=0,padx=5)

# updateButton = Button(btn_frame,text="Update",command=update_Record)
# updateButton.grid(row=0,column=1,padx=5)

# deleteButton = Button(btn_frame,text="Delete",command=delete_Record)
# deleteButton.grid(row=0,column=2,padx=5)

# clearButton = Button(btn_frame,text="Clear",command=clear_Record)
# clearButton.grid(row=0,column=3,padx=5)

# # creating treeview table 
# treeviewTable = ttk.Treeview(window,columns=('ID',"Name","Age"),show='headings')
# treeviewTable.pack(pady=10)

# # settings headings for table 
# treeviewTable.heading("ID",text='ID')
# treeviewTable.heading('Name',text='Name')
# treeviewTable.heading('Age',text='Age')

# # event to polulate fields info in the form 
# treeviewTable.bind('<ButtonRelease-1>',select_record)

# window.mainloop()




# from tkinter import *
# from tkinter import ttk, messagebox
# import mysql.connector

# def highlight_Records(search_value):
#     # clear any previous selection 
#     treeviewTable.selection_remove(treeviewTable.selection())
#     for item in treeviewTable.get_children():
#         record_values=treeviewTable.item(item,'values')

#         if search_value and (search_value==str(record_values[0]) or search_value.lower() in record_values[1].lower()):
#             treeviewTable.selection_set(item)
#             treeviewTable.focus(item)
#             break
# # search record function 
# def search(search_value):
#     # if(search_value.strip()==''):
#     #     for item in treeviewTable.get_children():
#     #         treeviewTable.delete(item)
#     #         return 
#     highlight_Records(search_value)  # Highlight the record
#     for item in treeviewTable.get_children():
#         treeviewTable.delete(item)
    
#     conn,cursor=connect_db()
#     if search_value.strip()=='':
#         query='select * from users'
#         cursor.execute(query)
#     else:
#         query='select * from users where id = %s or name like %s'
#         cursor.execute(query,(search_value,'%'+search_value+'%'))

#     records=cursor.fetchall()

#     for row in records:
#         treeviewTable.insert("",'end',values=row)
#     # cursor.close()
#     conn.close()


# # making database connection 
# def connect_db():
#     conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="mydatabase"
# )
#     cursor = conn.cursor()
#     return conn,cursor

# #displaying existing records in the treeview table
# def display_records():
#     conn,cursor=connect_db()
#     cursor.execute('select * from users')
#     rows=cursor.fetchall()
#     conn.close()
#     treeviewTable.delete(*treeviewTable.get_children())
#     for row in rows:
#         treeviewTable.insert('',END,values=row)

# # Function to insert record in the tree table
# def insert_Record():
#     id = idInput.get()
#     name = nameInput.get()
#     age = ageInput.get()
    
#     # Check if ID already exists
#     for child in treeviewTable.get_children():
#         if treeviewTable.item(child, "values")[0] == id:
#             messagebox.showwarning("Error", "ID already exists!")
#             return  # Stop further execution
    
#     if id and name and age:
#         conn,cursor=connect_db()
#         cursor.execute('insert into users (name,age) values(%s,%s)',(name,age))
#         conn.commit()
#         conn.close()
#         treeviewTable.insert('', 'end', values=(id, name, age))
#         display_records()
#         clear_Record()
#     else:
#         messagebox.showwarning('Error', 'All fields are required!')

# # Function to clear input fields        
# def clear_Record():
#     idInput.delete(0, END)
#     nameInput.delete(0, END)
#     ageInput.delete(0, END)

# # Function to delete a record
# def delete_Record():
#     selected_record = treeviewTable.focus()
#     if selected_record:
#         conn,cursor=connect_db()
#         values=treeviewTable.item(selected_record)['values']
#         if values:
#             cursor.execute('delete from users where id=%s',(values[0],))
#             conn.commit()
#             treeviewTable.delete(selected_record)
#             display_records()
#             clear_Record()
#     else:
#         messagebox.showerror('Error', 'No record selected to delete')

# # Function to update records 
# def update_Record():
#     selected_record = treeviewTable.focus()
#     if selected_record:
#         values = treeviewTable.item(selected_record)["values"]
#         if values:
#             conn,cursor=connect_db()
#             cursor.execute("UPDATE users SET name=%s, age=%s WHERE id=%s",(nameInput.get(), ageInput.get(), values[0]))
#             conn.commit()
#             display_records()
#             clear_Record()
#     else:
#         messagebox.showerror("Error", "No record selected to update")
#     # selected_record = treeviewTable.focus()
#     # if not selected_record:
#     #     messagebox.showerror('Error', 'No record selected to update')
#     #     return
    
#     # id = idInput.get()
#     # name = nameInput.get()
#     # age = ageInput.get()
    

#     # if id and name and age:
#     #     conn,cursor=connect_db()
#     #     cursor.execute('update users set name=%s, age=%s where id=%s',(name,age,id))
#     #     conn.commit()
#     #     display_records()
#     #     treeviewTable.item(selected_record, values=(id, name, age))
#     #     clear_Record()
#     # else:
#     #     messagebox.showerror("Error", "All fields must be filled to update!")

# # Function to select a record from treeview and populate form fields
# def select_record(event):
#     selected_item = treeviewTable.focus()
#     if not selected_item:
#         return  # If nothing is selected, do nothing

#     record_values = treeviewTable.item(selected_item)["values"]
#     if record_values:
#         idInput.delete(0, END)
#         nameInput.delete(0, END)
#         ageInput.delete(0, END)

#         idInput.insert(0, record_values[0])
#         nameInput.insert(0, record_values[1])
#         ageInput.insert(0, record_values[2])

# # Creating the main window
# window = Tk()
# window.title('CRUD Operation in Tkinter')
# window.geometry('600x400')

# # creating frame for search option 

# topFrame = Frame(window,width=400)
# topFrame.pack()

# # creating label and field to search 
# searchInputLabel=Label(topFrame,text="Enter value to search")
# searchInputLabel.grid(row=0,column=0)
# searchValue = Entry(topFrame)
# searchValue.grid(row=1,column=0)

# # creating button to search by id 
# searchBtn = Button(topFrame,text="Search",command=lambda:search(searchValue.get()))

# searchBtn.grid(row=2,column=0)

# # Creating form fields
# Label(window, text='ID').pack()
# idInput = Entry(window)
# idInput.pack()

# Label(window, text='Name').pack()
# nameInput = Entry(window)
# nameInput.pack()

# Label(window, text='Age').pack()
# ageInput = Entry(window)
# ageInput.pack()

# # Creating frame for buttons
# btn_frame = Frame(window)
# btn_frame.pack(pady=10)

# # Creating buttons
# addButton = Button(btn_frame, text="Add", command=insert_Record)
# addButton.grid(row=0, column=0, padx=5)

# updateButton = Button(btn_frame, text="Update", command=update_Record)
# updateButton.grid(row=0, column=1, padx=5)

# deleteButton = Button(btn_frame, text="Delete", command=delete_Record)
# deleteButton.grid(row=0, column=2, padx=5)

# clearButton = Button(btn_frame, text="Clear", command=clear_Record)
# clearButton.grid(row=0, column=3, padx=5)

# # Creating Treeview Table
# treeviewTable = ttk.Treeview(window, columns=('ID', 'Name', 'Age'), show='headings')
# treeviewTable.pack(pady=10)

# # Setting headings for table
# treeviewTable.heading("ID", text='ID')
# treeviewTable.heading("Name", text='Name')
# treeviewTable.heading("Age", text='Age')

# # Event to populate fields info in the form 
# treeviewTable.bind('<ButtonRelease-1>', select_record)

# display_records()

# window.mainloop()





from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

# Function to insert record
def insert_Record():
    id = idInput.get()
    name = nameInput.get()
    age = ageInput.get()

    if id and name and age:
        # Insert into MySQL database
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, name, age) VALUES (%s, %s, %s)", (id, name, age))
        conn.commit()
        cursor.close()
        conn.close()

        # Insert into TreeView
        treeviewTable.insert("", "end", values=(id, name, age))
        clear_Record()
    else:
        messagebox.showwarning("Error", "All fields are required!")

# Function to clear input fields
def clear_Record():
    idInput.delete(0, END)
    nameInput.delete(0, END)
    ageInput.delete(0, END)

# Function to delete record
def delete_Record():
    selected_record = treeviewTable.focus()
    if selected_record:
        values = treeviewTable.item(selected_record, "values")
        if values:
            # Delete from MySQL database
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (values[0],))
            conn.commit()
            cursor.close()
            conn.close()

            # Delete from TreeView
            treeviewTable.delete(selected_record)
            clear_Record()
    else:
        messagebox.showerror("Error", "No record selected to delete")

# Function to update record
def update_Record():
    selected_record = treeviewTable.focus()
    if selected_record:
        values = treeviewTable.item(selected_record, "values")
        if values:
            new_id = idInput.get()
            new_name = nameInput.get()
            new_age = ageInput.get()

            if new_id and new_name and new_age:
                # Update in MySQL database
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET name=%s, age=%s WHERE id=%s", (new_name, new_age, new_id))
                conn.commit()
                cursor.close()
                conn.close()

                # Update in TreeView
                treeviewTable.item(selected_record, values=(new_id, new_name, new_age))
                clear_Record()
            else:
                messagebox.showwarning("Error", "All fields are required!")
    else:
        messagebox.showerror("Error", "No record selected to update")

# Function to select a record from the TreeView
def select_record(event):
    selected_record = treeviewTable.focus()
    if selected_record:
        record_values = treeviewTable.item(selected_record)["values"]
        if record_values:
            # Clear previous entries
            clear_Record()

            # Populate input fields
            idInput.insert(0, record_values[0])
            nameInput.insert(0, record_values[1])
            ageInput.insert(0, record_values[2])

# Function to search records
def search_Record(search_value):
    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
    cursor = conn.cursor()

    if search_value.strip() == "":
        query = "SELECT * FROM users"
        cursor.execute(query)
    else:
        query = "SELECT * FROM users WHERE id = %s OR name LIKE %s"
        cursor.execute(query, (search_value, "%" + search_value + "%"))

    records = cursor.fetchall()

    # Clear TreeView
    for item in treeviewTable.get_children():
        treeviewTable.delete(item)

    # Insert found records into TreeView
    for row in records:
        treeviewTable.insert("", "end", values=row)

    cursor.close()
    conn.close()

    # Highlight record
    highlight_Record(search_value)

# Function to highlight a searched record
def highlight_Record(search_value):
    treeviewTable.selection_remove(treeviewTable.selection())  # Clear previous selection

    for item in treeviewTable.get_children():
        record_values = treeviewTable.item(item, "values")

        if search_value and (search_value == str(record_values[0]) or search_value.lower() in record_values[1].lower()):
            treeviewTable.selection_set(item)
            treeviewTable.focus(item)
            break  # Stop after first match

# GUI Setup
window = Tk()
window.title("Tkinter CRUD with MySQL")
window.geometry("600x500")

# Form Inputs
idLabel = Label(window, text="ID")
idLabel.pack()
idInput = Entry(window)
idInput.pack()

nameLabel = Label(window, text="Name")
nameLabel.pack()
nameInput = Entry(window)
nameInput.pack()

ageLabel = Label(window, text="Age")
ageLabel.pack()
ageInput = Entry(window)
ageInput.pack()

# Buttons
btn_frame = Frame(window)
btn_frame.pack(pady=10)

addButton = Button(btn_frame, text="Add", command=insert_Record)
addButton.grid(row=0, column=0, padx=5)

updateButton = Button(btn_frame, text="Update", command=update_Record)
updateButton.grid(row=0, column=1, padx=5)

deleteButton = Button(btn_frame, text="Delete", command=delete_Record)
deleteButton.grid(row=0, column=2, padx=5)

clearButton = Button(btn_frame, text="Clear", command=clear_Record)
clearButton.grid(row=0, column=3, padx=5)

# Search Bar
search_label = Label(window, text="Search (ID/Name):")
search_label.pack()
search_input = Entry(window)
search_input.pack()
search_input.bind("<KeyRelease>", lambda event: search_Record(search_input.get()))

search_button = Button(window, text="Search", command=lambda: search_Record(search_input.get()))
search_button.pack()

# TreeView Table
treeviewTable = ttk.Treeview(window, columns=("ID", "Name", "Age"), show="headings")
treeviewTable.pack(pady=10)

treeviewTable.heading("ID", text="ID")
treeviewTable.heading("Name", text="Name")
treeviewTable.heading("Age", text="Age")

# Populate Table with Data
search_Record("")

# Bind Click Event to Select Record
treeviewTable.bind("<ButtonRelease-1>", select_record)

window.mainloop()
