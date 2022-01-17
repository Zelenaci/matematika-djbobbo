#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        self.btn2 = tk.Button(self, text="About", command=self.about)
        self.btn2.pack()
    
    
    def generuj(self):
        funkce = random.choice([self.plus,self.minus,self.krat,self.deleno])
        funkce()
        if funkce == self.plus:
            print("plus")
        if funkce == self.minus:
            print("minus")            
        if funkce == self.deleno:
            print("deleno")
        if funkce == self.krat:
            print("krat")


    def plus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,100 - self.cisloA)
        self.vysledek = self.cisloA + self.cisloB
        self.lbl.config(text="+")

    def minus(self):
        self.lbl.congifg(text="-")
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,99)
        self.vysledek = self.cisloA - self.cisloB
   
    def deleno(self):
        self.vysledek = random.randint(1, 9)
        self.cisloB = random.randint(1, 9)
        self.cisloA = self.vysledek * self.cisloB
        self.lbl.congifg(text="/")
   
    def krat(self):
        self.lbl.congifg(text="*")
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,99)
       
   
    def about(self):
        self.generuj()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
