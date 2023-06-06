from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def handle_login():
    email = email_input.get()  # it will fetch the email inputted by the user
    password = password_input.get()

    if email == 'manish.login@gmail.com' and password == '1234':
        messagebox.showinfo('Login Successful',
                            'You have successfully logged in.')
    else:
        messagebox.showerror(
            'Login Failed', 'Invalid email or password. Please try again.')


root = Tk()  # root is an object of Tk class

root.title('Login Form')  # It will change the title of GUI window
root.iconbitmap('assets/favicon.ico')

# root.minsize(800, 500)  # It sets the minimum size for the Tkinter GUI window.

root.geometry('400x500')  # Initial screensize

root.configure(background='#0096DC')  # for changing bgColor

# logo
img = Image.open('assets/logo.png')
resized_img = img.resize((50, 50))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

# title
text_label = Label(root, text='Login', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('sans-serif', 24))

# email
email_label = Label(root, text='Enter Email', fg='#ffffff', bg='#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('sans-serif', 12))

# email input
email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

# password
password_label = Label(root, text='Enter Password', fg='#ffffff', bg='#0096DC')
password_label.pack(pady=(20, 5))
password_label.config(font=('sans-serif', 12))

# email input
password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1, 15))

# button-login
login_btn = Button(root, text='Login Here', bg='white',
                   fg='black', command=handle_login)
login_btn.pack(pady=(10, 20))
login_btn.config(font=('sans-serif', 10))

root.mainloop()  # mainloop makes GUI to be on screen consistently otherwise GUI will appear and vanish
