from tkinter import PhotoImage

class Assets(object):
    """Classe qui représente les paths des assets"""

    def __init__(self) -> None:
        self.MAP = PhotoImage(file="./core/assets/background/map.png")
        self.POMME = PhotoImage(file="./core/assets/pomme.png")

        self.TETE_HAUT = PhotoImage(file="./core/assets/snake/tete/haut.png")
        self.TETE_BAS = PhotoImage(file="./core/assets/snake/tete/bas.png")
        self.TETE_GAUCHE = PhotoImage(file="./core/assets/snake/tete/gauche.png")
        self.TETE_DROITE = PhotoImage(file="./core/assets/snake/tete/droite.png")
        self.CORPS_VERTICAL = PhotoImage(file="./core/assets/snake/corps/vertical.png")
        self.CORPS_HORIZONTAL = PhotoImage(file="./core/assets/snake/corps/horizontal.png")
        self.QUEUE_HAUT = PhotoImage(file="./core/assets/snake/queue/haut.png")
        self.QUEUE_BAS = PhotoImage(file="./core/assets/snake/queue/bas.png")
        self.QUEUE_GAUCHE = PhotoImage(file="./core/assets/snake/queue/gauche.png")
        self.QUEUE_DROITE = PhotoImage(file="./core/assets/snake/queue/droite.png")
        self.ANGLE_NW = PhotoImage(file="./core/assets/snake/angles/nw.png")
        self.ANGLE_NE = PhotoImage(file="./core/assets/snake/angles/ne.png")
        self.ANGLE_SW = PhotoImage(file="./core/assets/snake/angles/sw.png")
        self.ANGLE_SE = PhotoImage(file="./core/assets/snake/angles/se.png")

