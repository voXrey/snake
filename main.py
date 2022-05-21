from core.classes import Snake
import core.view as view
import core.functions as functions

DEPART = (15, 10)

# Création du tableau et du serpent
tab = functions.creer_tableau(20, 20)
tab[DEPART[0]][DEPART[1]] = 1
serpent = Snake(1, DEPART)

# Création de la fenêtre et du canvas
fen = view.creer_fenetre()
can = view.creer_canvas(1000, 1000, fen)

# On lance la fenêtre
fen.mainloop()