#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import  CENTER, E, LEFT, TOP,  N, UNDERLINE, BOTTOM, Label, Button, StringVar, Frame

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Okenko generujici priklady"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        
        #self.var9 = StringVar()      
        #self.frame9 = Frame(self)
        #self.frame9.pack()  
        
        
        self.lbl0 = tk.Label(self, text="Generátor náhodných příkladů  +  -  *  /")
        self.lbl0.config(justify=LEFT, padx=20, pady=10)
        self.lbl0.config(font="Times 10 bold")
        self.lbl0.pack(anchor=CENTER)

        self.lbl1 = tk.Label(self, text="A")
        #self.lbl1.config(justify=LEFT, padx=20, pady=10)
        self.lbl1.pack(anchor=E, side=tk.LEFT, pady=15,padx=10)

        self.lbl2 = tk.Label(self, text="Znamenko")
        #self.lbl2.config(justify=LEFT, padx=20, pady=10)
        self.lbl2.pack(anchor=E, side=tk.LEFT, pady=15,padx=10)

        self.lbl3 = tk.Label(self, text="B")
        #self.lbl3.config(justify=LEFT, padx=20, pady=10)
        self.lbl3.pack(anchor=E, side=tk.LEFT, pady=15,padx=10)
        
        self.lbl5 = tk.Label(self, text="=")
        self.lbl5.pack(anchor=E, side=tk.LEFT, pady=15,padx=10)
        
        self.lbl4 = tk.Label(self, text="C")
        #self.lbl4.config(justify=LEFT, padx=20, pady=10)
        self.lbl4.pack(anchor=E, side=tk.LEFT, pady=15,padx=10)
        

        self.btn4 = tk.Button(self, text="Vygenerovat  priklad", command = self.nahodny_priklad) 
        self.btn4.config (pady=5,padx=10)
        self.btn4.pack()
        
        self.btn5 = tk.Button(self, text="              Quit              ", command=self.quit)
        self.btn5.config (pady=5,padx=10)
        self.btn5.pack()
        
        self.btn6 = tk.Button(self, text="            About             ", command=self.about)
        self.btn6.config (pady=5,padx=10)
        self.btn6.pack()

    
    def generuj(self):
        funkce = random.choice([self.plus,self.minus,self.krat,self.deleno])
        funkce()
       # odstranil jsem zde neco

    def nahodny_priklad(self):
        nahodnej_priklad = random.choice([self.plus,self.minus,self.krat,self.deleno])
        nahodnej_priklad()

    def plus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,100 - self.cisloA)
        self.lbl1.config(text = self.cisloA)
        self.lbl3.config(text = self.cisloB)
        self.lbl2.config(text="+")
        self.vysledekC = self.cisloA + self.cisloB
        self.lbl4.config(text= self.vysledekC)
        return self.vysledekC
    
    def minus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,99)
        self.lbl1.config(text = self.cisloA)
        self.lbl3.config(text = self.cisloB)
        self.lbl2.config(text="-")
        self.vysledekC = self.cisloA - self.cisloB
        self.lbl4.config(text= self.vysledekC)
        return self.vysledekC
    
    def deleno(self):
        self.vysledekC = random.randint(1, 9)
        self.cisloB = random.randint(1, 9)
        self.cisloA = self.vysledekC * self.cisloB          #nejsem si jist jestli to má vliv 
        self.lbl1.config(text = self.cisloA)               #ale musel jsem logicky po sobě jdouci radky pozprehazovat
        self.lbl3.config(text = self.cisloB)
        self.lbl2.config(text="/")
        self.lbl4.config(text= self.vysledekC)
        return self.vysledekC
    
   
    def krat(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,99)              
        self.lbl1.config(text = self.cisloA)
        self.lbl2.config(text="*")
        self.lbl3.config(text = self.cisloB)  
        self.vysledekC = self.cisloA * self.cisloB 
        return self.vysledekC


    def about(self):
        self.generuj()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
