from tkinter import *
import tkinter as tk
from advanced import *
import oracledb
import os

dsn = "project_high"
username = "admin"
password = "b7_!uuDQYW#mF9Z"
wallet_dir = "C:/Users/FIRE FLY LAPTOP'S/OneDrive - Higher Education Commission/Desktop/AI 201/wallet"
wallet_pass = "b7_!uuDQYW#mF9Z"


def input_screen():

    root_2 = tk.Tk()

    def ADVANCED():  # calling final screen
        root_2.destroy()
        advanced_view()

    # oracle connect function
    ##################################################
    def oracle_search():  # sql search query
        connectstring = os.getenv('con_connect')
        connection = oracledb.connect(user=username, password=password, dsn=dsn,
                                      config_dir=wallet_dir, wallet_location=wallet_dir, wallet_password=wallet_pass)
        cursor = connection.cursor()
        search_query = "select * from customers where reg = (:2)"
        cursor.execute(search_query, e2.get())
        d = cursor.fetchall()
        print (d)
        connection.commit()
        cursor.close()
        connection.close()

    def oracle_add():  # sql cursor to add customers data
        connectstring = os.getenv('con_connect')
        connection = oracledb.connect(user=username, password=password, dsn=dsn,
                                      config_dir=wallet_dir, wallet_location=wallet_dir, wallet_password=wallet_pass)
        cursor = connection.cursor()
        add_query = "insert into customers (c_name,reg,st_name,v) values (:1,:2,:3,:4)"
        cursor.execute(add_query, (e1.get(), e2.get(),
                       stations.get(), vehicle.get()))
        # cursor.execute(add_query1,vehicle.get())
        connection.commit()
        cursor.close()
        connection.close()

    def oracle_disp():  # displaying data
        connectstring = os.getenv('con_connect')
        connection = oracledb.connect(user=username, password=password, dsn=dsn,
                                      config_dir=wallet_dir, wallet_location=wallet_dir, wallet_password=wallet_pass)
        cursor = connection.cursor()
        add_query = "select *from stations"
        cursor.execute(add_query)
        # cursor.execute(add_query1,vehicle.get())
        data = cursor.fetchall()
        print(data)
        # connection.commit()
        cursor.close()
        connection.close()

    e1 = StringVar(root_2)
    e2 = StringVar(root_2)
    stations = StringVar(root_2)
    stations.set(0)
    vehicle = StringVar(root_2)
    vehicle.set(0)

    root_2.title("Ez Rental Database")
    root_2.resizable(False, False)
    root_2.iconphoto(False, tk.PhotoImage(file='EZrentals.png'))
    root_2.configure(bg='white')
    root_2.attributes('-alpha', 0.85)

    Label(root_2, text='Name', font='Roboto 15', padx=10,
          fg='blue', bg='white').place(x=190, y=100)
    first_name_input = Entry(root_2, textvariable=e1, width=20, font="Sans",
                             borderwidth=6, bg="white", fg='blue').place(x=320, y=100)
    Label(root_2, text='Reg Number', font='Roboto 15',
          padx=10, fg='blue', bg='white').place(x=190, y=200)
    last_name_input = Entry(root_2, textvariable=e2, width=20, font="Sans",
                            borderwidth=6, bg="white", fg='blue').place(x=320, y=200)
    Label(root_2, text='Stations', font='Roboto 15',
          padx=10, fg='blue', bg='white').place(x=190, y=300)
    Radiobutton(root_2, text="S1", variable=stations, value='S1',
                font='Roboto 12', padx=10, fg='blue', bg='white').place(x=320, y=300)
    Radiobutton(root_2, text="S2", variable=stations, value='S2',
                font='Roboto 12', padx=10, fg='blue', bg='white').place(x=420, y=300)
    Radiobutton(root_2, text="S3", variable=stations, value='S3',
                font='Roboto 12', padx=10, fg='blue', bg='white').place(x=520, y=300)
    Radiobutton(root_2, text="S4", variable=stations, value='S4',
                font='Roboto 12', padx=10, fg='blue', bg='white').place(x=620, y=300)
    Label(root_2, text='Vehicle', font='Roboto 15', padx=10,
          fg='blue', bg='white').place(x=190, y=370)
    Radiobutton(root_2, text="BI-CYCLE", variable=vehicle, value='BI-CYCLE',
                font='Roboto 12', padx=10, fg='blue', bg='white').place(x=320, y=370)
    Radiobutton(root_2, text="E-BIKE", variable=vehicle, value='E-BIKE',
                font='Roboto 12', padx=10, fg='blue', bg='white').place(x=485, y=370)
    Radiobutton(root_2, text="GEAR BIKE", variable=vehicle, value='GEAR BIKE',
                font='Roboto 12', padx=10, fg='blue', bg='white').place(x=600, y=370)
    Radiobutton(root_2, text="SPORTS BIKE", variable=vehicle, value='SPORTS BIKE',
                font='Roboto 12', padx=10, fg='blue', bg='white').place(x=320, y=400)

    submit_button1 = Button(root_2, text="Search", borderwidth=3, font='Ariel 12 bold',
                            fg='blue', bg='white', command=oracle_search).place(x=470, y=500)
    add_button = Button(root_2, text="Register", borderwidth=3, font='Ariel 12 bold',
                        fg='blue', bg='white', command=oracle_add).place(x=350, y=500)
    catalogue = Button(root_2, text="Catalogue", borderwidth=3, font='Ariel 12 bold',
                       fg='blue', bg='white', command=oracle_disp).place(x=230, y=500)
    Advanced_options = Button(root_2, text="More options", borderwidth=3,
                              font='Ariel 12 bold', fg='blue', bg='white', command=ADVANCED).place(x=640, y=559)
    root_2.geometry('800x600')  # lengthxwidth
    root_2.mainloop()
