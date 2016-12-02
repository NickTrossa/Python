#!/opt/anaconda3/bin/python
'''
from tkinter import *
import time
"""
def onclick():
   pass
"""
a = "hola mundo\n"

root = Tk()
text = Text(root)

#for i in range(10):
text.insert("1.0", "H")
time.sleep(0.5)
text.insert("1.0", "o")
time.sleep(0.5)
text.insert("1.0", "l")
time.sleep(0.5)
text.insert("1.0", "a")
time.sleep(0.5)


text.insert(END, "Bye Bye.....\n")


text.pack()
"""
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
"""
root.mainloop()

'''
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
