from tkinter import IntVar
from classes import Snake

def creer_tableau(lignes:int, colonnes:int) -> list[list[int]]:
    """
    Créer un tableau rempli de 0

    Args:
        lignes (int): nombre de lignes
        colonnes (int): nombre de colonnes

    Returns:
        list[list[int]]: liste de listes de 0
    """
    return [[0 for i in range(colonnes)] for j in range(lignes)]

def update_score(score_var:IntVar, score:int) -> None:
    """
    Met à jour le score

    Args:
        score_var (IntVar): variable tkinter qui représente le score
        score (int): score à ajouter
    """
    actuel = score_var.get()
    score_var.set(actuel+score)


def nouvelle_position(prochain_mouvement:str, serpent:Snake, tab:list[list[int]]) -> tuple[int]:
    """
    Calcule la prochaine position de la tête sur le tableau

    Args:
        prochain_mouvement (str): direction vers laquelle part le serpent
        serpent (Snake): le serpent
        tab (list[list[int]]): tableau du jeu

    Returns:
        tuple[int]: prochaine position de la têtes
    """
    # On récupère la position actuelle de la tête du serpent
    position_tete = serpent.corps[0].position

    # On teste la variable prochain_mouvement pour connaître
    # la direction du serpent
    if prochain_mouvement == "haut":
        pass
    elif prochain_mouvement == "bas":
        pass
    elif prochain_mouvement == "gauche":
        pass
    elif prochain_mouvement == "droite":
        pass

def afficher_canva(W, H, fen, can):
    #Crée la base de l'interface
    fen = Tk()
    fen.title("Snake")
    can = Canvas(fen, width=W, height=H, bg = "#24222e")
    quadrillage = PhotoImage(file="background_snake.png")
    can.create_image(0, 0, anchor=NW, image=quadrillage)
    # Crée le bouton quitter
    quitter_button = PhotoImage(file="quitter_button.png")
    can.create_image(800, 100, image=quitter_button)
    # Crée le bouton commencer
    commencer_button = PhotoImage(file="commencer.png")
    can.create_image(800, 200, image=commencer_button)
    # Crée le bouton reprendre
    reprendre_button = PhotoImage(file="reprendre.png")
    can.create_image(800, 300, image=reprendre_button)
    # Crée le bouton pause
    pause_button = PhotoImage(file="pause.png")
    can.create_image(800, 400, image=pause_button)
    # lance l'interface
    can.pack()
    fen.mainloop()

def quitter():
    afficher_canva(fen).quit

def commencer(creer_tableau):
    creer_tableau(20, 20)

def recommencer(creer_tableau):
    creer_tableau(20, 20)

