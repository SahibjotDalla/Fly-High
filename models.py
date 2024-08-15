import pygame

player_image_left = pygame.image.load('images/player_left.png')
player_left = pygame.transform.scale(player_image_left, (28, 28))

player_image_right = pygame.image.load('images/player_right.png')
player_right = pygame.transform.scale(player_image_right, (28, 28))

player = player_left

seed_image = pygame.image.load('images/seed.png')
seed = pygame.transform.scale(seed_image, (15, 15))

posion_seed_image = pygame.image.load('images/posion_seed.png')
posion_seed = pygame.transform.scale(posion_seed_image, (15, 15))

background_image = pygame.image.load('images/background.png')
background = pygame.transform.scale(background_image, (400, 800))

spacebar_image = pygame.image.load('images/space.png')
spacebar = pygame.transform.scale(spacebar_image, (80, 80))

enter_image = pygame.image.load('images/enter.png')
enter = pygame.transform.scale(enter_image, (64, 64))

esc_image = pygame.image.load('images/esc.png')
esc = pygame.transform.scale(esc_image, (64, 64))

infinte_image = pygame.image.load('images/I_key.png')
infinte = pygame.transform.scale(infinte_image, (64, 64))

timer_image = pygame.image.load('images/T_key.png')
timer_pic = pygame.transform.scale(timer_image, (64, 64))

sec_60_image = pygame.image.load('images/60_sec.png')
sec_60 = pygame.transform.scale(sec_60_image, (32, 32))

sec_120_image = pygame.image.load('images/120_sec.png')
sec_120 = pygame.transform.scale(sec_120_image, (32, 32))

sec_180_image = pygame.image.load('images/180_sec.png')
sec_180 = pygame.transform.scale(sec_180_image, (32, 32))

sec_240_image = pygame.image.load('images/240_sec.png')
sec_240 = pygame.transform.scale(sec_240_image, (32, 32))

sec_300_image = pygame.image.load('images/300_sec.png')
sec_300 = pygame.transform.scale(sec_300_image, (32, 32))

sec_60 = pygame.transform.scale(sec_60_image, (32, 32))
sec_120 = pygame.transform.scale(sec_120_image, (32, 32))
sec_180 = pygame.transform.scale(sec_180_image, (32, 32))
sec_240 = pygame.transform.scale(sec_240_image, (32, 32))
sec_300 = pygame.transform.scale(sec_300_image, (32, 32))