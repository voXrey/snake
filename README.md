# Snake Project

## Description
Il s’agit d’un jeu classique *« snake »*. Le joueur dirige un serpent qui mange des pommes pour grandir et gagner des points. Si le serpent touche sa queue il meurt. En rentrant dans un mur il ressort par celui opposée.  
Ce jeu est créé dans le cadre d'un projet en groupe de NSI de niveau première.

## Développement
### Technologie
Le jeu sera développé avec le langage **python** (`version 3.9`) et la fenêtre graphique sera créée à partir de la librairie `tkinter`.

### La fenêtre
* La fenêtre mesurera `1000px / 1000px` et la map de déplacement du serpent en fera `900px / 900px` (chaque case représente `45x45 px`)
* Bouton pour le menu pause, score, temps... au dessus de la map

### La Map
* Elle sera modélisée par une liste de listes
* Un 0 signifie que la case est vide
* Un 1 siginifie que la case contient une pomme
* Un tuple sgnifie qu'une partie du serpent est présente

### Le serpent  
* Chaque morceau de serpent est représenté par son numéro dans le tableau (>= 1)  
* Le serpent est représentée par une instance de classe noommée **Snake**, elle est constamment présente dans le programme  
&nbsp; **Attributs:**  
&nbsp; - `corps` : contient le corps du serpent, liste de morceaux de corps  
&nbsp; - `numero` : contient le numéro du serpent (utile si on ajoute un autre serpent  
&nbsp; **Méthodes:**  
&nbsp; - `avancer` : permet de faire avancer le serpent en ajoutant un morceau de corps au débuts de la liste, en supprimant le dernier morceau (si besoin) et en modifiant certains paramètres pour certains morceaux de corps (l'ancien premier et le nouveau dernier), elle modifie également le tableau de jeu  
&nbsp; - `collision` : permet de savoir si le serpent entre en collision (la case de la tête n'est ni vide ni occupée par une pomme)   

* Les morceaux de serpent sont représentés par des instance d'une classe nommée **SnakeFrame**  
&nbsp;  **Attributs:**   
&nbsp; - `position` : position du morceau dans le tableau  
&nbsp; - `serpent` : numéro du serpent auquel ce morceau correspond  
&nbsp; - `suivant` : position du morceau suivant (vers la queue, *None si le morceau est la queue*)  
&nbsp; - `precedent` : position du morceau precedent (vers la tête, *None si le morceau est la tête*)  

## Utilisation

### Dépendances
* Python 3.9

### Pas à pas
*Aucune version n'a encore été publiée*
* Télécharger la dernière version du jeu
* `pip install -r requirements.txt` dans un terminal dans la racine du projet
* Exécuter le fichier `main.py` comme tout fichier python
