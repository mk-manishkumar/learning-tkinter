from tkinter import *
from tkinter import messagebox


def check_palindrome():
    input = word_input.get()
    reversed_input = input.lower()[::-1]

    if input.lower() == reversed_input:
        messagebox.showinfo('Yes', "It's Palindrome!")
    else:
        messagebox.showerror('No', "It's not Palindrome!")


root = Tk()

root.title('Palindrome Checker')
root.geometry('400x500')
root.minsize(400, 500)

root.configure(background='#8D3DAF')

text_label = Label(root, text='Palindrome Checker', fg='white', bg="#8D3DAF")
text_label.pack(pady=(100, 10))
text_label.config(font=('verdana', 24))

input_label = Label(root, text='Enter Word or Number',
                    fg='white', bg='#8D3DAF')
input_label.pack(pady=(20, 5))
input_label.config(font=('verdana', 12))

word_input = Entry(root, width=50)
word_input.pack(ipady=6, pady=(15, 15))

check_btn = Button(root, text="Check", bg='white',
                   fg='black', command=check_palindrome)
check_btn.pack(pady=(10, 20))
check_btn.config(font=('verdana', 10))

root.mainloop()
