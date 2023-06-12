from tkinter import *

def toggle_switch():
    if toggle_button["text"] == "Dark Mode":
        root.config(bg='black')
        toggle_button.config(text="Light Mode", bg='white', fg='black')
    else:
        root.config(bg='white')
        toggle_button.config(text="Dark Mode", bg='#202123', fg='white')

root = Tk()

root.title('Toggle Switch')
root.geometry('400x600')
root.config(bg='white')

toggle_button = Button(text='Dark Mode',bg='#202123',fg='white', width=10, height=1,command=toggle_switch)
toggle_button.pack(pady=(200,50))
toggle_button.configure(font=('Verdana',20))

root.mainloop()