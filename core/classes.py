
class SnakeFrame:
    """Cette classe représente un morceau du corps du serpent"""
    def __init__(self, serpent:int, position:tuple[int], precedent:tuple[int], suivant:tuple[int]):
        """
        Args:
            serpent (int): numéro du serpent
            position (tuple[int]): position du morceau dans la grille de jeu
            precedent (tuple[int]): position du morceau précédent
            suivant (tuple[int]): position du morceau suivant
        """
        self.serpent:int = serpent
        self.position:tuple[int] = position
        self.precedent:tuple[int] = precedent
        self.suivant:tuple[int] = suivant

class Snake:
    """Cette classe représente le serpent"""
    def __init__(self, numero:int, position_tete:tuple[int], position_queue:tuple[int]=None):
        """
        Args:
            numero (int): numéro du serpent
            position_tete (tuple[int]): position de la tête du serpent
            position_queue (tuple[int]): position de la queue du serpent
        """
        self.numero:int = numero

        if position_queue is None:
            self.corps = [SnakeFrame(
                serpent=numero,
                position=position_tete,
                precedent=None,
                suivant=None
            )]
        
        else:
            self.corps = [SnakeFrame(
                serpent=numero,
                position=position_tete,
                precedent=None,
                suivant=position_queue
            ),
            SnakeFrame(
                serpent=numero,
                position=position_queue,
                precedent=position_tete,
                suivant=None
            )]
        

    def collision(self, prochaine_position_tete:tuple[int], tab:list[list[int]]):
        """
        Détecte s'il y a une collision

        Args:
            prochaine_position_tete (tuple[int]): prochaine position de la tête
            tab (list[list[int]]): tableau du jeu

        Returns:
            True: Il y a une collision
            False: Il n'y a pas de collision
        """
        return tab[prochaine_position_tete[0]][prochaine_position_tete[1]] not in [-1, 0]

    def avancer(self, nouvelle_position_tete:tuple[int], tab:list[list[int]], agrandir:bool=False):
        """
        Fonction qui sert à faire avancer le corps du serpent en modifiant son corps
        mais aussi en modifiant le tableau de jeu. On part du principe que la
        méthode collision a été utilisée et qu'il n'y pas de collision.

        Args:
            nouvelle_position_tete (tuple[int]): Nouvelle position de la tête
            tab (list[list[int]]): Tableau du jeu
            agrandir (bool, optional): True si on souhaite agrandir le serpent, False sinon (par défaut)
        """
        # On modifie l'ancienne tête
        self.corps[0].precedent = nouvelle_position_tete

        # On place la nouvelle tête au debut de la liste représentant lecorps du serpent
        self.corps.insert(0, SnakeFrame(
            serpent=self.numero,
            precedent=None,
            suivant=self.corps[0].position
        ))
        # Et dans le tableau de jeu
        tab[nouvelle_position_tete[0]][nouvelle_position_tete[1]] = self.numero
        
        # Si le serpent ne doit pas grandir, la queue doit être supprimée, donc le
        # dernier élément de la liste représentant le corps du serpent
        if not agrandir:
            # On supprime la queue du corps
            queue = self.corps.pop()
            self.corps[-1].suivant = None
            # On modifie le tableau de jeu aussi
            tab[queue.position[0]][queue.position[1]] = 0

    