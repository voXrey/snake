import random
from tkinter import NW, Canvas

import core.variables as variables
from core.assets import Assets
from core.classes import Snake


def update_score(score:int):
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
    """
    Quitte le jeu en fermant le programme
    """
    exit()

def commencer():
    """
    Initialise le jeu en remettant les variables à 0
    """
    # Créer le tableau
    variables.tab = creer_tableau(19, 19)

    # Créer le serpent
    variables.serpent = Snake(1, variables.DEPART, variables.DEPART2)

    # Préparer la direction par défaut
    variables.direction = "Up"

    # Placer le serpent
    depart_l, depart_c = variables.DEPART
    depart2_l, depart2_c = variables.DEPART2
    variables.tab[depart_l][depart_c] = 1
    variables.tab[depart2_l][depart2_c] = 1

    # Remettre le score à 0
    variables.score = 0

    # Remttre le delai par défaut
    variables.delai = 500
    
    # Définir la position de la pomme
    apparition_pomme()

def pause():
    """
    Met ou enlève la pause du jeu
    """
    variables.pause = not variables.pause

def cote_frames(n:int):
    """
    Détermine de quels côtés d'une frame se trouvent la frame
    précédente et la frame suivante

    Args:
        n (int): index de la frame dans le corps du serpent

    Returns:
        tuple[str]: côtés de la frame précédente et de la frame suivante
    """
    # Déterminer les positions
    frame = variables.serpent.corps[n]
    frame_position = frame.position
    frame_suivante_position = frame.suivant
    frame_precedente_position = frame.precedent

    # Création des variables finales à retourner
    suivante_direction = None
    precedente_direction = None

    # Calcul de l'index maximal et de son opposé
    max_index = variables.LIGNES_COLONNES-1
    oppose_max_index = -max_index

    # Côté de la frame précédente
    if frame_precedente_position is None: pass # On vérifie qu'elle existe
    else:
        # On calcule la différence entre les lignes et colonnes
        # des frames
        diff_l = frame_precedente_position[0]-frame_position[0]
        diff_c = frame_precedente_position[1]-frame_position[1]

        # Si la différence correspond à l'index maximal ou à son opposé
        # alors le serpent à traversé la bordure et les orientations sont
        # inversées
        if diff_l == max_index: precedente_direction = "Up"
        elif diff_l == oppose_max_index: precedente_direction = "Down"
        elif diff_c == max_index: precedente_direction = "Left"
        elif diff_c == oppose_max_index: precedente_direction = "Right"
        # Sinon on cherche l'orientation normalement
        elif frame_precedente_position[0] < frame_position[0]: precedente_direction = "Up"
        elif frame_precedente_position[0] > frame_position[0]: precedente_direction = "Down"
        elif frame_precedente_position[1] < frame_position[1]: precedente_direction = "Left"
        else: precedente_direction = "Right"

    # Côté de la frame suivante
    if frame_suivante_position is None: pass # On vérifie qu'elle existe
    else:
        # On calcule la différence entre les lignes et colonnes
        # des frames
        diff_l = frame_suivante_position[0]-frame_position[0]
        diff_c = frame_suivante_position[1]-frame_position[1]

        # Si la différence correspond à l'index maximal ou à son opposé
        # alors le serpent à traversé la bordure et les orientations sont
        # inversées
        if diff_l == max_index: suivante_direction = "Up"
        elif diff_l == oppose_max_index: suivante_direction = "Down"
        elif diff_c == max_index: suivante_direction = "Left"
        elif diff_c == oppose_max_index: suivante_direction = "Right"
        # Sinon on cherche l'orientation normalement
        elif frame_suivante_position[0] < frame_position[0]: suivante_direction = "Up"
        elif frame_suivante_position[0] > frame_position[0]: suivante_direction = "Down"
        elif frame_suivante_position[1] < frame_position[1]: suivante_direction = "Left"
        else: suivante_direction = "Right"

    return (precedente_direction, suivante_direction)

def changer_direction(direction:str):
    """
    Cette fonction est appelée pour changer
    la direction actuelle vers laquelle se
    dirige le serpent

    Args:
        direction (str): nouvelle direction
    """
    # On regarde de quel côté se trouve la frame suivant la tête
    cotes = cote_frames(0)
    cote = cotes[1]

    if direction == cote:
        # Si la nouvelle direction va vers la frame
        # suivante on ne fait rien
        pass
    else:
        # Sinon on change la direction
        variables.direction = direction

def coordonnees():
    """
    Détermine en fonction de la direction vers laquelle
    va le serpent les coordonnées de la prochaine position de sa tête

    Returns:
        tuple[int]: ligne et colonne 
    """
    # On détermine la position de la tête du serpent et
    # de la direction vers laquelle va ce dernier
    tete_position = variables.serpent.corps[0].position
    direction = variables.direction

    # On détermine temporairement la prochaine position
    l, c = tete_position
    if direction == "Up": l -= 1
    elif direction == "Down": l += 1
    elif direction == "Left": c -= 1
    else: c += 1
    
    # On le place de l'autre côté de la map si le serpent la dépasse
    max_index = variables.LIGNES_COLONNES-1
    if l < 0: l = max_index
    elif l > max_index: l = 0
    elif c < 0: c = max_index
    elif c > max_index: c = 0

    return (l, c)

def deplacement(can:Canvas):
    """
    Cette fonction est appelée en boucle pour
    faire déplacer le serpent et mettre à jour le canvas

    Args:
        can (Canvas): canvas principal du jeu
    """
    # Si le jeu est en pause on ne fait rien
    if not variables.pause:
        # Calcul des prochaines coordonnées du serpent
        coords = coordonnees()
        # Déterminer si le serpent entre en collision
        collision = variables.serpent.collision(coords, variables.tab)

        # Déterminer si le serpent a mangé une pomme pour
        # le faire avancer en grandissant ou non
        pomme = (-1 == variables.tab[coords[0]][coords[1]])
        variables.serpent.avancer(coords, variables.tab, pomme)
        if pomme:
            # S'il a mangé une pomme, une autre spawn, le score
            # augmente et le delai diminue pour rendre le
            # jeu plus difficile
            apparition_pomme()
            augmenter_difficulte()
            # Le score ajouté dépend de la difficulté choisie
            update_score(int((10*variables.difficulte)*1.5))
        
        if collision:
            # S'il y a eu une collision met le jeu
            # sur un écran de fin et attend qu'on appuie sur
            # start pour recommencer
            
            # BUG
            # Le code suivant sera à ramplacer
            print(variables.score)
            commencer()
            pause()

        # Mettre à jour les éléments du canvas
        supprimer_elements(can)
        afficher_elements(can)

    # Répéter la fonction après le delai donné
    can.after(variables.delai, lambda: deplacement(can))

def quoi_afficher_corps():
    """
    Détermine quelle image mettre à quelle coordonnées
    pour afficher le serpent

    Returns:
        list[tuple[tuple[int], PhotoImage]]: liste des coordonnées et des images
    """
    # Préparation des variables
    corps = variables.serpent.corps
    resultats = []
    corps_count = len(corps)
    assets:Assets = variables.assets
    # Celles-ci permettent d'économiser des performances mineures
    vertical = ["Up", "Down"]
    horizontal = ["Left", "Right"]
    up_right = ["Up","Right"]
    down_right = ["Down", "Right"]
    down_left = ["Down", "Left"]

    # Lancement de la boucle
    i = 0
    while i < corps_count:
        # Préparation des variables de la boucle
        frame = corps[i]
        position = frame.position
        coords = (position[1]*variables.PIXELS_CASE, position[0]*variables.PIXELS_CASE)
        image = None
        dir_p, dir_s = cote_frames(i)

        # Si la frame est un corps simple on détermine
        # s'il est vertical ou horizontal
        if (dir_p in vertical) and (dir_s in vertical): image = assets.CORPS_VERTICAL
        elif (dir_p in horizontal) and (dir_s in horizontal): image = assets.CORPS_HORIZONTAL
        
        # Si c'est la tête
        elif  dir_p is None:
            if dir_s == "Up": image = assets.TETE_BAS
            elif dir_s == "Down": image = assets.TETE_HAUT
            elif dir_s == "Left": image = assets.TETE_DROITE
            else: image = assets.TETE_GAUCHE

        # Si c'est la queue
        elif dir_s is None:
            if dir_p == "Up": image = assets.QUEUE_HAUT
            elif dir_p == "Down": image = assets.QUEUE_BAS
            elif dir_p == "Left": image = assets.QUEUE_GAUCHE
            else: image = assets.QUEUE_DROITE

        # Sinon c'est un angle
        else:
            if (dir_p in up_right) and (dir_s in up_right): image = assets.ANGLE_NE
            elif (dir_p in down_right) and (dir_s in down_right): image = assets.ANGLE_SE
            elif (dir_p in down_left) and (dir_s in down_left): image = assets.ANGLE_SW
            else: image = assets.ANGLE_NW
        
        # On ajoute les coordonnées et l'image à la liste des résultats
        resultats.append((coords, image))
        i += 1

    return resultats

def supprimer_elements(can:Canvas):
    """
    Supprime tous les éléments du canvas

    Args:
        can (Canvas): canvas principal du jeu
    """
    can.delete('all')

def afficher_elements(can:Canvas):
    """
    Affiche les différents éléments du jeu

    Args:
        can (Canvas): canvas principal du jeu
    """
    # Ajout de la map
    can.create_image(0, 0, anchor=NW, image=variables.assets.MAP)

    # Ajout de la pomme
    pomme_ligne, pomme_colonne = variables.pomme
    can.create_image(
        pomme_colonne*variables.PIXELS_CASE,
        pomme_ligne*variables.PIXELS_CASE,
        anchor=NW,
        image=variables.assets.POMME
    )

    # Ajout du serpent
    corps = quoi_afficher_corps()
    for coords, image in corps:
        x, y = coords
        can.create_image(x, y, anchor=NW, image=image)
    
    # Ajout du score
    can.create_text(
        960,
        30,
        text=f"Score: {str(variables.score).zfill(4)}",
        font=variables.SCORE_FONT,
        justify='left',
        fill='white',
    )

    # Ajout du texte d'informations
    texte = f"""
        Difficulté : {variables.difficulte}

        <S> : Recommencer
        <Q> : Quitter
        <Echap>/<Espace> : Pause

        Utilise les flèches
        de ton clavier
        pour te déplacer
    """
    can.create_text(
        960,
        140,
        text=texte,
        font=variables.INFO_FONT,
        justify='left',
        fill='white',
    )

def apparition_pomme():
    """
    Fait apparaître aléatoirement une pomme
    """
    # Préparation d'une liste qui contiendra toutes
    # les places où pourraient apparaître les pommes
    places = []
    disponnible = 0 # Variable qui contien la valeur représentant une place vide
    for ligne in range(19):
        for colonne in range(19):
            if variables.tab[ligne][colonne] == disponnible:
                places.append((ligne, colonne))

    # Choix aléatoire de la place utilisée
    pomme_place = random.choice(places)
    ligne, colonne = pomme_place
    variables.tab[ligne][colonne] = -1
    variables.pomme = pomme_place

def augmenter_difficulte():
    """
    Augmente la difficultée du jeu en diminuant
    le délai de mise à jour
    """
    # Calcul du futur délai en fonction de la dicculté et du délai actuel
    future_delai = variables.delai-(variables.difficulte*15)
    # Il ne peut être en-dessous de d'un certain seuil
    seuil = (100/variables.difficulte)
    if future_delai <= seuil:
        variables.delai = seuil
    else:
        variables.delai = future_delai
