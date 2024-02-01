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

        self.entry = tk.Entry(self.master,  font=("Arial", 14), fg="navy")
        self.entry.grid(row=1, column=0, padx=5, pady=5)

        self.button = tk.Button(self.master, text="Zaszyfruj",  bg="navy", fg="white",  font=("Arial", 14), command=self.zaszyfruj_tekst)
        self.button.grid(row=2, column=0, padx=5, pady=5)

        self.result_label = tk.Label(self.master, text='', bg="LightPink",  fg="white",  font=("Arial", 14))
        self.result_label.grid(row=3, column=0, padx=5, pady=5)

        self.button_odszyfruj = tk.Button(self.master, text="Odszyfruj",  bg="navy", fg="white",  font=("Arial", 14), command=self.odszyfruj_tekst)
        self.button_odszyfruj.grid(row=4, column=0, padx=5, pady=5)

        self.odszyfruj_result_label = tk.Label(self.master, text='', bg="LightPink",   fg="white", font=("Arial", 14))
        self.odszyfruj_result_label.grid(row=5, column=0, padx=5, pady=5)

    def zaszyfruj_tekst(self):
        tekst = self.entry.get()
        global zaszyfrowany_tekst
        zaszyfrowany_tekst = SzyfrCezara(klucz_szyfrowania).szyfruj(tekst)
        self.result_label.config(text=f"Zaszyfrowany tekst: {zaszyfrowany_tekst}")

    def odszyfruj_tekst(self):
        print('odszyfruj tekst')
        odszyfrowany_tekst = SzyfrCezara(-klucz_szyfrowania).odszyfruj(zaszyfrowany_tekst)
        self.odszyfruj_result_label.config(text=f"Odszyfrowany tekst: {odszyfrowany_tekst}")

