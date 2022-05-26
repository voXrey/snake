from tkinter import NW, Canvas
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

def quitter():
    exit()

def commencer():
    game["tab"] = creer_tableau(20, 20)
    game["tab"][game["depart"][0]][game["depart"][1]] = 1
    game["serpent"] = Snake(1, game["depart"], game["depart2"])

def pause():
    game["pause"] = not game["pause"]

def cote_frames(n:int):
    frame = game["serpent"].corps[n]
    frame_position = frame.position
    frame_suivante_position = frame.suivant
    frame_precedente_position = frame.precedent

    suivante_direction = None
    precedente_direction = None

    if frame_precedente_position is None: pass
    else:
        if frame_precedente_position[0] < frame_position[0]: precedente_direction = "Up"
        elif frame_precedente_position[0] > frame_position[0]: precedente_direction = "Down"
        elif frame_precedente_position[1] < frame_position[1]: precedente_direction = "Left"
        else: precedente_direction = "Right"

    if frame_suivante_position is None: pass
    else:
        if frame_suivante_position[0] < frame_position[0]: suivante_direction = "Up"
        elif frame_suivante_position[0] > frame_position[0]: suivante_direction = "Down"
        elif frame_suivante_position[1] < frame_position[1]: suivante_direction = "Left"
        else: suivante_direction = "Right"

    return (precedente_direction, suivante_direction)

def bouger(direction:str):
    directions = cote_frames(0)
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
    l, c = tete_position
    if direction == "Up":
        l -= 1
    elif direction == "Down":
        l += 1
    elif direction == "Left":
        c -= 1
    else:
        c += 1
    
    # On le place de l'autre côté de la map si le serpent la dépasse
    if l < 0: l = 19
    elif l > 19: l = 0
    elif c < 0: c = 19
    elif c > 19: c = 0

    return (l, c)

def deplacement(can:Canvas):
    coords = coordonnees()
    collision = game["serpent"].collision(coords, game["tab"])
    if not collision:
        game["serpent"].avancer(coords, game["tab"], True)
    else:
        print("dead")

    supprimer_elements(can)
    afficher_elements(can)
    can.after(game["delai"], lambda: deplacement(can))

def quoi_afficher_corps(corps):
    resultats = []
    corps_count = len(corps)
    case_pixels = 45
    assets:Assets = game["assets"]

    vertical = ["Up", "Down"]
    horizontal = ["Left", "Right"]
    up_right = ["Up","Right"]
    down_right = ["Down", "Right"]
    down_left = ["Down", "Left"]

    i = 0
    while i < corps_count:
        frame = corps[i]
        position = frame.position
        coords = (position[1]*case_pixels, position[0]*case_pixels)
        image = None
        dir_p, dir_s = cote_frames(i)
        print(f"{i}: {dir_p}:{dir_s}")

        if (dir_p in vertical) and (dir_s in vertical): image = assets.CORPS_VERTICAL
        elif (dir_p in horizontal) and (dir_s in horizontal): image = assets.CORPS_HORIZONTAL
        
        elif  dir_p is None:
            if dir_s == "Up": image = assets.TETE_BAS
            elif dir_s == "Down": image = assets.TETE_HAUT
            elif dir_s == "Left": image = assets.TETE_DROITE
            else: image = assets.TETE_GAUCHE

        elif dir_s is None:
            if dir_p == "Up": image = assets.QUEUE_HAUT
            elif dir_p == "Down": image = assets.QUEUE_BAS
            elif dir_p == "Left": image = assets.QUEUE_GAUCHE
            else: image = assets.QUEUE_DROITE

        else:
            if (dir_p in up_right) and (dir_s in up_right): image = assets.ANGLE_NE
            elif (dir_p in down_right) and (dir_s in down_right): image = assets.ANGLE_SE
            elif (dir_p in down_left) and (dir_s in down_left): image = assets.ANGLE_SW
            else: image = assets.ANGLE_NW
        
        resultats.append((coords, image))
        i += 1

    return resultats

def supprimer_elements(can:Canvas):
    can.delete('all')

def afficher_elements(can:Canvas):
    assets:Assets = game["assets"]
    can.create_image(0, 0, anchor=NW, image=assets.MAP)

    corps = quoi_afficher_corps(game["serpent"].corps)
    
    for coords, image in corps:
        x, y = coords
        can.create_image(x, y, image=image)


"""
def apparition_pomme(tab):
    # parcourt le tableau puis créer une liste des coos dispo (=0) puis avec
    # random.choice on choit un x et un y où y'a rien et donc faire pop une pomme

def afficher_pomme(tab):
    # on prend l'emplacement du -1 puis on le mets sur le quadrillage

"""
