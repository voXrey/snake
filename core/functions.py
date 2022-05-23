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

"""
def quitter():
    afficher_canva(fen).quit

def commencer(creer_tableau):
    creer_tableau(20, 20)

def afficher_serpent(tab, can):
    # * x et y par taille case = 45 --> obtient coin en haut a gauche case
    # --> pour bas/droite on f +45

def angle_serpent(serpent, tab):


def affichage_serpent(serpent, tab, angle_serpent):

def apparition_pomme(tab):
    # parcourt le tableau puis créer une liste des coos dispo (=0) puis avec
    # random.choice on choit un x et un y où y'a rien et donc faire pop une pomme

def afficher_pomme(tab):
    # on prend l'emplacement du -1 puis on le mets sur le quadrillage

def pause():


def continuer():


def clique_bouton():

"""
