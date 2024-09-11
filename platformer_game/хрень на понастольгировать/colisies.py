#Ai_vani 100%
from turtle import speed
import pygame
import sys
import time
import random
##from create_sprite import Hero_sprite
pygame.init()
#W = 1500
#H = 900
W = 1300
H = 700
x = W//2
y = H//2
sc = pygame.display.set_mode((W, H))
class Hero_sprite(pygame.sprite.Sprite):
          def __init__(self, x, y, filename):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load(filename).convert_alpha()
                    self.rect = self.image.get_rect(center = (x,y))
sprite_hero_walk_left_1 = Hero_sprite(200,420, 'Data/images/the main character/Player_left_1.png')
sprite_hero_walk_left_1_1 = Hero_sprite(x,y,'Data/images/the main character/Player_left_2.png')
sprite_hero_walk_left_1_2 = Hero_sprite(x,y,'Data/images/the main character/Player_left_3.png')
sprite_hero_walk_left_2 = Hero_sprite(x,y, 'Data/images/the main character/Player_left_3.png')

sprite_hero_stand_1 = Hero_sprite(x,y, 'Data/images/the main character/stand_player.png')

sprite_hero_walk_right_1 = Hero_sprite(x,y, 'Data/images/the main character/Player_right_1.png')
sprite_hero_walk_right_1_1 = Hero_sprite(x,y,'Data/images/the main character/Player_right_2.png')
sprite_hero_walk_right_1_2 = Hero_sprite(x,y,'Data/images/the main character/Player_right_3.png')

sprite_hero_falling_1 = Hero_sprite(x,y,'Data/images/the main character/Player_Falling.png')

sprite_hero_attack_1 = Hero_sprite(x,y, 'Data/images/the main character/attack/Sprite_attack_hero_1.png')
sprite_hero_attack_2 = Hero_sprite(x,y, 'Data/images/the main character/attack/Sprite_attack_hero_2.png')
sprite_hero_attack_3 = Hero_sprite(x,y, 'Data/images/the main character/attack/Sprite_attack_hero_3.png')
sprite_hero_attack_4 = Hero_sprite(x,y, 'Data/images/the main character/attack/Sprite_attack_hero_4.png')
sprite_hero_attack_5 = Hero_sprite(x,y, 'Data/images/the main character/attack/Sprite_attack_hero_5.png')
sprite_hero_attack_6 = Hero_sprite(x,y, 'Data/images/the main character/attack/Sprite_attack_hero_6.png')
sprite_hero_attack_7 = Hero_sprite(x,y, 'Data/images/the main character/attack/Sprite_attack_hero_7.png')
speed_attack_anim = 30
speed_attack_anim_check = 0



walle = pygame.sprite.Group()


wall = Hero_sprite(x-625,y, 'Data/images/walls/wall_vertical_loca_1.png')
wall2 = Hero_sprite(x, y-325, 'Data/images/walls/wall_gorizontal_loca_1.png')
wall3 = Hero_sprite(x+625,y-100, 'Data/images/walls/wall_vertical_loca_pre_exit_1.png')

background_loca_1 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_1.png')
floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_1.png')



walle.add(wall2)
walle.add(floor_loca_1)
walle.add(wall)
walle.add(wall3)



pygame.mixer.music.load('Data/music/music_loca_1.ogg')
pygame.mixer.music.play()
jump_sound = pygame.mixer.Sound('Data/sounds/jump_sound.wav')

FPS = 220
moving = False
location = 1
clock = pygame.time.Clock()      
speed_change_walk = 32
speed_change_walk_check = 0
jump_power = 100#высота прыжка
jump_power_check = 0#проверка высоты прыжка
jumping = False#проверка на прыжок в настоящее время
jumping_wall = False#для коллизии с потолком
falling = False
jumping_wall_check = 0#проверка коллизии с потолком

while 1:
       try:
              for i in pygame.event.get():
                     if i.type == pygame.QUIT:
                            pygame.quit()
              if i.type != pygame.QUIT:
                     keys = pygame.key.get_pressed()
                     pressed = pygame.mouse.get_pressed()
                     if keys[pygame.K_r]:
                               print(sprite_hero_walk_left_1.rect)
                     if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                            sprite_hero_walk_left_2.rect.x -=1
                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                   moving = 'left'
                                   speed_change_walk_check +=1
                                   sprite_hero_walk_left_1.rect.x -= 1
                            else:
                                   sprite_hero_walk_left_2.rect.x +=1




                                    
                     elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                            sprite_hero_walk_left_2.rect.x +=1
                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                   speed_change_walk_check += 1
                                   moving = 'right'
                                   sprite_hero_walk_left_1.rect.x += 1

                            else:
                                   sprite_hero_walk_left_2.rect.x -=1


                    
                     if keys[pygame.K_UP] or jumping == True or keys[pygame.K_w]: 
                            if falling != True:
                                   sprite_hero_walk_left_2.rect.y -=1
                                   if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                          jump_power_check += 1
                                          sprite_hero_walk_left_1.rect.y -=1
                                          jumping = True
                                          if jump_power_check == 1:
                                                    jump_sound.play()
                                          if jump_power_check > jump_power and jump_power_check < jump_power * 2:
                                                 sprite_hero_walk_left_2.rect.y +=2
                                                 if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                                        sprite_hero_walk_left_1.rect.y +=2
                                                 else:
                                                        jump_power_check = 0
                                                        sprite_hero_walk_left_2.rect.y -=1
                                                        jumping = False
                                          elif jump_power_check > jump_power * 2:
                                                 jump_power_check = 0
                                                 sprite_hero_walk_left_2.rect.y +=1
                                                 jumping = False 
                                   else:
                                          jump_power_check = 0
                                          sprite_hero_walk_left_2.rect.y +=1
                                          jumping = False
                     if moving != False:
                                if pressed[0] or speed_attack_anim_check>0:
                                                  speed_attack_anim_check +=1
                                                  if speed_attack_anim_check  < speed_attack_anim /7:
                                                            sc.blit(sprite_hero_attack_1.image, sprite_hero_attack_1.rect)
                                                  elif speed_attack_anim_check  < speed_attack_anim /7 * 2:
                                                            sc.blit(sprite_hero_attack_2.image, sprite_hero_attack_2.rect)
                                                  elif speed_attack_anim_check  < speed_attack_anim /7 * 3:
                                                            sc.blit(sprite_hero_attack_3.image, sprite_hero_attack_3.rect)
                                                  elif speed_attack_anim_check  < speed_attack_anim /7 * 4:
                                                            sc.blit(sprite_hero_attack_4.image, sprite_hero_attack_4.rect)
                                                  elif speed_attack_anim_check  < speed_attack_anim /7 * 5:
                                                            sc.blit(sprite_hero_attack_5.image, sprite_hero_attack_5.rect)
                                                  elif speed_attack_anim_check  < speed_attack_anim /7 * 6:
                                                            sc.blit(sprite_hero_attack_6.image, sprite_hero_attack_6.rect)
                                                  elif speed_attack_anim_check  < speed_attack_anim /7 * 7:
                                                            sc.blit(sprite_hero_attack_7.image, sprite_hero_attack_7.rect)
                                                  else:
                                                            speed_attack_anim_check = 0
                     #жалкая попытка на исправление бага       
                     if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) >0:
                            sprite_hero_walk_left_2.rect.y -=2
                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                   sprite_hero_walk_left_1.rect.y-=1
                            else:
                                   sprite_hero_walk_left_2.rect.y+=1
                            sprite_hero_walk_left_2.rect.y+=1
                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                   sprite_hero_walk_left_1.rect.y+=1
                            else:
                                   sprite_hero_walk_left_2.rect.y-=1
                            sprite_hero_walk_left_2.rect.x += 1
                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                   sprite_hero_walk_left_1.rect.x +=1
                            else:
                                   sprite_hero_walk_left_2.rect.x -=1
                            sprite_hero_walk_left_2.rect.x-=1
                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                   sprite_hero_walk_left_1.rect.x-=1 
                            else:
                                   sprite_hero_walk_left_2.rect.x+=1
                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) >0:
                                   sprite_hero_walk_left_2.rect.y+=1
                                   if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) >0:
                                          sprite_hero_walk_left_2.rect.y-=2
                                          if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) >0:
                                                 sprite_hero_walk_left_2.rect.y+=3
                                                 if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) >0:
                                                        sprite_hero_walk_left_2.rect.x+=1
                     if jumping == True:
                            moving = 'jump'

                     if jumping == False:                 
                            sprite_hero_walk_left_2.rect.y +=1#падение
                            falling = True
                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                   sprite_hero_walk_left_1.rect.y +=1
                            else:
                                   falling = False
                                   sprite_hero_walk_left_2.rect.y-=1


                     if moving == False:
                            sc.blit(sprite_hero_stand_1.image, sprite_hero_stand_1.rect)
                            speed_change_walk_check = 0
                     elif moving == 'left':
                            if speed_change_walk_check < speed_change_walk /2+1:
                                   sc.blit(sprite_hero_walk_left_1.image, sprite_hero_walk_left_1.rect)
                            elif speed_change_walk_check > speed_change_walk/2-1 and speed_change_walk_check < speed_change_walk-1:
                                   sc.blit(sprite_hero_walk_left_1_1.image, sprite_hero_walk_left_1_1.rect)
                            elif speed_change_walk_check+1 >= speed_change_walk:
                                   if speed_change_walk_check < speed_change_walk * 1.5:
                                          sc.blit(sprite_hero_walk_left_1_2.image, sprite_hero_walk_left_1_2.rect)
                                   else:
                                          speed_change_walk_check = 0
                                          sc.blit(sprite_hero_walk_left_1_2.image, sprite_hero_walk_left_1_2.rect)
                     elif moving == 'right':
                            if speed_change_walk_check < speed_change_walk /2+1:
                                   sc.blit(sprite_hero_walk_right_1.image, sprite_hero_walk_right_1.rect)
                            elif speed_change_walk_check > speed_change_walk/2-1 and speed_change_walk_check < speed_change_walk-1:
                                   sc.blit(sprite_hero_walk_right_1_1.image, sprite_hero_walk_right_1_1.rect)
                            elif speed_change_walk_check+1 >= speed_change_walk:
                                   if speed_change_walk_check < speed_change_walk * 1.5:
                                          sc.blit(sprite_hero_walk_right_1_2.image, sprite_hero_walk_right_1_2.rect)
                                   else:
                                          speed_change_walk_check = 0
                                          sc.blit(sprite_hero_walk_right_1_2.image, sprite_hero_walk_right_1_2.rect)
                     elif moving == 'jump':
                            sc.blit(sprite_hero_falling_1.image, sprite_hero_falling_1.rect)
                     walle.draw(sc)
                     pygame.display.update()
                     sprite_hero_walk_left_2.rect = sprite_hero_walk_left_1.rect
                     sprite_hero_walk_left_1_1.rect = sprite_hero_walk_left_1.rect
                     sprite_hero_walk_left_1_2.rect = sprite_hero_walk_left_1.rect
                     sprite_hero_stand_1.rect = sprite_hero_walk_left_1.rect
                     sprite_hero_walk_right_1_1.rect = sprite_hero_walk_left_1.rect
                     sprite_hero_walk_right_1_2.rect = sprite_hero_walk_left_1.rect
                     sprite_hero_walk_right_1.rect = sprite_hero_walk_left_1.rect
                     sprite_hero_falling_1.rect = sprite_hero_walk_left_1.rect
                     if moving != 'left':
                               sprite_hero_attack_1.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_1.rect.x = sprite_hero_walk_left_1.rect.x+45
                               sprite_hero_attack_2.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_2.rect.x = sprite_hero_walk_left_1.rect.x+45
                               sprite_hero_attack_3.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_3.rect.x = sprite_hero_walk_left_1.rect.x+45
                               sprite_hero_attack_4.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_4.rect.x = sprite_hero_walk_left_1.rect.x+45
                               sprite_hero_attack_5.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_5.rect.x = sprite_hero_walk_left_1.rect.x+45
                               sprite_hero_attack_6.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_6.rect.x = sprite_hero_walk_left_1.rect.x+45
                               sprite_hero_attack_7.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_7.rect.x = sprite_hero_walk_left_1.rect.x+45
                     else:
                               sprite_hero_attack_1.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_1.rect.x = sprite_hero_walk_left_1.rect.x-65
                               sprite_hero_attack_2.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_2.rect.x = sprite_hero_walk_left_1.rect.x-65
                               sprite_hero_attack_3.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_3.rect.x = sprite_hero_walk_left_1.rect.x-65
                               sprite_hero_attack_4.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_4.rect.x = sprite_hero_walk_left_1.rect.x-65
                               sprite_hero_attack_5.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_5.rect.x = sprite_hero_walk_left_1.rect.x-65
                               sprite_hero_attack_6.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_6.rect.x = sprite_hero_walk_left_1.rect.x-65
                               sprite_hero_attack_7.rect.y = sprite_hero_walk_left_1.rect.y
                               sprite_hero_attack_7.rect.x = sprite_hero_walk_left_1.rect.x-65
                     moving = False
                     sc.fill((0,0,0))
                     sc.blit(background_loca_1.image, background_loca_1.rect)
                     sc.blit(floor_loca_1.image, floor_loca_1.rect)
                     if sprite_hero_walk_left_1.rect.x > 1300 and location == 1:
                               print('level complete')
                               location = 2
                               sprite_hero_walk_left_1.rect.x = 200
                               sprite_hero_walk_left_1.rect.y = 450
                               floor_loca_1.rect.x = -500
                     clock.tick(FPS)
       except:
              print('bye-bye')
              time.sleep(2)
              pygame.quit()
              quit()
