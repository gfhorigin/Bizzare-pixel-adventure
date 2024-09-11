from tkinter import *
from tkinter import ttk
import pygame as pg
import sqlite3
import sys
root =Tk()
class Menu:
    def __init__ (self):
        self.conn = sqlite3.connect('gameinfo.db')
        self.cur = self.conn.cursor()
        self.conn.commit()
        self.cur.close()
        
        root.geometry('600x400+200+100')
        self.lab = Label(text ="игра от gfh ,Ai-vani,wadoil,bambaleyla")
        self.lab.pack()
        try:
            self.b_ttk4.pack_forget()
        except:
            print("no pack")
        try:
            self.b_ttk4.grid_forget()
        except:
            print("no grid")
        self.b_ttk = Button(text="ИГРАТЬ" ,command  = self.game)
        self.b_ttk.pack()
        self.b_ttk1 = Button(text="НАСТРОЙКИ",command  = self.settings)
        self.b_ttk1.pack()
        self.b_ttk2 = Button(text="ТИТРЫ",command  = self.titry)
        self.b_ttk2.pack()
        self.b_ttk3 = Button(text="ВЫЙТИ",command  = self.quite)
        self.b_ttk3.pack()
        self.b_ttk4 = Button(text="<<назад" ,command  =self.__init__)   

    
    def settings(self):
        self.lab.pack_forget()
        self.b_ttk.pack_forget()
        self.b_ttk1.pack_forget()
        self.b_ttk2.pack_forget()
        self.b_ttk3.pack_forget()
        
        self.b_ttk4.pack()
    def quite (self):
            self.root.destroy()
    def titry (self):
            self.lab.pack_forget()
            self.b_ttk.pack_forget()
            self.b_ttk1.pack_forget()
            self.b_ttk2.pack_forget()
            self.b_ttk3.pack_forget()
             
            
            self.b_ttk4.pack()
    def game(self):        
        root.geometry('540x320+200+100')
        
        self.lab.pack_forget()
        self.b_ttk.pack_forget()
        self.b_ttk1.pack_forget()
        self.b_ttk2.pack_forget()
        self.b_ttk3.pack_forget()   
######        
        self.sv1=LabelFrame(text="Слот 1")
        self.sv2=LabelFrame(text="Слот 2")
        self.sv3=LabelFrame(text="Слот 3")
        self.svsl1=Label(self.sv1,bg='gray', width=20,height=17, relief='groove')
        self.svsl2=Label(self.sv2,bg='gray', width=20,height=17, relief='groove')
        self.svsl3=Label(self.sv3,bg='gray', width=20,height=17, relief='groove')
        
        self.svb1=Button(self.sv1,text="+",width=2,command=self.charplus)
        self.svb1d=Button(self.sv1,text="Удалить",width=6)
        self.svb2=Button(self.sv2,text="+",width=2,command=self.charplus)
        self.svb2d=Button(self.sv2,text="Удалить",width=6)
        self.svb3=Button(self.sv3,text="+",width=2,command=self.charplus)
        self.svb3d=Button(self.sv3,text="Удалить",width=6)
        
        self.svi1=Label(self.sv1,bg='gray', fg='white', width=19, justify=LEFT, wraplength=150)#тут указывается инфа о прохождении
        self.svi2=Label(self.sv2,bg='gray', fg='white', width=19, justify=LEFT, wraplength=150)
        self.svi3=Label(self.sv3,bg='gray', fg='white', width=19, justify=LEFT, wraplength=150)
######
        self.sv1.grid(column=0,row=0,padx=15)
        self.sv2.grid(column=1,row=0,padx=15)
        self.sv3.grid(column=2,row=0,padx=15)
        
        self.svsl1.grid(column=0,row=0)
        self.svsl2.grid(column=0,row=0)
        self.svsl3.grid(column=0,row=0)
        self.svi1.grid(column=0,row=0,sticky=N)
        self.svi2.grid(column=0,row=0,sticky=N)
        self.svi3.grid(column=0,row=0,sticky=N)
######        
        self.conn = sqlite3.connect('gameinfo.db')
        self.cur =self.conn.cursor()
        root.title("Слоты сохранения")
        self.slotcheck1="""SELECT * from Saves"""
        self.cur.execute(self.slotcheck1)
        self.slotcheck=self.cur.fetchall()
        print(self.slotcheck)
        self.cur.close()
        
        if self.slotcheck[0][1]=="None":
            self.svb1.grid(column=0,row=0)
        elif self.slotcheck[0][1]!="None":
            self.svb1.grid(column=0,row=1, sticky=W)
            self.svb1['text']="Играть"
            self.svb1['width']=5
            self.svi1['text']=("Имя: "+str(self.slotcheck[0][1])+"\nСыграно: "+str(self.slotcheck[0][2])+" ч.\nУбито мобов: "+str(self.slotcheck[0][5])+"\nПоследний убитый Босс:"+str(self.slotcheck[0][4]))
            self.svb1d.grid(column=0,row=1, sticky=E)
            
        if self.slotcheck[1][1]=="None":
            self.svb2.grid(column=0,row=0)
        elif self.slotcheck[1][1]!="None":
            self.svb2.grid(column=0,row=1, sticky=W)
            self.svb2['text']="Играть"
            self.svb2['width']=5
            self.svi2['text']=("Имя: "+str(slotcheck[1][1])+"\nСыграно: "+str(slotcheck[1][2])+" ч.\nУбито мобов: "+str(slotcheck[1][5])+"\nПоследний убитый Босс:"+str(slotcheck[1][4]))
            self.svb2d.grid(column=0,row=1, sticky=E)
            
        if self.slotcheck[2][1]=="None":
            self.svb3.grid(column=0,row=0)
        elif self.slotcheck[2][1]!="None":
            self.svb3.grid(column=0,row=1, sticky=W)
            self.svb3['text']="Играть"
            self.svb3['width']=5
            self.svi3['text']=("Имя: "+str(slotcheck[2][1])+"\nСыграно: "+str(slotcheck[2][2])+" ч.\nУбито мобов: "+str(slotcheck[2][5])+"\nПоследний убитый Босс:"+str(slotcheck[2][4]))
            self.svb3d.grid(column=0,row=1, sticky=E)
            
    def charplus(self):
        self.redact=Toplevel()
        self.redact.geometry("200x80+370+120")
        self.redact.title("Создание персонажа")
        self.charcreateinfo=Label(self.redact,text="Выберите имя своему персонажу")
        self.charcreateinfo.pack()
        self.entername=Entry(self.redact)
        self.entername.pack()
        self.charcreatebutt=Button(self.redact,text='OK',command=self.createchar)
        self.charcreatebutt.pack()
    def createchar(self):
        createname=self.entername.get()
        self.redact.destroy()
        self.conn = sqlite3.connect('gameinfo.db')
        self.cur =self.conn.cursor()
        charcreate="""UPDATE Saves SET Name=? WHERE ID = 1"""
        self.cur.execute(charcreate,createname)
        self.conn.commit()
        self.cur.close()

##        root.title("Слоты сохранения")
##        self.slotcheck1="""SELECT * from Saves"""
##        self.cur.execute(self.slotcheck1)
##        self.slotcheck=self.cur.fetchall()
##        print(self.slotcheck)
##        self.cur.close()
        
##    def update_sqlite_table():
##    try:
##        sqlite_connection = sqlite3.connect('sqlite_python.db')
##        cursor = sqlite_connection.cursor()
##        print("Подключен к SQLite")
##
##        sql_update_query = """Update sqlitedb_developers set salary = 10000 where id = 4"""
##        cursor.execute(sql_update_query)
##        sqlite_connection.commit()
##        print("Запись успешно обновлена")
##        cursor.close()
##    
##    
    def play(self):
            root.destroy()
            #Ai_vani not 100%
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

Platformer=Menu()
root.mainloop()
