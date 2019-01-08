import platform
if platform.system()=='Darwin':
	from tkinter import *
else:
	from Tkinter import *
import random

finestra = Tk()

w=500
h=500

tela = Canvas(finestra,width=w,height=h)
tela.pack()


def _centro(c):
   return ( (c[0]+c[2])/2, (c[1]+c[3])/2 )

def _distanzaQ(p1,p2):
   return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


class Auto:
   global tela
   def __init__(self):
      self.punti=0
      self.lato=20
      L=self.lato/2
      W=w/2
      H=h/2
      self.disegno = tela.create_oval(W-L,H-L,W+L,H+L,fill="green")
      self.punteggio = tela.create_text(W,20,text=str(self.punti))
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
        
   def _comando(self):
      if self.direzione == "O": tela.move(self.disegno,self.v,0)
      if self.direzione == "E": tela.move(self.disegno,-self.v,0)
      if self.direzione == "N": tela.move(self.disegno,0,-self.v)
      if self.direzione == "S": tela.move(self.disegno,0,self.v)
    
   def _bordi(self):
      c=tela.coords(self.disegno)     
      if c[0]<0: 
         c[0]=w-1
         c[2]=w-1+self.lato
      if c[0]>w:
         c[0]=0
         c[2]=self.lato
      if c[1]<0:
         c[1]=h-1
         c[3]=h-1+self.lato
      if c[1]>h:
         c[1]=0
         c[3]=self.lato   
      tela.coords(self.disegno,c[0],c[1],c[2],c[3])

   def _collisioni(self):
      c = tela.coords(self.disegno)
      c = _centro(c)
      for o in self.ostacoli:
         co = tela.coords(o.disegno)
         co = _centro(co)
         if _distanzaQ(c,co) < (self.lato)**2:
            tela.itemconfig(self.disegno,fill='red')
            tela.itemconfig(o.disegno,fill='red')
            self.continua = False
            o.continua = False

        
   def _avanza(self):
      self._comando()
      self._bordi()
      self._collisioni()
      self.punti=self.punti+self.v
      tela.itemconfig(self.punteggio,text=str(self.punti))
      if self.continua: tela.after(40,self._avanza)

   def inizia(self):
      self._avanza()

class Ostacolo:
   global tela
   def __init__(self):
      self.lato=20
      L=self.lato/2
      W=random.randint(L,w-L)
      H=random.randint(L,h-L)
      self.disegno = tela.create_oval(W-L,H-L,W+L,H+L,fill="blue")
      self.direzione = "O"
      self.v = 1
      self.continua = True

   def _comando(self):
      self.v=random.randint(0,4)
      RX=random.randint(-self.v,self.v)
      RY=random.randint(-self.v,self.v)
      tela.move(self.disegno,RX,RY)

   def _bordi(self):
      c=tela.coords(self.disegno)     
      if c[0]<0: 
         c[0]=w-1
         c[2]=w-1+self.lato
      if c[0]>w:
         c[0]=0
         c[2]=self.lato
      if c[1]<0:
         c[1]=h-1
         c[3]=h-1+self.lato
      if c[1]>h:
         c[1]=0
         c[3]=self.lato   
      tela.coords(self.disegno,c[0],c[1],c[2],c[3])

         
   def _avanza(self):
      self._comando()
      self._bordi()
      if self.continua: tela.after(40,self._avanza)

   def inizia(self):
      self._avanza()


auto = Auto()

ostacoli=[]
for i in range(0,10):
   ostacoli.append(Ostacolo())
   
auto.ostacoli=ostacoli

auto.inizia()
for o in ostacoli: o.inizia()

finestra.mainloop()
