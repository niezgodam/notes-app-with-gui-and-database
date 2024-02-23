import mysql.connector
import getpass
import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sys
import subprocess

###USING IN ENV
import os
from dotenv import load_dotenv
load_dotenv()
###


mydb = mysql.connector.connect(
    host = os.getenv('HOST'),
    user = os.getenv('USER'),
    password = os.getenv('PASSWORD'),
)

name_of_schema = os.getenv("SCHEMA")
background_path = os.getenv("BACKGROUNDPATH")
notes_picture_path = os.getenv("NOTESPATH")
cur = mydb.cursor()

    
def loadingDB():
    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'SELECT COUNT(notes_id) FROM monday')
    for i in cur:
        count = i[0]
    monday_listbox.delete(0,count)
    cur.execute(f'SELECT * FROM monday')
    for i in cur:
        monday_listbox.insert(i[0],i[1])



    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'SELECT COUNT(notes_id) FROM tuesday')
    for i in cur:
        count = i[0]
    tuesday_listbox.delete(0,count)
    cur.execute(f'SELECT * FROM tuesday')
    for i in cur:
        tuesday_listbox.insert(i[0],i[1])


    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'SELECT COUNT(notes_id) FROM wednesday')
    for i in cur:
        count = i[0]
    wednesday_listbox.delete(0,count)
    cur.execute(f'SELECT * FROM wednesday')
    for i in cur:
        wednesday_listbox.insert(i[0],i[1])

    
    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'SELECT COUNT(notes_id) FROM thursday')
    for i in cur:
        count = i[0]
    thursday_listbox.delete(0,count)
    cur.execute(f'SELECT * FROM thursday')
    for i in cur:
        thursday_listbox.insert(i[0],i[1])



    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'SELECT COUNT(notes_id) FROM friday')
    for i in cur:
        count = i[0]
    friday_listbox.delete(0,count)
    cur.execute(f'SELECT * FROM friday')
    for i in cur:
        friday_listbox.insert(i[0],i[1])


    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'SELECT COUNT(notes_id) FROM saturday')
    for i in cur:
        count = i[0]
    saturday_listbox.delete(0,count)
    cur.execute(f'SELECT * FROM saturday')
    for i in cur:
        saturday_listbox.insert(i[0],i[1])


    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'SELECT COUNT(notes_id) FROM sunday')
    for i in cur:
        count = i[0]
    sunday_listbox.delete(0,count)
    cur.execute(f'SELECT * FROM sunday')
    for i in cur:
        sunday_listbox.insert(i[0],i[1])



def listbox_choose(event):
    if str(event.widget) == ".!listbox":
        return "monday"
    elif str(event.widget) == ".!listbox2":
        return "tuesday"
    elif str(event.widget) == ".!listbox3":
        return "wednesday"
    elif str(event.widget) == ".!listbox4":
        return "thursday"
    elif str(event.widget) == ".!listbox5":
        return "friday"
    elif str(event.widget) == ".!listbox6":
        return "saturday"
    elif str(event.widget) == ".!listbox7":
        return "sunday"
    
def selected_choose(event):
    day = listbox_choose(event)
    selected = event.widget.curselection()
    new_window = Toplevel()
    new_window.title("NOTES")
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2)-(WINDOW_WIDTH/2))
    y = int((screen_height/2)-(WINDOW_HEIGHT/2))
    new_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'SELECT notes FROM {day} WHERE notes_id = {selected[0]+1}')
    for i in cur:
        textxd = i[0]
    backgroundImagenew = PhotoImage(file=notes_picture_path)
    new_label = Label(new_window,image=backgroundImagenew,width=600,height=600)
    new_label.pack()
    text_label = Label(new_window, text=textxd,background="#abdddb", font=("Ink Free",18),width=38,height=17,wraplength=500)
    text_label.place(relx=0.5, rely=0.52, anchor="center")
    new_window.update()
    new_window.mainloop()



def add_monday_data():
    input_text = text.get("1.0", END)
    cur.execute(f'USE {name_of_schema}')
    cur.execute('SELECT COUNT(notes_id) FROM monday')
    for  i in cur:
        count = i
    cur.execute(f'INSERT monday(notes_id,notes) VALUES({count[0]+1},"{input_text}")')
    mydb.commit()
    loadingDB()
    new_window.destroy()


def add_monday():
    global text
    global new_window
    new_window = Toplevel()
    new_window.title("ADD NOTES")

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2)-(WINDOW_WIDTH/2))
    y = int((screen_height/2)-(WINDOW_HEIGHT/2))
    new_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")


    backgroundImagenew = PhotoImage(file=notes_picture_path)
    new_label = Label(new_window,image=backgroundImagenew,width=600,height=600,compound="top")
    new_label.pack()

    text = Text(new_window, bg="#abdddb", fg="black",font=("Ink Free",18,'bold'),padx=0,pady=0,width=39,height=18)
    text.place(x=7, y=50)

    add_button = Button(new_window,text="ADD",width=15,height=1,command=add_monday_data)
    add_button.place(x=240,y=15)
    new_window.mainloop()





def delete_monday():
    selected = monday_listbox.curselection()

    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'DELETE FROM monday WHERE notes_id = {selected[0]+1}')



    cur.execute(f'SELECT notes_id FROM monday WHERE notes_id >= {selected[0]+2}')
    rows_to_update = cur.fetchall()
    
    for row in rows_to_update:

        cur.execute(f'UPDATE monday SET notes_id = {row[0] - 1} WHERE notes_id = {row[0]}')

    mydb.commit()
    loadingDB()


def add_tuesday_data():
    input_text = text.get("1.0", END)
    cur.execute(f'USE {name_of_schema}')
    cur.execute('SELECT COUNT(notes_id) FROM tuesday')
    for  i in cur:
        count = i
    cur.execute(f'INSERT tuesday(notes_id,notes) VALUES({count[0]+1},"{input_text}")')
    mydb.commit()
    loadingDB()
    new_window.destroy()


def add_tuesday():
    global text
    global new_window
    new_window = Toplevel()
    new_window.title("ADD NOTES")

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2)-(WINDOW_WIDTH/2))
    y = int((screen_height/2)-(WINDOW_HEIGHT/2))
    new_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")


    backgroundImagenew = PhotoImage(file=notes_picture_path)
    new_label = Label(new_window,image=backgroundImagenew,width=600,height=600,compound="top")
    new_label.pack()

    text = Text(new_window, bg="#abdddb", fg="black",font=("Ink Free",18,'bold'),padx=0,pady=0,width=39,height=18)
    text.place(x=7, y=50)

    add_button = Button(new_window,text="ADD",width=15,height=1,command=add_tuesday_data)
    add_button.place(x=240,y=15)
    new_window.mainloop()





def delete_tuesday():
    selected = tuesday_listbox.curselection()

    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'DELETE FROM tuesday WHERE notes_id = {selected[0]+1}')



    cur.execute(f'SELECT notes_id FROM tuesday WHERE notes_id >= {selected[0]+2}')
    rows_to_update = cur.fetchall()
    
    for row in rows_to_update:

        cur.execute(f'UPDATE tuesday SET notes_id = {row[0] - 1} WHERE notes_id = {row[0]}')

    mydb.commit()
    loadingDB()



def add_wednesday_data():
    input_text = text.get("1.0", END)
    cur.execute(f'USE {name_of_schema}')
    cur.execute('SELECT COUNT(notes_id) FROM wednesday')
    for  i in cur:
        count = i
    cur.execute(f'INSERT wednesday(notes_id,notes) VALUES({count[0]+1},"{input_text}")')
    mydb.commit()
    loadingDB()
    new_window.destroy()


def add_wednesday():
    global text
    global new_window
    new_window = Toplevel()
    new_window.title("ADD NOTES")

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2)-(WINDOW_WIDTH/2))
    y = int((screen_height/2)-(WINDOW_HEIGHT/2))
    new_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")


    backgroundImagenew = PhotoImage(file=notes_picture_path)
    new_label = Label(new_window,image=backgroundImagenew,width=600,height=600,compound="top")
    new_label.pack()

    text = Text(new_window, bg="#abdddb", fg="black",font=("Ink Free",18,'bold'),padx=0,pady=0,width=39,height=18)
    text.place(x=7, y=50)

    add_button = Button(new_window,text="ADD",width=15,height=1,command=add_wednesday_data)
    add_button.place(x=240,y=15)
    new_window.mainloop()




def delete_wednesday():
    selected = wednesday_listbox.curselection()

    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'DELETE FROM wednesday WHERE notes_id = {selected[0]+1}')



    cur.execute(f'SELECT notes_id FROM wednesday WHERE notes_id >= {selected[0]+2}')
    rows_to_update = cur.fetchall()
    
    for row in rows_to_update:

        cur.execute(f'UPDATE wednesday SET notes_id = {row[0] - 1} WHERE notes_id = {row[0]}')

    mydb.commit()
    loadingDB()



def add_thursday_data():
    input_text = text.get("1.0", END)
    cur.execute(f'USE {name_of_schema}')
    cur.execute('SELECT COUNT(notes_id) FROM thursday')
    for  i in cur:
        count = i
    cur.execute(f'INSERT thursday(notes_id,notes) VALUES({count[0]+1},"{input_text}")')
    mydb.commit()
    loadingDB()
    new_window.destroy()


def add_thursday():
    global text
    global new_window
    new_window = Toplevel()
    new_window.title("ADD NOTES")

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2)-(WINDOW_WIDTH/2))
    y = int((screen_height/2)-(WINDOW_HEIGHT/2))
    new_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")


    backgroundImagenew = PhotoImage(file=notes_picture_path)
    new_label = Label(new_window,image=backgroundImagenew,width=600,height=600,compound="top")
    new_label.pack()

    text = Text(new_window, bg="#abdddb", fg="black",font=("Ink Free",18,'bold'),padx=0,pady=0,width=39,height=18)
    text.place(x=7, y=50)

    add_button = Button(new_window,text="ADD",width=15,height=1,command=add_thursday_data)
    add_button.place(x=240,y=15)
    new_window.mainloop()





def delete_thursday():
    selected = thursday_listbox.curselection()

    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'DELETE FROM thursday WHERE notes_id = {selected[0]+1}')



    cur.execute(f'SELECT notes_id FROM thursday WHERE notes_id >= {selected[0]+2}')
    rows_to_update = cur.fetchall()
    
    for row in rows_to_update:

        cur.execute(f'UPDATE thursday SET notes_id = {row[0] - 1} WHERE notes_id = {row[0]}')

    mydb.commit()
    loadingDB()


def add_friday_data():
    input_text = text.get("1.0", END)
    cur.execute(f'USE {name_of_schema}')
    cur.execute('SELECT COUNT(notes_id) FROM friday')
    for  i in cur:
        count = i
    cur.execute(f'INSERT friday(notes_id,notes) VALUES({count[0]+1},"{input_text}")')
    mydb.commit()
    loadingDB()
    new_window.destroy()


def add_friday():
    global text
    global new_window
    new_window = Toplevel()
    new_window.title("ADD NOTES")

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2)-(WINDOW_WIDTH/2))
    y = int((screen_height/2)-(WINDOW_HEIGHT/2))
    new_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")


    backgroundImagenew = PhotoImage(file=notes_picture_path)
    new_label = Label(new_window,image=backgroundImagenew,width=600,height=600,compound="top")
    new_label.pack()

    text = Text(new_window, bg="#abdddb", fg="black",font=("Ink Free",18,'bold'),padx=0,pady=0,width=39,height=18)
    text.place(x=7, y=50)

    add_button = Button(new_window,text="ADD",width=15,height=1,command=add_friday_data)
    add_button.place(x=240,y=15)
    new_window.mainloop()





def delete_friday():
    selected = friday_listbox.curselection()

    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'DELETE FROM friday WHERE notes_id = {selected[0]+1}')



    cur.execute(f'SELECT notes_id FROM friday WHERE notes_id >= {selected[0]+2}')
    rows_to_update = cur.fetchall()
    
    for row in rows_to_update:

        cur.execute(f'UPDATE friday SET notes_id = {row[0] - 1} WHERE notes_id = {row[0]}')

    mydb.commit()
    loadingDB()
    


def add_saturday_data():
    input_text = text.get("1.0", END)
    cur.execute(f'USE {name_of_schema}')
    cur.execute('SELECT COUNT(notes_id) FROM saturday')
    for  i in cur:
        count = i
    cur.execute(f'INSERT saturday(notes_id,notes) VALUES({count[0]+1},"{input_text}")')
    mydb.commit()
    loadingDB()
    new_window.destroy()


def add_saturday():
    global text
    global new_window
    new_window = Toplevel()
    new_window.title("ADD NOTES")

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2)-(WINDOW_WIDTH/2))
    y = int((screen_height/2)-(WINDOW_HEIGHT/2))
    new_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")


    backgroundImagenew = PhotoImage(file=notes_picture_path)
    new_label = Label(new_window,image=backgroundImagenew,width=600,height=600,compound="top")
    new_label.pack()

    text = Text(new_window, bg="#abdddb", fg="black",font=("Ink Free",18,'bold'),padx=0,pady=0,width=39,height=18)
    text.place(x=7, y=50)

    add_button = Button(new_window,text="ADD",width=15,height=1,command=add_saturday_data)
    add_button.place(x=240,y=15)
    new_window.mainloop()





def delete_saturday():
    selected = saturday_listbox.curselection()

    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'DELETE FROM saturday WHERE notes_id = {selected[0]+1}')



    cur.execute(f'SELECT notes_id FROM saturday WHERE notes_id >= {selected[0]+2}')
    rows_to_update = cur.fetchall()
    
    for row in rows_to_update:

        cur.execute(f'UPDATE saturday SET notes_id = {row[0] - 1} WHERE notes_id = {row[0]}')

    mydb.commit()
    loadingDB()

def add_sunday_data():
    input_text = text.get("1.0", END)
    cur.execute(f'USE {name_of_schema}')
    cur.execute('SELECT COUNT(notes_id) FROM sunday')
    for  i in cur:
        count = i
    cur.execute(f'INSERT sunday(notes_id,notes) VALUES({count[0]+1},"{input_text}")')
    mydb.commit()
    loadingDB()
    new_window.destroy()


def add_sunday():
    global text
    global new_window
    new_window = Toplevel()
    new_window.title("ADD NOTES")

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2)-(WINDOW_WIDTH/2))
    y = int((screen_height/2)-(WINDOW_HEIGHT/2))
    new_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")


    backgroundImagenew = PhotoImage(file=notes_picture_path)
    new_label = Label(new_window,image=backgroundImagenew,width=600,height=600,compound="top")
    new_label.pack()

    text = Text(new_window, bg="#abdddb", fg="black",font=("Ink Free",18,'bold'),padx=0,pady=0,width=39,height=18)
    text.place(x=7, y=50)

    add_button = Button(new_window,text="ADD",width=15,height=1,command=add_sunday_data)
    add_button.place(x=240,y=15)
    new_window.mainloop()





def delete_sunday():
    selected = sunday_listbox.curselection()

    cur.execute(f'USE {name_of_schema}')
    cur.execute(f'DELETE FROM sunday WHERE notes_id = {selected[0]+1}')



    cur.execute(f'SELECT notes_id FROM sunday WHERE notes_id >= {selected[0]+2}')
    rows_to_update = cur.fetchall()
    
    for row in rows_to_update:

        cur.execute(f'UPDATE sunday SET notes_id = {row[0] - 1} WHERE notes_id = {row[0]}')

    mydb.commit()
    loadingDB()



def refresh():
    python_executable = sys.executable
    script_path = sys.argv[0]
    
    subprocess.Popen([python_executable, script_path])
    sys.exit()




window = Tk()
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 1080
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(WINDOW_WIDTH/2))
y = int((screen_height/2)-(WINDOW_HEIGHT/2))



window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
window.title("NOTESapp")
window.resizable(False,False)

window.bind("<Double-Button-1>",selected_choose)



backgroundImage = PhotoImage(file=background_path)
background_label = Label(window,image=backgroundImage,compound="top").pack()


monday_listbox = Listbox(window,highlightthickness=0,background="#f8f5ef",bd=0,fg="black",font=("Ink Free",17),width=12,height=26)
monday_listbox.place(x=80,y=180)

tuesday_listbox = Listbox(window, highlightthickness=0,background="#f8f5ef",bd=0,fg="black",font=("Ink Free",17),width=13,height=26)
tuesday_listbox.place(x=245,y=180)

wednesday_listbox = Listbox(window, highlightthickness=0,background="#f8f5ef",bd=0,fg="black",font=("Ink Free",17),width=13,height=26)
wednesday_listbox.place(x=425,y=180)

thursday_listbox = Listbox(window,highlightthickness=0, background="#f8f5ef",bd=0,fg="black",font=("Ink Free",17),width=13,height=26)
thursday_listbox.place(x=605,y=180)

friday_listbox = Listbox(window, highlightthickness=0,background="#f8f5ef",bd=0,fg="black",font=("Ink Free",17),width=13,height=26)
friday_listbox.place(x=785,y=180)

saturday_listbox = Listbox(window,highlightthickness=0, background="#f8f5ef",bd=0,fg="black",font=("Ink Free",17),width=13,height=26)
saturday_listbox.place(x=965,y=180)

sunday_listbox = Listbox(window, highlightthickness=0,background="#f8f5ef",bd=0,fg="black",font=("Ink Free",17),width=13,height=26)
sunday_listbox.place(x=1145,y=180)


add_monday_button = Button(window,command=add_monday,text="ADD",font=("Consolas",10),width=10,height=0)
add_monday_button.place(x=80,y=952)

delete_monday_button = Button(window,command=delete_monday,text="DELETE",font=("Consolas",10),width=10,height=0)
delete_monday_button.place(x=160,y=952)



add_tuesday_button = Button(window,command=add_tuesday,text="ADD",font=("Consolas",10),width=12,height=0)
add_tuesday_button.place(x=241,y=952)


delete_tuesday_button = Button(window,command=delete_tuesday,text="DELETE",font=("Consolas",10),width=12,height=0)
delete_tuesday_button.place(x=331,y=952)



add_wednesday_button = Button(window,command=add_wednesday,text="ADD",font=("Consolas",10),width=12,height=0)
add_wednesday_button.place(x=420,y=952)

delete_wednesday_button = Button(window,command=delete_wednesday,text="DELETE",font=("Consolas",10),width=12,height=0)
delete_wednesday_button.place(x=512,y=952)



add_thursday_button = Button(window,command=add_thursday,text="ADD",font=("Consolas",10),width=12,height=0)
add_thursday_button.place(x=600,y=952)

delete_thursday_button = Button(window,command=delete_thursday,text="DELETE",font=("Consolas",10),width=12,height=0)
delete_thursday_button.place(x=693,y=952)



add_friday_button = Button(window,command=add_friday,text="ADD",font=("Consolas",10),width=12,height=0)
add_friday_button.place(x=781,y=952)


delete_friday_button = Button(window,command=delete_friday,text="DELETE",font=("Consolas",10),width=12,height=0)
delete_friday_button.place(x=874,y=952)


add_saturday_button = Button(window,command=add_saturday,text="ADD",font=("Consolas",10),width=12,height=0)
add_saturday_button.place(x=960,y=952)


delete_saturday_button = Button(window,command=delete_saturday,text="DELETE",font=("Consolas",10),width=12,height=0)
delete_saturday_button.place(x=1052,y=952)


add_sunday_button = Button(window,command=add_sunday,text="ADD",font=("Consolas",10),width=12,height=0)
add_sunday_button.place(x=1140,y=952)


delete_sunday_button = Button(window,command=delete_sunday,text="DELETE",font=("Consolas",10),width=11,height=0)
delete_sunday_button.place(x=1234,y=952)


loadingDB()
window.mainloop()
