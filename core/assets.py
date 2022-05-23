class Assets(object):
    """Classe qui représente les paths des assets"""

    MAP = "./core/assets/background/map.png"
    QUADRILLAGE = "./core/assets/background/quadrillage.png"
    POMME = "./core/assets/pomme.png"

    BOUTON_QUITTER = "./core/assets/boutons/quitter.png"
    BOUTON_COMMENCER = "./core/assets/boutons/commencer.png"
    BOUTON_REPRENDRE = "./core/assets/boutons/reprendre.png"
    BOUTON_PAUSE = "./core/assets/boutons/pause.png"

    TETE_HAUT = "./core/assets/snake/tete/haut.png"
    TETE_BAS = "./core/assets/snake/tete/bas.png"
    TETE_GAUCHE = "./core/assets/snake/tete/gauche.png"
    TETE_DROITE = "./core/assets/snake/tete/droite.png"
    CORPS_VERTICAL = "./core/assets/snake/corps/vertical.png"
    CORPS_HORIZONTAL = "./core/assets/snake/corps/horizontal.png"
    QUEUE_HAUT = "./core/assets/snake/queue/haut.png"
    QUEUE_BAS = "./core/assets/snake/queue/bas.png"
    QUEUE_GAUCHE = "./core/assets/snake/queue/gauche.png"
    QUEUE_DROITE = "./core/assets/snake/queue/droite.png"

    def __setattr__(self, *_):
        """Afin de ne pas changer la valeur des variables par erreur"""
        raise Exception("Tried to change the value of a constant")

assets = Assets()