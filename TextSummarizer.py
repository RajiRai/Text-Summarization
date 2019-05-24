
# coding: utf-8

# In[ ]:

from gensim.summarization import summarize
from tkinter import *
import tkinter 
from tkinter import messagebox
top = Tk()

def process():
    sentence=Entry.get(E1)
    ans=summarize(sentence)
    Entry.insert(E4,0,ans)
    print(ans)

top.title("Text Summarizer")
L1 = Label(top, text="Text Summarizer",).grid(row=0,column=1)
L2 = Label(top, text="Enter text to summerize",).grid(row=1,column=0)
L3 = Label(top, text="Answer",).grid(row=4,column=0)
E1 = Entry(top, bd=5)
E1.grid(row=1, column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B=Button(top, text ="Submit",command = process).grid(row=5,column=1,)

top.mainloop()

