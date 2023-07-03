import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()

root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")


def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    corrected_word = str(a.correct())

    if word == corrected_word:
        result.config(text="Correct Spelling", fg="green")
        spell.config(text="")
    else:
        result.config(text="")
        spell.config(text="Correct text is: " + corrected_word)


heading = Label(root, text="Spelling Checker", font=(
    "Verdana", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30,
                   font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="Check", font=("arial", 20, "bold"),
                fg="white", bg="red", command=check_spelling)
button.pack()

spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=350, y=250, anchor='center')

result = Label(root, font=("poppins", 20), bg="#dae6f6")
result.place(x=350, y=300, anchor='center')

root.mainloop()
