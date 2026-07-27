import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accept":
        #user info
        firstname = first_name_entry.get() #revisi _lebel menjadi _entry
        lastname = last_name_entry.get() #revisi _lebel menjadi _entry

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print("first name: ", firstname, "last name: ", lastname)
            print("Title: ", title, "age: ", age, "nationality: ", nationality)
            print("# Course: ", numcourses, "# Semesters: ", numsemesters)
            print("registration status: ", registration_status)
            print("--------------------------------------------")

            #create Table
            conn = sqlite3.connect('data1.db')
            table_create_query = '''CERATE TABLE IF NOT EXISTS Student_Data
                    (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT,
                    registration_status TEXT, num_courses INT, num_semesters INT)'''
            conn.execute(table_create_query)

            #insert data
            data_insert_query = '''INSERT INTO Student_Data (firstname, lastname, title, age, nationality,
            registration_status, num_courses, num_semseters) VALUES (?,?,?,?,?,?,?,?)'''
            data_insert_tuple = (firstname, lastname, title, age, nationality, registration_status, numcourses, numsemesters)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()
        else:
            tkinter.messagebox.showwarning(title= "Error",
            message="first name and last name are required")
    else:
        tkinter.messagebox.showwarning(title= "Error",
        message="you have not accepted terms and conditions")

window = tkinter.Tk()
window.title("data entry form")
frame = tkinter.Frame(window)
frame.pack()

# saving user input
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=10, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame) #revisi label menjadi entry
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Apa", "Mr", "Ms", "Dr", "Prof"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=8, to=50)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antartika", "Asia", "Europe", "North America", "Oceaania", "South Amercia"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# saving course info
course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10) 
registered_label = tkinter.Label(course_frame, text="Registration status")
reg_status_var = tkinter.StringVar(value="NOT Registered")
registered_check = tkinter.Checkbutton(course_frame, text="Curently Register",
variable=reg_status_var, onvalue="Registered", offvalue="NOT Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(course_frame, text= "# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(course_frame, from_=0, to= 50)
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(course_frame, text= "# Semester")
numsemesters_spinbox = tkinter.Spinbox(course_frame, from_=0, to= '20')
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=5, pady=10)

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accept")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accept", offvalue="Not Accept")
terms_check.grid(row=0, column=0)

#button Accept
button = tkinter.Button(frame, text="Enter Data", command=enter_data) #command="enter_data"
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


window.mainloop()

