import requests
from tkinter import *  # from tkinter library import all the classes
from urllib.request import urlopen
from PIL import ImageTk, Image  # Python Imaging Library
import io  # The io module provides classes and functions for handling input and output operations, such as reading from or writing to files, working with streams, and manipulating data.

# The webbrowser module provides a high-level interface for displaying web-based documents to users. It allows you to open web pages, URLs, and files in the user's default web browser.
import webbrowser


class NewsApp:

    def __init__(self):

        # fetch data
        self.data = requests.get(
            'https://newsapi.org/v2/top-headlines?country=in&apiKey=d897fc7fa5ba4cf4ad3862f6997270f5').json()
        # initial GUI load
        self.load_gui()

        # load the 1st news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.title('News')
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):

        # clear the skin for the new news item
        self.clear()

        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://th.bing.com/th/id/OIP.iB4O5aZEzLkZv0X7tVdjEQHaHa?pid=ImgDet&w=900&h=900&rs=1'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image=photo)
        label.pack()

        heading = Label(self.root, text=self.data['articles'][index]['title'],
                        bg='black', fg='white', wraplength=350, justify='center')

        heading.pack(pady=(10, 20))
        heading.config(font=('Poppins', 15))

        description = Label(self.root, text=self.data['articles'][index]['description'],
                            bg='black', fg='white', wraplength=350, justify='center')

        description.pack(pady=(2, 20))
        description.config(font=('Poppins', 12))

        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        if index != 0:
            prev = Button(frame, text='Prev', width=16, height=3,
                          command=lambda: self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read_more = Button(frame, text='Read More', width=16, height=3,
                           command=lambda: self.open_link(self.data['articles'][index]['url']))
        read_more.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame, text='Next', width=16, height=3,
                          command=lambda: self.load_news_item(index+1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self, url):
        webbrowser.open(url)


obj = NewsApp()
