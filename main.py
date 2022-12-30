from tkinter import *
import tkinter as tk
from input import *

#Window 2 function
############################################################################################################
def new_window():
    root.destroy()
    input_screen()
############################################################################################################


########Initial Screen
root = tk.Tk()
root.title("EZ-Rentals DataBase")
root.resizable(False,False)
root.iconphoto(False,tk.PhotoImage(file='EZRentals.png'))
background_image = tk.PhotoImage(file='EZRentals.png')
Label(root,image=background_image).place(x=180,y=100)
root.attributes('-alpha',0.85)

submit_button = Button(root,text='Enter',borderwidth=3,font='Ariel 18 italic bold',command=new_window,fg='blue',bg='white').place(rely=0.9, relx=0.55, x=0, y=0,anchor=SE)

root.geometry('800x600') #lengthxwidth
root.mainloop()


