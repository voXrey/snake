import tkinter
from tkinter import NW, Button, Canvas, IntVar, PhotoImage, Tk

import core.functions as func
from core.assets import Assets


def update_score(score_var:IntVar, score:int) -> None:
    """
    Met à jour le score

    Args:
        score_var (IntVar): variable tkinter du score
        score (int): score à ajouter
    """
    actuel = score_var.get()
    score_var.set(actuel+score)

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
    
    return fen
