import random
from tkinter import NW, Canvas

import core.variables as variables
from core.assets import Assets
from core.classes import Snake


def aff():
    for ligne in variables.tab:
        print(ligne)
    print("-----------------------------------")

def update_score(score:int) -> None:
    """
    Met à jour le score

    Args:
        score (int): score à ajouter
    """
    variables.score += score

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
    variables.tab = creer_tableau(19, 19)

    depart_l, depart_c = variables.DEPART
    depart2_l, depart2_c = variables.DEPART2
    variables.tab[depart_l][depart_c] = 1
    variables.tab[depart2_l][depart2_c] = 1
    
    variables.serpent = Snake(1, variables.DEPART, variables.DEPART2)
    variables.direction = "Up"

    variables.score = 0
    
    apparition_pomme()

def pause():
    variables.pause = not variables.pause

def cote_frames(n:int):
    frame = variables.serpent.corps[n]
    frame_position = frame.position
    frame_suivante_position = frame.suivant
    frame_precedente_position = frame.precedent

    suivante_direction = None
    precedente_direction = None

    lignes_colonnes_count = 18
    oppose_lignes_colonnes_count = -lignes_colonnes_count

    if frame_precedente_position is None: pass
    else:
        diff_l = frame_precedente_position[0]-frame_position[0]
        diff_c = frame_precedente_position[1]-frame_position[1]

        if diff_l == lignes_colonnes_count: precedente_direction = "Up"
        elif diff_l == oppose_lignes_colonnes_count: precedente_direction = "Down"
        elif diff_c == lignes_colonnes_count: precedente_direction = "Left"
        elif diff_c == oppose_lignes_colonnes_count: precedente_direction = "Right"
        elif frame_precedente_position[0] < frame_position[0]: precedente_direction = "Up"
        elif frame_precedente_position[0] > frame_position[0]: precedente_direction = "Down"
        elif frame_precedente_position[1] < frame_position[1]: precedente_direction = "Left"
        else: precedente_direction = "Right"

    if frame_suivante_position is None: pass
    else:
        diff_l = frame_suivante_position[0]-frame_position[0]
        diff_c = frame_suivante_position[1]-frame_position[1]

        if diff_l == lignes_colonnes_count: suivante_direction = "Up"
        elif diff_l == oppose_lignes_colonnes_count: suivante_direction = "Down"
        elif diff_c == lignes_colonnes_count: suivante_direction = "Left"
        elif diff_c == oppose_lignes_colonnes_count: suivante_direction = "Right"
        elif frame_suivante_position[0] < frame_position[0]: suivante_direction = "Up"
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

    variables.direction = direction

def coordonnees():
    tete_position = variables.serpent.corps[0].position
    direction = variables.direction

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
    if l < 0: l = 18
    elif l > 18: l = 0
    elif c < 0: c = 18
    elif c > 18: c = 0

    return (l, c)

def deplacement(can:Canvas):
    if not variables.pause:
        coords = coordonnees()
        collision = variables.serpent.collision(coords, variables.tab)

        if not collision:
            pomme = (-1 == variables.tab[coords[0]][coords[1]])
            variables.serpent.avancer(coords, variables.tab, pomme)
            if pomme:
                apparition_pomme()
                augmenter_difficulte()
                update_score(10*variables.difficulte)
        else:
            print("dead")

        supprimer_elements(can)
        afficher_elements(can)
    can.after(variables.delai, lambda: deplacement(can))

def quoi_afficher_corps(corps):
    resultats = []
    corps_count = len(corps)
    case_pixels = 45
    assets:Assets = variables.assets

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
    case_pixels = 45

    assets:Assets = variables.assets
    can.create_image(0, 0, anchor=NW, image=assets.MAP)

    pomme_ligne, pomme_colonne = variables.pomme
    can.create_image(pomme_colonne*case_pixels, pomme_ligne*case_pixels, anchor=NW, image=assets.POMME)

    corps = quoi_afficher_corps(variables.serpent.corps)
    for coords, image in corps:
        x, y = coords
        can.create_image(x, y, anchor=NW, image=image)
    
    can.create_text(960, 30, text=f"Score: {str(variables.score).zfill(3)}", font=('Fixedsys', 20, 'bold'), justify='left', fill='white', )

def apparition_pomme():
    places = []
    disponnible = 0
    for ligne in range(19):
        for colonne in range(19):
            if variables.tab[ligne][colonne] == disponnible:
                places.append((ligne, colonne))

    pomme_place = random.choice(places)
    ligne, colonne = pomme_place
    variables.tab[ligne][colonne] = -1
    variables.pomme = pomme_place

def augmenter_difficulte():
    future_delai = variables.delai-(variables.difficulte*15)
    if future_delai <= 10:
        variables.delai = 10
    else:
        variables.delai = future_delai
