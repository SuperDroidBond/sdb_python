import pygame, sys
from pygame.locals import *

pygame.mixer.pre_init()
pygame.init()

clock = pygame.time.Clock()
screen_size = [360, 640]
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption('SDB SpaceShip')

background = pygame.image.load("background.png")
debris = pygame.image.load('debris2_brown.png')

#planet = pygame.image.load("one.png")
planets = ['one.png', 'two.png', 'three.png']
p_index = 0
planet = pygame.image.load(planets[p_index])

spaceship = pygame.image.load("spaceship.png")
spaceship_x = 160
spaceship_direction = 'right'

bullet = pygame.image.load('bullet.png')
fired = False
bullet_x = 180
bullet_y = 465

planet_x = 140
move_direction = 'right'
time = 0
game_over = False

boom = pygame.image.load("boom.png")

#collision sound
explosion_sound = pygame.mixer.Sound('explosion.ogg')
explosion_sound.set_volume(0.5)

def game_win():
	screen.blit(background, [0, 0])
	screen.blit(debris,(time*.3,0))
	screen.blit(debris,(time*.3-360,0))

# Main Game Logic
def game_logic():
	global move_direction
	global time
	global spaceship_direction
	global game_over
	global planet_x
	global spaceship_x
	global bullet_x
	global bullet_y
	global planet
	global p_index
	global planets

	if move_direction == 'right':
		planet_x = planet_x + 5
		if planet_x == 300:
		    move_direction = 'left'
	else:
		planet_x = planet_x - 5
		if planet_x == 0:
			move_direction = 'right'

	screen.blit(planet, [planet_x, 50])

	pygame.event.get()
	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP] == True:
		fired = True
		if fired is True:
			bullet_y -= 5
			if bullet_y <= 50:
				fired = False
				bullet_y = 500

	if keys[pygame.K_LEFT] == True and spaceship_x != 40:
		spaceship_x -= 5
		bullet_x -= 5
		spaceship_direction = 'left'

	if keys[pygame.K_RIGHT] == True and spaceship_x != 320:
		spaceship_x += 5
		bullet_x += 5
		spaceship_direction = 'right'

	screen.blit(spaceship, [spaceship_x, 500])
	screen.blit(bullet, [bullet_x, bullet_y])
	time = time + 1

	if bullet_y < 60 and planet_x > 120 and planet_x < 180:
		p_index += 1
		screen.blit(boom, [130, 50])
		explosion_sound.play()
		if p_index < len(planets):
			planet = pygame.image.load(planets[p_index])
			planet_x = 10
		else:
			game_over = True

#Update Screen
def update_screen():
	pygame.display.update()
	clock.tick(60)

while True:
	pygame.event.get()
	keys = pygame.key.get_pressed()
	game_win()
	if not game_over:
		game_logic()
	else:
		myfont = pygame.font.SysFont("Comic Sans MS", 80)
		label = myfont.render("You WON", 1, (255,255,255))
		screen.blit(label, (55,640/2))
	update_screen()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
