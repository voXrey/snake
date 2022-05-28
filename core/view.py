import tkinter
from tkinter import NW, Canvas, Event, Tk

import core.functions as func


def touche(event:Event):
    """
    Cette fonction se déclenche quand une touche du clavier
    est appuyées ce qui permet ensuite de trier les touches
    attendues de celles inattendues et de réagir en fonction

    Args:
        event (Event): évènement tkinter
    """
    # Récupérer le nom de la touche appuyée
    key = event.keysym
    # Création des différentes actions en fonction
    # de la touche appuyée 
    actions = {
        "Up": lambda: func.changer_direction("Up"),
        "Down": lambda: func.changer_direction("Down"),
        "Left": lambda: func.changer_direction("Left"),
        "Right": lambda: func.changer_direction("Right"),
        "q": lambda: func.quitter(),
        "s":  lambda: func.commencer(),
        "space": lambda: func.pause(),
        "Escape": lambda: func.pause(),
    }
    # Ne tente de déclencher l'action que si la touche
    # est attendue, sinon ne fait rien
    if key in actions: actions[key]()

def creer_canvas(W:int, H:int, fen:tkinter.Tk, assets) -> Canvas:
    """
    Créer le canvas principal du jeu

    Args:
        W (int): largeur du canvas
        H (int): hauteur du canvas
        fen (tkinter.Tk): fenêtre principale du jeu
        assets: les assets du jeu

    Returns:
        Canvas: canvas principal
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
    fen.title("Snake") # Changement du noom de la fenêtre
    fen.iconbitmap("./core/assets/icon/icon.ico") # Changement du l'icone de la fenêtre
    fen.attributes('-fullscreen', True) # Mettre la fenêtre en plein écran
    
    return fen
