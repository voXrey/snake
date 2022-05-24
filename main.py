from core.classes import Snake
import core.view as view
import core.functions as functions
from core.assets import Assets

# Initialise le jeu
functions.commencer()

# Création de la fenêtre
fen = view.creer_fenetre()

# Création des assets
assets = Assets()

# On ajoute les évènements
fen.bind("<Key>", view.touche)

# Création du canvas
can = view.creer_canvas(900, 1300, fen, assets)

# On lance la fenêtre
fen.mainloop()
