                          # PROJECT 5: PASSWORD VALIDATOR


from tkinter import *
import bcrypt
import tkinter.messagebox

def validate(password):
    hashed_password=b'$2b$12$zJXchiAXtKdBXZH9zYBYH.mUOQM.htcm/0HdJ0TnWaqokfcUkGJwm'
    password=bytes(password,encoding='utf=8')
    if bcrypt.checkpw(password,hashed_password):
        tkinter.messagebox.showinfo('Validation', "Login Successful")
    else:
        tkinter.messagebox.showinfo('Validation', "Wrong password")

root=Tk()
root.geometry('400x300')
root.title('Password validator')

label=Label(root,text='Enter your password:',font=('Algerian',15))
label.grid(row=0,column=0)

password_entry=Entry(root)
password_entry.grid(row=0,column=1)

button=Button(root,text='Validate',padx=4,pady=4,command=lambda:validate(password_entry.get()))
button.grid(row=2,column=1)

root.mainloop()