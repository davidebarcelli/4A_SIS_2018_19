# Questo e' un commento in python

# In python le variabili non hanno un tipo escliito, quindi non necessitano dichiarazione
a = 1
# per stamapre una variabile bast usare print
print(a)

# e' possbile fare stampe piu' complesse, ma tenedo conto dei tipi
print("a = "+str(a)+" !!")

# in python non eistono {}, la dipendenza si escplicita con l'indetazione
if(a>0):
	print("numero")
	print("positivo")
else:
	print("numero")
	print("negativo")
# notate che tutte le sitruzioni indentate fanno parte del blocco dipendente

# in python il for funziona con i range
a=10
for i in range(0,a):
	a=a-1
	print("i="+str(i)+", a="+str(a))
# notate che anche modificando il valore di a il ciclo esegue 10 volte, perche'?
# perche' il range viene generato all'inizio, in fatti si potrebbe anche scrivere

a=10
r = range(0,a)
for i in r:
	a=a-1
	print("i="+str(i)+", a="+str(a))

