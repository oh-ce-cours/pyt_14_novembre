from tkinter import *


def clicked():
    print("clicked")


fenetre = Tk()
bouton = Button(fenetre, text="Ne fait rien", command=clicked)
bouton.pack()
fenetre.mainloop()

