import pygame, random, sys

from models import *

from pygame.locals import*
pygame.init()

pygame.display.set_caption("Fly High")

WINDOW_SIZE = (400, 800)
FPS = 60

clock = pygame.time.Clock()
WIN = pygame.display.set_mode(WINDOW_SIZE)

moving_right = False
moving_left = False

game_loop = False
infinte_mode = False
timer_mode = False

display_menu = False
start_menu = True
mode_selected = False
timer_menu = False 
enter_menu = False

game_font_small = pygame.font.Font('fonts/NONSTOP.TTF', 30)
game_font_medium = pygame.font.Font('fonts/NONSTOP.TTF', 40)
game_font_big = pygame.font.Font('fonts/NONSTOP.TTF', 80)
game_font_large = pygame.font.Font('fonts/NONSTOP.TTF', 100)
logo_font = pygame.font.Font('fonts/blox-brk.regular.ttf', 90)

# Scores

postion_reset = False

infinte_score = 0
timer_60_score = 0
timer_120_score = 0
timer_180_score = 0
timer_240_score = 0
timer_300_score = 0

infinte_high_score = 0
timer_60_high_score = 0
timer_120_high_score = 0
timer_180_high_score = 0
timer_240_high_score = 0
timer_300_high_score = 0

score_60 = False
score_120 = False
score_180 = False
score_240 = False
score_300 = False

timer = None

seed_x = [50, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350]
seed_y = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 640, 680, 690, 700]

random_seed_x = random.choice(seed_x)
random_seed_y = random.choice(seed_y)

random_posion_seed_x = random.choice(seed_x)
random_posion_seed_y = random.choice(seed_y)

player_location = [200, 50]
seed_location = [random_seed_x, random_seed_y]
posion_seed_location = [random_posion_seed_x, random_posion_seed_y]
player_y_speed = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player.get_width(), player.get_height())
seed_rect = pygame.Rect(seed_location[0], seed_location[1], seed.get_width(), seed.get_height())
posion_seed_rect = pygame.Rect(posion_seed_location[0], posion_seed_location[1], posion_seed.get_width(), posion_seed.get_height())

# Resume Menu
resume_surface = game_font_small.render("RESUME", True, (255, 255, 255))
resume_rect = resume_surface.get_rect(center = (80, 730))

# Start Menu
start_surface = game_font_medium.render("START", True, (255, 255, 255))
start_rect = start_surface.get_rect(center = (200, 730))

# Exit menu
exit_surface = game_font_small.render("EXIT", True, (255, 255, 255))
exit_rect = exit_surface.get_rect(center = (340, 730))

# Logo Menu
logo_surface = logo_font.render("fly high", True, (255, 255, 255))
logo_rect = logo_surface.get_rect(center = (200, 200),)

infinte_surface = game_font_small.render("Infinte", True, (255, 255, 255))
infinte_rect = infinte_surface.get_rect(center = (120, 450))

timer_surface = game_font_small.render("Timer", True, (255, 255, 255))
timer_rect = timer_surface.get_rect(center = (120, 600))

mode_surface = game_font_small.render("Mode Not Selected", True, (255, 255, 255))
mode_rect = mode_surface.get_rect(center = (200, 300))

while True:

      print(player_y_speed)

      WIN.fill((14, 209, 69))

      WIN.blit(background, (0, 0))

      if infinte_score > infinte_high_score:
            infinte_high_score = infinte_score

      if timer_60_score > timer_60_high_score:
            timer_60_high_score = timer_60_score

      if timer_120_score > timer_120_high_score:
            timer_120_high_score = timer_120_score

      if timer_180_score > timer_180_high_score:
            timer_180_high_score = timer_180_score

      if timer_240_score > timer_240_high_score:
            timer_240_high_score = timer_240_score
            
      if timer_300_score > timer_300_high_score:
            timer_300_high_score = timer_300_score
      
      if game_loop == True:
            if infinte_mode == True:
                  game_score_surface = game_font_large.render(str(int(infinte_score)),True,(255,255,255))
                  game_score_rect = game_score_surface.get_rect(center = (200, 400),)
                  WIN.blit(game_score_surface, game_score_rect)

            if timer_mode == True:

                  game_score_surface = game_font_large.render(f"{int(timer_60_score)}",True,(255,255,255))
                  game_score_rect = game_score_surface.get_rect(center = (200, 400),)

                  if score_60 == True:
                        game_score_surface = game_font_large.render(f"{int(timer_60_score)}",True,(255,255,255))
                  if score_120 == True:
                        game_score_surface = game_font_large.render(f"{int(timer_120_score)}",True,(255,255,255))
                  if score_180 == True:
                        game_score_surface = game_font_large.render(f"{int(timer_180_score)}",True,(255,255,255))
                  if score_240 == True:
                        game_score_surface = game_font_large.render(f"{int(timer_240_score)}",True,(255,255,255))
                  if score_300 == True:
                        game_score_surface = game_font_large.render(f"{int(timer_300_score)}",True,(255,255,255))
                  
                  menu_score_surface = game_font_medium.render(f"{int(timer)}", True, (255, 255, 255))
                  menu_score_rect = menu_score_surface.get_rect(center = (50, 50))
                  WIN.blit(menu_score_surface, menu_score_rect)
                  WIN.blit(game_score_surface, game_score_rect)

      if game_loop == False:
            WIN.blit(logo_surface, logo_rect)
            
            high_score_surface = game_font_big.render(f"{int(infinte_high_score)}", True, (255, 255, 255))
            high_score_rect = high_score_surface.get_rect(center = (300, 380))
            WIN.blit(high_score_surface, high_score_rect)

            best_text_surface = game_font_small.render("Best", True, (255, 255, 255))
            best_text_rect = best_text_surface.get_rect(center = (300, 450))
            WIN.blit(best_text_surface, best_text_rect)

            if start_menu == True:
                  high_score_surface = game_font_big.render("N/A", True, (255, 255, 255))
                  high_score_rect = high_score_surface.get_rect(center = (300, 530))

            if score_60 == True:
                  high_score_surface = game_font_big.render(f"{int(timer_60_high_score)}", True, (255, 255, 255))
                  high_score_rect = high_score_surface.get_rect(center = (300, 530))
            if score_120 == True:
                  high_score_surface = game_font_big.render(f"{int(timer_120_high_score)}", True, (255, 255, 255))
                  high_score_rect = high_score_surface.get_rect(center = (300, 530))
            if score_180 == True:
                  high_score_surface = game_font_big.render(f"{int(timer_180_high_score)}", True, (255, 255, 255))
                  high_score_rect = high_score_surface.get_rect(center = (300, 530))
            if score_240 == True:
                  high_score_surface = game_font_big.render(f"{int(timer_240_high_score)}", True, (255, 255, 255))
                  high_score_rect = high_score_surface.get_rect(center = (300, 530))
            if score_300 == True:
                  high_score_surface = game_font_big.render(f"{int(timer_300_high_score)}", True, (255, 255, 255))
                  high_score_rect = high_score_surface.get_rect(center = (300, 530))

            best_text_surface = game_font_small.render("Best", True, (255, 255, 255))
            best_text_rect = best_text_surface.get_rect(center = (300, 600))
            WIN.blit(best_text_surface, best_text_rect)
            WIN.blit(high_score_surface, high_score_rect)

            if infinte_mode == False:
                  if timer_menu == True:
                        if start_menu == True:
                              WIN.blit(sec_60, (100, 630))
                              WIN.blit(sec_120, (140, 630))
                              WIN.blit(sec_180, (180, 630))
                              WIN.blit(sec_240, (220, 630))
                              WIN.blit(sec_300, (260, 630))                           
                  else:
                        timer_menu == False

      if postion_reset == True:
            random_seed_x = random.choice(seed_x)
            random_seed_y = random.choice(seed_y)

            random_posion_seed_x = random.choice(seed_x)
            random_posion_seed_y = random.choice(seed_y)

            seed_location = [random_seed_x, random_seed_y]
            posion_seed_location = [random_posion_seed_x, random_posion_seed_y]

            seed_rect = pygame.Rect(seed_location[0], seed_location[1], seed.get_width(), seed.get_height())
            posion_seed_rect = pygame.Rect(posion_seed_location[0], posion_seed_location[1], posion_seed.get_width(), posion_seed.get_height())
      
      if infinte_mode == True:
            if start_menu == False:
                  if game_loop == False:
                        menu_score_surface = game_font_big.render(f"{int(infinte_score)}", True, (255, 255, 255))
                        menu_score_rect = menu_score_surface.get_rect(center = (100, 380))
                        WIN.blit(menu_score_surface, menu_score_rect)

                        score_text_surface = game_font_small.render("Score", True, (255, 255, 255))
                        score_text_rect = score_text_surface.get_rect(center = (100, 450))
                        WIN.blit(score_text_surface, score_text_rect)

      if timer_mode == True:
            if start_menu == False:
                  if game_loop == False:
                        menu_score_surface = game_font_big.render(f"{int(timer_60_score)}", True, (255, 255, 255))
                        menu_score_rect = menu_score_surface.get_rect(center = (100, 530))
                        WIN.blit(menu_score_surface, menu_score_rect)

                        score_text_surface = game_font_small.render("Score", True, (255, 255, 255))
                        score_text_rect = score_text_surface.get_rect(center = (100, 600))
                        WIN.blit(score_text_surface, score_text_rect)

      if start_menu == True:
            if game_loop == False:
                  display_menu = False
                  WIN.blit(start_surface, start_rect)
                  WIN.blit(spacebar, (160, 730))

                  WIN.blit(infinte, (85, 350))
                  WIN.blit(timer_pic, (85, 500))
                  WIN.blit(infinte_surface, infinte_rect)
                  WIN.blit(timer_surface, timer_rect)

                  if infinte_mode == True:
                        infinte = pygame.transform.scale(infinte_image, (70, 70))
                        WIN.blit(infinte, (85, 350))
                  else:
                        infinte = pygame.transform.scale(infinte_image, (64, 64))
                        WIN.blit(infinte, (85, 350))

                  if timer_mode == True:
                        timer_menu = True
                        timer_pic = pygame.transform.scale(timer_image, (70, 70))
                        WIN.blit(timer_pic, (85, 500))
                  else:
                        timer_menu = False
                        timer_pic = pygame.transform.scale(timer_image, (64, 64))
                        WIN.blit(timer_pic, (85, 500))

                  if mode_selected == False:
                        WIN.blit(mode_surface, mode_rect)

      if display_menu == True:
            WIN.blit(resume_surface, resume_rect)
            WIN.blit(spacebar, (40, 730))

            WIN.blit(exit_surface, exit_rect)
            WIN.blit(enter, (305, 745))
      else:
            start_menu == True
      
      if timer == 0:
            enter_menu = True
            mode_selected = False
            game_loop = False
            timer_menu = False
            timer = None
      
      if enter_menu == True:
            exit_surface = game_font_small.render("EXIT", True, (255, 255, 255))
            exit_rect = exit_surface.get_rect(center = (200, 700))
            WIN.blit(exit_surface, exit_rect)
            WIN.blit(enter, (165, 730))
      
      if timer == None:
            mode_selected == False

      
      for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()

            if event.type == KEYDOWN:
                  if game_loop == False:
                        
                        if event.key == K_SPACE:
                              if mode_selected == True:
                                    game_loop = True
                                    display_menu = False
                                    start_menu = False
                              
                        if start_menu == False:
                              if event.key == K_RETURN:
                                    game_loop = False
                                    timer = None
                                    enter_menu = False
                                    display_menu = False
                                    infinte_mode = False
                                    timer_mode = False
                                    timer_menu = False
                                    mode_selected = False
                                    start_menu = True
                                    infinte_score = 0
                                    timer_60_score = 0
                                    timer_120_score = 0
                                    timer_180_score = 0
                                    timer_240_score = 0
                                    timer_300_score = 0
                                    score_60 = False
                                    score_120 = False
                                    score_180 = False
                                    score_240 = False
                                    score_300 = False
                                    player_location = [200, 50]
                                    player_y_speed = 0
                              
                        if timer_menu == True:
                              if event.key == K_1:
                                    timer = 60 
                                    mode_selected = True
                                    score_60 = True
                                    score_120 = False
                                    score_180 = False
                                    score_240 = False
                                    score_300 = False

                                    sec_60 = pygame.transform.scale(sec_60_image, (35, 35))
                              else:
                                    sec_60 = pygame.transform.scale(sec_60_image, (32, 32))
                                    

                              if event.key == K_2:
                                    timer = 120  
                                    score_60 = False
                                    score_120 = True
                                    score_180 = False
                                    score_240 = False
                                    score_300 = False
                                    mode_selected = True

                                    sec_120 = pygame.transform.scale(sec_120_image, (35, 35))
                              else:
                                    sec_120 = pygame.transform.scale(sec_120_image, (32, 32))
                                    

                              if event.key == K_3:
                                    timer = 180 
                                    score_60 = False
                                    score_120 = False
                                    score_180 = True
                                    score_240 = False
                                    score_300 = False
                                    mode_selected = True

                                    sec_180 = pygame.transform.scale(sec_180_image, (35, 35))
                              else:
                                    sec_180 = pygame.transform.scale(sec_180_image, (32, 32))
                                    

                              if event.key == K_4:
                                    timer = 240 
                                    score_60 = False
                                    score_120 = False
                                    score_180 = False
                                    score_240 = True
                                    score_300 = False
                                    mode_selected = True
                                    
                                    sec_240 = pygame.transform.scale(sec_240_image, (35, 35))
                              else:
                                    sec_240 = pygame.transform.scale(sec_240_image, (32, 32))
                                    

                              if event.key == K_5:
                                    timer = 300 
                                    score_60 = False
                                    score_120 = False
                                    score_180 = False
                                    score_240 = False
                                    score_300 = True
                                    mode_selected = True

                                    sec_300 = pygame.transform.scale(sec_300_image, (35, 35))
                              else:
                                    sec_300 = pygame.transform.scale(sec_300_image, (32, 32))

                        if event.key == K_t:
                              score_60 = False
                              score_120 = False
                              score_180 = False
                              score_240 = False
                              score_300 = False
                              timer_mode = True
                              timer_menu = True
                              infinte_mode = False
                              mode_selected = False

                        if event.key == K_i:
                              mode_selected = True
                              infinte_mode = True
                              timer_mode = False
                              time_menu = False
                              score_60 = False
                              score_120 = False
                              score_180 = False
                              score_240 = False
                              score_300 = False
                              timer = None
                                    

                  if event.key == K_ESCAPE:
                        game_loop = False
                        display_menu = True
                              
                  if event.key == K_RIGHT:
                        moving_right = True
                  if event.key == K_LEFT:
                        moving_left = True

            if event.type == KEYUP:
                  if event.key == K_RIGHT:
                        moving_right = False
                  if event.key == K_LEFT:
                        moving_left = False

            if timer_menu == True:
                  if game_loop == True:
                        timer_speed = pygame.USEREVENT
                        pygame.time.set_timer(timer_speed, 500) 
                        if event.type == timer_speed:
                              timer -= 1
# ------------------------------------------------------------------------------------------------------ !!!!!!!!!!!!!!!!!!!!!
      if game_loop == True:

            WIN.blit(esc, (5, 730))
            WIN.blit(player, player_location)
            WIN.blit(seed, seed_location)
            WIN.blit(posion_seed, posion_seed_location)
                  
            if player_location[1] > WINDOW_SIZE[1]-player.get_height():
                  player_y_speed = -player_y_speed
            else:
                  player_y_speed += 0.2
            player_location[1] += player_y_speed

            if player_location[0] > 450:
                  player_location[0] -= 500
            if player_location[0] < -50:
                  player_location[0] += 450
            
            if moving_right == True:
                  player_location[0] += 4
                  player = player_right
            if moving_left == True:
                  player_location[0] -= 4
                  player = player_left
            
            player_rect.x = player_location[0]
            player_rect.y = player_location[1]

            if player_rect.colliderect(seed_rect):
                  if infinte_mode == True:
                        infinte_score += 1
                  if timer_mode == True:
                        if score_60 == True:
                              timer_60_score += 1
                        if score_120 == True:
                              timer_120_score += 1
                        if score_180 == True:
                              timer_180_score += 1
                        if score_240 == True:
                              timer_240_score += 1
                        if score_300 == True:
                              timer_300_score += 1

                  random_seed_x = random.choice(seed_x)
                  random_seed_y = random.choice(seed_y)

                  random_posion_seed_x = random.choice(seed_x)
                  random_posion_seed_y = random.choice(seed_y)

                  seed_location = [random_seed_x, random_seed_y]
                  posion_seed_location = [random_posion_seed_x, random_posion_seed_y]

                  seed_rect = pygame.Rect(seed_location[0], seed_location[1], seed.get_width(), seed.get_height())
                  posion_seed_rect = pygame.Rect(posion_seed_location[0], posion_seed_location[1], posion_seed.get_width(), posion_seed.get_height())

                  WIN.blit(seed, seed_location)
                  WIN.blit(posion_seed, seed_location)

            if player_rect.colliderect(posion_seed_rect):
                  game_loop = False
                  timer = None
                  enter_menu = False
                  display_menu = False
                  infinte_mode = False
                  timer_mode = False
                  timer_menu = False
                  mode_selected = False
                  start_menu = True
                  infinte_score = 0
                  timer_60_score = 0
                  timer_120_score = 0
                  timer_180_score = 0
                  timer_240_score = 0
                  timer_300_score = 0
                  score_60 = False
                  score_120 = False
                  score_180 = False
                  score_240 = False
                  score_300 = False
                  player_location = [200, 50]
                  player_y_speed = 0

      pygame.display.update()
      clock.tick(FPS)