from tkinter import IntVar

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

