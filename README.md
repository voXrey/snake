# Snake Project

## Description
Il s’agit d’un jeu classique *« snake »*. Le joueur dirige un serpent qui mange des pommes pour grandir et gagner des points. Si le serpent touche sa queue il meurt. En rentrant dans un mur il ressort par celui opposée.  
Ce jeu est créé dans le cadre d'un projet en groupe de NSI de niveau première.

## Développement
### Technologie
Le jeu sera développé avec le langage **python** (`version 3.9`) et la fenêtre graphique sera créée à partir de la librairie `tkinter`.

### La fenêtre
* La fenêtre mesurera `1000px / 1000px` et la map de déplacement du serpent en fera `900px / 900px`
* Bouton pour le menu pause, score, temps... au dessus de la map

### La Map
* Elle sera modélisée par une liste de listes
* Un 0 signifie que la case est vide
* Un 1 siginifie que la case contient une pomme
* Un tuple sgnifie qu'une partie du serpent est présente

### Le serpent
* La position de la tête du serpent sera stockée et mise à jour dans le programme
* Le corps entier sera stockée dans la map sous forme de tuple de modèle :  
&nbsp; (`numéro du serpent`, `morceau précédent`, `morceau suivant`)  
&nbsp; **numéro du serpent**: par défaut 1 s'il y a un seul serpent
&nbsp; **morceau précédent**: position du morceau de serpent précédent (vers la tête), `None` si c'est la tête
&nbsp; **morceau suivant**: position du morceau de serpent suivant (vers le bout de la queue) `None` si c'est le bout de la queue

## Utilisation

### Dépendances
* Python 3.9

### Pas à pas
*Aucune version n'a encore été publiée*
* Télécharger la dernière version du jeu
* `pip install -r requirements.txt` dans un terminal dans la racine du projet
* Exécuter le fichier `main.py` comme tout fichier python
