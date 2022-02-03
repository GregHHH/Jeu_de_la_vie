from generate import *

custom_array = np.array([
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
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

def compute_number_neighbors(paded_frame, index_line, index_column):
	number_neighbors = 0
	for i in range(index_line - 1, index_line + 2):
		for j in range(index_column - 1, index_column + 2):
				number_neighbors += paded_frame[i][j]
	number_neighbors -= paded_frame[index_line][index_column]
	return number_neighbors

def add_padding (frame):
	paded_frame = np.pad(frame, 1, mode='constant')
	return paded_frame

def copy_with_rules(array):
	size_lin = len(array)
	size_col = len(array[0])
	cp_array = np.zeros((size_lin, size_col), int)
 	
	# TODO: toute la grille n'est pas visitée à cause du -1 (bordures)
	for i in range(1, size_lin - 1):
		for j in range(1, size_col - 1):
			# On applique les règles du Jeu de la Vie
			number_neighbors = compute_number_neighbors(array, i, j)
			if array[i][j] == 0 and number_neighbors == 3:
				cp_array[i][j] = 1
			elif array[i][j] == 1 and (number_neighbors == 2 or number_neighbors == 3):
				cp_array[i][j] = 1
			else:
				continue
	return cp_array

def print_frame(surface, i):
    screen.fill((30, 30, 30))
    screen.blit(surface, (0,0))
    pg.display.flip()

def change_delay(delay):
	if delay == 1:
		delay = 0.5
	elif delay == 0.5:
		delay = 0.2
	elif delay == 0.2:
		delay = 2
	elif delay == 2:
		delay = 1
	return delay

# def change_color(color_stat):
# 	colors = [0,0,0]

	# if color_stat == 1:
	# 	color_stat = 2
	# 	colors = [255, 17, 0]
	# elif color_stat == 2:
	# 	color_stat = 3
	# 	colors = [4, 255, 0]
	# elif color_stat == 3:
	# 	color_stat = 1
	# 	colors = [21, 0, 255]
	# return (colors, color_stat)

if (sys.argv[1]) == '-c':
	array = custom_array
else:
	size_lin = int(sys.argv[1]) if len(sys.argv) >= 3 else int(20)
	size_col = int(sys.argv[2]) if len(sys.argv) >= 3 else int(20)
	density = int(sys.argv[3]) if len(sys.argv) >= 3 else int(30)
	array = generate(size_lin, size_col, density)
array = add_padding(array)

i = 0

pg.init()
pg.display.set_caption('Jeu de la vie')
clock = pg.time.Clock()

size_lin = len(array)
size_col = len(array[0])
size_pixel = 10

screen_height = size_lin * size_pixel
screen_width = size_col * size_pixel
colors = np.array([[255, 255, 255], [250, 90, 120]]) # couleurs des éléments du tableau en fonction de leur valeur
screen = pg.display.set_mode((screen_height, screen_width)) # création de la fenetre

color_stat = 1
delay = 1

pause = False
running = True
while running:
	for event in pg.event.get():
		if event.type == pg.QUIT: # fermeture de la fenetre avec le bouton fermeture
			running = False

		# On change de couleur en appuyant sur la barre d'espace car c'est rigolo, faut pas chercher plus loin
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_SPACE:
				if color_stat == 1:
					color_stat = 2
					colors[1] = [255, 17, 0]
				elif color_stat == 2:
					color_stat = 3
					colors[1] = [4, 255, 0]
				elif color_stat == 3:
					color_stat = 1
					colors[1] = [21, 0, 255]
				
			if event.key == pg.K_RETURN:
				delay = change_delay(delay)

	surface = pg.surfarray.make_surface(colors[array])
	surface = pg.transform.scale(surface, (size_lin * size_pixel, size_col * size_pixel))
	surface = pg.transform.rotate(surface, -90) # Pygame prend comme origine le coin bas/gauche, notre tableau est représenté en partant du coin haut/gauche.

	print_frame(surface, i)
	time.sleep(delay)
	i+=1
	array = copy_with_rules(array)
	clock.tick(60)
