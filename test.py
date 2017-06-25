print ("Hello")

# On importe Tkinter
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.geometry('200x200')

# On crée un label
champ_label = Label(fenetre, text="Hello")
champ_label2 = Label(fenetre, text="Hello again")

# On affiche le label dans la fenêtre
champ_label.pack()
champ_label2.pack()

# On crée un bouton
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
# On affiche le bouton dans la fenêtre
bouton_quitter.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
