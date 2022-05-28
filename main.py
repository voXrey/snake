import core.functions as functions
import core.variables as variables
import core.view as view
from core.assets import Assets

# Initialise le jeu
functions.commencer()

# Création de la fenêtre
fen = view.creer_fenetre()

# Création des assets
variables.assets = Assets()

# On ajoute les évènements
fen.bind("<Key>", view.touche) # Celui-ci se déclenche quand un touche du clavier est appuyée

# Création du canvas
can = view.creer_canvas(variables.W_CANVAS, variables.H_CANVAS, fen, variables.assets)

# On appelle la fonction de déplacement en boucle
# c'est également elle qui s'occupe des autres
# mises à jour du canvas tel que l'affichage des éléments
fen.after(variables.delai, lambda:functions.deplacement(can))

# On lance la fenêtre
fen.mainloop()
