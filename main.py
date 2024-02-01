from app.gui import SzyfrGUI
from app.szyfr import SzyfrCezara

import tkinter as tk

def main():
    root = tk.Tk()
    app = SzyfrGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()