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

def afficher_canva(W, H, fen, can):
    #Crée la base de l'interface
    fen = Tk()
    fen.title("Snake")
    can = Canvas(fen, width=W, height=H, bg = "#24222e")
    quadrillage = PhotoImage(file="background_snake.png")
    can.create_image(0, 0, anchor=NW, image=quadrillage)
    # Crée le bouton quitter
    quitter_button = PhotoImage(file="quitter_button.png")
    can.create_image(800, 100, image=quitter_button)
    # Crée le bouton commencer
    commencer_button = PhotoImage(file="commencer.png")
    can.create_image(800, 200, image=commencer_button)
    # Crée le bouton reprendre
    reprendre_button = PhotoImage(file="reprendre.png")
    can.create_image(800, 300, image=reprendre_button)
    # Crée le bouton pause
    pause_button = PhotoImage(file="pause.png")
    can.create_image(800, 400, image=pause_button)
    # lance l'interface
    can.pack()
    fen.mainloop()

def quitter():
    afficher_canva(fen).quit

def commencer(creer_tableau):
    creer_tableau(20, 20)

def recommencer(creer_tableau):
    creer_tableau(20, 20)
