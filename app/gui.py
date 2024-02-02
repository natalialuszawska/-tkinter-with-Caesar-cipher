import tkinter as tk
from app.szyfr import SzyfrCezara
from tkmacosx import Button
klucz_szyfrowania = 3

import tkinter as tk
from app.szyfr import SzyfrCezara

klucz_szyfrowania = 3

class SzyfrGUI:
    zaszyfrowany_tekst = None

    def __init__(self,master):
        self.master = master
        self.master.config(bg="LightPink")

        self.label = tk.Label(self.master, text='Wprowadź tekst', bg="LightPink",  fg="white", font=("Arial", 14))
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry = tk.Entry(self.master, bg="navy" , fg="white", font=("Arial", 14))
        self.entry.grid(row=1, column=0, padx=5, pady=5)

        self.button = Button(self.master, text="Zaszyfruj",  bg="navy", fg="white",  font=("Arial", 14), borderless=1, command=self.zaszyfruj_tekst)
        self.button.grid(row=2, column=0, padx=5, pady=5)

        self.result_label = tk.Label(self.master, text='', bg="LightPink",  fg="white",  font=("Arial", 14))
        self.result_label.grid(row=3, column=0, padx=5, pady=5)


        self.button_odszyfruj = Button(self.master, text="Odszyfruj",  bg="navy", fg="white",borderless=1, font=("Arial", 14), command=self.odszyfruj_tekst)
        self.button_odszyfruj.grid(row=4, column=0, padx=5, pady=5)

        self.odszyfruj_result_label = tk.Label(self.master, text='', bg="LightPink",   fg="white", font=("Arial", 14))
        self.odszyfruj_result_label.grid(row=5, column=0, padx=5, pady=5)

    def zaszyfruj_tekst(self):
        tekst = self.entry.get()
        if not tekst:
            self.result_label.config(text="Proszę wprowadzić tekst do zaszyfrowania.")
            return
        global zaszyfrowany_tekst
        zaszyfrowany_tekst = SzyfrCezara(klucz_szyfrowania).szyfruj(tekst)
        self.result_label.config(text=f"Zaszyfrowany tekst: {zaszyfrowany_tekst}")

    def odszyfruj_tekst(self):
        if not hasattr(self, 'zaszyfrowany_tekst'):
            self.odszyfruj_result_label.config(text="Brak zaszyfrowanego tekstu do odszyfrowania.")
            return
        odszyfrowany_tekst = SzyfrCezara(-klucz_szyfrowania).szyfruj(zaszyfrowany_tekst)
        self.odszyfruj_result_label.config(text=f"Odszyfrowany tekst: {odszyfrowany_tekst}")
