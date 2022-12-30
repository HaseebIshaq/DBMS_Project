from tkinter import *
import tkinter as tk
from tkinter import ttk
from treedisplay_adv import *
import oracledb
# import cx_Oracle as cx
# from cx_Oracle import *
import os

dsn = "project_high"
username = "admin"
password = "b7_!uuDQYW#mF9Z"
wallet_dir = "C:/Users/FIRE FLY LAPTOP'S/OneDrive - Higher Education Commission/Desktop/AI 201/wallet"
wallet_pass = "b7_!uuDQYW#mF9Z"


def advanced_view():

    root_3 = tk.Tk()
    root_3.title("EZ-Rentals DataBase")
    root_3.resizable(False, False)
    root_3.iconphoto(False, tk.PhotoImage(file='clogo.png'))
    root_3.configure(bg='white')
    root_3.attributes('-alpha', 0.85)
    common_var = IntVar(root_3)

    def mega_queries(option):
        connectstring = os.getenv('con_connect')
        connection = oracledb.connect(user=username, password=password, dsn=dsn,
                                      config_dir=wallet_dir, wallet_location=wallet_dir, wallet_password=wallet_pass)
        # connection = cx.connect(user='sys', password="admin123", mode=cx.SYSDBA)
        cursor = connection.cursor()
        if (option == 1):
            q1 = ("select * from customers where st_name = 'S1'")
            cursor.execute(q1)
            data = cursor.fetchall()
            print(data)
            connection.commit()
            cursor.close()
            connection.close()
        if (option == 2):
            q1 = ("select * from customers where st_name = 'S2'")
            cursor.execute(q1)
            data = cursor.fetchall()
            print(data)
            connection.commit()
            cursor.close()
            connection.close()
        if (option == 3):
            q1 = ("select * from customers where st_name = 'S3'")
            cursor.execute(q1)
            data = cursor.fetchall()
            print(data)
            connection.commit()
            cursor.close()
            connection.close()
        if (option == 4):
            q1 = ("select * from customers where st_name = 'S4'")
            cursor.execute(q1)
            data = cursor.fetchall()
            print(data)
            connection.commit()
            cursor.close()
            connection.close()
        if (option == 5):
            q1 = ("select * from customers where v = 'BI-CYCLE'")
            cursor.execute(q1)
            data = cursor.fetchall()
            print(data)
            connection.commit()
            cursor.close()
            connection.close()
        if (option == 6):
            q1 = ("select * from customers where v = 'E-BIKE'")
            cursor.execute(q1)
            data = cursor.fetchall()
            print(data)
            connection.commit()
            cursor.close()
            connection.close()
        if (option == 7):
            q1 = ("select * from customers where v = 'GEAR BIKE'")
            cursor.execute(q1)
            data = cursor.fetchall()
            print(data)
            connection.commit()
            cursor.close()
            connection.close()
        if (option == 8):
            q1 = ("select * from customers where v = 'SPORTS BIKE'")
            cursor.execute(q1)
            data = cursor.fetchall()
            print(data)
            connection.commit()
            cursor.close()
            connection.close()
        if (option == 9):
            q1 = ("select reg,count(v) from customers group by reg")
            cursor.execute(q1)
            data = cursor.fetchall()
            print(data)
            connection.commit()
            cursor.close()
            connection.close()

        def tree_window(record):
            root_3.destroy()
            # tableview(record)

    Label(root_3, text='Stations', font='Roboto 15', padx=10,
          fg='purple', bg='white').place(x=360, y=10)
    Radiobutton(root_3, text="Customers from Station 1", variable=common_var,
                value=1, font='Roboto 12', padx=10, fg='blue', bg='white').place(x=120, y=70)
    Radiobutton(root_3, text="Customers from Station 2", variable=common_var,
                value=2, font='Roboto 12', padx=10, fg='blue', bg='white').place(x=470, y=70)
    Radiobutton(root_3, text="Customers from Station 3", variable=common_var,
                value=3, font='Roboto 12', padx=10, fg='blue', bg='white').place(x=120, y=130)
    Radiobutton(root_3, text="Customers from Station 4", variable=common_var,
                value=4, font='Roboto 12', padx=10, fg='blue', bg='white').place(x=470, y=130)
    Label(root_3, text='Vehicles', font='Roboto 15', padx=10,
          fg='purple', bg='white').place(x=360, y=240)
    Radiobutton(root_3, text="Customers that took BI-CYCLE", variable=common_var,
                value=5, font='Roboto 12', padx=10, fg='blue', bg='white').place(x=120, y=300)
    Radiobutton(root_3, text="Customers that took E-BIKE", variable=common_var,
                value=6, font='Roboto 12', padx=10, fg='blue', bg='white').place(x=470, y=300)
    Radiobutton(root_3, text="Customers that took GEAR BIKE", variable=common_var,
                value=7, font='Roboto 12', padx=10, fg='blue', bg='white').place(x=120, y=360)
    Radiobutton(root_3, text="Customers that took SPORTS BIKE", variable=common_var,
                value=8, font='Roboto 12', padx=10, fg='blue', bg='white').place(x=470, y=360)
    Radiobutton(root_3, text="SUMMARY of ALL the records w.r.t. each station and vehicle",
                variable=common_var, value=9, font='Roboto 12', padx=10, fg='blue', bg='white').place(x=280, y=400)

    execute_button = Button(root_3, text='Execute & Close', borderwidth=3, font='Ariel 12 bold',
                            command=lambda: mega_queries(common_var), fg='blue', bg='white')
    execute_button.place(x=650, y=560)
    root_3.geometry('800x600')  # lengthxwidth
    root_3.mainloop()


# advanced_view()
