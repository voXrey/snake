

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

def collision(position_tete:tuple[int], tab:list[list]) -> bool:
    """
    Savoir si le serpent entre en collision avec
    autre chose qu'une pomme

    Args:
        position_tete (tuple[int]): nouvelle position de la tête
        tab (list[list]): tableau du jeu

    Returns:
        bool: `True` si il entre en collision, `False` si non
    """
    ligne, colonne = position_tete
    return tab[ligne][colonne] not in [0, 1]

def corps_serpent(position_tete:tuple[int], tab:list[list]) -> list[tuple]:
    """
    Récupère toutes les positions (x, y) du corps du serpent
    en comptant la tête

    Args:
        position_tete (tuple[int]): position de la tête
        tab (list[list]): tableau du jeu

    Returns:
        list[tuple]: positions du corps
    """
    corps = [position_tete]
    while True:
        position_precedent = corps[-1]
        ligne_precedent, colonne_precedent = position_precedent

        position = tab[ligne_precedent][colonne_precedent][2]
        ligne, colonne = position

        suivant = tab[ligne][colonne][2]
        corps.append(position)
        if suivant is None: break
    return corps
    
'''
TO TEST
t = [
    [0, (1, None, (1, 1)), 1],
    [0, (1, (0, 1), (2, 1)), ()],
    [0, (1, (1, 1), (2, 2)), (1, (2, 1), None)],
]
'''