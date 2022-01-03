##### Victor Avenel & Grégory Haton - Groupe 9

---

### Tout est possible,

### Tout est réalisable,

# c'est  **LE JEU DE LA VIE!**

## Règles:

Le jeu se déroule sur une grille à deux dimensions (matrice) dont les cases sont appelées « cellules », par analogie avec les cellules vivantes.

Chaque cellule peut  prendre deux états distincts : « **vivante** » ou « **morte** » (1 ou 0).

Une cellule possède **huit voisins**, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement.

À chaque itération, l'état d’une cellule est entièrement déterminé par l’état de ses huit cellules voisines, selon les règles suivantes :

- une cellule **morte** possédant exactement trois cellules voisines vivantes devient vivante
- une cellule **vivante** possédant deux ou trois cellules voisines vivantes le reste, sinon elle meurt

---

## Utilisation du programme:

### Étape N°1: Géneration de la grille:

Pour commencer, il est nécéssaire de choisir la taille de notre grille. Pour cela, on execute le  fichier main.py avec comme arguments le nombre de lignes, de colonnes et le pourcentage de cellules vivantes lors de la première itération:

```shell
python3 main.py {nbr_lignes} {nbr_colonnes} {pourcentage}
```

```shell
python3 main.py 8 2 40
```

⚠️ La valeur par defaut des lignes / colonnes est de **20** en l'absence de valeurs choisies par l'utilisateur.

⚠️ La valeur par defaut de la proportion de cellules vivantes est de **30%** en l'absence de valeurs choisies par l'utilisateur.

si le programme est exécuté avec l'option '-c', la grille personnalisée présente dans main.py sera utilisée.

```python
python3 main.py -c
```

Lors de l'éxecution du programme, il est possible de faire varier **la vitesse d'affichage** en appuyant sur la touche **ENTRER**.
La **couleur** des cellules vivantes peut varier grâce à la **barre d'espace**.

## Compréhension du code:

#### Partie 1 - Mise en place des grilles de jeu:

Nous avons mis en place 2 implémentations pour la création des grilles à l'aide de la bibliothèque **numpy**:

La première, est un **array** classique.

La seconde, utilise la fonction **zeros** de **numpy** afin de créer une grille remplie de 0 aux bonnes dimensions qui ont été récupérées via **argv** de la bibliothèque **sys.**

```python
size_lin = int(sys.argv[1])
size_col = int(sys.argv[2])
density = int(sys.argv[3])
```

``` python⚠
array = np.zeros((lin, col), dtype=int)
```

Pour remplir le tableau aléatoire avec la bonne densité de 0, nous avons parcouru le tableau en intégralité en remplacant certains 0 par des 1. Grâce à **randint** de la bibliothèque **random**, nous avons remplacé les 0 lorsque le chiffre obtenu est inférieur à notre densité.

```python
r = random.randint(1, 101)
if r <= density and cpt <= ((lin * col) * density / 100 ):
    array[i][j] = 1
```

⚠️ À noter que cette technique manque de précision pour les tableaux contenants peu de valeurs mais reste suffisament éfficace pour notre utilisation. (Loi des grands nombres)

Afin d'afficher le plus proprement possible les figures du Jeu de la vie, nous avons dû ajouter une bordure autour de notre tableau précédemment crée. (merci de nous avoir fourni cette partie)

#### Partie 2 - Gestion des règles du jeu de la vie

Cette partie est divisée en 2 sous parties relativement faciles à mettre en place:

* Le comptage du nombre de voisins de chaque case

  ```python
  for i in range(index_line - 1, index_line + 2):
  		for j in range(index_column - 1, index_column + 2):
  			number_neighbors += paded_frame[i][j]
  			number_neighbors -= paded_frame[index_line][index_column]
  ```
* L'application des règles du JDV.

```python
if array[i][j] == 0 and number_neighbors == 3:
	cp_array[i][j] = 1
elif array[i][j] == 1 and (number_neighbors == 2 or number_neighbors == 3):
	cp_array[i][j] = 1
else:
	continue
```

#### Partie 4 - Affichage via Pygame:

Cette partie a été la plus difficile du programme,

Premièrement car nous n'avions jamais ou très peu utilisé cette immense bibliothèque et deuxiemement car les syntaxes de ces fonctions sont très différentes de celles disponibles par défault dans Python ou dans d'autres bibliothèques comme numpy.

* Initialisation de la fenêtre:

  ```python
  pg.init()
  pg.display.set_caption('Jeu de la vie')
  ```

  ```python
  screen = pg.display.set_mode((screen_height, screen_width))
  ```
* Affichage du tableau:

  ```python
  surface = pg.surfarray.make_surface(colors[array])
  surface = pg.transform.scale(surface, (size_lin * size_pixel, size_col * size_pixel))
  ```

  **transform.scale** est important afin de voir la grille correctement sachant qu'une cellule = un pixel par defaut

  ```screen.fill((30,
  screen.blit(surface, (0,0))
  pg.display.flip()
  pg.display.flip()
  ```

  ⚠️ A noter que pygame utilise un point d'origine différent que ce que l'on s'attent à avoir en regardant notre tableau. il est donc nécéssaire de réaliser une rotation de 90° pour afficher le tableau dans le bon sens.

  ```python
  surface = pg.transform.rotate(surface, -90)

  ```

  On utilise aussi la fonction **time.clock** de pygame pour afficher proprement la grille. On évite comme cela les clignotements lorsque le programme affiche la grille morceau par morceau.

  ```python
  clock = pg.time.Clock()
  clock.tick(60)
  ```
* **Gestion des raccourcis clavier:**

  **On utilise event.type de pygame pour lire les évènements liés aux périphériques de l'ordinateur:**

  * **QUIT pour le clique sur le bouton de fermeture**
  * **KEYDOWN pour les touches du clavier**

## Problèmes rencontrés:

* L'utilisation de pygame, nottament à cause des grosses différences entre la version 1 et 2 qui rendent plus difficile la recherche d'exemples (ex: les fonctions liées aux touches du clavier).
  Les erreurs renvoyées par pygame ne sont pas toujours très explicites et parfois même renvoient des erreurs complètement différentes du problème réellement rencontré.
* L'organisation du code afin de le rendre lisible facilement a été et est une tâche relativement difficile, certaines parties du code sont relativement longues et très denses. Pouvoir et savoir diviser correctement le programme en sous fichiers organisés rend la lecture plus facile mais nécessite un travail supplémentaire pour implémenter chaque fonction au lieu de simplement écrire les instructions les unes après les autres.
* L'absence de tests unitaires pour controler le fonctionnement de certaines fonctions (ex: remplissage du tableau aléatoire). Cela à ralenti notre travail lors des premiers jours.

## Liste de paterns sympathiques:

```python
densité maximale:

python3 20 20 100
```

```
la grenouille:

[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]

```

```python
La fleur:

[
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

```

## TODO:

Ci-dessous, les élements que l'ont aurait aimé ajouter en plus dans notre programme ou ce qui aurait pu être amélioré:

* la fonction **change_color** ne fonctionne pas correctement, l'implémentation se situe donc directement dans le main == peu lisible
* Ajouter un systeme afin de créer une grille aléatoire via la fenêtre de pygame
* Ajouter un menu pour remplacer les raccourcis clavier du changement de vitesse, de couleur ainsi que de supprimer les arguments de lancement qui sont certes fonctionnels mais peu pratiques à utiliser.
* Parfois, les figurent débordent sur la bordure ce qui les effaces. Il aurait été intéréssant de pouvoir faire varier dynamiquement la taille du tableau pour l'aggrandire lorsque cela est nécessaire afin d'empecher ce problème d'arriver.
