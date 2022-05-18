from tkinter import IntVar, Tk, PhotoImage, Canvas, NW
from assets import assets

def update_score(score_var:IntVar, score:int) -> None:
    """
    Met à jour le score

    Args:
        score_var (IntVar): variable tkinter qui représente le score
        score (int): score à ajouter
    """
    actuel = score_var.get()
    score_var.set(actuel+score)

def afficher_canva(W, H, fen, can):
    #Crée la base de l'interface
    fen = Tk()
    fen.title("Snake")
    can = Canvas(fen, width=W, height=H, bg = "#24222e")
    quadrillage = PhotoImage(file=assets.BACKGROUND_SNAKE)
    can.create_image(0, 0, anchor=NW, image=quadrillage)
    # Crée le bouton quitter
    quitter_button = PhotoImage(file=assets.BOUTON_QUITTER)
    can.create_image(800, 100, image=quitter_button)
    # Crée le bouton commencer
    commencer_button = PhotoImage(file=assets.BOUTON_COMMENCER)
    can.create_image(800, 200, image=commencer_button)
    # Crée le bouton reprendre
    reprendre_button = PhotoImage(file=assets.BOUTON_REPRENDRE)
    can.create_image(800, 300, image=reprendre_button)
    # Crée le bouton pause
    pause_button = PhotoImage(file=assets.BOUTON_PAUSE)
    can.create_image(800, 400, image=pause_button)
    # lance l'interface
    can.pack()
    fen.mainloop()