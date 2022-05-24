from tkinter import Canvas
from core.assets import Assets
from core.variables import game
from core.classes import Snake

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


def quitter():
    exit()

def commencer():
    game["tab"] = creer_tableau(20, 20)
    game["tab"][game["depart"][0]][game["depart"][1]] = 1
    game["serpent"] = Snake(1, game["depart"], game["depart2"])

def pause():
    game["pause"] = not game["pause"]


def directions_frame(n:int):
    frame = game["serpent"].corps[n]
    frame_position = frame.position
    frame_suivante_position = frame.suivant
    frame_precedente_position = frame.precedent

    suivante_direction = None
    precedente_direction = None

    if frame_suivante_position is None: pass
    else:
        if frame_suivante_position[0] < frame_position[0]: suivante_direction = "Down"
        elif frame_suivante_position[0] > frame_position[0]: suivante_direction = "Up"
        elif frame_suivante_position[1] < frame_position[1]: suivante_direction = "Right"
        else: suivante_direction = "Left"

    if frame_precedente_position is None: pass
    else:
        if frame_precedente_position[0] < frame_position[0]: precedente_direction = "Up"
        elif frame_precedente_position[0] > frame_position[0]: precedente_direction = "Down"
        elif frame_precedente_position[1] < frame_position[1]: precedente_direction = "Left"
        else: precedente_direction = "Right"

    return (precedente_direction, suivante_direction)

def bouger(direction:str):
    directions = directions_frame(0)
    direction_actuelle = directions[1]

    up_down = ["Up", "Down"]
    left_right = ["Left", "Right"]
    if (direction in up_down) and (direction_actuelle in up_down): return
    elif (direction in left_right) and (direction_actuelle in left_right): return

    game["direction"] = direction

def coordonnees():
    tete_position = game["serpent"].corps[0].position
    direction = game["direction"]

    # On détermine temporairement la prochaine position
    prochaine_position = None
    if direction == "Up":
        l, c = tete_position
        l -= 1
        prochaine_position = (l, c)
    elif direction == "Down":
        l, c = tete_position
        l += 1
        prochaine_position = (l, c)
    elif direction == "Left":
        l, c = tete_position
        c -= 1
        prochaine_position = (l, c)
    else:
        l, c = tete_position
        c += 1
        prochaine_position = (l, c)
    
    # On le place de l'autre côté de la map si le serpent la dépasse
    if prochaine_position[0] < 0: prochaine_position[0] = 19
    elif prochaine_position[0] > 19: prochaine_position[0] = 0
    elif prochaine_position[1] < 0: prochaine_position[1] = 19
    elif prochaine_position[1] > 19: prochaine_position[1] = 0

    return prochaine_position

def deplacement():
    coords = coordonnees()
    collision = game["serpent"].collision(coords, game["tab"])
    if collision:
        game["serpent"].avancer(coords, game["tab"], False)
    else:
        print("dead")

def quoi_afficher_corps(corps):
    resultats = []
    corps_count = len(corps)
    case_pixels = 45
    assets:Assets = game["assets"]

    i = 0
    while i < corps_count:
        frame = corps[i]
        position = frame.position
        coords = (position[1]*case_pixels, position[0]*case_pixels)
        image = None
        dir_p, dir_s = directions_frame(i)

        if dir_p == dir_s:
            vertical = ["Up", "Down"]
            if dir_p in vertical: image = assets.CORPS_VERTICAL
            else: image = assets.CORPS_HORIZONTAL
        
        elif  dir_p is None:
            if dir_s == "Up": image = assets.TETE_HAUT
            elif dir_s == "Down": image = assets.TETE_BAS
            elif dir_s == "Left": image = assets.TETE_GAUCHE
            else: image = assets.TETE_DROITE

        elif dir_s is None:
            if dir_p == "Up": image = assets.QUEUE_HAUT
            elif dir_p == "Down": image = assets.QUEUE_BAS
            elif dir_p == "Left": image = assets.QUEUE_GAUCHE
            else: image = assets.QUEUE_DROITE

        else:
            up_right = ["Up", "Right"]
            right_down = ["Right", "Down"]
            down_left = ["Down", "Left"]
            if (dir_p in up_right) and (dir_s in up_right): image = assets.ANGLE_NE
            elif (dir_p in right_down) and (dir_s in right_down): image = assets.ANGLE_SE
            elif (dir_p in down_left) and (dir_s in down_left): image = assets.ANGLE_SW
            else: image = assets.ANGLE_NW
        
        resultats.append(coords, image)
        i += 1

    return resultats

"""
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

"""
