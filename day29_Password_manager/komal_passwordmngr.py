from tkinter import *
from tkinter import messagebox
#from tkinter import Canvas
from random import choice, randint, shuffle
import pyperclip
# Pyperclip is a cross-platform Python module for copy and 
# paste clipboard functions. It works with Python 2 and 3. 
# Install on Windows: pip install pyperclip

def password_generator():    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pwdList =[]
    pwdList += [choice(letters) for _ in range(randint(8,10))]
    pwdList += [choice(numbers) for _ in range(randint(2,4))]
    pwdList += [choice(symbols) for _ in range(randint(2,4))]
    print(pwdList)
    shuffle(pwdList)
    password = "".join(pwdList)
    print(password)
    #password_entry.insert(END, text=password)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    #pyperclip.paste() #paste the last copied

def save():
    websitename = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(websitename) ==0 or len(email) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        is_OK = messagebox.askokcancel(title=websitename, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_OK:
            with open("datainfo.txt","a") as file1:
                file1.write(f"{websitename} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



#UI Setup
window = Tk()
window.title("This is a Passord Manager Program")
window.config(padx=25, pady=25)
#spacing around the inside part of window

canvas = Canvas(width=250, height=250)
logoimg = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logoimg)
canvas.grid (column=0, row=0, columnspan=2)


#Labels:
website_Label = Label(text="Website: ")
website_Label.grid(column=0, row=1)
email_Label = Label(text="Email: ")
email_Label.grid(column=0, row=2)
password_Label = Label(text="Password: ")
password_Label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry= Entry(width=35)
email_entry.insert(0,"komal@sample.com")
email_entry.grid(column=1, row=2)
password_entry= Entry(width=35)
password_entry.grid(column=1, row=3)

#Button
generate_btn = Button( text="Generate Password", command=password_generator)
#, sticky="w" to make left alignment
generate_btn.grid(column=1, row=4 , sticky="w")
add_btn= Button(text="Add/Save", command=save)
#, sticky="e" to make right alignment
add_btn.grid(column=1, row=4,columnspan=2, sticky="e")
window.mainloop()

#NW , N , NE, W, CENTER, E , SW, S, SE