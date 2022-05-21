from tkinter import IntVar, Tk, PhotoImage, Canvas, NW
import tkinter
from assets import assets

def update_score(score_var:IntVar, score:int) -> None:
    """
    Met à jour le score

    Args:
        score_var (tkinter.IntVar): variable tkinter qui représente le score
        score (int): score à ajouter
    """
    actuel = score_var.get()
    score_var.set(actuel+score)

def ajouter_boutons(can:Canvas) -> Canvas:
    """
    Ajoute les boutons au canvas

    Args:
        can (tkinter.Canvas): canvas 

    Returns:
        tkinter.Canvas: le canvas avec les boutons
    """
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

    return can

def creer_canvas(W:int, H:int, fen:tkinter.Tk) -> Canvas:
    """
    Créer le canvas

    Args:
        W (int): largeur du canvas
        H (int): hauteur du canvas
        fen (tkinter.Tk): fenetre du jeu

    Returns:
        tkinter.Canvas: le canvas
    """
    # Création du canvas
    can = Canvas(fen, width=W, height=H, bg = "#24222e")

    # Ajout du quadrillage, map du jeu
    quadrillage = PhotoImage(file=assets.BACKGROUND_SNAKE)
    can.create_image(0, 0, anchor=NW, image=quadrillage)

    # Ajout des boutons
    can = ajouter_boutons(can)

    can.pack()
    return can

def creer_fenetre() -> Tk:
    """
    Créer la fenêtre du jeu

    Returns:
        tkinter.Tk: fenêtre
    """
    #Créer la base de l'interface
    fen = Tk()
    fen.title("Snake")
    
    return fen
