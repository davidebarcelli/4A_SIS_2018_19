from tkinter import *

finestra = Tk()

tela = Canvas(finestra,width=500,height=500)
tela.pack()

class Auto:
    def __init__(self):
        global tela
        self.disegno = tela.create_oval(250,250,270,270,fill="red")
        self.direzione = "O"
        self.v = 1
        self.continua = True
        tela.focus_set()
        tela.bind("<Key>",self._tastiera)

    def _tastiera(self,event):
        if event.char=='m': self.v = self.v + 1
        if event.char=='n': self.v = self.v - 1
        if self.v>3:        self.v=3
        if self.v<0:        self.v=0
        if event.char=='w': self.direzione = "N"
        if event.char=='a': self.direzione = "E"
        if event.char=='s': self.direzione = "S"
        if event.char=='d': self.direzione = "O"

    def _avanza(self):
        if not self.continua: return
        global tela
        if self.direzione == "O": tela.move(self.disegno,self.v,0)
        if self.direzione == "E": tela.move(self.disegno,-self.v,0)
        if self.direzione == "N": tela.move(self.disegno,0,-self.v)
        if self.direzione == "S": tela.move(self.disegno,0,self.v)
        tela.after(40,self.inizia)

    def inizia(self):
        self._avanza()


auto = Auto()
auto.inizia()

finestra.mainloop()
