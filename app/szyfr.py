class SzyfrCezara:
    def __init__(self, klucz):
        self.klucz = klucz

    def szyfruj(self, tekst):
        print('wprowadzony tekst:', tekst)
        zaszyfrowany_tekst = ''
        for znak in tekst:
            if znak.isalpha():
                start = ord('A') if znak.isupper() else ord('a')
                zaszyfrowany_tekst += chr((ord(znak) - start + self.klucz) % 26 + start)
            else:
                zaszyfrowany_tekst += znak
        return zaszyfrowany_tekst

    def odszyfruj(self, tekst):
        return self.szyfruj(tekst)    
