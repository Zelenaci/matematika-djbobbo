#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import  CENTER, E, LEFT, TOP,  N, UNDERLINE, BOTTOM, HORIZONTAL, Label, Button, Scale,  StringVar, Frame, Entry   # vsechno mozne jsem si zkousel a tak jsou tu importnute i nepouzite funkce

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Okenko generujici priklady"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
         
        self.lbl0 = tk.Label(self, text="Generátor náhodných příkladů  +  -  *  /")
        self.lbl0.config(justify=LEFT, padx=20, pady=15)
        self.lbl0.config(font="Times 10 bold")
        self.lbl0.pack(anchor=CENTER)
        
        self.lbl1 = tk.Label(self, text="A")
        self.lbl1.pack(anchor=E, side=tk.LEFT, pady=15,padx=10)

        self.lbl2 = tk.Label(self, text="Znamenko")
        self.lbl2.pack(anchor=E, side=tk.LEFT, pady=15,padx=10)

        self.lbl3 = tk.Label(self, text="B")
        self.lbl3.pack(anchor=E, side=tk.LEFT, pady=15,padx=10)
        
        self.lbl5 = tk.Label(self, text="=")
        self.lbl5.pack(anchor=E, side=tk.LEFT, pady=15,padx=10)
        
        self.lbl4 = tk.Label(self, text="C")
        self.lbl4.config(justify=LEFT, padx=20, pady=10)     #myslel jsem ze funkcí Pack_forget() vyresim problem toho aby se muj label ukazal az po stisknuti tlacitka,
        self.lbl4.pack_forget()                              #zaroven ale na stejne rovine co ostatni labely, bohuzel se muj LBL4 (vysledek) stale zobrazuje uplne dole tomuhle moc nerozumim
        
        
        self.lbl5 = tk.Label(text="Kolik myslíš že to bude ?")
        self.lbl5.pack(padx=5)

        self.var5 = StringVar()                             # vim ze zadavaci pole je podvod protoze nic nedela kdyz neco zadate, nicmene jsem si schvalne chtel zkusit vysledky pomoci tlacitek a ne porovnani inputu protoze to uz umim
        self.ent5 = Entry(self)
        self.ent5.pack(pady=10,padx=10)  
        
        self.btn4 = tk.Button(self, text="Vygenerovat  priklad", command = self.nahodny_priklad) 
        self.btn4.config (pady=5,padx=10)
        self.btn4.pack(anchor=CENTER)
        
        self.btn6 = tk.Button(self, text="Zkontroluj  výsledek", command= self.zobraz_vysledek)
        self.btn6.config (pady=5,padx=10)
        self.btn6.pack(anchor=CENTER)
        
        self.btn6 = tk.Button(self, text="   Schovej výsledek   ", command=self.schovavac)
        self.btn6.config (pady=5,padx=10)
        self.btn6.pack(anchor=CENTER)
    
        self.btn5 = tk.Button(self, text="              Quit              ", command=self.quit)
        self.btn5.config (pady=5,padx=10)
        self.btn5.pack(anchor=CENTER)
        
        
    
      

    def nahodny_priklad(self):
        nahodnej_priklad = random.choice([self.plus,self.minus,self.krat,self.deleno])
        nahodnej_priklad()

    def zobraz_vysledek(self):
        zobrazovac= self.lbl4.pack()
        zobrazovac

    
    def schovavac(self):
        schovat_vysledek= self.lbl4.pack_forget()
        schovat_vysledek
    
    def plus(self):
        self.cisloA = random.randint(1,50)                           # aby to vychazelo tak 50 ne 99
        self.cisloB = random.randint(1,50 - self.cisloA)
        self.lbl1.config(text = self.cisloA)
        self.lbl3.config(text = self.cisloB)
        self.lbl2.config(text="+")
        self.vysledekC = self.cisloA + self.cisloB
        self.lbl4.config(text= self.vysledekC)
        #return self.vysledekC                                     
    
    def minus(self):
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,99)
        self.lbl1.config(text = self.cisloA)
        self.lbl3.config(text = self.cisloB)
        self.lbl2.config(text="-")
        self.vysledekC = self.cisloA - self.cisloB
        self.lbl4.config(text= self.vysledekC)
        #return self.vysledekC                                #rozhodl jsem se jit jinou cestou a tak Return neni potreba MYSLIM, NEJSEM SI JIST
    
    def deleno(self):
        self.vysledekC = random.randint(1, 9)
        self.cisloB = random.randint(1, 9)
        self.cisloA = self.vysledekC * self.cisloB         #nejsem si jist jestli to má vliv 
        self.lbl1.config(text = self.cisloA)               #ale musel jsem logicky po sobě jdouci radky pozprehazovat
        self.lbl3.config(text = self.cisloB)
        self.lbl2.config(text="/")
        self.lbl4.config(text= self.vysledekC)
        #return self.vysledekC
    
   
    def krat(self):
        self.cisloA = random.randint(1, 9)                # mel jsem zde rozmezi 1-99, to je spatne pokud 
        self.cisloB = random.randint(1, 9)                # dojde na krat dvoucifernych cisel nedojde k vysledku ale k chybe
        self.lbl1.config(text = self.cisloA)
        self.lbl2.config(text="*")
        self.lbl3.config(text = self.cisloB)  
        self.vysledekC = self.cisloA * self.cisloB 
        self.lbl4.config(text= self.vysledekC)
        #return self.vysledekC


    def about(self):
        self.generuj()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
