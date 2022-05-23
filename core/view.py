from tkinter import IntVar, Tk, PhotoImage, Canvas, NW, Button
import tkinter
from core.assets import assets
import core.functions as func

def update_score(score_var:IntVar, score:int) -> None:
    """
    Met à jour le score

    Args:
        score_var (tkinter.IntVar): variable tkinter qui représente le score
        score (int): score à ajouter
    """
    actuel = score_var.get()
    score_var.set(actuel+score)

def ajouter_boutons(can):
    """
    Ajoute les boutons au canvas

    Args:
        can (tkinter.Canvas): canvas 

    Returns:
        tkinter.Canvas: le canvas avec les boutons
    """
    # Crée le bouton quitter
    image = PhotoImage(assets.BOUTON_QUITTER)
    quitter_button = Button(
        can,
        image=image,
        command= lambda: func.quitter(can),
        width=200,
        height=100
    )
    quitter_button.pack()
    """
    # Crée le bouton commencer
    commencer_button = PhotoImage(file=assets.BOUTON_COMMENCER)
    can.create_image(800, 200, image=commencer_button)

    # Crée le bouton reprendre
    reprendre_button = PhotoImage(file=assets.BOUTON_REPRENDRE)
    can.create_image(800, 300, image=reprendre_button)

    # Crée le bouton pause
    pause_button = PhotoImage(file=assets.BOUTON_PAUSE)
    can.create_image(800, 400, image=pause_button)
    """

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
    map_ = PhotoImage(name="map", file=assets.MAP)
    can.map = map_
    #quadrillage = PhotoImage(file=assets.QUADRILLAGE)
    can.create_image(0, 0, anchor=NW, image=map_)
    #can.create_image(0, 0, anchor=NW, image=quadrillage)

    # Ajout des boutons
    #ajouter_boutons(can)

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
