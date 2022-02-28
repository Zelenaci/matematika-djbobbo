#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import  CENTER, E, LEFT, TOP,  N, UNDERLINE, BOTTOM, HORIZONTAL, Label, Button, Scale,  StringVar, Frame, Entry  

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Okenko"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
         
        self.lbl0 = tk.Label(self, text="Nadpis")
        self.lbl0.config(justify=CENTER, padx=20, pady=15)
        self.lbl0.config(font="Times 10 bold")
        self.lbl0.grid(row =0 , column =0 ,columnspan=7)
        
        self.lbl1 = tk.Label(self, text="1")
        self.lbl1.grid(row =1 , column =2 ,columnspan=5)

        self.lbl1 = tk.Label(self, text="2")
        self.lbl1.grid(row =3 , column =3 )

        self.lbl2 = tk.Label(self, text="3")
        self.lbl2.grid(row =3 , column =4 )

        self.lbl3 = tk.Label(self, text="4")
        self.lbl3.grid(row =3 , column =5 )
        
        self.lbl4 = tk.Label(self, text="5")
        self.lbl4.grid(row =3 , column =6 )
        
       

        self.var1 = StringVar()                             
        self.ent1 = Entry(self)
        self.ent1.grid(row =2 , column =2 ,columnspan= 5 )
        
        self.btn1 = tk.Button(self, text="T1" ) 
        self.btn1.config (pady=5,padx=10)
        self.btn1.grid(row =4 , column =3 )
        
        self.btn2 = tk.Button(self, text="T2" )
        self.btn2.config (pady=5,padx=10)
        self.btn2.grid(row =4 , column =4 )
        
        self.btn3 = tk.Button(self, text="T3")
        self.btn3.config (pady=5,padx=10)
        self.btn3.grid(row =4 , column =5 )
    
        self.btn4 = tk.Button(self, text="T4")
        self.btn4.config (pady=5,padx=10)
        self.btn4.grid(row =4 , column =6 )
        
    
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
