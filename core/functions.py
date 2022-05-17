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