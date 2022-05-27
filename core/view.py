import tkinter
from tkinter import NW, Button, Canvas, IntVar, Label, PhotoImage, Tk

import core.functions as func
from core.assets import Assets
from core.variables import game
from tkinter import Event

def touche(event:Event):
    key = event.keysym
    options = {
        "Up": lambda: func.bouger("Up"),
        "Down": lambda: func.bouger("Down"),
        "Left": lambda: func.bouger("Left"),
        "Right": lambda: func.bouger("Right"),
        "q": lambda: func.quitter(),
        "s":  lambda: func.commencer(),
        "space": lambda: func.pause(),
        "Escape": lambda: func.pause(),
    }
    if key in options: options[key]()

def creer_canvas(W:int, H:int, fen:tkinter.Tk, assets:Assets) -> Canvas:
    """
    Créer le canvas principal du jeu

    Args:
        W (int): largeur
        H (int): hauteur
        fen (tkinter.Tk): fenêtre du jeu
        assets (Assets): les assets

    Returns:
        Canvas: le canvas du jeu
    """
    # Création du canvas
    can = Canvas(fen, width=W, height=H, bg = "#24222e")
    
    # Ajout de la map du jeu
    can.create_image(0, 0, anchor=NW, image=assets.MAP)

    can.pack()
    return can

def creer_fenetre() -> Tk:
    """
    Créer la fenêtre du jeu

    Returns:
        Tk: La fenêtre
    """
    #Créer la base de l'interface
    fen = Tk()
    fen.title("Snake")
    fen.iconbitmap("./core/assets/icon/icon.ico")
    fen.attributes('-fullscreen', True)
    
    return fen
