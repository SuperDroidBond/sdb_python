import pygame

pygame.init()
clock = pygame.time.Clock()
screen_size = [360, 640]
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load("background.png")

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

boom = pygame.image.load("boom.png")

#collision sound
explosion_sound = pygame.mixer.Sound('explosion.ogg')
explosion_sound.set_volume(0.5)

keep_alive = True

while keep_alive:
	screen.blit(background, [0, 0])
	pygame.event.get()
	keys = pygame.key.get_pressed()
	if move_direction == 'right':
		planet_x = planet_x + 5
		if planet_x == 300:
		    move_direction = 'left'
	else:
		planet_x = planet_x - 5
		if planet_x == 0:
			move_direction = 'right'

	#screen.blit(planet, [140, 50])
	screen.blit(planet, [planet_x, 50])

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

	#screen.blit(spaceship, [160, 500])
	screen.blit(spaceship, [spaceship_x, 500])
	#screen.blit(bullet, [180, 465])
	screen.blit(bullet, [bullet_x, bullet_y])

	if bullet_y < 80 and planet_x > 120 and planet_x < 180:
		print('BOOM')
		screen.blit(boom, [130, 50])
		explosion_sound.play()
		p_index += 1
		if p_index < len(planets):
			planet = pygame.image.load(planets[p_index])
			planet_x = 10
		else:
			print("You Won")
			keep_alive = False

	pygame.display.update()
	clock.tick(60)
