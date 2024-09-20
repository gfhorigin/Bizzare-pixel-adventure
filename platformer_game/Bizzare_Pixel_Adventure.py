import pygame
import sys
import time
import random
from tkinter import *
from threading import Thread
import sqlite3
root = Tk()
root.title(' Bizzare pixel Adventure')
root.resizable(False, False)
class Potato:
          def __init__(self):
                         self.main() 
          def main(self):
                    import pygame as pg
                    pg.init()
                    self.developer_sound= pygame.mixer.Sound('Data/sounds/developer_mode.mp3')
##                    #self.main_menu_music = pg.mixer.Sound('Data/music/main_menu_music_1.ogg')
##                    #self.main_menu_music.play()
                    self.click_button_sound = pg.mixer.Sound('Data/sounds/click_button_sound.wav')
                    self.y = 300
                    self.x = 300
                    self.w = root.winfo_screenwidth()
                    self.h = root.winfo_screenheight()
                    self.w = self.w//2 # середина экрана
                    self.h = self.h//2
                    root.geometry('{}x{}+{}+{}'.format(205, 176, self.w,self.h))
                    
                    self.New_game_button = PhotoImage(file = 'Data/menu_button/New_Game_button.gif')
                    self.Continue_button = PhotoImage(file = 'Data/menu_button/Continue_button.gif')
                    self.Play_game_button = PhotoImage(file = 'Data/menu_button/Play_button.gif')
                    self.Settings_game_button = PhotoImage(file = 'Data/menu_button/Settings_button.gif')
                    self.Extra_button = PhotoImage(file = 'Data/menu_button/extra_button.gif')
                    self.Quit_game_button = PhotoImage(file = 'Data/menu_button/Quit_game_button.gif')
                    self.aivanello = PhotoImage(file = 'Data/images/decorations/characters info/Ai_vani.gif')
                    self.grish = PhotoImage(file = 'Data/images/decorations/characters info/Grisha.gif')
                    self.olegius = PhotoImage(file = 'Data/images/decorations/characters info/Oleg.gif')
                    self.gifigi = PhotoImage(file = 'Data/images/decorations/characters info/gfh.gif')
                    self.cirab = PhotoImage(file = 'Data/images/decorations/characters info/crab.gif')
                    self.bambaleylius = PhotoImage(file = 'Data/images/decorations/characters info/bambaleyla.gif')
                    self.Ericius = PhotoImage(file = 'Data/images/decorations/characters info/Aricius.gif')
                    self.guardian = PhotoImage(file = 'Data/images/decorations/characters info/guardian.gif')

                    
                    self.play_game = Button(text="play",command =self.save,image = self.Play_game_button)
                    #self.settings_game = Button(image = self.Settings_game_button, command = self.settings)
                    self.extra_game = Button(image = self.Extra_button, command = self.extras)
                    self.quit_game = Button(image = self.Quit_game_button, command = self.quit)
                    
                    self.play_game.grid()
                    #self.settings_game.grid()
                    self.extra_game.grid()
                    self.quit_game.grid()
                    
                    self.conn = sqlite3.connect('gameinfo.db')
                    self.cur = self.conn.cursor()
                    self.conn.commit()
                    self.cur.close()
                    self.locationsave=0
                    a=0#заглушка для try except'ов
                    self.choosencharacter=0
                    try:
                        self.b_ttk4.grid_forget()
                    except:
                        a+=1
                    try:
                        self.b_ttk4.grid_forget()
                    except:
                        a+=1
                    try:
                        self.sv1.grid_forget()
                        self.svsl1.grid_forget()
                        self.svi1.grid_forget()
                    except:
                        a+=1
                    try:
                        self.sv2.grid_forget()
                        self.svsl2.grid_forget()
                        self.svi2.grid_forget()
                    except:
                        a+=1
                    try:
                        self.sv3.grid_forget()
                        self.svsl3.grid_forget()
                        self.svi3.grid_forget()
                    except:
                        a+=1
                    try:
                        self.svb1.grid_forget()
                        self.svb1d.grid_forget()
                    except:
                        a+=1
                    try:
                        self.svb2.grid_forget()
                        self.svb2d.grid_forget()
                    except:
                        a+=1
                    try:
                        self.svb3.grid_forget()
                        self.svb3d.grid_forget()
                    except:
                        a+=1
                    
                    self.b_ttk4 = Button(text="<<назад" ,command  =self.__init__)   
                    try:
                        self.developer_info.destroy()
                        self.button_developer.destroy()
                    except AttributeError:
                        pass
                    try:
                        if self.developer == False:
                            self.developer_info = Label(text = 'Developer mode is disabled') 
                        elif self.developer == True:
                            self.developer_info = Label(text = 'Developer mode is enabled') 
                    except AttributeError:
                        self.developer_info = Label(text = 'Developer mode is disabled') 
                    self.developer_info.grid()
                    self.button_developer = Button(text = 'on/off', command = self.on_developer)
                    self.button_developer.grid()
          def quit(self):
            root.destroy()
          def on_developer(self):
            self.developer_sound.play()
            if self.developer == False:
                self.developer = True
                self.developer_info['text'] = 'Developer mode is enabled'
            else:
                self.developer = False
                self.developer_info['text'] = 'Developer mode is disabled'
                
          def save(self): #загрузка меню сохранений
            root.geometry('560x380')
            a=0#заглушка для try-except
            try:
                self.play_game.grid_forget()
                #self.settings_game.grid_forget()
                self.extra_game.grid_forget()
                self.quit_game.grid_forget()
            except:
                a+=1
                
            self.sv1=LabelFrame(text="Слот 1") 
            self.sv2=LabelFrame(text="Слот 2")
            self.sv3=LabelFrame(text="Слот 3")
            self.svsl1=Label(self.sv1,bg='gray', width=21,height=17, relief='groove')
            self.svsl2=Label(self.sv2,bg='gray', width=21,height=17, relief='groove')
            self.svsl3=Label(self.sv3,bg='gray', width=21,height=17, relief='groove',text="out of order")
            
            self.svb1=Button(self.sv1,text="+",width=2,command=self.charplus)
            self.svb1d=Button(self.sv1,text="Удалить",width=6,command=self.predeletechar1)
            self.svb2=Button(self.sv2,text="+",width=2,command=self.charplus2)
            self.svb2d=Button(self.sv2,text="Удалить",width=6,command=self.predeletechar2)
            self.svb3=Button(self.sv3,text="+",width=2)
            self.svb3d=Button(self.sv3,text="Удалить",width=6)
            
            self.svi1=Label(self.sv1,bg='gray', fg='white', width=20, justify=LEFT, wraplength=150)#тут указывается инфа о прохождении
            self.svi2=Label(self.sv2,bg='gray', fg='white', width=20, justify=LEFT, wraplength=150)
            self.svi3=Label(self.sv3,bg='gray', fg='white', width=20, justify=LEFT, wraplength=150)
    ######
            self.b_ttk4.grid(column=1,row=1) 
            self.sv1.grid(column=0,row=0,padx=14)
            self.sv2.grid(column=1,row=0,padx=14)
            self.sv3.grid(column=2,row=0,padx=14)
            
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
            if self.developer == True:    
                print(self.slotcheck)#нужно Кириллу для отладки
            self.cur.close()
##################            ##чек босса
            if int(self.slotcheck[0][4])>15 and int(self.slotcheck[0][4])<22:#save1
                bossname="Эрициус"
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 1", ((bossname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save1: Boss name set ``Эрициус``")
            elif int(self.slotcheck[0][4])>22 and int(self.slotcheck[0][4])<30:
                bossname="Крабоид"
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 1", ((bossname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save1: Boss name set ``Крабоид``")
            elif int(self.slotcheck[0][4])>=30:
                bossname="Григорий"
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 1", ((bossname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save1: Boss name set ``Григорий``")
            else:
                bossname="Нет"
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 1", ((bossname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save1: Boss name set ``Нет``")
                    
            if int(self.slotcheck[1][4])>15 and int(self.slotcheck[1][4])<22:#save2
                bossname="Эрициус"
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 2", ((bossname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save2: Boss name set ``Эрициус``")
            elif int(self.slotcheck[1][4])>22 and int(self.slotcheck[1][4])<30:
                bossname="Крабоид"
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 2", ((bossname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save2: Boss name set ``Крабоид``")
            elif int(self.slotcheck[1][4])>=30:
                bossname="Григорий"
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 2", ((bossname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save2: Boss name set ``Григорий``")
            else:
                bossname="Нет"
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 2", ((bossname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save2: Boss name set ``Нет``")
                    
##            if int(self.slotcheck[2][4])>15 and int(self.slotcheck[2][4])<22:#save3
##                bossname="Эрициус"
##                self.conn = sqlite3.connect('gameinfo.db')
##                self.cur =self.conn.cursor()
##                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 3", ((bossname,)))
##                self.conn.commit()
##                self.cur.close()
##                if self.developer == True:    
##                    print("save3: Boss name set ``Эрициус``")
##            elif int(self.slotcheck[2][4])>22 and int(self.slotcheck[2][4])<30:
##                bossname="Крабоид"
##                self.conn = sqlite3.connect('gameinfo.db')
##                self.cur =self.conn.cursor()
##                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 3", ((bossname,)))
##                self.conn.commit()
##                self.cur.close()
##                if self.developer == True:    
##                    print("save3: Boss name set ``Крабоид``")
##            elif int(self.slotcheck[2][4])>=30:
##                bossname="Григорий"
##                self.conn = sqlite3.connect('gameinfo.db')
##                self.cur =self.conn.cursor()
##                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 3", ((bossname,)))
##                self.conn.commit()
##                self.cur.close()
##                if self.developer == True:    
##                    print("save3: Boss name set ``Григорий``")
##            else:
##                bossname="Нет"
##                self.conn = sqlite3.connect('gameinfo.db')
##                self.cur =self.conn.cursor()
##                self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 3", ((bossname,)))
##                self.conn.commit()
##                self.cur.close()
##                if self.developer == True:    
##                    print("save3: Boss name set ``Нет``")
##################            ##чек локации сейва 1
            sa=5
            if int(self.slotcheck[0][4])>=1 and int(self.slotcheck[0][4])<=5 or int(self.slotcheck[0][4])==5:
                if self.developer == True:    
                    print(self.slotcheck[0][4])
                locname=str("1-")+str(self.slotcheck[0][4])
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 1", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save1: location name set ", locname)
            if int(self.slotcheck[0][4])==8:
                locname=("1-6")
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 1", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save1: location name set ", locname) 
            elif int(self.slotcheck[0][4])>=9 and int(self.slotcheck[0][4])<=15 or int(self.slotcheck[0][4])==15:
                locname=str("2-")+str(self.slotcheck[0][4]-8)
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 1", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save1: location name set ", locname)
            elif int(self.slotcheck[0][4])>=16 and int(self.slotcheck[0][4])<=22 or int(self.slotcheck[0][4])==22:
                locname=str("3-")+str(self.slotcheck[0][4]-15)
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 1", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save1: location name set ", locname)
            elif int(self.slotcheck[0][4])>=23 and int(self.slotcheck[0][4])<=30 or int(self.slotcheck[0][4])==30:
                locname=str("4-")+str(self.slotcheck[0][4]-22)
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 1", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save1: location name set ", locname)
##################            ##чек локации сейва 2
            if int(self.slotcheck[1][4])>=1 and int(self.slotcheck[1][4])<=5 or int(self.slotcheck[1][4])==5:
                locname=str("1-")+str(self.slotcheck[1][4])
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 2", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save2: location name set ", locname)
            if int(self.slotcheck[1][4])==8:
                locname=("1-6")
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 2", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save2: location name set ", locname)
            elif int(self.slotcheck[1][4])>=9 and int(self.slotcheck[1][4])<=15 or int(self.slotcheck[1][4])==15:
                locname=str("2-")+str(self.slotcheck[1][4]-8)
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 2", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save2: location name set ", locname)
            elif int(self.slotcheck[1][4])>=16 and int(self.slotcheck[1][4])<=22 or int(self.slotcheck[1][4])==22:
                locname=str("3-")+str(self.slotcheck[1][4]-15)
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 2", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save2: location name set ", locname)
            elif int(self.slotcheck[1][4])>=23 and int(self.slotcheck[1][4])<=30 or int(self.slotcheck[1][4])==30:
                locname=str("4-")+str(self.slotcheck[1][4]-22)
                self.conn = sqlite3.connect('gameinfo.db')
                self.cur =self.conn.cursor()
                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 2", ((locname,)))
                self.conn.commit()
                self.cur.close()
                if self.developer == True:    
                    print("save2: location name set ", locname)
####################            ##чек локации сейва 3
##            if int(self.slotcheck[2][4])>=1 and int(self.slotcheck[2][4])<=5 or int(self.slotcheck[2][4])==5:
##                locname=str("1-")+str(self.slotcheck[2][4])
##                self.conn = sqlite3.connect('gameinfo.db')
##                self.cur =self.conn.cursor()
##                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 3", ((locname,)))
##                self.conn.commit()
##                self.cur.close()
##                if self.developer == True:    
##                    print("save3: location name set ", locname)
##            if int(self.slotcheck[2][4])==8:
##                locname=("1-6")
##                self.conn = sqlite3.connect('gameinfo.db')
##                self.cur =self.conn.cursor()
##                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 3", ((locname,)))
##                self.conn.commit()
##                self.cur.close()
##                if self.developer == True:    
##                    print("save3: location name set ", locname)
##            elif int(self.slotcheck[2][4])>=9 and int(self.slotcheck[2][4])<=15 or int(self.slotcheck[2][4])==15:
##                locname=str("2-")+str(self.slotcheck[2][4]-8)
##                self.conn = sqlite3.connect('gameinfo.db')
##                self.cur =self.conn.cursor()
##                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 3", ((locname,)))
##                self.conn.commit()
##                self.cur.close()
##                if self.developer == True:    
##                    print("save3: location name set ", locname)
##            elif int(self.slotcheck[2][4])>=16 and int(self.slotcheck[2][4])<=22 or int(self.slotcheck[2][4])==22:
##                locname=str("3-")+str(self.slotcheck[2][4]-15)
##                self.conn = sqlite3.connect('gameinfo.db')
##                self.cur =self.conn.cursor()
##                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 3", ((locname,)))
##                self.conn.commit()
##                self.cur.close()
##                if self.developer == True:    
##                    print("save3: location name set ", locname)
##            elif int(self.slotcheck[2][4])>=23 and int(self.slotcheck[2][4])<=30 or int(self.slotcheck[2][4])==30:
##                locname=str("4-")+str(self.slotcheck[2][4]-22)
##                self.conn = sqlite3.connect('gameinfo.db')
##                self.cur =self.conn.cursor()
##                self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 3", ((locname,)))
##                self.conn.commit()
##                self.cur.close()
##                if self.developer == True:    
##                    print("save3: location name set ", locname)
            ##
            if self.slotcheck[0][1]=="None":#инфа слотов
                self.svb1.grid(column=0,row=0)
            elif self.slotcheck[0][1]!="None":
                self.svb1.grid(column=0,row=1, sticky=W)
                self.svb1['text']="Играть"
                self.svb1['command']=self.play1
                self.svb1['width']=5
                if self.slotcheck[0][4] < 9:
                    number_loca = '1-'
                    number_room = self.slotcheck[0][4] +1
                    boss_name = 'Нет'
                    if number_room >= 4:
                        number_room -=1
                    if number_room == 8:
                        number_room = 6
                elif self.slotcheck[0][4] < 16:
                    number_loca = '2-' 
                    boss_name = 'Нет'
                    number_room = self.slotcheck[0][4] - 8
                elif self.slotcheck[0][4] < 23:
                    number_loca = '3-'
                    boss_name = 'Эрициус'
                    number_room = self.slotcheck[0][4] - 15
                elif self.slotcheck[0][4] < 31:
                    number_loca = '4-'
                    boss_name = 'Крабоид'
                    number_room = self.slotcheck[0][4] - 22
                    if self.slotcheck[0][4] == 29:
                        number_loca = '4-'
                    if self.slotcheck[0][4] == 30:
                        number_loca = '4-'


                self.svi1['text']=("Имя: "+str(self.slotcheck[0][1])+"\nПоследний убитый Босс: "+"\n"+str(boss_name)+"\nПоследняя локация: " + str(number_loca) +str(number_room))
                self.svb1d.grid(column=0,row=1, sticky=E)
                


            if self.slotcheck[1][1]=="None":
                self.svb2.grid(column=0,row=0)
                if self.developer == True:    
                    print(self.slotcheck[1][4])
            
            elif self.slotcheck[1][1]!="None":
                self.svb2.grid(column=0,row=1, sticky=W)
                self.svb2['text']="Играть"
                self.svb2['command']=self.play2
                self.svb2['width']=5
                if self.slotcheck[1][4] < 9:
                    number_loca = '1-'
                    number_room = self.slotcheck[1][4] +1
                    boss_name = 'Нет'
                    if number_room >= 4:
                        number_room -=1
                    if number_room == 8:
                        number_room = 6
                elif self.slotcheck[1][4] < 16:
                    number_loca = '2-' 
                    boss_name = 'Нет'
                    number_room = self.slotcheck[1][4] - 8
                elif self.slotcheck[1][4] < 23:
                    number_loca = '3-'
                    boss_name = 'Эрициус'
                    number_room = self.slotcheck[1][4] - 15
                elif self.slotcheck[1][4] < 31:
                    number_loca = '4-'
                    boss_name = 'Крабоид'
                    number_room = self.slotcheck[1][4] - 22
                    if self.slotcheck[1][4] == 29:
                        number_loca = '4-'
                    if self.slotcheck[1][4] == 30:
                        number_loca = '4-'
                self.svi2['text']=("Имя: "+str(self.slotcheck[1][1])+"\nПоследний убитый Босс: "+"\n"+str(boss_name)+"\nПоследняя локация: " + str(number_loca) +str(number_room))
                self.svb2d.grid(column=0,row=1, sticky=E)
                
##            if self.slotcheck[2][1]=="None":
##                self.svb3.grid(column=0,row=0)
##                if self.developer == True:    
##                    print('ASD')
##            elif self.slotcheck[2][1]!="None":
##                self.svb3.grid(column=0,row=1, sticky=W)
##                self.svb3['text']="Играть"
##                self.svb3['command']=self.play3
##                self.svb3['width']=5
##                if self.slotcheck[2][4] < 9:
##                    number_loca = '1-'
##                    number_room = self.slotcheck[2][4] +1
##                    boss_name = 'Нет'
##                    if number_room >= 4:
##                        number_room -=1
##                    if number_room == 8:
##                        number_room = 6
##                elif self.slotcheck[2][4] < 16:
##                    number_loca = '2-' 
##                    boss_name = 'Нет'
##                    number_room = self.slotcheck[2][4] - 8
##                elif self.slotcheck[2][4] < 23:
##                    number_loca = '3-'
##                    boss_name = 'Эрициус'
##                    number_room = self.slotcheck[2][4] - 15
##                elif self.slotcheck[2][4] < 31:
##                    number_loca = '4-'
##                    boss_name = 'Крабоид'
##                    number_room = self.slotcheck[2][4] - 22
##                    if self.slotcheck[2][4] == 29:
##                        number_loca = '4-'
##                    if self.slotcheck[2][4] == 30:
##                        number_loca = '4-'
##                self.svi3['text']=("Имя: "+str(self.slotcheck[2][1])+"\nПоследний убитый Босс: "+"\n"+str(boss_name)+"\nПоследняя локация: " + str(number_loca) +str(number_room))
##                self.svb3d.grid(column=0,row=1, sticky=E)
                
          def charplus(self):#создание персонажа
            self.redact=Toplevel()
            self.redact.geometry("200x80+370+120")
            self.redact.title("Создание персонажа")
            self.charcreateinfo=Label(self.redact,text="Выберите имя своему персонажу")
            self.charcreateinfo.grid()
            self.entername=Entry(self.redact)
            self.entername.grid()
            self.charcreatebutt=Button(self.redact,text='OK',command=self.createchar)
            self.charcreatebutt.grid()
            self.bullshit()
          def createchar(self):#установка персонажа
            createname=self.entername.get()
            self.redact.destroy()
            self.conn = sqlite3.connect('gameinfo.db')
            self.cur =self.conn.cursor()
            self.cur.execute("UPDATE Saves SET Name=? WHERE ID = 1", ((createname,)))
            self.conn.commit()
            self.cur.close()
            root.after(10, self.save)
          def charplus2(self):
            self.redact=Toplevel()
            self.redact.geometry("200x80+370+120")
            self.redact.title("Создание персонажа")
            self.charcreateinfo=Label(self.redact,text="Выберите имя своему персонажу")
            self.charcreateinfo.grid()
            self.entername=Entry(self.redact)
            self.entername.grid()
            self.charcreatebutt=Button(self.redact,text='OK',command=self.createchar2)
            self.charcreatebutt.grid()
            self.bullshit()
          def createchar2(self):
            createname=self.entername.get()
            self.redact.destroy()
            self.conn = sqlite3.connect('gameinfo.db')
            self.cur =self.conn.cursor()
            self.cur.execute("UPDATE Saves SET Name=? WHERE ID = 2", ((createname,)))
            self.conn.commit()
            self.cur.close()
            root.after(10, self.save)
##          def charplus3(self):
##            self.redact=Toplevel()
##            self.redact.geometry("200x80+370+120")
##            self.redact.title("Создание персонажа")
##            self.charcreateinfo=Label(self.redact,text="Выберите имя своему персонажу")
##            self.charcreateinfo.grid()
##            self.entername=Entry(self.redact)
##            self.entername.grid()
##            self.charcreatebutt=Button(self.redact,text='OK',command=self.createchar3)
##            self.charcreatebutt.grid()
##            self.bullshit()
##          def createchar3(self):
##            createname=self.entername.get()
##            self.redact.destroy()
##            self.conn = sqlite3.connect('gameinfo.db')
##            self.cur =self.conn.cursor()
##            self.cur.execute("UPDATE Saves SET Name=? WHERE ID = 3", ((createname,)))
##            self.conn.commit()
##            self.cur.close()
##            root.after(10, self.save)
            
          def predeletechar1(self):#удаление персонажа
            self.delete=Toplevel()
            self.delete.geometry("200x60+370+120")
            self.delete.title("Вы уверены?")
            self.chardeleteinfo=Label(self.delete,text="Вы хотите удалить это сохранение?")
            self.chardeleteinfo.grid()
            self.chardeletebutt=Button(self.delete,text='Да',command=self.deletechar1)
            self.chardeletebutt.grid()
          def deletechar1(self):#стирание персонажа
            self.conn = sqlite3.connect('gameinfo.db')
            self.cur =self.conn.cursor()
            none="None"
            self.cur.execute("UPDATE Saves SET Name=? WHERE ID = 1", ((none,)))
            self.cur.execute("UPDATE Saves SET kills=? WHERE ID = 1", ((0,)))
            self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 1", (("нет",)))
            self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((0,)))
            self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 1", (("1-1",)))
            self.cur.execute("UPDATE Saves SET Ai_vani=? WHERE ID = 1", ((0,)))
            self.cur.execute("UPDATE Saves SET GFH=? WHERE ID = 1", ((0,)))
            self.cur.execute("UPDATE Saves SET Bambaleyla=? WHERE ID = 1", ((0,)))
            self.sv1.grid_forget()
            self.svsl1.grid_forget()
            self.svb1.grid_forget()
            self.svi1.grid_forget()
            self.svb1d.grid_forget()
            self.delete.destroy()
            self.conn.commit()
            self.cur.close()
            self.bullshit()
            root.after(10, self.save)
          def predeletechar2(self):
            self.delete2=Toplevel()
            self.delete2.geometry("200x60+370+120")
            self.delete2.title("Вы уверены?")
            self.chardeleteinfo=Label(self.delete2,text="Вы хотите удалить это сохранение?")
            self.chardeleteinfo.grid()
            self.chardeletebutt=Button(self.delete2,text='Да',command=self.deletechar2)
            self.chardeletebutt.grid()
          def deletechar2(self): 
            self.conn = sqlite3.connect('gameinfo.db')
            self.cur =self.conn.cursor()
            none="None"
            self.cur.execute("UPDATE Saves SET Name=? WHERE ID = 2", ((none,)))
            self.cur.execute("UPDATE Saves SET kills=? WHERE ID = 2", ((0,)))
            self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 2", (("нет",)))
            self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((0,)))
            self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 2", (("1-1",)))
            self.cur.execute("UPDATE Saves SET Ai_vani=? WHERE ID = 2", ((0,)))
            self.cur.execute("UPDATE Saves SET GFH=? WHERE ID = 2", ((0,)))
            self.cur.execute("UPDATE Saves SET Bambaleyla=? WHERE ID = 2", ((0,)))
            self.sv2.grid_forget()
            self.svsl2.grid_forget()
            self.svb2.grid_forget()
            self.svi2.grid_forget()
            self.svb2d.grid_forget()
            self.delete2.destroy()
            self.conn.commit()
            self.cur.close()
            self.bullshit()
            root.after(10, self.save)
##          def predeletechar3(self):
##            self.delete3=Toplevel()
##            self.delete3.geometry("200x60+370+120")
##            self.delete3.title("Вы уверены?")
##            self.chardeleteinfo=Label(self.delete3,text="Вы хотите удалить это сохранение?")
##            self.chardeleteinfo.grid()
##            self.chardeletebutt=Button(self.delete3,text='Да',command=self.deletechar3)
##            self.chardeletebutt.grid()
##          def deletechar3(self): 
##            self.conn = sqlite3.connect('gameinfo.db')
##            self.cur =self.conn.cursor()
##            none="None"
##            self.cur.execute("UPDATE Saves SET Name=? WHERE ID = 3", ((none,)))
##            self.cur.execute("UPDATE Saves SET kills=? WHERE ID = 3", ((0,)))
##            self.cur.execute("UPDATE Saves SET LKB=? WHERE ID = 3", (("нет",)))
##            self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((0,)))
##            self.cur.execute("UPDATE Saves SET loc_name=? WHERE ID = 3", (("1-1",)))
##            self.cur.execute("UPDATE Saves SET Ai_vani=? WHERE ID = 3", ((0,)))
##            self.cur.execute("UPDATE Saves SET GFH=? WHERE ID = 3", ((0,)))
##            self.cur.execute("UPDATE Saves SET Bambaleyla=? WHERE ID = 3", ((0,)))
##            self.sv3.grid_forget()
##            self.svsl3.grid_forget()
##            self.svb3.grid_forget()
##            self.svi3.grid_forget()
##            self.svb3d.grid_forget()
##            self.svsl3.grid_forget()
##            self.delete3.destroy()
##            self.conn.commit()
##            self.cur.close()
##            self.bullshit()
##            root.after(10, self.save)
          def bullshit(self):#это необходимо для корректной работы меню
            a=0
            try:
                self.b_ttk4.grid_forget()
            except:
                a+=1
            try:
                self.b_ttk4.grid_forget()
            except:
                a+=1
            try:
                self.sv1.grid_forget()
                self.svsl1.grid_forget()
                self.svi1.grid_forget()
            except:
                a+=1
            try:
                self.sv2.grid_forget()
                self.svsl2.grid_forget()
                self.svi2.grid_forget()
            except:
                a+=1
            try:
                self.sv3.grid_forget()
                self.svsl3.grid_forget()
                self.svi3.grid_forget()
            except:
                a+=1
            try:
                self.svb1.grid_forget()
                self.svb1d.grid_forget()
            except:
                a+=1
            try:
                self.svb2.grid_forget()
                self.svb2d.grid_forget()
            except:
                a+=1
            try:
                self.svb3.grid_forget()
                self.svb3d.grid_forget()
            except:
                a+=1            
    ##запуск игры
          def play1(self):
            self.choosencharacter=1
            self.game()
          def play2(self):
            self.choosencharacter=2
            self.game()
##          def play3(self):
##            self.choosencharacter=3
##            self.game()
    #####конец кода кирилла, ниже только смерть 
          def extras(self):
                self.click_button_sound.play()
                self.extras_tk = Toplevel()
                self.extras_tk.title('Extras')
                self.extras_tk.resizable(False, False)
                self.extras_tk.geometry(('550x236+{}+{}'.format(self.w,self.h)))
                self.extras_tk['bg'] = '#000000'
                f1 = open('extra.txt')
                num_str = 0
                for i in f1:
                        if num_str == 0:
                            if i.count('False') == 1:
                                 Ai_vani_open = False
                            elif i.count('True') == 1:
                                    Ai_vani_open = True
                        elif num_str == 1:
                                if i.count('False') == 1:
                                    gfh_open = False
                                else:
                                    gfh_open = True
                        elif num_str == 2:
                                if i.count('False') == 1:
                                    bambaleyla_open = False
                                elif i.count('True') == 1:
                                    bambaleyla_open = True
                        elif num_str == 3:
                                if i.count('False') == 1:
                                    oleg_open = False
                                elif i.count('True') == 1:
                                    oleg_open = True
                        elif num_str == 4:
                                if i.count('False') == 1:
                                    grisha_open = False
                                elif i.count('True') == 1:
                                    grisha_open = True
                        elif num_str == 5:
                                if i.count('False') == 1:
                                    ericius_open = False
                                elif i.count('True') == 1:
                                    ericius_open = True
                        elif num_str == 6:
                                if i.count('False') == 1:
                                    kraboid_open = False
                                elif i.count('True') == 1:
                                    kraboid_open = True
                        elif num_str == 7:
                                if i.count('False') == 1:
                                    guardian_open = False
                                elif i.count('True') == 1:
                                    guardian_open = True
                        num_str+=1
                f1.close()
                self.aivani_button = Button(self.extras_tk,image = self.aivanello, command = self.info_aivani)
                self.grisha_button = Button(self.extras_tk,image = self.grish ,command = self.info_grisha)
                self.olegius_button = Button(self.extras_tk,image = self.olegius, command = self.info_Oleg)
                self.gifigi_button = Button(self.extras_tk,image = self.gifigi, command = self.info_gfh)
                self.cirab_button = Button(self.extras_tk,image = self.cirab , command = self.info_craboid)
                self.bambaleylius_button = Button(self.extras_tk,image = self.bambaleylius, command = self.info_bambaleylaq)
                self.Ericius_button = Button(self.extras_tk,image = self.Ericius,command = self.info_Ericius)
                self.guardian_button = Button(self.extras_tk,image = self.guardian , command = self.info_straje)
                if Ai_vani_open == True:
                        self.aivani_button.grid(row=0, column=0)
                else:
                        self.aivanello_close = PhotoImage(file = 'Data/images/decorations/characters info/Ai_vani_close.gif')
                        self.aivani_button_close = Button(self.extras_tk,image = self.aivanello_close)
                        self.aivani_button_close.grid(row=0, column=0)
                if gfh_open == True:
                        self.gifigi_button.grid(row=0, column=1)
                else:
                        self.gfh_close = PhotoImage(file = 'Data/images/decorations/characters info/gfh_close.gif')
                        self.gfh_button_close = Button(self.extras_tk,image = self.gfh_close)
                        self.gfh_button_close.grid(row=0, column=1)
                if bambaleyla_open == True:
                        self.bambaleylius_button.grid(row=0, column=2)
                else:
                        self.bambaleyla_close = PhotoImage(file = 'Data/images/decorations/characters info/bambaleyla_close.gif')
                        self.bambaleyla_button_close = Button(self.extras_tk,image = self.bambaleyla_close)
                        self.bambaleyla_button_close.grid(row=0, column=2)
                if oleg_open == True:
                        self.olegius_button.grid(row=0, column=3)
                else:
                        self.olegius_close = PhotoImage(file = 'Data/images/decorations/characters info/Oleg_close.gif')
                        self.olegius_button_close = Button(self.extras_tk,image = self.olegius_close)
                        self.olegius_button_close.grid(row=0, column=3)
                if grisha_open == True:
                        self.grisha_button.grid(row=1, column=0)
                else:
                        self.grisha_close = PhotoImage(file = 'Data/images/decorations/characters info/grisha_close.gif')
                        self.grisha_button_close = Button(self.extras_tk,image = self.grisha_close)
                        self.grisha_button_close.grid(row=1, column=0)
                if ericius_open == True:
                        self.Ericius_button.grid(row=1, column=1)
                else:
                        self.ericius_close = PhotoImage(file = 'Data/images/decorations/characters info/Aricius_close.gif')
                        self.ericius_button_close = Button(self.extras_tk,image = self.ericius_close)
                        self.ericius_button_close.grid(row=1, column=1)
                if kraboid_open == True:
                        self.cirab_button.grid(row=1, column=2)
                else:
                        self.kraboid_close = PhotoImage(file = 'Data/images/decorations/characters info/crab_close.gif')
                        self.kraboid_button_close = Button(self.extras_tk,image = self.kraboid_close)
                        self.kraboid_button_close.grid(row=1, column=2)
                if guardian_open == True:
                        self.guardian_button.grid(row=1, column=3)
                else:
                        self.guardian_close = PhotoImage(file = 'Data/images/decorations/characters info/guardian_close.gif')
                        self.guardian_button_close = Button(self.extras_tk,image = self.guardian_close)
                        self.guardian_button_close.grid(row=1, column=3)
                if self.developer == True:
                        self.but = Button(self.extras_tk, text = 'заблокировать ориджины', command = self.close_origins) 
                        self.but.grid(row=2, column=1)
                        self.but2 = Button(self.extras_tk, text = 'разблокировать ориджины', command = self.open_origins) 
                        self.but2.grid(row=2, column=2)
                else:
                        self.extras_tk.geometry(('425x213+{}+{}'.format(self.w,self.h)))
          def close_origins(self):
            list = ['Ai_vani = False\nGfh = False\nBambaleyla = False\nOleg = False\nGrisha = False\nAricius = False\nKraboid = False\nGuardian = False']
            f2 = open('Extra.txt', 'w')
            f2.write(list[0])
            f2.close()
            self.extras_tk.destroy()
            self.extras()
          def open_origins(self):
            list = ['Ai_vani = True\nGfh = True\nBambaleyla = True\nOleg = True\nGrisha = True\nAricius = True\nKraboid = True\nGuardian = True']
            for i in list:
                i.replace('True', 'False')
            f2 = open('Extra.txt', 'w')
            f2.write(list[0])
            f2.close()
            self.extras_tk.destroy()
            self.extras()
          def info_bambaleylaq(self):
                self.bambaleyla_info2 = Toplevel()
                self.bambaleyla_info2.title('bambaleyla')
                self.bambaleyla_info2.resizable(False, False)
                self.bambaleyla_info2.geometry('500x280+{}+{}'.format(self.w,self.h))
                self.bambaleyla_info2['bg'] = '#ff9900'
                self.label = Label(self.bambaleyla_info2, text = 'bambaleyla')
                self.label1 = Label(self.bambaleyla_info2, text = 'Когда bambaleyla был ещё ребёнком, в его городе была война. \nКороль думал, как бы её остановить. ')
                self.label2 = Label(self.bambaleyla_info2, text = 'И вот в один прекрасный день bambaleyla и ещё пару ребят отправили в храм за \nсвященным артефактом. Пока дети добирались туда, попутчики bambaleylы погибли.')
                self.label3 = Label(self.bambaleyla_info2, text = 'Ребёнок зашёл в храм и увидел странную материю. Он приблизился, и её часть \nбыстрым движением прыгнула в его глаз, от чего он стал фиолетовым. ')
                self.label4 = Label(self.bambaleyla_info2, text = 'Ребёнок испугался и быстро убежал оттуда. Когда он пришёл, войны в его \nгосударстве уже не было. Но мальчика  стали боятся, так как \nтеперь он мог преобразовывать материю. ')
                self.label5 = Label(self.bambaleyla_info2, text = 'Король не видел ничего в этом страшного, до того момента когда мальчик \nво сне из его чашки превратил огромный булыжник и чуть ли не раздавил короля.')
                self.label6 = Label(self.bambaleyla_info2, text = 'bambaleylу прогнали из родных земель. Он скитался очень долго и пристрастился к \nнекоторым вредным привычкам. Но однажды ему повезло, и он смог найти себе \nпостоянное место жительства. До сей поры, bambaleyla живёт в подвале замка.')
                asdd = '#ffc266'
                self.label['bg'] = asdd
                self.label1['bg'] = asdd
                self.label2['bg']= asdd
                self.label3['bg']= asdd
                self.label4['bg']= asdd
                self.label5['bg']= asdd
                self.label6['bg']= asdd
                self.label.grid()
                self.label1.grid()
                self.label2.grid()
                self.label3.grid()
                self.label4.grid()
                self.label5.grid()
                self.label6.grid()
          def info_Ericius(self):
                self.Ericius_info2 = Toplevel()
                self.Ericius_info2.title('Эрициус')
                self.Ericius_info2.resizable(False, False)
                self.Ericius_info2.geometry('455x150+{}+{}'.format(self.w,self.h))
                self.Ericius_info2['bg'] = '#EFC03E'
                self.label = Label(self.Ericius_info2, text = 'Эрициус')
                self.label2 = Label(self.Ericius_info2, text = 'Эрициус был бедняком. Он хотел стать богаче\nи для этого, он пошел в Казино Демона.')
                self.label3 = Label(self.Ericius_info2, text = 'К сожалению, ему не везло, и он потерял абсолютно всё что у него оставалось.')
                self.label4 = Label(self.Ericius_info2, text = 'Он решился на серьёзный шаг: он поставил на кон свою душу...\nНа удивление, на этот раз ему повезло, и он обрёл великую силу и богатство')
                self.label5 = Label(self.Ericius_info2, text = 'Эту самую силу хотел получить Гриша \nи из-за чего он и поручил его убить Олегу')
                
                asdd = '#EFA83E'
                self.label['bg'] = asdd
                self.label2['bg']= asdd
                self.label3['bg']= asdd
                self.label4['bg']= asdd
                self.label5['bg']= asdd

                self.label.grid()
                self.label2.grid()
                self.label3.grid()
                self.label4.grid()
                self.label5.grid()
          def info_Oleg(self):
                self.Oleg_info2 = Toplevel()
                self.Oleg_info2.title('Олег')
                self.Oleg_info2.resizable(False, False)
                self.Oleg_info2.geometry('740x150+{}+{}'.format(self.w,self.h))
                self.Oleg_info2['bg'] = '#ffbcd9'
                self.label = Label(self.Oleg_info2, text = 'Олегина')
                self.label2 = Label(self.Oleg_info2, text = 'Олегина спокойно жила себе со своим питомцем Крабоидом. Так продолжалось пока Гриша в ярости не напал на деревню. ')
                self.label3 = Label(self.Oleg_info2, text = 'Родители Олегины спрятали её в храме где она не старея спала много лет...')
 
                
                asdd = '#a4c238'
                self.label['bg'] = asdd
                self.label2['bg']= asdd
                self.label3['bg']= asdd
       
                self.label.grid()
                self.label2.grid()
                self.label3.grid()
                #self.label4.grid()
                #self.label5.grid()
          def info_straje(self):
                self.straje_info2 = Toplevel()
                self.straje_info2.title('Всевидящий страж')
                self.straje_info2.resizable(False, False)
                self.straje_info2.geometry('700x150+{}+{}'.format(self.w,self.h))
                self.straje_info2['bg'] = '#7a29a3'
                self.label = Label(self.straje_info2, text = 'Всевидящий страж')
                self.label2 = Label(self.straje_info2, text = '- Это 20 метровый голем охраняющий врата небесного царства. Он обладает щитом способным отразить все что он видит, ')
                self.label3 = Label(self.straje_info2, text = 'эта сила заключена в его глазах. Не смотря на свой размер он довольно быстр.')
                self.label4 = Label(self.straje_info2, text = 'Но в один момент его подчинил Гриша дабы запалучить его мощь себе, но Грише помешали gfh,bambaleyla и Ai-vani.')
                self.label5 = Label(self.straje_info2, text = 'В результате этой битвы страж был разрушен, а его единственый уцелевший глаз забрал gfh')
                
                asdd = '#808080'
                self.label['bg'] = asdd
                self.label2['bg']= asdd
                self.label3['bg']= asdd
                self.label4['bg']= asdd
                self.label5['bg']= asdd

                self.label.grid()
                self.label2.grid()
                self.label3.grid()
                self.label4.grid()
                self.label5.grid()
          def info_craboid(self):
                self.craboid_info2 = Toplevel()
                self.craboid_info2.title('Крабоид')
                self.craboid_info2.resizable(False, False)
                self.craboid_info2.geometry('740x150+{}+{}'.format(self.w,self.h))
                self.craboid_info2['bg'] = '#b0b7c6'
                self.label = Label(self.craboid_info2, text = 'Крабоид')
                self.label2 = Label(self.craboid_info2, text = 'До нападения гришы на деревню Олегины, Крабоид был питомцем Олегины, но в те времна его размер не превышал обычного краба. ')
                self.label3 = Label(self.craboid_info2, text = 'Когда Олегину отправили в храм, Крабоид еле спасся. Он долго скитался в попытках найти себе новый дом, ')
                self.label4 = Label(self.craboid_info2, text = 'и вот, спустя долгое, время он нашел грибную пещеру где и стал жить долгие годы.')
                self.label5 = Label(self.craboid_info2, text = 'В печали и тоске....')
                
                asdd = '#a6bdd7'
                self.label['bg'] = asdd
                self.label2['bg']= asdd
                self.label3['bg']= asdd
                self.label4['bg']= asdd
                self.label5['bg']= asdd

                self.label.grid()
                self.label2.grid()
                self.label3.grid()
                self.label4.grid()
                self.label5.grid()
          def info_grisha(self):
                self.grisha_info2 = Toplevel()
                self.grisha_info2.title('Гриша')
                self.grisha_info2.resizable(False, False)
                self.grisha_info2.geometry('540x350+{}+{}'.format(self.w,self.h))
                self.grisha_info2['bg'] = '#654321'
                self.label = Label(self.grisha_info2, text = 'Гриша')
                self.label2 = Label(self.grisha_info2, text = 'Долгое время назад Гриша был великим колдуном и лучшим выпускником школы ')
                self.label3 = Label(self.grisha_info2, text = 'вихря. Школа вихря - это величественное здание с не менее великой ')
                self.label4 = Label(self.grisha_info2, text = 'историей. Все было хорошо, пока однажды, на школу вихря не напала армия ')
                self.label5 = Label(self.grisha_info2, text = 'нежити. Король, которому директор школы отправил письмо с просьбой о помощи, решил, что ')
                self.label6 = Label(self.grisha_info2, text = 'школа и сама справится. Но школа была разрушена. Гриша был опечален этим и его ')
                self.label7 = Label(self.grisha_info2, text = 'охватила ярость .Он захотел отомстить, но даже такому могучему колдуну как Гриша в ')
                self.label8 = Label(self.grisha_info2, text = 'одиночку одолеть армию было бы невозможно. И он начал искать силы и нашел. ')
                self.label9 = Label(self.grisha_info2, text = 'Рассеянные разрушением школы чары раскрыли там шляпу дарующею ')
                self.label10 = Label(self.grisha_info2, text = 'невероятные силы. Надев эту шляпу, Гришу охватил еще больший гнев в порыве ')
                self.label11 = Label(self.grisha_info2, text = 'которого он уничтожил деревню Олегины. Немного придя в себя он понял что настоящая ')
                self.label12 = Label(self.grisha_info2, text = 'месть свершится когда он уничтожит всё, что дорого Королю. Для достижения этой цели он решил  ')
                self.label13 = Label(self.grisha_info2, text = 'захватить всевидящего стража  охраняющего небесные врата, но ему помешали ')
                self.label14 = Label(self.grisha_info2, text = 'полубоги охраняющие этот мир. Грише пришлось бежать, но как раз в это время начала ')
                self.label15 = Label(self.grisha_info2, text = 'пробуждаться Олегина и Гриша решил завербовать её, чтобы та устранила для него ')
                self.label16 = Label(self.grisha_info2, text = 'могущественных существ и он смог восстановить силы их душами.')
                asdd = '#a4c238'
                self.label['bg'] = asdd
                self.label2['bg']= asdd
                self.label3['bg']= asdd
                self.label4['bg']= asdd
                self.label5['bg']= asdd
                self.label6['bg'] = asdd
                self.label7['bg']= asdd
                self.label8['bg']= asdd
                self.label9['bg']= asdd
                self.label10['bg']= asdd
                self.label11['bg'] = asdd
                self.label12['bg']= asdd
                self.label13['bg']= asdd
                self.label14['bg']= asdd
                self.label15['bg']= asdd
                self.label16['bg']= asdd
                

                self.label.grid()
                self.label2.grid()
                self.label3.grid()
                self.label4.grid()
                self.label5.grid()
                self.label6.grid()
                self.label7.grid()
                self.label8.grid()
                self.label9.grid()
                self.label10.grid()
                self.label11.grid()
                self.label12.grid()
                self.label13.grid()
                self.label14.grid()
                self.label15.grid()
                self.label16.grid()
          def info_gfh(self):
                self.gfh_info2 = Toplevel()
                self.gfh_info2.title('gfh')
                self.gfh_info2.resizable(False, False)
                self.gfh_info2.geometry('500x500+{}+{}'.format(self.w,self.h))
                self.gfh_info2['bg'] = '#77DDE7'
                self.labe0l = Label(self.gfh_info2, text = 'gfh ')
                self.label = Label(self.gfh_info2, text = 'Когда то давно родился юнец у которого был талант к заклинаниям. Свей первое  ')
                self.label2 = Label(self.gfh_info2, text = 'заклинание он прочёл в 5 лет.')
                self.label5 = Label(self.gfh_info2, text = 'Жил гфх в крупном городе в котором имелась огромная библиотека .Но спустя ')
                self.label6 = Label(self.gfh_info2, text = 'время  гфх стало не хватать знаний хранящихся в ней, и он начал исследовать')
                self.label7 = Label(self.gfh_info2, text = 'древние руины. Некоторые заклинания были настолько сильные, что даже при ')
                self.label8 = Label(self.gfh_info2, text = 'немаленькой по человеческим меркам запасе сил гфх их стало не хватать.')
                self.label9 = Label(self.gfh_info2, text = 'В поисках решения этой проблемы гфх проводил много исследований.')
                self.label16 = Label(self.gfh_info2, text = 'Гфх долго не мог найти способ, пока однажды ')
                self.label17 = Label(self.gfh_info2, text = 'один из его артефактов не засек всплеск энергии. Гфх тут-же направился к её ')
                self.label18 = Label(self.gfh_info2, text = 'источнику, это оказался комок энергии оставленый на мгновение переместившимся ')
                self.label19 = Label(self.gfh_info2, text = 'сюда непостижимо сильным существом. Прикоснувшись к нему он впитался гфх ')
                self.label20 = Label(self.gfh_info2, text = 'наделив его колоссально огромными силами, а его глаза начали светится ')
                self.label21 = Label(self.gfh_info2, text = 'от той мощи, что он получил.')
                self.label24 = Label(self.gfh_info2, text = 'У него ушли годы на освоение этой силы. Один раз он зарядил ими тот артефакт, ')
                self.label26 = Label(self.gfh_info2, text = 'который помог ему найти сгусток энергии, и он указал на далёкий скрытый храм. ')
                self.label27 = Label(self.gfh_info2, text = 'Благодаря новой силе гфх смог к нему пройти. В этом храме он узнал о других ')
                self.label28 = Label(self.gfh_info2, text = 'мирах. Там же он нашел артефакт создающий проходы в пространстве ')
                self.label29 = Label(self.gfh_info2, text = 'за пределами этого мира, это место гфх прозвал сюжетной дырой  ')  
                self.label30 = Label(self.gfh_info2, text = 'Вдохновлённый существованием другихмиро, гфх решил покинуть свой дом ')
                self.label31 = Label(self.gfh_info2, text = 'и отправится на их исследование.')
             
                asdd = '#FFFFFF'
                self.labe0l['bg'] = asdd
                self.label['bg'] = asdd
                self.label2['bg']= asdd
                #self.label3['bg']= asdd
                #self.label4['bg']= asdd
                self.label5['bg']= asdd
                self.label6['bg'] = asdd
                self.label7['bg']= asdd
                self.label8['bg']= asdd
                self.label9['bg']= asdd
                #self.label10['bg']= asdd
                #self.label11['bg'] = asdd
                ##self.label12['bg']= asdd
                #self.label13['bg']= asdd
                #self.label14['bg']= asdd
                #self.label15['bg']= asdd
                self.label16['bg'] = asdd
                self.label17['bg']= asdd
                self.label18['bg']= asdd
                self.label19['bg']= asdd
                self.label20['bg']= asdd                
                self.label21['bg'] = asdd
                #self.label22['bg']= asdd
                #self.label23['bg']= asdd
                self.label24['bg']= asdd
                #self.label25['bg']= asdd
                self.label26['bg'] = asdd
                self.label27['bg']= asdd
                self.label28['bg']= asdd
                self.label29['bg']= asdd
                self.label30['bg']= asdd
                self.label31['bg'] = asdd
             
                self.labe0l.grid()
                self.label.grid()
                self.label2.grid()
                #self.label3.grid()
                #self.label4.grid()
                self.label5.grid()
                self.label6.grid()
                self.label7.grid()
                self.label8.grid()
                self.label9.grid()
                #self.label10.grid()
                #self.label11.grid()
                #self.label12.grid()
                #self.label13.grid()
                #self.label14.grid()
                #self.label15.grid()
                self.label16.grid()
                self.label17.grid()
                self.label18.grid()
                self.label19.grid()
                self.label20.grid()              
                self.label21.grid()
                #self.label22.grid()
                #self.label23.grid()
                self.label24.grid()
                #self.label25.grid()
                self.label26.grid()
                self.label27.grid()
                self.label28.grid()
                self.label29.grid()
                self.label30.grid()
                self.label31.grid()
             
          def info_aivani(self):
              
                self.ai_vani_info2 = Toplevel()
                self.ai_vani_info2.title('Ai_vani')
                self.ai_vani_info2.resizable(False, False)
                self.ai_vani_info2.geometry('560x500+{}+{}'.format(self.w,self.h))
                self.ai_vani_info2['bg'] = '#000A22'
                self.label = Label(self.ai_vani_info2, text = 'Ai_vani')
                
                self.label2 = Label(self.ai_vani_info2, text = 'В стародавние времена, когда Боги ещё не ушли из этого мира, уже существовали люди.\nЭти люди развивались во всех аспектах. ')
                self.label3 = Label(self.ai_vani_info2, text = 'Со временем, когда людей становилось всё больше, а их жизнь стала гораздо проще, \nлюдям это стало надоедать и они начали становиться раздражительными. ')
                self.label4 = Label(self.ai_vani_info2, text = 'Со временем, их раздражение переросло в гнев. Гнев, что поражал жизни простых \nсельчан, с течением времени разрастался.')
                self.label5 = Label(self.ai_vani_info2, text = 'Этот гнев стал преобразовываться в Тёмную оболочку. Тёмная оболочка росла и \n становилась всё более смертельной')
                self.label6 = Label(self.ai_vani_info2, text = 'Со временем люди осознали, что стоит за убийством крестьян. Они начали \nпробовать всевозможные способы изгнать  Тьму из их мира, \nдабы жизнь крестьян стала спокойней.')
                self.label7 = Label(self.ai_vani_info2, text = 'Так, однажды они обратились за помощью к богам.  Те же, на удивление, \nуслышали их зов и решили спасти жизни сельчанам. Спустя некоторое время раздумий, \nони решили собрать всю  Тьму по миру в единую оболочку, заколдовав её. ')
                self.label8 = Label(self.ai_vani_info2, text = 'Эта тёмная оболочка больше не могла разрушать жизни крестьян, из-за чего\n постоянно становилась всё печальней.  С какого-то момента, \nОна стала принимать смутную форму, напоминающую человека.')
                self.label9 = Label(self.ai_vani_info2, text = 'У неё появились разум и способности, которыми она не могла пользоваться.  \nТёмная оболочка обратилась к богам с просьбой дать силы обуздать свои магические \nумения, на что те за издевательства над людьми решили проклясть её.')

                self.label10 = Label(self.ai_vani_info2, text = 'Они заточили тьму в тёмную мантию, с помощью которой  Тьма могла наконец \nпользоваться своими силами, но при этом обязываясь защищать людей от тёмных сил.')
                self.label11 = Label(self.ai_vani_info2, text = 'С тех пор Оболочка скрывается от людей и постоянно спасает их от возможных \nбед, пребывая в бесконечной печали.')
                asdd = '#244590'
                self.label['bg'] = asdd
                #self.label['text'] = '#FFFFFF'
                self.label2['bg']= asdd
                self.label3['bg']= asdd
                self.label4['bg']= asdd
                self.label5['bg']= asdd
                self.label6['bg']= asdd
                self.label7['bg']= asdd
                self.label8['bg']= asdd
                self.label9['bg']= asdd
                self.label10['bg']= asdd
                self.label11['bg']= asdd


                self.label.grid()
                self.label2.grid()
                self.label3.grid()
                self.label4.grid()
                self.label5.grid()
                self.label6.grid()
                self.label7.grid()
                self.label8.grid()
                self.label9.grid()
                self.label10.grid()
                self.label11.grid()


          def settings(self):
                    self.click_button_sound.play()
                    self.settings_tk = Toplevel()
                    self.settings_tk.title('Settings')
                    self.settings_tk.resizable(False, False)
                    self.settings_tk.geometry('300x300+{}+{}'.format(self.w,self.h))
                    self.geometry = Label(self.settings_tk, text = 'Величина игрового окна:')
                    self.geometry_300x300 = Button(self.settings_tk, text = '300x300', command = self.rez300x300)
                    self.geometry_480x480 = Button(self.settings_tk, text = '480x480', command = self.rez480x480)
                    self.geometry.pack()
                    self.geometry_300x300.pack()
                    self.geometry_480x480.pack()
          def rez300x300(self):
                    self. click_button_sound.play()
                    self.x = 300
                    self.y = 300
                    root.geometry('{}x{}+{}+{}'.format(self.x, self.y, self.w,self.h))
                    self.settings_tk.geometry('300x300+{}+{}'.format(self.w,self.h))
          def rez480x480(self):
                    self.click_button_sound.play()
                    self.x = 480
                    self.y = 480
                    root.geometry('{}x{}+{}+{}'.format(self.x, self.y, self.w,self.h))
                    self.settings_tk.geometry('480x480+{}+{}'.format(self.w,self.h))
          def game(self):
            root.destroy()
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
            atk_Grisha = -1
            H = 700
            x = W//2
            y = H//2
            progruzka_levela = 1
            sc = pygame.display.set_mode((W, H))
            Oleg_amulet=False#артефакт айвани
            vzat=0#артефакт чёрта
            Oleg_sigara=False#сигарета
            Oleg_eye=False
            no_two_gfh = False
            class Hero_sprite(pygame.sprite.Sprite):
                      def __init__(self, x, y, filename):
                                pygame.sprite.Sprite.__init__(self)
                                self.image = pygame.image.load(filename).convert_alpha()
                                self.rect = self.image.get_rect(center = (x,y))
            def polozhenie_personazha(x_pers,y_pers): #ипользуется при прорисовки уровней для экономии строк
                sprite_hero_walk_left_1.rect.x = x_pers
                sprite_hero_walk_left_1.rect.y = y_pers
            
                   
            sprite_hero_walk_left_1 = Hero_sprite(W//2,H//2, 'Data/images/the main character/Player_left_1.png')
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
            
            sprite_hero_attack_2_l = Hero_sprite(x,y, 'Data/images/the main character/attack/atk_left/Sprite_attack_hero_2.png')
            sprite_hero_attack_3_l = Hero_sprite(x,y, 'Data/images/the main character/attack/atk_left/Sprite_attack_hero_3.png')
            sprite_hero_attack_4_l = Hero_sprite(x,y, 'Data/images/the main character/attack/atk_left/Sprite_attack_hero_4.png')
            sprite_hero_attack_5_l = Hero_sprite(x,y, 'Data/images/the main character/attack/atk_left/Sprite_attack_hero_5.png')
            sprite_hero_attack_6_l = Hero_sprite(x,y, 'Data/images/the main character/attack/atk_left/Sprite_attack_hero_6.png')
            sprite_hero_attack_7_l = Hero_sprite(x,y, 'Data/images/the main character/attack/atk_left/Sprite_attack_hero_7.png')
            speed_attack_anim = 30
            speed_attack_anim_check = 0
            ##загрузка
            self.conn = sqlite3.connect('gameinfo.db')
            self.cur = self.conn.cursor()
            self.slotcheck1="""SELECT * from Saves"""
            self.cur.execute(self.slotcheck1)
            self.slotcheck=self.cur.fetchall()
            if self.choosencharacter==1:
                location=int(self.slotcheck[0][4])
                if self.developer == True:    
                    print("save 1: location selected")
            elif self.choosencharacter==2:
                location=int(self.slotcheck[1][4])
                if self.developer == True:    
                    print("save 2: location selected")
            else:
                print("\n")
##            else:
##                location=int(self.slotcheck[2][4])
##                if self.developer == True:    
##                    print("save 3: location selected")
            self.conn.commit()
            self.cur.close()

            ##########################проверка артефактов
            ##проверка артефакта айвани
            if self.choosencharacter==1 and self.slotcheck[0][6]==1:
                Oleg_amulet=True
                if self.developer == True:    
                    print("save 1: Ai_vani's artifact collected")
            elif self.choosencharacter==2 and self.slotcheck[1][6]==1:
                Oleg_amulet=True
                if self.developer == True:    
                    print("save 2: Ai_vani's artifact collected")
##            elif self.choosencharacter==3 and self.slotcheck[2][6]==1:
##                Oleg_amulet=True
##                if self.developer == True:    
##                    print("save 3: Ai_vani's artifact collected")
            else:
                if self.developer == True:    
                    print("\n")
            if Oleg_amulet == True:
                cord_x = sprite_hero_walk_left_2.rect.x
                cord_y = sprite_hero_walk_left_2.rect.y
                sprite_hero_walk_left_1.kill()
                sprite_hero_walk_left_1_2.kill()
                sprite_hero_walk_left_1_1.kill()
                sprite_hero_stand_1.kill()
                sprite_hero_walk_right_1.kill()
                sprite_hero_walk_right_1_1.kill()
                sprite_hero_walk_right_1_2.kill()
                sprite_hero_walk_left_1 = Hero_sprite(cord_x, cord_y, 'Data/images/the main character/Player_left_1_amulet.png')

                sprite_hero_walk_left_1_1 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_left_2_amulet.png')
                sprite_hero_walk_left_1_2 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_left_3_amulet.png')
                sprite_hero_walk_left_2 = Hero_sprite(cord_x, cord_y, 'Data/images/the main character/Player_left_3_amulet.png')

                sprite_hero_stand_1 = Hero_sprite(cord_x, cord_y, 'Data/images/the main character/stand_player_amulet.png')

                sprite_hero_walk_right_1 = Hero_sprite(cord_x, cord_y, 'Data/images/the main character/Player_right_1_amulet.png')
                sprite_hero_walk_right_1_1 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_right_2_amulet.png')
                sprite_hero_walk_right_1_2 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_right_3_amulet.png')

                sprite_hero_falling_1 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_Falling_amulet.png')
            ##проверка артефакта гфх
            Oleg_eye = False
            if self.choosencharacter==1 and self.slotcheck[0][7]==True:
                vzat=1
                Oleg_eye=True
                if self.developer == True:    
                    print("save 1: GFH's artifact collected")
            elif self.choosencharacter==2 and self.slotcheck[1][7]==True:
                vzat=1
                Oleg_eye=True
                if self.developer == True:    
                    print("save 2: GFH's artifact collected")
##            elif self.choosencharacter==3 and self.slotcheck[2][7]==True:
##                vzat=1
##                Oleg_eye=True
##                if self.developer == True:    
##                    print("save 3: GFH's artifact collected")
            else:
                if self.developer == True:    
                    print("\n")

           # print('OLEG EYE: ',Oleg_eye)
            ##проверка артефакта бамбы
            if self.choosencharacter==1 and self.slotcheck[0][8]==1:
                Oleg_sigara=True
                if self.developer == True:    
                    print("save 1: Bambaleyla's artifact collected")
            elif self.choosencharacter==2 and self.slotcheck[1][8]==1:
                Oleg_sigara=True
                if self.developer == True:    
                    print("save 2: Bambaleyla's artifact collected")
##            elif self.choosencharacter==3 and self.slotcheck[2][8]==1:
##                Oleg_sigara=True
##                if self.developer == True:    
##                    print("save 3: Bambaleyla's artifact collected")
            else:
                if self.developer == True:    
                    print("\n")
            ##
            
            text_color = (240, 230, 140)

            blood_puddle = pygame.sprite.Group()
            walle = pygame.sprite.Group()
            spikes = pygame.sprite.Group()
            moving_block = pygame.sprite.Group()
            attack_hero = pygame.sprite.Group()
            trigger_red_button = pygame.sprite.Group()
            trigger_orange_button = pygame.sprite.Group()
            not_active_trigger_wall = pygame.sprite.Group()
            decoration = pygame.sprite.Group()
            falling_blocks = pygame.sprite.Group()
            trigers =pygame.sprite.Group()
            particles =pygame.sprite.Group()
            particles_amulet =pygame.sprite.Group()
            evil = pygame.sprite.Group()
            boss_collison =pygame.sprite.Group()
            decoration_attack = pygame.sprite.Group()
            for_pause = pygame.sprite.Group()

            particles_list = []
            particles_na_rasstrel = []
            Characters_for_dialog =pygame.sprite.Group()
            dialoge_check = 0
            ai_vani_anim = 320
            ai_vani_anim_check = 0
            trigger_red_button_check = False
            crush_wall_on = False
            no_two = False
            attack_hero.add(sprite_hero_attack_1)
            attack_hero.add(sprite_hero_attack_2)
            attack_hero.add(sprite_hero_attack_3)
            attack_hero.add(sprite_hero_attack_4)
            attack_hero.add(sprite_hero_attack_5)
            attack_hero.add(sprite_hero_attack_6)
            attack_hero.add(sprite_hero_attack_7)
            attack_hero.add(sprite_hero_attack_2_l)
            attack_hero.add(sprite_hero_attack_3_l)
            attack_hero.add(sprite_hero_attack_4_l)
            attack_hero.add(sprite_hero_attack_5_l)
            attack_hero.add(sprite_hero_attack_6_l)
            attack_hero.add(sprite_hero_attack_7_l)
            click_z = False
            spike_texture_1 = 0
            spike_texture_2 = 0
            play_music_grisha = False
            spike_texture_3 = 0
            spike_check = 0
            mov_block_napravlenie = 'up'
            evil_napravlenie = 'left'
            perehod_y = 10
            Grisha_alive = True

            udar_vlev = True
            udar_vprav = True

            FPS = 220
            key_z = 50
            artefact_go = 0
            key_z_check = 0
            #main_music_loca1 = pygame.mixer.music.load('Data/music/music_loca_1.ogg')
            pygame.init()
            main_music_loca1 = pygame.mixer.Sound('Data/music/music_loca_1_1.ogg') 
            #main_music_loca1_2 = pygame.mixer.Sound('Data/music/music_loca_1_2.ogg') 
            Ai_vani_secret_music = pygame.mixer.Sound('Data/music/music_secret_aivani.ogg') 
            bambaleyla_secret_music = pygame.mixer.Sound('Data/music/bambaleyla_music.ogg')
            Grisha_music = pygame.mixer.Sound('Data/music/Grisha_music.ogg')
            titles_music = pygame.mixer.Sound('Data/music/titles_music.ogg')

            mysterious_whisper = pygame.mixer.Sound('Data/sounds/mysterious_whisper.mp3')
            breaking_tree_sound = pygame.mixer.Sound('Data/sounds/breaking_tree_sound.mp3')
            player_punch_sound = pygame.mixer.Sound('Data/sounds/player_punch.mp3')
            first_boss_death = pygame.mixer.Sound('Data/sounds/first_boss_death.wav')
            die_beatle = pygame.mixer.Sound('Data/sounds/beatle_die.mp3')
            die_snake = pygame.mixer.Sound('Data/sounds/die_snake.mp3')
            laser_atk = pygame.mixer.Sound('Data/sounds/laser_atk.mp3')
            die_skeleton= pygame.mixer.Sound('Data/sounds/die_skeleton.mp3')
            fart_bambaleyla= pygame.mixer.Sound('Data/sounds/bambaleyla_fart.mp3')
            bunch_bambaleyla= pygame.mixer.Sound('Data/sounds/bunch.mp3')
            crush_wall_bambaleyla= pygame.mixer.Sound('Data/sounds/crush_bambaleyla_wall.mp3')

            lazer_sound_1= pygame.mixer.Sound('Data/sounds/lazer_sound_1.mp3')
            lazer_sound_2= pygame.mixer.Sound('Data/sounds/lazer_sound_2.mp3')
            lazer_sound_3= pygame.mixer.Sound('Data/sounds/lazer_sound_3.mp3')
            lazer_sound_4= pygame.mixer.Sound('Data/sounds/lazer_sound_4.mp3')

            departure_sound= pygame.mixer.Sound('Data/sounds/departure.mp3')
            break_spikes= pygame.mixer.Sound('Data/sounds/break_spikes.mp3')

            #main_music_loca1_3 = pygame.mixer.Sound('Data/music/music_loca_1_3.ogg') 

            music_loca_1 = [main_music_loca1]#, main_music_loca1_2]#, main_music_loca1_3]

            #main_menu_music = pygame.mixer.Sound('main_menu_music_1.ogg') 

            lenght_main_music_loca1 = main_music_loca1.get_length()
            jump_sound = pygame.mixer.Sound('Data/sounds/jump_sound.wav')
            #die_sound = pygame.mixer.Sound('Data/sounds/jump_sound.wav')
            die_sound = pygame.mixer.Sound('Data/sounds/die_sound.wav')
            ominous_laughter_aivani = pygame.mixer.Sound('Data/sounds/ominous_laughter.mp3') 
            die_caban_sound = pygame.mixer.Sound('Data/sounds/die_caban_sound.mp3') 
            na_rasstrel = []
            FPS = 220
            dialoge_grisha = False
            moving = False
            particles_spisok = ['Data/images/particles/Ai_vani_particle_1.png', 'Data/images/particles/Ai_vani_particle_2.png']
            udar_vpravo = False
            map_number = 0 #номер локации. Не комнаты
            ai_vani_secret_room = False


            particles_amulet_list = []
            particle_amulet_check = 0
            particle_amulet = 65
            
            wall = Hero_sprite(25,350, 'Data/images/walls/wall_vertical_loca_1.png')
            wall2 = Hero_sprite(650, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
            wall3 = Hero_sprite(1275,250, 'Data/images/walls/wall_vertical_loca_pre_exit_1.png')
            text_frame = Hero_sprite(650, 200, 'Data/images/walls/frame_loca_1.png')

            background_loca_1 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_1.png')
            background_loca_2 = Hero_sprite(x,y-25, 'Data/images/backgrounds/bg_loca_2.png')
            background_loca_3 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_3.png')
            background_loca_4 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_4.png')
            background_Ai_vani_room = Hero_sprite(x,y, 'Data/images/backgrounds/Ai_vani_bg_room.png')
            background_loca_gfh = Hero_sprite(x,y, 'Data/images/backgrounds/bg_gfh.png')
            background_bambaleyla_room = Hero_sprite(x,y, 'Data/images/backgrounds/bambaleyla_bg_room.png')
            background_abyss = Hero_sprite(x,y, 'Data/images/backgrounds/bg_abyss.png')
            floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_1.png')
            font = pygame.font.Font(None, 36)
            
            if location == 0 and map_number == 0:
                            text = font.render(
                                "Для ходьбы испрользуйте клавиши A и D", True, (text_color))
                            place = text.get_rect(
                                center=(650, 200))

                            na_rasstrel.append(wall2)
                            na_rasstrel.append(floor_loca_1)
                            na_rasstrel.append(wall)
                            na_rasstrel.append(wall3)
                            na_rasstrel.append(text_frame)
                            decoration.add(text_frame)
                            walle.add(wall2)
                            walle.add(floor_loca_1)
                            walle.add(wall)
                            walle.add(wall3)
                            
            clock = pygame.time.Clock()
            
            speed_change_walk = 32
            can_moving = True
            particle_aivani = 35
            particle_aivani_check = 0
            speed_change_walk_check = 0
            jump_power = 100#высота прыжка
            jump_power_check = 0#проверка высоты прыжка
            jumping = False#проверка на прыжок в настоящее время
            jumping_wall = False#для коллизии с потолком
            falling = False
            jumping_wall_check = 0#проверка коллизии с потолком
            perehod_x = 1200
            level_number = 1
            music_loca_1_check = random.randint(0,(len(music_loca_1) -1))
            secret_bambaleyla = False
            sec = 0
            credits_loca_1_check = 0
            music_loca_1[music_loca_1_check].play()
            pause = False
            schetcik_pause = 0
            progruzka_levela_gfh = 0
            gfh_level = False
            no_two_bambaleyla = False
            blackout = Hero_sprite(x,y, 'Data/images/decorations/blackout.png')
            while 1:
                   
                                 sec +=0.0047
                   #try:        
                                 for i in pygame.event.get():
                                        if i.type == pygame.QUIT:
                                               pygame.quit()          
                                 if sec > music_loca_1[music_loca_1_check].get_length():
                                   sec = 0
                                   music_loca_1[music_loca_1_check].stop()  
                                   music_loca_1_check = random.randint(0,(len(music_loca_1) -1))
                                   music_loca_1[music_loca_1_check].play()  
                          
                        #---------------------------------------------это херня для передвежения не трогать это чтобы gfh не путался в этом непонятном коде так что не оброщайте внимания --------------------------------------------------
#                          if i.type != pygame.QUIT:
                                 keys = pygame.key.get_pressed()
                                 pressed = pygame.mouse.get_pressed()
                                 if pause ==  True:
                                         pause_sign = Hero_sprite(650,350, 'Data/images/decorations/pause.png')
                                         
                                         for_pause.add(pause_sign)
                                         
                                 if keys[pygame.K_q]:
                                    
                                         if pause ==  True:
                                             
                                                 pause = False
                                         else:       
                                             pause = True
                                             walle.draw(sc)
                                             spikes.draw(sc)
                                             moving_block.draw(sc)
                                             falling_blocks.draw(sc)
                                             trigger_red_button.draw(sc)
                                             trigger_orange_button.draw(sc)
                                             not_active_trigger_wall.draw(sc)
                                             trigers.draw(sc)
                                             particles.draw(sc)
                                             particles_amulet.draw(sc)
                                             evil.draw(sc)
                                             boss_collison.draw(sc)
                                             sc.blit(sprite_hero_stand_1.image, sprite_hero_stand_1.rect)
                                             sc.blit(blackout.image, blackout.rect)
                                         time.sleep(0.25)
                                         
                                 
                                        
                                 if pause ==  True:
                                     
                                     
                                     
                                     for_pause.draw(sc)
                                     pygame.display.update()
                                     continue
                                    
                           
                                         
                                 
                                       
                                 if keys[pygame.K_z]:
                                    if self.developer == True:
                                        if key_z_check == key_z and key_z == 50:
                                            key_z_check = 0
                                            if location < 30:
                                                for ii in na_rasstrel:
                                                    ii.kill()
                                                location +=1
                                                progruzka_levela = 1
                                            elif location == 30:
                                                  hp_gregory = -1
                                                  speed_spawn_particle_atk_0 = 150
                                                  speed_spawn_particle_atk_0_check = 0
                                                  parts_atk_0 = []
                                                  Grisha_music.stop()
                                                  parts_atk_0_in_laser = []
                                                  laser_atk_0_sprite_1 = []
                                                  atk_Grisha = 4
                                            else:
                                                print('it`s last loca')

                                        if ai_vani_secret_room == True:
                                            Ai_vani_secret_music.stop()
                                            music_loca_1[music_loca_1_check].play()
                                            ai_vani_secret_room= False
                                        key_z_check +=1
                                 elif keys[pygame.K_p] :
                                    if self.developer == True:
                                        progruzka_levela = 1
                                    
                                        for ii in na_rasstrel:
                                            ii.kill()
                                        location = 28
                                       
                                        
                                        time.sleep(0.25)
                                 elif keys[pygame.K_u] :
                                    if self.developer == True:
                                        for ii in na_rasstrel:
                                            ii.kill()
                                        location +=1
                                        progruzka_levela = 1 
                                
                                        
                                        time.sleep(0.25)
                                 if location != 30 and location != 31:

                                   if keys[pygame.K_a] and can_moving == True:
                                          sprite_hero_walk_left_2.rect.x -=1
                                          if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                                 moving = 'left'
                                                 speed_change_walk_check +=1
                                                 sprite_hero_walk_left_1.rect.x -= 1
                                          else:
                                                 sprite_hero_walk_left_2.rect.x +=1




                                                  
                                   elif keys[pygame.K_d] and can_moving == True:
                                          sprite_hero_walk_left_2.rect.x +=1
                                          if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) ==0:
                                                 speed_change_walk_check += 1
                                                 moving = 'right'
                                                 udar_vpravo = True
                                                 sprite_hero_walk_left_1.rect.x += 1

                                          else:
                                                 sprite_hero_walk_left_2.rect.x -=1


                                  
                                       
                                   if jumping == True or keys[pygame.K_w] and can_moving == True: 
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
                                   if keys[pygame.K_d]:
                                              if pressed[0] and can_moving == True or speed_attack_anim_check > 0 and can_moving == True:
                                                if udar_vprav == True or speed_attack_anim_check > 0:
                                                                sprite_hero_attack_1.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_1.rect.x = sprite_hero_walk_left_1.rect.x+25
                                                                sprite_hero_attack_2.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_2.rect.x = sprite_hero_walk_left_1.rect.x+25
                                                                sprite_hero_attack_3.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_3.rect.x = sprite_hero_walk_left_1.rect.x+25
                                                                sprite_hero_attack_4.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_4.rect.x = sprite_hero_walk_left_1.rect.x+25
                                                                sprite_hero_attack_5.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_5.rect.x = sprite_hero_walk_left_1.rect.x+25
                                                                sprite_hero_attack_6.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_6.rect.x = sprite_hero_walk_left_1.rect.x+25
                                                                sprite_hero_attack_7.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_7.rect.x = sprite_hero_walk_left_1.rect.x+25
                                                                #player_punch_sound.play()
                                                                speed_attack_anim_check +=1
                                                                if speed_attack_anim_check  < speed_attack_anim /7:
                                                                          player_punch_sound.play()
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
                                              else:
                                                speed_attack_anim_check = 0
                                   elif keys[pygame.K_a]:
                                                  if pressed[0] and can_moving == True or speed_attack_anim_check > 0 and can_moving == True:
                                                    if udar_vlev == True or speed_attack_anim_check > 0:
                                                                
                                                                sprite_hero_attack_2_l.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_2_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                                                sprite_hero_attack_3_l.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_3_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                                                sprite_hero_attack_4_l.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_4_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                                                sprite_hero_attack_5_l.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_5_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                                                sprite_hero_attack_6_l.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_6_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                                                sprite_hero_attack_7_l.rect.y = sprite_hero_walk_left_1.rect.y
                                                                sprite_hero_attack_7_l.rect.x = sprite_hero_walk_left_1.rect.x-85  
                                                                speed_attack_anim_check +=1
                                                                if speed_attack_anim_check  < speed_attack_anim /7 * 2:
                                                                          player_punch_sound.play()
                                                                          #sc.blit(sprite_hero_attack_2.image, sprite_hero_attack_2.rect)
                                                                          sc.blit(sprite_hero_attack_2_l.image, sprite_hero_attack_2_l.rect)
                                                                elif speed_attack_anim_check  < speed_attack_anim /7 * 3:
                                                                          sc.blit(sprite_hero_attack_3_l.image, sprite_hero_attack_3_l.rect)
                                                                elif speed_attack_anim_check  < speed_attack_anim /7 * 4:
                                                                          #sc.blit(sprite_hero_attack_4.image, sprite_hero_attack_4.rect)
                                                                          sc.blit(sprite_hero_attack_4_l.image, sprite_hero_attack_4_l.rect)
                                                                elif speed_attack_anim_check  < speed_attack_anim /7 * 5:
                                                                          #sc.blit(sprite_hero_attack_5.image, sprite_hero_attack_5.rect)
                                                                          sc.blit(sprite_hero_attack_5_l.image, sprite_hero_attack_5_l.rect)
                                                                elif speed_attack_anim_check  < speed_attack_anim /7 * 6:
                                                                          #sc.blit(sprite_hero_attack_6.image, sprite_hero_attack_6.rect)
                                                                          sc.blit(sprite_hero_attack_6_l.image, sprite_hero_attack_6_l.rect)
                                                                elif speed_attack_anim_check  < speed_attack_anim /7 * 7:
                                                                          #sc.blit(sprite_hero_attack_7.image, sprite_hero_attack_7.rect)
                                                                          sc.blit(sprite_hero_attack_7_l.image, sprite_hero_attack_7_l.rect)
                                                                else:
                                                                        speed_attack_anim_check = 0
                                                  else:
                                                    speed_attack_anim_check = 0
                                 #---------------------------------------------------------это чтобы gfh не путался в этом непонятном коде так что не оброщайте внимания---------------------------------------------------------------------
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
                                 
                                 if location == 10 or location == 11 or location == 12 or location == 13 or location == 14 or location >= 15:
                                    walle.draw(sc)
                                    decoration.draw(sc)
                                 else:
                                    walle.draw(sc)
                                 spikes.draw(sc)
                                 moving_block.draw(sc)
                                 falling_blocks.draw(sc)
                                 trigger_red_button.draw(sc)
                                 trigger_orange_button.draw(sc)
                                 not_active_trigger_wall.draw(sc)
                                 trigers.draw(sc)
                                 particles.draw(sc)
                                 particles_amulet.draw(sc)
                                 evil.draw(sc)
                                 boss_collison.draw(sc)
                                 pygame.display.update()
                                 
                                 sprite_hero_walk_left_2.rect = sprite_hero_walk_left_1.rect
                                 sprite_hero_walk_left_1_1.rect = sprite_hero_walk_left_1.rect
                                 sprite_hero_walk_left_1_2.rect = sprite_hero_walk_left_1.rect
                                 sprite_hero_stand_1.rect = sprite_hero_walk_left_1.rect
                                 sprite_hero_walk_right_1_1.rect = sprite_hero_walk_left_1.rect
                                 sprite_hero_walk_right_1_2.rect = sprite_hero_walk_left_1.rect
                                 sprite_hero_walk_right_1.rect = sprite_hero_walk_left_1.rect
                                 sprite_hero_falling_1.rect = sprite_hero_walk_left_1.rect
                                 
        
                                 if keys[pygame.K_d] and pressed[0] and udar_vprav == True and can_moving == True:
                                           sprite_hero_attack_1.rect.y = sprite_hero_walk_left_1.rect.y
                                           sprite_hero_attack_1.rect.x = sprite_hero_walk_left_1.rect.x+25
                                           sprite_hero_attack_2.rect.y = sprite_hero_walk_left_1.rect.y
                                           sprite_hero_attack_2.rect.x = sprite_hero_walk_left_1.rect.x+25
                                           sprite_hero_attack_3.rect.y = sprite_hero_walk_left_1.rect.y
                                           sprite_hero_attack_3.rect.x = sprite_hero_walk_left_1.rect.x+25
                                           sprite_hero_attack_4.rect.y = sprite_hero_walk_left_1.rect.y
                                           sprite_hero_attack_4.rect.x = sprite_hero_walk_left_1.rect.x+25
                                           sprite_hero_attack_5.rect.y = sprite_hero_walk_left_1.rect.y
                                           sprite_hero_attack_5.rect.x = sprite_hero_walk_left_1.rect.x+25
                                           sprite_hero_attack_6.rect.y = sprite_hero_walk_left_1.rect.y
                                           sprite_hero_attack_6.rect.x = sprite_hero_walk_left_1.rect.x+25
                                           sprite_hero_attack_7.rect.y = sprite_hero_walk_left_1.rect.y
                                           sprite_hero_attack_7.rect.x = sprite_hero_walk_left_1.rect.x+25
                                           sprite_hero_attack_1.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                           udar_vprav = False
                                           udar_vlev = False


                                           sprite_hero_attack_2_l.rect.y = -10000
                                            
                                           sprite_hero_attack_3_l.rect.y = -10000
                                           sprite_hero_attack_4_l.rect.y = -10000
                                           sprite_hero_attack_5_l.rect.y = -10000
                                           sprite_hero_attack_6_l.rect.y = -10000
                                           sprite_hero_attack_7_l.rect.y = -10000
                                 else:
                                  if pressed[0]and can_moving == True:
                                    pass
                                  else:
                                    udar_vprav = True
                                 if keys[pygame.K_a] and pressed[0] and udar_vlev == True and can_moving == True:#moving == 'left' and pressed[0] or  moving == 'jump'  :# moving == False and pressed[0]:
                                            udar_vlev = False
                                            udar_vprav = False
                                            sprite_hero_attack_2_l.rect.y = sprite_hero_walk_left_1.rect.y
                                            sprite_hero_attack_2_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                            sprite_hero_attack_3_l.rect.y = sprite_hero_walk_left_1.rect.y
                                            sprite_hero_attack_3_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                            sprite_hero_attack_4_l.rect.y = sprite_hero_walk_left_1.rect.y
                                            sprite_hero_attack_4_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                            sprite_hero_attack_5_l.rect.y = sprite_hero_walk_left_1.rect.y
                                            sprite_hero_attack_5_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                            sprite_hero_attack_6_l.rect.y = sprite_hero_walk_left_1.rect.y
                                            sprite_hero_attack_6_l.rect.x = sprite_hero_walk_left_1.rect.x-85
                                            sprite_hero_attack_7_l.rect.y = sprite_hero_walk_left_1.rect.y
                                            sprite_hero_attack_7_l.rect.x = sprite_hero_walk_left_1.rect.x-85  
                                            sprite_hero_attack_1.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                            sprite_hero_attack_1.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                            sprite_hero_attack_2.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                            sprite_hero_attack_2.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                            sprite_hero_attack_3.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                            sprite_hero_attack_3.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                            sprite_hero_attack_4.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                            sprite_hero_attack_4.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                            sprite_hero_attack_5.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                            sprite_hero_attack_5.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                            sprite_hero_attack_6.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                            sprite_hero_attack_6.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                            sprite_hero_attack_7.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                            sprite_hero_attack_7.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                 else:
                                  if pressed[0] and can_moving == True:
                                    pass
                                  else:
                                    udar_vlev = True

                                 moving = False
                                 #---------------------------------------------------------это чтобы gfh не путался в этом непонятном коде так что не оброщайте внимания---------------------------------------------------------------------
                                 sc.fill((0,0,0))
                                 if map_number == 0 and location < 9 and ai_vani_secret_room == False:
                                    sc.blit(background_loca_1.image, background_loca_1.rect)
                                    decoration.draw(sc)
                                 elif map_number == 1 or location >= 9 and ai_vani_secret_room == False and location <= 15: 
                                    sc.blit(background_loca_2.image, background_loca_2.rect)
                                    decoration.draw(sc)
                                 elif location > 15 and location < 23:
                                    sc.blit(background_loca_3.image, background_loca_3.rect)
                                 elif ai_vani_secret_room == True:
                                    sc.blit(background_Ai_vani_room.image, background_Ai_vani_room.rect)
                                 elif secret_bambaleyla == True:
                                    sc.blit(background_bambaleyla_room.image, background_bambaleyla_room.rect)
                                 elif location > 22 and location <30:
                                    sc.blit(background_loca_4.image, background_loca_4.rect)
                                 elif location == 30:
                                    sc.blit(background_abyss.image, background_abyss.rect)
                                 elif location == 333:
                                    sc.blit(background_loca_gfh.image, background_loca_gfh.rect)
                                 #elif map_number == 1:
                                 #   sc.blit(background_loca_2.image, background_loca_2.rect)
                                
                                 if location == 0:
                                     decoration.draw(sc)
                                     sc.blit(text, place)
                                 if location == 27:
                                  if sprite_hero_walk_left_2.rect.x > 1250:
                                    if sprite_hero_walk_left_2.rect.y > 500:
                                                for ii in na_rasstrel:
                                                    ii.kill()
                                                location +=2
                                                progruzka_levela = 1
                                    else:
                                      for ii in na_rasstrel:
                                        ii.kill()
                                      secret_bambaleyla = True
                                      music_loca_1[music_loca_1_check].stop()
                                      bambaleyla_secret_music.play()
                                    progruzka_levela = 1 
                                  if secret_bambaleyla == True:
                                    if sprite_hero_walk_left_2.rect.x < 0:
                                      secret_bambaleyla = False
                                      bambaleyla_secret_music.stop()
                                      music_loca_1[music_loca_1_check].play()
                                      progruzka_levela = 1 
                                      for ii in na_rasstrel:
                                        ii.kill()
                                 if sprite_hero_walk_left_1.rect.y > 730 :
                                     for ii in na_rasstrel:
                                                     ii.kill()
                                     progruzka_levela = 1
                                     die_sound.play()
                                 if sprite_hero_walk_left_1.rect.x > perehod_x or sprite_hero_walk_left_1.rect.y < perehod_y :
                                    trigger_red_button_check = False
                                    for ii in na_rasstrel:
                                        ii.kill()
                                    progruzka_levela = 1 
                                    location = level_number
                                    if ai_vani_secret_room == True:
                                        Ai_vani_secret_music.stop()
                                        music_loca_1[music_loca_1_check].play()
                                        ai_vani_secret_room= False
                                 if pygame.sprite.spritecollide(sprite_hero_walk_left_2, spikes,True):#шип 1
                                          progruzka_levela = 1
                                          die_sound.play()
                                          for ii in na_rasstrel:
                                                    ii.kill()
                                 if speed_attack_anim_check == 0 or progruzka_levela == 1: 
                                        speed_attack_anim_check = 0                                     
                                        sprite_hero_attack_1.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                        sprite_hero_attack_1.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                        sprite_hero_attack_2.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                        sprite_hero_attack_2.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                        sprite_hero_attack_3.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                        sprite_hero_attack_3.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                        sprite_hero_attack_4.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                        sprite_hero_attack_4.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                        sprite_hero_attack_5.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                        sprite_hero_attack_5.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                        sprite_hero_attack_6.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                        sprite_hero_attack_6.rect.x = sprite_hero_walk_left_1.rect.x-10000
                                        sprite_hero_attack_7.rect.y = sprite_hero_walk_left_1.rect.y-10000
                                        sprite_hero_attack_7.rect.x = sprite_hero_walk_left_1.rect.x-10000


                                        sprite_hero_attack_2_l.rect.y = -10000
                                        
                                        sprite_hero_attack_3_l.rect.y = -10000
                                        sprite_hero_attack_4_l.rect.y = -10000
                                        sprite_hero_attack_5_l.rect.y = -10000
                                        sprite_hero_attack_6_l.rect.y = -10000
                                        sprite_hero_attack_7_l.rect.y = -10000
                                 udar_vpravo = False
                                 if map_number == 0:
                                     if  location == 1:
                                               text = font.render("Для прыжков используйте клавишу W", True, (text_color))
                                               place = text.get_rect(center=(650, 200))
                                               decoration.draw(sc)
                                               sc.blit(text, place)
                                               
                                               if progruzka_levela == 1 :#1-1
                                                   self.conn = sqlite3.connect('gameinfo.db')
                                                   self.cur = self.conn.cursor()
                                                   if self.choosencharacter==1:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 1 updated")
                                                   elif self.choosencharacter==2:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 2 updated")
                                                   else:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 3 updated")
                                                   self.conn.commit()
                                                   self.cur.close()
                                                   text_frame = Hero_sprite(650, 200, 'Data/images/walls/frame_loca_1.png') 
                                                   polozhenie_personazha(200,450) #это отвечает за то где перса заспавнит на уровне
                                                   progruzka_levela = 0 # обезательно иначе уровень будет бесконечно прогружатьса
                                                   perehod_x = 1200 #куда надо дойти игроку что бы перейти на следующий левл  на следующий уровней есть такаяже но для у
                                                   level_number = 3 #на какой левл перекинет после этого
                                                   wall = Hero_sprite(25,350, 'Data/images/walls/wall_vertical_loca_1.png')
                                                   wall2 = Hero_sprite(650, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
                                                   wall3 = Hero_sprite(1275,250, 'Data/images/walls/wall_vertical_loca_pre_exit_1.png')
                                                   
                                          
                                                  
                

                                                 
                                                   floor_loca_1 = Hero_sprite(-190,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   platform  = Hero_sprite(700,645, 'Data/images/walls/2.png')
                                                   floor_loca_2 = Hero_sprite(1600,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   na_rasstrel.append(wall2)
                                                   na_rasstrel.append(text_frame)
                                                   na_rasstrel.append(floor_loca_1)
                                                   na_rasstrel.append(floor_loca_2)
                                                   na_rasstrel.append(wall)
                                                   na_rasstrel.append(wall3)
                                                   na_rasstrel.append(platform)
                                                   decoration.add(text_frame)
                                                   walle.add(platform)
                                                   walle.add(wall2)
                                                   walle.add(floor_loca_1)
                                                   walle.add(floor_loca_2)
                                                   walle.add(wall)
                                                   walle.add(wall3)
                                               
                                                   
                                     if  location == 2:
                                              if progruzka_levela == 1 :#1-2
                                                   self.conn = sqlite3.connect('gameinfo.db')
                                                   self.cur = self.conn.cursor()
                                                   if self.choosencharacter==1:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                    if self.developer == True:    
                                                            print("save 1 updated")
                                                   elif self.choosencharacter==2:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                    if self.developer == True:    
                                                            print("save 2 updated")
                                                   else:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                    if self.developer == True:    
                                                            print("save 3 updated")
                                                   self.conn.commit()
                                                   self.cur.close()
                                                   polozhenie_personazha(200,450)
                                                   progruzka_levela = 0
                                                   perehod_x = 1200
                                                   level_number = 3
                                                   wall = Hero_sprite(25,350, 'Data/images/walls/wall_vertical_loca_1.png')
                                                   wall2 = Hero_sprite(650, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
                                                   wall3 = Hero_sprite(1275,250, 'Data/images/walls/wall_vertical_loca_pre_exit_1.png')
                                                   
                                          
                                                  
                

                                                 
                                                   floor_loca_1 = Hero_sprite(-250,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   platform2  = Hero_sprite(500,645, 'Data/images/walls/2.png')
                                                   platform  = Hero_sprite(700,645, 'Data/images/walls/2.png')
                                                   platform1  = Hero_sprite(900,645, 'Data/images/walls/2.png')
                                                   floor_loca_2 = Hero_sprite(1800,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   na_rasstrel.append(wall2)
                                                   na_rasstrel.append(floor_loca_1)
                                                   na_rasstrel.append(floor_loca_2)
                                                   na_rasstrel.append(wall)
                                                   na_rasstrel.append(wall3)
                                                   na_rasstrel.append(platform)
                                                   na_rasstrel.append(platform1)
                                                   na_rasstrel.append(platform2)
                                                   walle.add(platform)
                                                   walle.add(platform1)
                                                   walle.add(platform2)
                                                   walle.add(wall2)
                                                   walle.add(floor_loca_1)
                                                   walle.add(floor_loca_2)
                                                   walle.add(wall)
                                                   walle.add(wall3)
                                     if  location == 3:
                                            text = font.render("При коллизии с шипами, ваш персонаж умрёт", True, (text_color))
                                            place = text.get_rect(center=(400, 200))
                                            decoration.draw(sc)
                                            sc.blit(text, place)   
                                               

                                              
                                            if progruzka_levela == 1 :#1-3
                                                   self.conn = sqlite3.connect('gameinfo.db')
                                                   self.cur = self.conn.cursor()
                                                   if self.choosencharacter==1:
                                                     self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                     if self.developer == True:    
                                                        print("save 1 updated")
                                                   elif self.choosencharacter==2:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 2 updated")
                                                   else:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 3 updated")
                                                   self.conn.commit()
                                                   self.cur.close()
                                                   polozhenie_personazha(200,450)
                                                   progruzka_levela = 0
                                                   perehod_x = 999999
                                                   level_number = 4
                                                   text_frame = Hero_sprite(400, 200, 'Data/images/walls/big_1_frame_loca_1.png') 
                                                   wall = Hero_sprite(25,350, 'Data/images/walls/wall_vertical_loca_1.png')
                                                   wall2 = Hero_sprite(100, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
                                                   wall3 = Hero_sprite(1275,350, 'Data/images/walls/wall_vertical_loca_1.png')
                                                   wall4 = Hero_sprite(1800, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
                                                   pika = Hero_sprite(525, 525, 'Data/images/spikes/sprite_spike_1.png')
                                                   pika1 = Hero_sprite(725, 350, 'Data/images/spikes/sprite_spike_1.png')
                                                   pika2 = Hero_sprite(925, 180, 'Data/images/spikes/sprite_spike_1.png')
                

                                                 
                                                   floor_loca_1 = Hero_sprite(-250,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   floor_loca_2 = Hero_sprite(1900,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   platform2  = Hero_sprite(500,545, 'Data/images/walls/2.png')
                                                   platform  = Hero_sprite(700,370, 'Data/images/walls/2.png')
                                                   platform1  = Hero_sprite(900,200, 'Data/images/walls/2.png')
                                                   na_rasstrel.append(text_frame)
                                                   na_rasstrel.append(wall2)
                                                   na_rasstrel.append(floor_loca_1)
                                                   na_rasstrel.append(floor_loca_2)
                                                   na_rasstrel.append(pika)
                                                   na_rasstrel.append(pika1)
                                                   na_rasstrel.append(pika2)
                                                   na_rasstrel.append(wall)
                                                   na_rasstrel.append(wall3)
                                                   na_rasstrel.append(wall4)
                                                   na_rasstrel.append(platform)
                                                   na_rasstrel.append(platform1)
                                                   na_rasstrel.append(platform2)
                                                   walle.add(platform)
                                                   walle.add(platform1)
                                                   walle.add(platform2)
                                                   walle.add(wall2)
                                                   walle.add(wall4)
                                                   walle.add(floor_loca_1)
                                                   decoration.add(text_frame)
                                                   walle.add(floor_loca_2)
                                                   
                                                   walle.add(wall)
                                                   walle.add(wall3)
                                                   spikes.add(pika)
                                                   spikes.add(pika1)
                                                   spikes.add(pika2)
                                     if location == 4:
                                               self.locationsave=location
                                               #
                                               
                                               text = font.render("Кнопки могут убирать стены", True, (text_color))
                                               text1 = font.render("Нажмите на кнопку ударив по ней, нажав ЛКМ при беге", True, (text_color))
                                               place = text.get_rect(center=(650, 200))
                                               place2 = text.get_rect(center=(475, 300))
                                               decoration.draw(sc)
                                               sc.blit(text, place)
                                               sc.blit(text1, place2)
                                               try:
                                                  #---------------------------------------------------------механику удаления стен кнопкой брать отсюда--------------------------------------------------------------------
                                                   if pygame.sprite.spritecollide(red_trigger_button_object, attack_hero, False)  :    
                                                               
                                                               
                                                               
                                                               red_trigger_button_object.kill()
                                                               red_trigger_wall.kill()
                                                               
                                                               red_click_trigger_button_object = Hero_sprite(55,560, 'Data/images/walls/clicked_trigger_red_button_vertical_1.png')
                                                               red_trigger_wall = Hero_sprite(99999,99999, 'Data/images/walls/trigger_red_wall_vertical_1.png')
                                                               
                                                               walle.add(red_trigger_wall)
                                                               trigger_red_button.add(red_click_trigger_button_object)
                                                               na_rasstrel.append(red_click_trigger_button_object)
                                                               na_rasstrel.append(red_trigger_wall)
                                                               
                                                               
                                                               
                                                  
                                               except:
                                                   pass
                                                   
                                               if progruzka_levela == 1:#1-4
                                                   self.conn = sqlite3.connect('gameinfo.db')
                                                   self.cur = self.conn.cursor()
                                                   if self.choosencharacter==1:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 1 updated")
                                                   elif self.choosencharacter==2:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 2 updated")
                                                   else:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 3 updated")
                                                   self.conn.commit()
                                                   self.cur.close()
                                                   floor_loca_1 = Hero_sprite(-200,675, 'Data/images/backgrounds/floor_loca_1.png')  
                                                   floor_loca_2 = Hero_sprite(1500,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   wall = Hero_sprite(650, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
                                                   wall2 = Hero_sprite(25,350, 'Data/images/walls/wall_vertical_loca_1.png')
                                                   wall3 = Hero_sprite(1275,250, 'Data/images/walls/wall_vertical_loca_pre_exit_1.png')
                                                   text_frame = Hero_sprite(650, 200, 'Data/images/walls/frame_loca_1.png') 
                                                   text_frame2 = Hero_sprite(650, 300, 'Data/images/walls/big_2_frame_loca_1.png') 
                                                   
                                                     
                                                  
                                                   red_trigger_button_object = Hero_sprite(60,560, 'Data/images/walls/trigger_red_button_vertical_1.png')
                                                   red_trigger_wall = Hero_sprite(1275,500, 'Data/images/walls/trigger_red_wall_vertical_1.png')
                                                   progruzka_levela = 0
                                                   perehod_x = 1200
                                                   perehod_y = -10000000
                                                   level_number = 5
                                                   na_rasstrel.append(text_frame)
                                                   na_rasstrel.append(text_frame2)
                                                   na_rasstrel.append(wall2)
                                                   na_rasstrel.append(floor_loca_1)
                                                   na_rasstrel.append(floor_loca_2)
                                                   #na_rasstrel.append(pika)
                                                   #na_rasstrel.append(pika1)
                                                   #na_rasstrel.append(pika2)
                                                   na_rasstrel.append(wall)
                                                   na_rasstrel.append(wall3)
                                                   #na_rasstrel.append(wall4)
                                                   
                                                   decoration.add(text_frame)  
                                                   decoration.add(text_frame2) 
                                                   walle.add(floor_loca_1)
                                                   walle.add(floor_loca_2)
                                                   walle.add(wall)
                                                   walle.add(wall2)
                                                   walle.add(wall3)
                                     
                                                   if trigger_red_button_check == False:
                                                     try:
                                                         red_click_trigger_button_object.kill()
                                                     except:
                                                         pass
                                                     polozhenie_personazha(200,450)
                                                     
                                                     trigger_red_button.add(red_trigger_button_object)
                                                     walle.add(red_trigger_wall)
                                                     na_rasstrel.append(red_trigger_button_object)
                                                     na_rasstrel.append(red_trigger_wall)
                                                            
                                     if  location == 5:
                                               self.locationsave=location
                                               
                                               text = font.render("Кнопки также могут создавать стены", True, (text_color))
                                               text1 = font.render("Если вас придавит летающий блок, вы умрёте", True, (text_color))
                                               place = text.get_rect(center=(650, 200))
                                               place2 = text.get_rect(center=(585, 300))
                                               decoration.draw(sc)
                                               sc.blit(text, place)
                                               sc.blit(text1, place2)
                                               try:
                                                           if sprite_hero_walk_left_1.rect.y > niz_levela and len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) >0:
                                                            for ii in na_rasstrel:
                                                             ii.kill()
                                                            progruzka_levela = 1
                                                            die_sound.play()   
                                               except:
                                                           pass
                                                      
                                               try:
                                                       try:
                                                           mov_block.kill()
                                                       except:
                                                           pass
                                                        
                                                       mov_block = Hero_sprite(250,mov_block_y, 'Data/images/walls/moving_block_1.png')
                                                       
                                                       na_rasstrel.append(mov_block)
                                                       moving_block.add(mov_block)
                                                       walle.add(mov_block)
                                                       
                                                       if mov_block_napravlenie == 'up':
                                                            
                                                            mov_block_y -=1
                                                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, moving_block, False)) >0 and mov_block_y >= sprite_hero_walk_left_1.rect.y+167  :
                                                                sprite_hero_walk_left_1.rect.y-=1
                                                            if mov_block_y == 240 :
                                                                   mov_block_napravlenie = 'down'
                                                       if mov_block_napravlenie == 'down':
                                                            
                                                            mov_block_y += 1
                                                            
                                                            if mov_block_y == 600:
                                                                   mov_block_napravlenie = 'up'
                         
                                                       
                                                       
                                                       
                                               except:
                                                   pass 
                                               try:
                                                   #---------------------------------------------------------------------------механику кнопок которые спавнят стену брать от сюда-----------------------
                                                   if pygame.sprite.spritecollide(red_trigger_button_object, attack_hero, False)  :   
                                                               
                                                               
                                                               
                                                               
                                                               red_trigger_button_object.kill()
                                                               trigger_red_gorizontal_wall.kill()
                                                               
                                                               red_click_trigger_button_object = Hero_sprite(55,150, 'Data/images/walls/clicked_trigger_red_button_vertical_1.png')
                                                               trigger_red_gorizontal_wall1 = Hero_sprite(800,675, 'Data/images/walls/trigger_red_wall_gorizontal_1.png')

                                                               walle.add(trigger_red_gorizontal_wall1)
                                                               trigger_red_button.add(red_click_trigger_button_object)
                                                               na_rasstrel.append(red_click_trigger_button_object)
                                                               na_rasstrel.append(trigger_red_gorizontal_wall1)
                                                              
                                                              
                                                               
                                                               
                                                               
                                                  
                                               except:
                                                   pass 
                                               if progruzka_levela == 1:#1-5
                                                   self.conn = sqlite3.connect('gameinfo.db')
                                                   self.cur = self.conn.cursor()
                                                   if self.choosencharacter==1:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 1 updated")
                                                   elif self.choosencharacter==2:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 2 updated")
                                                   else:
                                                    self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                    if self.developer == True:    
                                                        print("save 3 updated")
                                                   self.conn.commit()
                                                   self.cur.close()
                                                   niz_levela = 520
                                                   
                                                   podem_blocka = 100
                                                   progruzka_levela = 0
                                                   perehod_x = 1200
                                                   level_number = 8
                                                   wall = Hero_sprite(25,350, 'Data/images/walls/wall_vertical_loca_1.png')
                                                   wall2 = Hero_sprite(650, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
                                                   wall3 = Hero_sprite(1275,250, 'Data/images/walls/wall_vertical_loca_pre_exit_1.png')
                                                   mov_block_y = 450
                                                   text_frame = Hero_sprite(650, 200, 'Data/images/walls/frame_loca_1.png') 
                                                   text_frame2 = Hero_sprite(650, 300, 'Data/images/walls/big_2_frame_loca_1.png') 
                                                   
                                                   if trigger_red_button_check == False:
                                                            try:
                                                                trigger_red_gorizontal_wall1.kill()
                                                            except:
                                                                pass
                                                            trigger_red_gorizontal_wall = Hero_sprite(800,675, 'Data/images/walls/trigger_red_wall_gorizontal_1.png')
                                                            red_trigger_button_object = Hero_sprite(60,150, 'Data/images/walls/trigger_red_button_vertical_1.png')
                                                            not_active_trigger_wall.add(trigger_red_gorizontal_wall)
                                                            try:
                                                                na_rasstrel.append(red_trigger_button_object)
                                                                na_rasstrel.append(red_trigger_wall)
                                                            except:
                                                                pass
                                                            polozhenie_personazha(125,450)
                                                   
                                                  
                
                                                   traectory_mov_cube = Hero_sprite(250,425 , 'Data/images/walls/trajectory_moving_block_1.png')
                                                  
                                                   floor_loca_1 = Hero_sprite(-100,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   floor_loca_2 = Hero_sprite(1750,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   na_rasstrel.append(text_frame)
                                                   na_rasstrel.append(text_frame2)
                                                   na_rasstrel.append(wall2)
                                                   na_rasstrel.append(floor_loca_1)
                                                   na_rasstrel.append(floor_loca_2)
                                                   na_rasstrel.append(wall)
                                                   na_rasstrel.append(wall3)
                                                   
                                                   na_rasstrel.append(trigger_red_gorizontal_wall)
                                                   na_rasstrel.append(red_trigger_button_object)
                                                   na_rasstrel.append(traectory_mov_cube)
                                                   decoration.add(traectory_mov_cube)
                                                   decoration.add(text_frame)
                                                   decoration.add(text_frame2)
                                                   walle.add(wall2)
                                                   
                                                   walle.add(floor_loca_1)
                                                   walle.add(floor_loca_2)
                                                   walle.add(wall)
                                                   walle.add(wall3)
                                                   

                                                   trigger_red_button.add(red_trigger_button_object)
                                     if  location == 6:
                                         decoration.draw(sc)
                                        
                                         try:
                                                           if sprite_hero_walk_left_1.rect.y > niz_levela and len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) >0:
                                                            for ii in na_rasstrel:
                                                             ii.kill()
                                                            progruzka_levela = 1
                                                            die_sound.play()
                                                            
                                                               
                                         except:
                                                           pass
                                                      
                                         try:
                                                       try:
                                                           mov_block.kill()
                                                       except:
                                                           pass
                                                        
                                                       mov_block = Hero_sprite(200,mov_block_y, 'Data/images/walls/moving_block_1.png')
                                                       
                                                       na_rasstrel.append(mov_block)
                                                       moving_block.add(mov_block)
                                                       walle.add(mov_block)
                                                       
                                                       if mov_block_napravlenie == 'up':
                                                            
                                                            mov_block_y -=1
                                                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, moving_block, False)) >0 and mov_block_y >= sprite_hero_walk_left_1.rect.y+167:
                                                                sprite_hero_walk_left_1.rect.y-=1
                                                            if mov_block_y == 240:
                                                                   mov_block_napravlenie = 'down'
                                                       if mov_block_napravlenie == 'down':
                                                            
                                                            mov_block_y += 1
                                                            
                                                            if mov_block_y == 600:
                                                                   mov_block_napravlenie = 'up'
                                         except:
                                                   pass
                                         try:
                                             if pygame.sprite.spritecollide(sprite_hero_walk_left_2, falling_blocks, False):
                                                            for ii in na_rasstrel:
                                                             ii.kill()
                                                            progruzka_levela = 1
                                                            die_sound.play()
                                            
                                             
                                         except:
                                             pass
                                         try:
                                             if  len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, trigers, False)) >0  or trig == 1 :
                                                            
                                                            try:
                                                                   kill_block.kill()
                                                            except:
                                                                    pass
                                                            trig = 1  
                                                            kill_block = Hero_sprite(700,kill_move_y, 'Data/images/walls/falling_block_1.png')
                                                            falling_blocks.add(kill_block)
                                                            na_rasstrel.append(kill_block)
                                                            kill_move_y +=20
                                                            if kill_move_y == 900:
                                                                   pass
                                            
                                             
                                         except:
                                             pass
                                         try:
                                                   #---------------------------------------------------------------------------механику кнопок которые спавнят стену брать от сюда-----------------------
                                                   if pygame.sprite.spritecollide(red_trigger_button_object, attack_hero, False)  :   
                                                               
                                                               
                                                               try:
                                                                   orange_trigger_button_object.kill()
                                                               except:
                                                                    pass
                                                               
                                                               platform.kill()
                                                               orange_trigger_button_object.kill()
                                                               platform  = Hero_sprite(700,645, 'Data/images/walls/2.png')
                                                               walle.add(platform)
                                                               na_rasstrel.append(platform)
                                                               orange_click_trigger_button_object = Hero_sprite(55,150, 'Data/images/walls/clicked_trigger_orange_button_vertical_1.png')
                                                               

                                                              
                                                               trigger_orange_button.add(orange_click_trigger_button_object)
                                                               na_rasstrel.append(orange_click_trigger_button_object)
                                                               
                                                              
                                                              
                                                               
                                                               
                                                               
                                                  
                                         except:
                                                   pass 
                                         if progruzka_levela == 1:
                                                   kill_move_y = 170
                                                   trig = 0
                                                   niz_levela = 520
                                                   progruzka_levela = 0
                                                   perehod_x = 1200 
                                                   level_number = 8 
                                                   wall = Hero_sprite(25,350, 'Data/images/walls/wall_vertical_loca_1.png')
                                                   wall2 = Hero_sprite(650, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
                                                   wall3 = Hero_sprite(1275,250, 'Data/images/walls/wall_vertical_loca_pre_exit_1.png')
                                                   
                                                   #traectory_kill_block = Hero_sprite(700, 175 , 'Data/images/walls/trajectory_falling_block_1.png')
                                                   polozhenie_personazha(70,450)
                                                   

                                                   traectory_mov_cube = Hero_sprite(200,425 , 'Data/images/walls/trajectory_moving_block_1.png')
                                                     
                                                  
                                                   

                                                   if trigger_red_button_check == False:
                                                            
                                                            orange_trigger_button_object = Hero_sprite(60,150, 'Data/images/walls/trigger_orange_button_vertical_1.png')
                                                            
                                                            na_rasstrel.append(orange_trigger_button_object)
                                                            trigger_orange_button.add(orange_trigger_button_object)
                                                   if trigger_red_button_check == False:
                                                            try:
                                                                   kill_block.kill()
                                                            except:
                                                                    pass
                                                            kill_block = Hero_sprite(700,kill_move_y, 'Data/images/walls/falling_block_1.png')
                                                            falling_blocks.add(kill_block)
                                                            na_rasstrel.append(kill_block) 
                                                            
                                                   floor_loca_1 = Hero_sprite(-190,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   platform  = Hero_sprite(700,645, 'Data/images/walls/2.png')
                                                   floor_loca_2 = Hero_sprite(1600,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                   na_rasstrel.append(wall2)
                                                   na_rasstrel.append(floor_loca_1)
                                                   na_rasstrel.append(floor_loca_2)
                                                   na_rasstrel.append(wall)
                                                   na_rasstrel.append(wall3)
                                                   na_rasstrel.append(platform)
                                                   #na_rasstrel.append(traectory_kill_block)
                                                   na_rasstrel.append(traectory_mov_cube)
                                                   ##добавь всю фигню на расстрел
                                                   walle.add(platform)
                                                   walle.add(wall2)
                                                   walle.add(floor_loca_1)
                                                   walle.add(floor_loca_2)
                                                   walle.add(wall)
                                                   walle.add(wall3)    
                                                   trigers.add(platform)
                                                   #decoration.add(traectory_kill_block)
                                                   decoration.add(traectory_mov_cube)
                                                  
                                     if  location == 7:
                                            
                                             
                                             try:
                                                               if sprite_hero_walk_left_1.rect.y > niz_levela and len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) >0:
                                                                for ii in na_rasstrel:
                                                                 ii.kill()
                                                                progruzka_levela = 1
                                                                die_sound.play()
                                                                
                                                                   
                                             except:
                                                               pass
                                             try:
                                                     if pygame.sprite.spritecollide(sprite_hero_walk_left_2, falling_blocks, False):
                                                                    for ii in na_rasstrel:
                                                                     ii.kill()
                                                                    progruzka_levela = 1
                                                                    die_sound.play()
                                                
                                                 
                                             except:
                                                 pass
                                             try:
                                                 if  len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, trigers, False)) >0  or trig == 1 :
                                                                
                                                                try:
                                                                       kill_block.kill()
                                                                except:
                                                                        pass
                                                                trig = 1  
                                                                kill_block = Hero_sprite(700,kill_move_y, 'Data/images/walls/falling_block_1.png')
                                                                falling_blocks.add(kill_block)
                                                                na_rasstrel.append(kill_block)
                                                                kill_move_y +=20
                                                                if kill_move_y == 900:
                                                                       pass
                                                
                                                 
                                             except:
                                                 pass
                                             try:
                                                   #---------------------------------------------------------------------------механику кнопок которые спавнят стену брать от сюда-----------------------
                                                   if pygame.sprite.spritecollide(orange_trigger_button_object, attack_hero, False)  :   
                                                               
                                                               
                                                               try:
                                                                   orange_trigger_button_object.kill()
                                                               except:
                                                                    pass
                                                               
                                                               
                                                               platform.kill()
                                                               orange_trigger_button_object.kill()
                                                               platform  = Hero_sprite(700,645, 'Data/images/walls/2.png')
                                                               walle.add(platform)
                                                               na_rasstrel.append(platform)
                                                               
                                                               orange_click_trigger_button_object = Hero_sprite(55,550, 'Data/images/walls/clicked_trigger_orange_button_vertical_1.png')
                                                               

                                                              
                                                               trigger_orange_button.add(orange_click_trigger_button_object)
                                                               na_rasstrel.append(orange_click_trigger_button_object)
                                                               
                                                              
                                                              
                                                               
                                                               
                                                               
                                                  
                                             except:
                                                   pass
                                             try:
                                                 if pygame.sprite.spritecollide(red_trigger_button_object, attack_hero, False)  :   
                                                                   
                                                                   
                                                                   
                                                                   
                                                               red_trigger_button_object.kill()
                                                               red_trigger_wall.kill()
                                                               
                                                               red_click_trigger_button_object = Hero_sprite(1245,420, 'Data/images/walls/clicked_trigger_red_button_vertical_left_1.png')
                                                               red_trigger_wall = Hero_sprite(99999,99999, 'Data/images/walls/trigger_red_wall_vertical_1.png')
                                                               
                                                               walle.add(red_trigger_wall)
                                                               trigger_red_button.add(red_click_trigger_button_object)
                                                               na_rasstrel.append(red_click_trigger_button_object)
                                                               na_rasstrel.append(red_trigger_wall)
                                             except:
                                                 pass
                                             if progruzka_levela == 1:
                                                     level_number = 8
                                                     trig = 0
                                                     kill_move_y = 170
                                                     wall = Hero_sprite(25,350, 'Data/images/walls/wall_vertical_loca_1.png')
                                                     wall2 = Hero_sprite(650, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
                                                     wall3 = Hero_sprite(1275,250, 'Data/images/walls/wall_vertical_loca_pre_exit_1.png')

                                                     background_loca_1 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_1.png')
                                                     platform  = Hero_sprite(700,645, 'Data/images/walls/2.png')
                                                     progruzka_levela = 0
                                                     platform2 = Hero_sprite(140,675, 'Data/images/walls/active_trigger_wall_gorizontal_1.png')
                                                     platform3 = Hero_sprite(1000,600, 'Data/images/walls/2.png')
                                                     
                                                 
                                                     red_trigger_button_object = Hero_sprite(1240,420, 'Data/images/walls/trigger_red_button_vertical_left_1.png')

                                                     #pika = Hero_sprite(55,700, 'Data/images/spikes/sprite_red_trigger_spike_1.png')
                                                     floor_loca_1 = Hero_sprite(1800,675, 'Data/images/backgrounds/floor_loca_1.png')
                                                     polozhenie_personazha(100,400)
                                                     na_rasstrel.append(wall2)
                                                     na_rasstrel.append(floor_loca_1)
                                                     na_rasstrel.append(wall)
                                                     na_rasstrel.append(wall3)
                                                     na_rasstrel.append(platform)
                                                     trigers.add(platform)
                                                     
                                                     if trigger_red_button_check == False:
                                                            
                                                            orange_trigger_button_object = Hero_sprite(60,550, 'Data/images/walls/trigger_orange_button_vertical_1.png')
                                                            
                                                            na_rasstrel.append(orange_trigger_button_object)
                                                            trigger_orange_button.add(orange_trigger_button_object)
                                                     if trigger_red_button_check == False:
                                                            try:
                                                                   kill_block.kill()
                                                            except:
                                                                    pass
                                                            kill_block = Hero_sprite(700,kill_move_y, 'Data/images/walls/falling_block_1.png')
                                                            falling_blocks.add(kill_block)
                                                            na_rasstrel.append(kill_block)
                                                     if trigger_red_button_check == False:
                                                         
                                                         polozhenie_personazha(200,450)
                                                         red_trigger_wall = Hero_sprite(1275,500, 'Data/images/walls/trigger_red_wall_vertical_1.png')
                                                         trigger_red_button.add(red_trigger_button_object)
                                                         walle.add(red_trigger_wall)
                                                         na_rasstrel.append(red_trigger_button_object)
                                                         na_rasstrel.append(red_trigger_wall)
                                                     na_rasstrel.append(platform)
                                                     na_rasstrel.append(platform2)
                                                     na_rasstrel.append(platform3)
                                                   
                                                     na_rasstrel.append(floor_loca_1)
                                          
                                                     
                                                     na_rasstrel.append(red_trigger_button_object)
                                                    
                                                     #na_rasstrel.append(red_trigger_wall)
                                                   
                                                     #na_rasstrel.append(pika)
                                                     
                                                    
                                                     walle.add(floor_loca_1)
                                                     #spikes.add(pika)
                                                     #walle.add(platform)
                                                     walle.add(platform2)
                                                     walle.add(platform3)
                                                     walle.add(wall2)
                                                     walle.add(wall)
                                                     walle.add(wall3)
                                                     
                                                  
                                                    

                                     if location == 8:
                                              credits_loca_1_check += 1
                                              if credits_loca_1_check > 0 and credits_loca_1_check <= 1000:
                                                     text = font.render("Drunk Wizard Studio представляет:", True, (text_color))
                                              elif credits_loca_1_check > 1000 and credits_loca_1_check <= 2000:
                                                     text = font.render("Bizzare Pixel Adveture", True, (text_color))
                                              elif credits_loca_1_check > 2000 and credits_loca_1_check <= 3000:
                                                     text = font.render("Программисты: Ai_vani, Gfh", True, (text_color))
                                              elif credits_loca_1_check > 3000 and credits_loca_1_check <= 4000:
                                                     text = font.render("Художник-аниматор: Ai_vani", True, (text_color))
                                              elif credits_loca_1_check > 4000 and credits_loca_1_check <= 5000:
                                                     text = font.render("Художник: Wadoilus_Prime, Ai_vani", True, (text_color))
                                              else:
                                                     text = font.render("Приятной игры от команды Drunk Wizard Studio", True, (text_color))
                                              
                                              
                                              place = text.get_rect(center=(650, 200))
                                              decoration.draw(sc)
                                              sc.blit(text, place)
                                               
                                              if progruzka_levela == 1 :#1-6
                                                     self.conn = sqlite3.connect('gameinfo.db')
                                                     self.cur = self.conn.cursor()
                                                     if self.choosencharacter==1:
                                                      self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                      if self.developer == True:    
                                                            print("save 1 updated")
                                                     elif self.choosencharacter==2:
                                                      self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                      if self.developer == True:    
                                                            print("save 2 updated")
                                                     else:
                                                      self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                      if self.developer == True:    
                                                            print("save 3 updated")
                                                     self.conn.commit()
                                                     self.cur.close()
                                                     self.locationsave=location
                                                     
                                                  
                                                     level_number = 9
                                                     progruzka_levela = 0

                                                     polozhenie_personazha(100,400)
                                                     wall = Hero_sprite(25,350, 'Data/images/walls/wall_vertical_loca_1.png')
                                                     wall2 = Hero_sprite(650, 25, 'Data/images/walls/wall_gorizontal_loca_1.png')
                                                     wall3 = Hero_sprite(1275,250, 'Data/images/walls/wall_vertical_loca_pre_exit_1.png')
                                                     text_frame = Hero_sprite(650, 200, 'Data/images/walls/frame_loca_1.png')

                                                  

                                                     floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_1.png')

                                                     
                                                     na_rasstrel.append(wall2)
                                                     na_rasstrel.append(floor_loca_1)
                                                     na_rasstrel.append(wall)
                                                     na_rasstrel.append(wall3)
                                                     na_rasstrel.append(text_frame)
                                                     decoration.add(text_frame)
                                                     walle.add(wall2)
                                                     walle.add(floor_loca_1)
                                                     walle.add(wall)
                                                     walle.add(wall3)

                                     if location == 9:
                                        Characters_for_dialog.draw(sc)
                                        decoration.draw(sc)
                                        if ai_vani_secret_room == True  :
                                            no_two = True
                                            if Oleg_amulet == False and dialoge_check== 6301:
                                                if particle_amulet_check == particle_amulet:
                                                    particle_amulet_object = Hero_sprite(amulet.rect.x +random.randint(-20, 50), amulet.rect.y - 40, 'Data/images/particles/amulet_particle_1.png')
                                                    particles_amulet_list.append(particle_amulet_object)
                                                    particles_amulet.add(particle_amulet_object)
                                                    na_rasstrel.append(particle_amulet_object)
                                                    particle_amulet_check = 0
                                                particle_amulet_check +=1

                                                na_rasstrel_parti = []
                                                for i in range(len(particles_amulet_list)):
                                                    particles_amulet_list[i].rect.y +=1
                                                    if len(pygame.sprite.spritecollide(particles_amulet_list[i], walle, False)) > 0:
                                                        na_rasstrel_parti.append(particles_amulet_list[i])
                                                for i in range(len(na_rasstrel_parti)):
                                                    particles_amulet_list[i].kill()
                                                    particles_amulet_list.pop(i)

            
                                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, decoration, False)) > 0 and dialoge_check == 6301 and Oleg_amulet == False:
                                                    text = font.render("Нажмите `E`, чтобы взять предмет", True, (text_color))
                                                    sc.blit(text_frame.image, text_frame.rect)  
                                                    place = text.get_rect(center=(700, 200))
                                                    sc.blit(text, place) 
                                                    if keys[pygame.K_e] :#Взятие медальона Айвани
                                                            #Cохранение
                                                            cord_x = sprite_hero_walk_left_2.rect.x
                                                            cord_y = sprite_hero_walk_left_2.rect.y
                                                            sprite_hero_walk_left_1.kill()
                                                            sprite_hero_walk_left_1_2.kill()
                                                            sprite_hero_walk_left_1_1.kill()
                                                            sprite_hero_stand_1.kill()
                                                            sprite_hero_walk_right_1.kill()
                                                            sprite_hero_walk_right_1_1.kill()
                                                            sprite_hero_walk_right_1_2.kill()
                                                            sprite_hero_walk_left_1 = Hero_sprite(cord_x, cord_y, 'Data/images/the main character/Player_left_1_amulet.png')

                                                            sprite_hero_walk_left_1_1 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_left_2_amulet.png')
                                                            sprite_hero_walk_left_1_2 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_left_3_amulet.png')
                                                            sprite_hero_walk_left_2 = Hero_sprite(cord_x, cord_y, 'Data/images/the main character/Player_left_3_amulet.png')

                                                            sprite_hero_stand_1 = Hero_sprite(cord_x, cord_y, 'Data/images/the main character/stand_player_amulet.png')

                                                            sprite_hero_walk_right_1 = Hero_sprite(cord_x, cord_y, 'Data/images/the main character/Player_right_1_amulet.png')
                                                            sprite_hero_walk_right_1_1 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_right_2_amulet.png')
                                                            sprite_hero_walk_right_1_2 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_right_3_amulet.png')

                                                            sprite_hero_falling_1 = Hero_sprite(cord_x, cord_y,'Data/images/the main character/Player_Falling_amulet.png')
                                                            dialoge_check=7000
                                                            amulet.kill()
                                                            for iqwe in particles_amulet_list:
                                                                iqwe.kill()

                                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, Characters_for_dialog, False)) > 0 and dialoge_check <=6300 or dialoge_check >= 7000 and dialoge_check <=7700 and Oleg_amulet == False:
                                                can_moving = False
                                                sc.blit(text_frame.image, text_frame.rect)  
                                                if dialoge_check == 0 and dialoge_check <= 700:
                                                            text = font.render("Приветствую, Странник! Что привело тебя сюда? ", True, (text_color))
                                                elif dialoge_check == 700 and dialoge_check <= 1400:
                                                            text = font.render("Хотя сейчас не об этом, у меня мало времени", True, (text_color))
                                                elif dialoge_check == 1400 and dialoge_check <= 2100:
                                                            text = font.render("Я хочу тебе кое-что поведать...", True, (text_color))
                                                elif dialoge_check == 2100 and dialoge_check <= 2800:
                                                            text = font.render("``Мир скрывает что-то от тебя, что-то тайное... Тёмное!``", True, (text_color))
                                                            ominous_laughter_aivani.play()
                                                elif dialoge_check == 3500 and dialoge_check <= 4200:
                                                            text = font.render("Конечно, кто я такой, чтобы вмешиваться в твою судьбу?...", True, (text_color))
                                                elif dialoge_check == 4900 and dialoge_check <= 5600:
                                                            text = font.render("Но я хочу дать тебе амулет.", True, (text_color))
                                                elif dialoge_check == 5600 and dialoge_check <= 6300:
                                                            text = font.render("Он может спасти, или проклясть заблудшую душу", True, (text_color))
                                                elif dialoge_check == 7000 and dialoge_check <=7700:
                                                            text = font.render("тойв зомг тенойм облочоки зи сстоиот!", True, (text_color))
                                                            mysterious_whisper.play()

                                                place = text.get_rect(center=(700, 200))
                                                dialoge_check+=1
                                                if dialoge_check == 7700:
                                                    Oleg_amulet = True
                                                    if self.choosencharacter==1:
                                                        self.conn = sqlite3.connect('gameinfo.db')
                                                        self.cur =self.conn.cursor()
                                                        self.cur.execute("UPDATE Saves SET Ai_vani=? WHERE ID = 1", ((1,)))
                                                        self.conn.commit()
                                                        self.cur.close()
                                                        if self.developer == True:    
                                                            print("save 1: Ai_vani's artifact was collected")
                                                    elif self.choosencharacter==2:
                                                        self.conn = sqlite3.connect('gameinfo.db')
                                                        self.cur =self.conn.cursor()
                                                        self.cur.execute("UPDATE Saves SET Ai_vani=? WHERE ID = 2", ((1,)))
                                                        self.conn.commit()
                                                        self.cur.close()
                                                        if self.developer == True:    
                                                            print("save 2: Ai_vani's artifact was collected")
                                                    elif self.choosencharacter==3:
                                                        self.conn = sqlite3.connect('gameinfo.db')
                                                        self.cur =self.conn.cursor()
                                                        self.cur.execute("UPDATE Saves SET Ai_vani=? WHERE ID = 3", ((1,)))
                                                        self.conn.commit()
                                                        self.cur.close()
                                                        if self.developer == True:    
                                                            print("save 3: Ai_vani's artifact was collected")
                                                    else:
                                                        if self.developer == True:    
                                                            print("\n")
                                                    ##
                                                if dialoge_check == 6301:
                                                            amulet = Hero_sprite(600,speed_check_amulet, 'Data/images/decorations/amulet.png')
                                                            amulet.move = 'UP'
                                                            na_rasstrel.append(amulet)
                                                            decoration.add(amulet)
                                                sc.blit(text, place) 
                                                sc.blit(Ai_vani_frame.image, Ai_vani_frame.rect)
                                            else:
                                                can_moving = True


                                            if dialoge_check == 6301 and Oleg_amulet == False:
                                                if amulet.move == 'UP':
                                                    speed_check_amulet -=1
                                                    if speed_check_amulet == 515:
                                                        amulet.move = 'DOWN'
                                                elif amulet.move == 'DOWN':
                                                    speed_check_amulet +=1
                                                    if speed_check_amulet == 550:
                                                        amulet.move = 'UP'
                                            particle_aivani_check +=1
                                            if particle_aivani_check == particle_aivani:
                                                Jigurda = random.randint(0, len(particles_spisok) -1)
                                                particle_aivani_object = Hero_sprite(Ai_vani.rect.x +random.randint(-5, 100), Ai_vani.rect.y - 40, particles_spisok[Jigurda])
                                                particles_list.append(particle_aivani_object)
                                                particles.add(particle_aivani_object)
                                                na_rasstrel.append(particle_aivani_object)
                                                particle_aivani_check = 0
                                            na_rasstrel_part = []
                                            for i in range(len(particles_list)):
                                                particles_list[i].rect.y +=1
                                                if len(pygame.sprite.spritecollide(particles_list[i], walle, False)) > 0:
                                                    particles_na_rasstrel.append(particles_list[i])
                                                    na_rasstrel_part.append(particles_list[i])
                                            for i in range(len(na_rasstrel_part)):
                                                particles_list.pop(i)


                                            ai_vani_anim_check += 1
                                            if ai_vani_anim_check == ai_vani_anim // 4:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(300, 550, 'Data/images/characters/Ai_vani_1.png')
                                                Characters_for_dialog.add(Ai_vani)
                                                na_rasstrel.append(Ai_vani)
                                            elif ai_vani_anim_check == ai_vani_anim //4 * 2:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(300, 550, 'Data/images/characters/Ai_vani_2.png')
                                                Characters_for_dialog.add(Ai_vani)
                                                na_rasstrel.append(Ai_vani)
                                            elif ai_vani_anim_check == ai_vani_anim // 4 * 3:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(300, 550, 'Data/images/characters/Ai_vani_3.png')
                                                Characters_for_dialog.add(Ai_vani)
                                                na_rasstrel.append(Ai_vani)
                                            elif ai_vani_anim_check == ai_vani_anim:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(300, 550, 'Data/images/characters/Ai_vani_2.png')
                                                Characters_for_dialog.add(Ai_vani)
                                                na_rasstrel.append(Ai_vani)
                                                ai_vani_anim_check = 0


                                            for i in range(len(particles_na_rasstrel)):
                                       
                                                particles_na_rasstrel[i].kill()
                                        if sprite_hero_walk_left_2.rect.x <= 0 and no_two != True and Oleg_amulet == False:
                                            text_color = ((255,255,255))
                                            ai_vani_secret_room = True
                                            speed_check_amulet = 570
                                            if dialoge_grisha == False:
                                                level_number = 9
                                            dialoge_check = 0
                                            music_loca_1[music_loca_1_check].stop()
                                            Ai_vani_secret_music.play()
                                            polozhenie_personazha(1000,500)
                                            for ii in na_rasstrel:
                                                     ii.kill()
                                            floor = Hero_sprite(x,y+325, 'Data/images/backgrounds/Ai_vani_floor_room.png')
                                            wall = Hero_sprite(25,350, 'Data/images/walls/Ai_vani_vertical_wall.png')
                                            wall2 = Hero_sprite(650, 25, 'Data/images/walls/Ai_vani_floor_gorizontal_wall.png')
                                            wall3 = Hero_sprite(1275,250, 'Data/images/walls/Ai_vani_vertical_wall_pre_exit.png')
                                            walle.add(wall2)
                                            walle.add(wall3)
                                            walle.add(wall)
                                            walle.add(floor)
                                            pedestal = Hero_sprite(600,580, 'Data/images/decorations/pedestal.png')
                                            Ai_vani = Hero_sprite(300, 550, 'Data/images/characters/Ai_vani_1.png')
                                            Ai_vani_frame = Hero_sprite(250, 200, 'Data/images/characters/Ai_vani_frame.png')
                                            text_frame = Hero_sprite(700, 200, 'Data/images/walls/Ai_vani_Frame_for_text.png')
                                            na_rasstrel.append(pedestal)
                                            na_rasstrel.append(text_frame)
                                            na_rasstrel.append(Ai_vani_frame)
                                            na_rasstrel.append(floor)
                                            na_rasstrel.append(Ai_vani)
                                            na_rasstrel.append(wall3)
                                            na_rasstrel.append(wall)
                                            na_rasstrel.append(wall2)
                                            decoration.add(pedestal)
                                            #walle.add(pedestal)
                                            Characters_for_dialog.add(Ai_vani)







                                        if ai_vani_secret_room != True :        
                                            if len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, Characters_for_dialog, False)) > 0 or dialoge_check >=1 and moving == False:
                                                
                                                         dialoge_check +=2
                                                         can_moving = False
                                                         dialoge_grisha = True
                                                         if dialoge_check == 0 and dialoge_check <= 1000:
                                                            text = font.render("Здравствуй, Герой! Моё имя Гриша. Я - великий маг.", True, (text_color)) 
                                                         elif dialoge_check > 1000 and dialoge_check <= 2000:
                                                            text = font.render("Сейчас наша задача одолеть Злые силы, заполонившие мир!", True, (text_color))  
                                                         elif dialoge_check > 2000 and dialoge_check <= 3000:
                                                            text = font.render("Первая наша задача - Эрициус, глава Леса", True, (text_color))     
                                                         elif dialoge_check > 3000 and dialoge_check <= 4000:
                                                            text = font.render("Путь к нему лежит через весь лес.", True, (text_color))   
                                                            text2 = font.render("Он наполненный опасностями, но я знаю, что ты справишься!", True, (text_color))  
                                                         elif dialoge_check > 4000 and dialoge_check <= 5000:
                                                            text = font.render("А теперь, Герой, ступай! Одолей Злые силы!", True, (text_color))  
                                                         if dialoge_check >= 5000:
                                                            can_moving = True
                                                         place = text.get_rect(center=(700, 200))
                                            else:
                                                can_moving = True
                                            #decoration.draw(sc)              
                                            if dialoge_check >0 and dialoge_check < 5001: 
                                                sc.blit(text_frame.image, text_frame.rect)   
                                                if dialoge_check > 3000 and dialoge_check <= 4000:
                                                    sc.blit(text, (place.x-165, place.y+10))
                                                    sc.blit(text2, (place.x-165, place.y-10))
                                                    sc.blit(Grisha_frame.image, Grisha_frame.rect)
                                                else:    
                                                    sc.blit(Grisha_frame.image, Grisha_frame.rect)
                                                    sc.blit(text, place) 
                                                #if dialoge_check <= 6000:
                                                    #time.sleep(0.2)
                                            if len(pygame.sprite.spritecollide(wall, attack_hero, False)):
                                                wall.kill()
                                                wall = Hero_sprite(25,500, 'Data/images/walls/open_wall_vertical_loca_2_1.png')
                                                na_rasstrel.append(wall)
                                                decoration.add(wall)
                                        if progruzka_levela == 1:#2-1
                                                         self.conn = sqlite3.connect('gameinfo.db')
                                                         self.cur = self.conn.cursor()
                                                         if self.choosencharacter==1:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                          if self.developer == True:    
                                                                print("save 1 updated")
                                                         elif self.choosencharacter==2:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                          if self.developer == True:    
                                                                print("save 2 updated")
                                                         else:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 3 updated")
                                                         self.conn.commit()
                                                         self.cur.close()
                                                         dialoge_check = 0
                                                         text_color = ((153, 146, 113))
                                                         text = font.render("Здравствуй, Герой! Моё имя Гриша. Я - великий маг.", True, (text_color)) 
                                                         progruzka_levela = 0

                                                         ai_vani_secret_room = False
                                                         level_number = 10
                                                         polozhenie_personazha(100,500)
                                                         wall = Hero_sprite(25,500, 'Data/images/walls/wall_vertical_loca_2_1.png')
                                                         floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_2.png')
                                                         background_loca_1.image= 'Data/images/backgrounds/bg_loca_2.png'
                                                         if dialoge_check <= 7000:
                                                            text_frame = Hero_sprite(700, 200, 'Data/images/walls/frame_loca_2.png')
                                                            Grisha = Hero_sprite(660, 577, 'Data/images/characters/Grisha_1.png')
                                                            Grisha_frame = Hero_sprite(250, 200, 'Data/images/characters/Grisha_frame.png')
                                                            na_rasstrel.append(Grisha)
                                                            na_rasstrel.append(Grisha_frame)
                                                            na_rasstrel.append(text_frame)
                                                            Characters_for_dialog.add(Grisha)
                                                         cloud = Hero_sprite(150,random.randint(50,150), 'Data/images/decorations/cloud_1.png')
                                                         cloud2 = Hero_sprite(1000,random.randint(50,150), 'Data/images/decorations/cloud_2.png')
                                                         na_rasstrel.append(floor_loca_1)
                                                         na_rasstrel.append(wall)
                                                         na_rasstrel.append(wall3)
                                                         #trigers.append(wall)
                                                         na_rasstrel.append(cloud)
                                                         na_rasstrel.append(cloud2)
                                                         na_rasstrel.append(wall)
                                                         decoration.add(cloud)
                                                         decoration.add(cloud2)
                                                         walle.add(floor_loca_1)
                                                         walle.add(wall)
                                 if location == 10:
                                     if ai_vani_secret_room == True:
                                        Ai_vani_secret_music.stop()
                                        music_loca_1[music_loca_1_check].play()
                                        ai_vani_secret_room= False
                                     try :
                                         if pygame.sprite.spritecollide(kaban, attack_hero, False)  :
                                             kaban.kill()
                                             if evil_napravlenie != 'stop':
                                                 die_caban_sound.play()
                                                 die_caban_sound.set_volume(0.1)
                                             evil_napravlenie = 'stop'
                                     except:
                                         pass
                                     try :
                                         if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False)  :
                                             for ii in na_rasstrel:
                                                     ii.kill()

                                                     progruzka_levela = 1 
                                     except:
                                         pass
            
                                     try:
                                         try:
                                             kaban.kill()
                                         except:
                                             pass
                                         speed_anim_caban_check +=1
                                         if speed_anim_caban == speed_anim_caban_check:
                                            speed_anim_caban_check = 0
                                         if evil_napravlenie == 'left':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_1_left.png')                                                 
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_2_left.png')
                                                 evil.add(kaban)
                                                 kaban.image = pygame.transform.scale(kaban.image, (140, 85))
                                                 na_rasstrel.append(kaban)
                                                 evil_x -= 2
                                                 if evil_x <= evil_gokuda_1:
                                                     
                                                     
                                               
                                                    evil_napravlenie = 'right'
                                         elif evil_napravlenie == 'right':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_1_right.png')
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_2_right.png')
                                                 evil.add(kaban)
                                                 na_rasstrel.append(kaban)
                                                 evil_x += 2
                                                 if evil_x >= evil_gokuda_2:
                                                     
                                                     
                                                 
                                                    evil_napravlenie = 'left'
                                     except:
                                         pass
                                     decoration.draw(sc)
                                     if progruzka_levela == 1:#2-2
                                                         self.conn = sqlite3.connect('gameinfo.db')
                                                         self.cur = self.conn.cursor()
                                                         if self.choosencharacter==1:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 1 updated")
                                                         elif self.choosencharacter==2:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 2 updated")
                                                         else:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 3 updated")
                                                         self.conn.commit()
                                                         self.cur.close()
                                                         self.locationsave=location
                                                         
                                                         text_color = ((153, 146, 113))
                                                         #background_loca_2.kill()
                                                         background_loca_2.kill()
                                                         background_loca_2 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_2_1.png')
                                                         progruzka_levela = 0
                                                         speed_anim_caban = 26
                                                         speed_anim_caban_check = 0
                                                         level_number = 11
                                                         polozhenie_personazha(200,500)
                                                         wall = Hero_sprite(80, 470, 'Data/images/walls/tree_wall_loca_2.png')
                                                         floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_2.png')
                                                         leaf = Hero_sprite(120, 265, 'Data/images/walls/tree_decor_loca_2.png')
                                                         evil_x = 800
                                                         walle.add(wall)
                                                         na_rasstrel.append(wall)
                                                         na_rasstrel.append(leaf)
                                                         decoration.add(leaf)
                                                         evil_y = 607
                                                         evil_gokuda_1 = 600
                                                         evil_gokuda_2 = 1000
                                                         evil_napravlenie = 'left'
                                                         na_rasstrel.append(floor_loca_1)
                                                         
                                                         
                                                         
                                                         walle.add(floor_loca_1)
                                 if location == 11:
                                     if ai_vani_secret_room == True:
                                        Ai_vani_secret_music.stop()
                                        music_loca_1[music_loca_1_check].play()
                                        ai_vani_secret_room= False
                                     try :
                                         if pygame.sprite.spritecollide(kaban, attack_hero, False)   :
                                             if evil_napravlenie != 'stop':
                                                 die_caban_sound.play()
                                                 die_caban_sound.set_volume(0.1)
                                                 kaban.kill()
                                             
                                             evil_napravlenie = 'stop'
                                     except:
                                         pass
                                     try :
                                         if pygame.sprite.spritecollide(kaban1, attack_hero, False)   :
                                             if evil_napravlenie1 != 'stop':
                                                 die_caban_sound.play()
                                                 die_caban_sound.set_volume(0.1)
                                                 kaban1.kill()
                                             
                                             evil_napravlenie1 = 'stop'
                                     except:
                                         pass
                                     try :
                                         if pygame.sprite.spritecollide(wall1, attack_hero, False)   :
                                             if kill_drevo == 0 :
                                                 breaking_tree_sound.play()
                                                 wall1.kill()
                                             kill_drevo =1
                                     except:
                                         pass
                                     
                                     try :
                                         if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False)  :
                                             for ii in na_rasstrel:
                                                     ii.kill()

                                                     progruzka_levela = 1 
                                     except:
                                         pass
            
                                     try:
                                         try:
                                             kaban.kill()
                                         except:
                                             pass
                                         speed_anim_caban_check +=1
                                         if speed_anim_caban == speed_anim_caban_check:
                                            speed_anim_caban_check = 0
                                         if evil_napravlenie == 'left':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_1_left.png')                                                 
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_2_left.png')
                                                 evil.add(kaban)
                                                 kaban.image = pygame.transform.scale(kaban.image, (140, 85))
                                                 na_rasstrel.append(kaban)
                                                 evil_x -= 2
                                                 if evil_x <= evil_gokuda_1:
                                                     
                                                     
                                               
                                                    evil_napravlenie = 'right'
                                         elif evil_napravlenie == 'right':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_1_right.png')
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_2_right.png')
                                                 evil.add(kaban)
                                                 na_rasstrel.append(kaban)
                                                 evil_x += 2
                                                 if evil_x >= evil_gokuda_2:
                                                     
                                                     
                                                 
                                                    evil_napravlenie = 'left'
                                     except:
                                         pass
                                     try:
                                         try:
                                             kaban1.kill()
                                         except:
                                             pass
                                         speed_anim_caban_check +=1
                                         if speed_anim_caban == speed_anim_caban_check:
                                            speed_anim_caban_check = 0
                                         if evil_napravlenie1 == 'left':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban1 = Hero_sprite(evil_x1,evil_y,'Data/images/enemies/cabans/caban_1_left.png')                                                 
                                                 else:
                                                    kaban1 = Hero_sprite(evil_x1,evil_y,'Data/images/enemies/cabans/caban_2_left.png')
                                                 evil.add(kaban1)
                                                 kaban.image = pygame.transform.scale(kaban.image, (140, 85))
                                                 na_rasstrel.append(kaban1)
                                                 evil_x1 -= 2
                                                 if evil_x1 <= evil_gokuda_11:
                                                     
                                                     
                                               
                                                    evil_napravlenie1 = 'right'
                                         elif evil_napravlenie1 == 'right':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban1 = Hero_sprite(evil_x1,evil_y+3,'Data/images/enemies/cabans/caban_1_right.png')
                                                 else:
                                                    kaban1 = Hero_sprite(evil_x1,evil_y+3,'Data/images/enemies/cabans/caban_2_right.png')
                                                 evil.add(kaban1)
                                                 na_rasstrel.append(kaban1)
                                                 evil_x1 += 2
                                                 if evil_x1 >= evil_gokuda_21:
                                                     
                                                     
                                                 
                                                    evil_napravlenie1 = 'left'
                                     except:
                                         pass
                                     decoration.draw(sc)
                                     if progruzka_levela == 1:#2-3
                                                         self.conn = sqlite3.connect('gameinfo.db')
                                                         self.cur = self.conn.cursor()
                                                         if self.choosencharacter==1:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 1 updated")
                                                         elif self.choosencharacter==2:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 2 updated")
                                                         else:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 3 updated")
                                                         self.conn.commit()
                                                         self.cur.close()#передайте Антонио, что кондратьев - гей
                                                         kill_drevo = 0
                                                         text_color = ((153, 146, 113))
                                                         #background_loca_2.kill()
                                                         background_loca_2.kill()
                                                         background_loca_2 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_2_1.png')
                                                         progruzka_levela = 0
                                                         speed_anim_caban = 26
                                                         speed_anim_caban_check = 0
                                                         level_number = 12
                                                         polozhenie_personazha(200,500)
                                                         wall = Hero_sprite(80, 470, 'Data/images/walls/tree_wall_loca_2.png')
                                                         wall1 = Hero_sprite(780, 470, 'Data/images/walls/rotten_wood_loca_2.png')
                                                         floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_2.png')
                                                         leaf = Hero_sprite(120, 265, 'Data/images/walls/tree_decor_loca_2.png')
                                                         evil_x = 1100
                                                         walle.add(wall)
                                                         
                                                         na_rasstrel.append(wall)
                                                         
                                                         na_rasstrel.append(leaf)
                                                         decoration.add(leaf)
                                                         decoration.add(wall1)
                                                         na_rasstrel.append(wall1)
                                                         evil_y = 607
                                                         evil_gokuda_1 = 900
                                                         evil_gokuda_2 = 1250
                                                         evil_napravlenie = 'left'
                                                         evil_y1 = 607
                                                         evil_x1 = 500
                                                         evil_gokuda_11 = 400
                                                         evil_gokuda_21 = 700
                                                         evil_napravlenie1 = 'left'
                                                         na_rasstrel.append(floor_loca_1)
                                                         walle.add(floor_loca_1)
                                                         walle.add(wall1)
                                 
                                 if location == 12:
                                     try :
                                         if pygame.sprite.spritecollide(kaban, attack_hero, False)   :
                                             if evil_napravlenie != 'stop':
                                                 die_caban_sound.play()
                                                 die_caban_sound.set_volume(0.1)
                                                 kaban.kill()
                                             
                                             evil_napravlenie = 'stop'
                                     except:
                                         pass
                                    
                                     
                                     
                                     try :
                                         if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False)  :
                                             for ii in na_rasstrel:
                                                     ii.kill()

                                                     progruzka_levela = 1 
                                     except:
                                         pass
            
                                     try:
                                         try:
                                             kaban.kill()
                                         except:
                                             pass
                                         speed_anim_caban_check +=1
                                         if speed_anim_caban == speed_anim_caban_check:
                                            speed_anim_caban_check = 0
                                         if evil_napravlenie == 'left':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_1_left.png')                                                 
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_2_left.png')
                                                 evil.add(kaban)
                                                 kaban.image = pygame.transform.scale(kaban.image, (140, 85))
                                                 na_rasstrel.append(kaban)
                                                 evil_x -= 2
                                                 if evil_x <= evil_gokuda_1:
                                                     
                                                     
                                               
                                                    evil_napravlenie = 'right'
                                         elif evil_napravlenie == 'right':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_1_right.png')
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_2_right.png')
                                                 evil.add(kaban)
                                                 na_rasstrel.append(kaban)
                                                 evil_x += 2
                                                 if evil_x >= evil_gokuda_2:
                                                     
                                                     
                                                 
                                                    evil_napravlenie = 'left'
                                     except:
                                         pass
                                     if progruzka_levela == 1:#2-4
                                                         self.conn = sqlite3.connect('gameinfo.db')
                                                         self.cur = self.conn.cursor()
                                                         if self.choosencharacter==1:
                                                           self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                           if self.developer == True:    
                                                            print("save 1 updated")
                                                         elif self.choosencharacter==2:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 2 updated")
                                                         else:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 3 updated")
                                                         self.conn.commit()
                                                         self.cur.close()
                                                         text_color = ((153, 146, 113))
                                                         #background_loca_2.kill()
                                                         background_loca_2.kill()
                                                         background_loca_2 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_2_1.png')
                                                         progruzka_levela = 0
                                                         speed_anim_caban = 26
                                                         speed_anim_caban_check = 0
                                                         level_number = 13
                                                         polozhenie_personazha(200,500)
                                                         wall = Hero_sprite(80, 470, 'Data/images/walls/tree_wall_loca_2.png')
                                                         wall1 = Hero_sprite(500, 470, 'Data/images/walls/tree_wall_loca_2.png')
                                                         floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_2.png')
                                                         leaf = Hero_sprite(120, 265, 'Data/images/walls/tree_decor_loca_2.png')
                                                         platform = Hero_sprite(420, 500, 'Data/images/walls/branche_left.png')
                                                         na_rasstrel.append(platform)
                                                         leaf1 = Hero_sprite(540, 265, 'Data/images/walls/tree_decor_loca_2.png')
                                                         walle.add(platform)
                                                         platform1 = Hero_sprite(160, 400, 'Data/images/walls/branche_right.png')
                                                         na_rasstrel.append(platform1)
                                                         
                                                         walle.add(platform1)
                                                         evil_x = 1100
                                                         walle.add(wall)
                                                         na_rasstrel.append(wall)
                                                         na_rasstrel.append(wall1)
                                                         
                                                         na_rasstrel.append(leaf)
                                                         na_rasstrel.append(leaf1)
                                                         walle.add(floor_loca_1)
                                                         
                                                         
                                                         walle.add(wall1)
                                                         na_rasstrel.append(floor_loca_1)
                                                         decoration.add(leaf)
                                                         decoration.add(leaf1)
                                                         perehod_y = -10000
                                                         evil_y = 607
                                                         evil_gokuda_1 = 900
                                                         evil_gokuda_2 = 1250
                                                         evil_napravlenie = 'left'
                                 if location == 13:
                                     if ai_vani_secret_room == True:
                                        Ai_vani_secret_music.stop()
                                        music_loca_1[music_loca_1_check].play()
                                        ai_vani_secret_room= False
                                     try :
                                         if pygame.sprite.spritecollide(kaban, attack_hero, False)   :
                                             if evil_napravlenie != 'stop':
                                                 die_caban_sound.play()
                                                 die_caban_sound.set_volume(0.1)
                                                 kaban.kill()
                                             
                                             evil_napravlenie = 'stop'
                                     except:
                                         pass
                                     try :
                                         if pygame.sprite.spritecollide(kaban1, attack_hero, False)   :
                                             if evil_napravlenie1 != 'stop':
                                                 die_caban_sound.play()
                                                 die_caban_sound.set_volume(0.1)
                                                 kaban1.kill()
                                             
                                             evil_napravlenie1 = 'stop'
                                     except:
                                         pass
                                     try :
                                         if pygame.sprite.spritecollide(wall1, attack_hero, False)   :
                                             if kill_drevo == 0 :
                                                 breaking_tree_sound.play()
                                                 wall1.kill()
                                             kill_drevo =1
                                     except:
                                         pass
                                     
                                     try :
                                         if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False)  :
                                             for ii in na_rasstrel:
                                                     ii.kill()

                                                     progruzka_levela = 1 
                                     except:
                                         pass
            
                                     try:
                                         try:
                                             kaban.kill()
                                         except:
                                             pass
                                         speed_anim_caban_check +=1
                                         if speed_anim_caban == speed_anim_caban_check:
                                            speed_anim_caban_check = 0
                                         if evil_napravlenie == 'left':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_1_left.png')                                                 
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_2_left.png')
                                                 evil.add(kaban)
                                                 kaban.image = pygame.transform.scale(kaban.image, (140, 85))
                                                 na_rasstrel.append(kaban)
                                                 evil_x -= 2
                                                 if evil_x <= evil_gokuda_1:
                                                     
                                                     
                                               
                                                    evil_napravlenie = 'right'
                                         elif evil_napravlenie == 'right':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_1_right.png')
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_2_right.png')
                                                 evil.add(kaban)
                                                 na_rasstrel.append(kaban)
                                                 evil_x += 2
                                                 if evil_x >= evil_gokuda_2:
                                                     
                                                     
                                                 
                                                    evil_napravlenie = 'left'
                                     except:
                                         pass
                                     try:
                                         try:
                                             kaban1.kill()
                                         except:
                                             pass
                                         speed_anim_caban_check +=1
                                         if speed_anim_caban == speed_anim_caban_check:
                                            speed_anim_caban_check = 0
                                         if evil_napravlenie1 == 'left':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban1 = Hero_sprite(evil_x1,evil_y1,'Data/images/enemies/cabans/caban_1_left.png')                                                 
                                                 else:
                                                    kaban1 = Hero_sprite(evil_x1,evil_y1,'Data/images/enemies/cabans/caban_2_left.png')
                                                 evil.add(kaban1)
                                                 kaban.image = pygame.transform.scale(kaban.image, (140, 85))
                                                 na_rasstrel.append(kaban1)
                                                 evil_x1 -= 2
                                                 if evil_x1 <= evil_gokuda_11:
                                                     
                                                     
                                               
                                                    evil_napravlenie1 = 'right'
                                         elif evil_napravlenie1 == 'right':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban1 = Hero_sprite(evil_x1,evil_y1+3,'Data/images/enemies/cabans/caban_1_right.png')
                                                 else:
                                                    kaban1 = Hero_sprite(evil_x1,evil_y1+3,'Data/images/enemies/cabans/caban_2_right.png')
                                                 evil.add(kaban1)
                                                 na_rasstrel.append(kaban1)
                                                 evil_x1 += 2
                                                 if evil_x1 >= evil_gokuda_21:
                                                     
                                                     
                                                 
                                                    evil_napravlenie1 = 'left'
                                     except:
                                         pass
                                     if progruzka_levela == 1:#2-5
                                                         self.conn = sqlite3.connect('gameinfo.db')
                                                         self.cur = self.conn.cursor()
                                                         if self.choosencharacter==1:
                                                           self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                           if self.developer == True:    
                                                            print("save 1 updated")
                                                         elif self.choosencharacter==2:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 2 updated")
                                                         else:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 3 updated")
                                                         self.conn.commit()
                                                         self.cur.close()
                                                         text_color = ((153, 146, 113))
                                                         #background_loca_2.kill()
                                                         background_loca_2.kill()
                                                         background_loca_2 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_2_1.png')
                                                         progruzka_levela = 0
                                                         speed_anim_caban = 26
                                                         speed_anim_caban_check = 0
                                                         level_number = 14
                                                         polozhenie_personazha(200,500)
                                                         wall = Hero_sprite(80, 470, 'Data/images/walls/tree_wall_loca_2.png')
                                                         wall1 = Hero_sprite(700, 470, 'Data/images/walls/tree_wall_loca_2.png')
                                                         floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_2.png')
                                                         leaf = Hero_sprite(120, 265, 'Data/images/walls/tree_decor_loca_2.png')
                                                         platform = Hero_sprite(620, 500, 'Data/images/walls/branche_left.png')
                                                         na_rasstrel.append(platform)
                                                         leaf1 = Hero_sprite(720, 265, 'Data/images/walls/tree_decor_loca_2.png')
                                                         walle.add(platform)
                                                         platform1 = Hero_sprite(230, 400, 'Data/images/walls/long_branche_right.png')
                                                         na_rasstrel.append(platform1)
                                                         evil_y1 = 350
                                                         evil_x1 = 300
                                                         evil_gokuda_11 = 200
                                                         evil_gokuda_21 = 300
                                                         evil_napravlenie1 = 'left'
                                                         walle.add(platform1)
                                                         evil_x = 1100
                                                         walle.add(wall)
                                                         na_rasstrel.append(wall)
                                                         na_rasstrel.append(wall1)
                                                         
                                                         na_rasstrel.append(leaf)
                                                         na_rasstrel.append(leaf1)
                                                         walle.add(floor_loca_1)
                                                         
                                                         
                                                         walle.add(wall1)
                                                         na_rasstrel.append(floor_loca_1)
                                                         decoration.add(leaf)
                                                         decoration.add(leaf1)
                                                         perehod_y = -10000
                                                         evil_y = 607
                                                         evil_gokuda_1 = 900
                                                         evil_gokuda_2 = 1250
                                                         evil_napravlenie = 'left'
                                 if location == 333 :
                                     try:
                                         
                                         if artefact_go == 1 :
                                             if keys[pygame.K_e]:#Взятие артефакта ГФХ
                                                 vzat = 1
                                                 if self.choosencharacter==1:
                                                        self.conn = sqlite3.connect('gameinfo.db')
                                                        self.cur =self.conn.cursor()
                                                        self.cur.execute("UPDATE Saves SET GFH=? WHERE ID = 1", ((True,)))
                                                        self.conn.commit()
                                                        self.cur.close()
                                                        if self.developer == True:    
                                                            print("save 1: GFH's artifact was collected")
                                                 elif self.choosencharacter==2:
                                                        self.conn = sqlite3.connect('gameinfo.db')
                                                        self.cur =self.conn.cursor()
                                                        self.cur.execute("UPDATE Saves SET GFH=? WHERE ID = 2", ((True,)))
                                                        self.conn.commit()
                                                        self.cur.close()
                                                        if self.developer == True:    
                                                            print("save 2: GFH's artifact was collected")
                                                 elif self.choosencharacter==3:
                                                        self.conn = sqlite3.connect('gameinfo.db')
                                                        self.cur =self.conn.cursor()
                                                        self.cur.execute("UPDATE Saves SET GFH=? WHERE ID = 3", ((True,)))
                                                        self.conn.commit()
                                                        self.cur.close()
                                                        if self.developer == True:    
                                                            print("save 3: GFH's artifact was collected")
                                                 else:
                                                        if self.developer == True:    
                                                            print("\n")
                                                 Oleg_eye = True
                                             if vzat == 0:
                                                 sc.blit(gfh_artefact.image, gfh_artefact.rect)
                                             else:
                                                 sc.blit(gfh_artefact_non.image, gfh_artefact_non.rect)
                                             if  sprite_hero_walk_left_1.rect.x > 350 and  sprite_hero_walk_left_1.rect.x < 500:
                                         
                                                  
                                                  if vzat == 0:
                                                      sc.blit(gfh_frame_text.image, gfh_frame_text.rect)
                                                      text = font.render("*нажмите E что бы взять*", True, (text_color))
                                                      sc.blit(text, (place.x-10, place.y-10))
                                         if  sprite_hero_walk_left_1.rect.x < 350 and dialoge_check < 63000:
                                                    
                                                   
                                                    dialoge_check += 10
                                                    
                                                    if dialoge_check >= 0 :
                                                        
                                                   
                                                        can_moving = False
                                                        sc.blit(gfh_frame.image, gfh_frame.rect) 
                                                        
                                                        sc.blit(gfh_frame_text.image, gfh_frame_text.rect) 
                                                  
                                                    if dialoge_check > 1000 or dialoge_check < 1000:
                                                        
                                                         text = font.render("Приветствую тебя, путник!", True, (text_color))#тут тексты
                                                    
                                                    if dialoge_check >= 8000:
                                                        
                                                         text = font.render("Это местo называется сюжетной дырой.", True, (text_color))
                                                    
                                                    if dialoge_check >= 16000:
                                                        
                                                         text = font.render("Я вижу что твоему другу грозит опасность.", True, (text_color))
                                                    
                                                    if dialoge_check >= 24000:
                                                        
                                                         text = font.render("Возьми это и оно защитит его.", True, (text_color))
                                                    
                                                    if dialoge_check >= 36000:
                                                       
                                                         text = font.render("Это глаз  всевидящего стража.", True, (text_color))
                                                    
                                                    if dialoge_check >= 44000:
                                                      
                                                         text = font.render("Но его сила не вечна.", True, (text_color))
                                                    
                                                    if dialoge_check >= 62000:
                                                        
                                                         text = font.render("Прощай.", True, (text_color))
                                                         can_moving = True
                                                    if dialoge_check >= 24000:
                                                        artefact_go = 1
                                                        
                                                    if dialoge_check >0:
                                                        
                                                        sc.blit(text, (place.x-30, place.y-10))
                                               
                                                    
                                                    
                                     except:
                                         pass
                                     if progruzka_levela == 1 and no_two_gfh == False:
                                                    try:
                                                        kaban.kill()
                                                    except:
                                                        pass
                                                    no_two_gfh = True
                                                    can_moving = True
                                                    text_color = ((0,0,0))
                                                    level_number = 14
                                                    artefact_go = 0
                                                    progruzka_levela= 0
                                                    gfh_level = False
                                                    text = font.render(
                                                            "Для ходьбы испрользуйте клавиши A и D", True, (text_color))
                                                    place = text.get_rect(
                                                            center=(650, 200))
                                                    perehod_x = 1270
                                                    dialoge_check = 0
                                                    gfh_artefact  = Hero_sprite(450,550, 'Data/images/decorations/artefact_gfh.png')
                                                    gfh_artefact_non  = Hero_sprite(450,550, 'Data/images/decorations/artefact_gfh_non.png')
                                                    gfh_frame_text = Hero_sprite(700,200, 'Data/images/characters/gfh_text_frame.png')
                                                    gfh_frame = Hero_sprite(250,200, 'Data/images/characters/gfh_diol.png')
                                                    polozhenie_personazha(1000, 500)
                                                    floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_gfh.jpg')
                                                    na_rasstrel.append(floor_loca_1)
                                                    walle.add(floor_loca_1)
                                                    wall = Hero_sprite(25, 350, 'Data/images/walls/gfh_wall.png')
                                                    wall2 =   Hero_sprite(1275,150, 'Data/images/walls/gfh_wall.png')    
                                                    wall3 =   Hero_sprite(650, 25, 'Data/images/backgrounds/floor_gfh.jpg')   
                                                    walle.add(wall)
                                                    walle.add(wall2)
                                                    walle.add(wall3)
                                                    gfh = Hero_sprite(300,550, 'Data/images/characters/gfh.png')
                                                    na_rasstrel.append(gfh)
                                                    decoration.add(gfh)
                                                    na_rasstrel.append(wall)
                                                    na_rasstrel.append(wall2)  
                                                    na_rasstrel.append(wall3)
                                                    text = font.render("Приветствую тебя ,путник!.", True, (text_color))
                                 if location == 14:
                                     try :
                                         if no_two_gfh ==True:
                                            secretke_gfh = -100000
                                     except:
                                         pass
                                     try :
                                         if sprite_hero_walk_left_1.rect.x < secretke_gfh :
                                            for ii in na_rasstrel:
                                                     ii.kill()
                                                     level_number = 333
                                                     perehod_x = 1
                                     except:
                                         pass
                                     
                                     try :
                                        if vzat == 0 and no_two_gfh == False:
                                             if pygame.sprite.spritecollide(wall, attack_hero, False)   :
                                                 if kill_drevo == 0 :
                                                     breaking_tree_sound.play()
                                                     wall.kill()
                                                     platform1.kill()
                                                     leaf.kill()
                                                 kill_drevo =1
                                     except:
                                         pass
                                     try :
                                         if pygame.sprite.spritecollide(kaban, attack_hero, False)   :
                                             if evil_napravlenie != 'stop':
                                                 die_caban_sound.play()
                                                 die_caban_sound.set_volume(0.1)
                                                 kaban.kill()
                                             
                                             evil_napravlenie = 'stop'
                                     except:
                                         pass
                                    
                                     
                                     
                                     try :
                                         if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False)  :
                                             for ii in na_rasstrel:
                                                     ii.kill()

                                                     progruzka_levela = 1 
                                     except:
                                         pass
            
                                     try:
                                         try:
                                             kaban.kill()
                                         except:
                                             pass
                                         speed_anim_caban_check +=1
                                         if speed_anim_caban == speed_anim_caban_check:
                                            speed_anim_caban_check = 0
                                         if evil_napravlenie == 'left':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_1_left.png')                                                 
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y,'Data/images/enemies/cabans/caban_2_left.png')
                                                 evil.add(kaban)
                                                 kaban.image = pygame.transform.scale(kaban.image, (140, 85))
                                                 na_rasstrel.append(kaban)
                                                 evil_x -= 2
                                                 if evil_x <= evil_gokuda_1:
                                                     
                                                     
                                               
                                                    evil_napravlenie = 'right'
                                         elif evil_napravlenie == 'right':
                                                 if speed_anim_caban_check <= speed_anim_caban //2:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_1_right.png')
                                                 else:
                                                    kaban = Hero_sprite(evil_x,evil_y+3,'Data/images/enemies/cabans/caban_2_right.png')
                                                 evil.add(kaban)
                                                 na_rasstrel.append(kaban)
                                                 evil_x += 2
                                                 if evil_x >= evil_gokuda_2:
                                                     
                                                     
                                                 
                                                    evil_napravlenie = 'left'
                                     except:
                                         pass
                                     try:
                                                   #---------------------------------------------------------------------------механику кнопок которые спавнят стену брать от сюда-----------------------
                                                   if pygame.sprite.spritecollide(red_trigger_button_object, attack_hero, False)  :   
                                                               
                                                               
                                                               
                                                               
                                                               red_trigger_button_object.kill()
                                                               red_trigger_wall.kill()
                                                               
                                                               red_click_trigger_button_object = Hero_sprite(465,300, 'Data/images/walls/clicked_trigger_red_button_vertical_left_1.png')
                                                               trigger_red_wall1 = Hero_sprite(800,9000, 'Data/images/walls/trigger_red_wall_gorizontal_1.png')

                                                               walle.add(trigger_red_wall1)
                                                               trigger_red_button.add(red_click_trigger_button_object)
                                                               na_rasstrel.append(red_click_trigger_button_object)
                                                               na_rasstrel.append(trigger_red_wall1)
                                                              
                                                              
                                                               
                                                               
                                                               
                                                  
                                     except:
                                                   pass 
                                     if progruzka_levela == 1:#2-6
                                                         self.conn = sqlite3.connect('gameinfo.db')
                                                         self.cur = self.conn.cursor()
                                                         if self.choosencharacter==1:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 1 updated")
                                                         elif self.choosencharacter==2:
                                                          self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                          if self.developer == True:    
                                                            print("save 2 updated")
                                                         else:
                                                           self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                           if self.developer == True:    
                                                            print("save 3 updated")
                                                         self.conn.commit()
                                                         self.cur.close()
                                                         
                                                         secretke_gfh = 80
                                                         kill_drevo =0
                                                         text_color = ((153, 146, 113))
                                                         #background_loca_2.kill()
                                                         background_loca_2.kill()
                                                         background_loca_2 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_2_1.png')
                                                         kill_drevo =0
                                                         progruzka_levela = 0
                                                         speed_anim_caban = 26
                                                         speed_anim_caban_check = 0
                                                         level_number = 15
                                                         polozhenie_personazha(250,500)
                                                         wall = Hero_sprite(80, 470, 'Data/images/walls/tree_wall_loca_2.png')
                                                         wall1 = Hero_sprite(500, 270, 'Data/images/walls/tree_wall_loca_2.png')
                                                         floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_2.png')
                                                         leaf = Hero_sprite(120, 265, 'Data/images/walls/tree_decor_loca_2.png')
                                                         red_trigger_button_object = Hero_sprite(460,300, 'Data/images/walls/trigger_red_button_vertical_left_1.png')
                                                         red_trigger_wall = Hero_sprite(500,500, 'Data/images/walls/trigger_red_wall_vertical_1.png')
                                                         vhod = Hero_sprite(1290,350, 'Data/images/walls/vhod_v_pen.png')
                                                         decoration.add(vhod)
                                                         if trigger_red_button_check == False:
                                                             try:
                                                                 red_click_trigger_button_object.kill()
                                                             except:
                                                                 pass
                                                             polozhenie_personazha(300,450)
                                                             
                                                             trigger_red_button.add(red_trigger_button_object)
                                                             walle.add(red_trigger_wall)
                                                             na_rasstrel.append(red_trigger_button_object)
                                                             na_rasstrel.append(red_trigger_wall)
                                                        
                                                         
                                                         platform1 = Hero_sprite(160, 500, 'Data/images/walls/branche_right.png')
                                                         na_rasstrel.append(platform1)
                                                         na_rasstrel.append(vhod)
                                                         walle.add(platform1)
                                                         evil_x = 1100
                                                         walle.add(wall)
                                                         na_rasstrel.append(wall)
                                                         na_rasstrel.append(wall1)
                                                         
                                                         na_rasstrel.append(leaf)
                                                  
                                                         walle.add(floor_loca_1)
                                                         
                                                         
                                                         walle.add(wall1)
                                                         na_rasstrel.append(floor_loca_1)
                                                         decoration.add(leaf)
                                              
                                                         perehod_y = -10000
                                                         evil_y = 607
                                                         evil_gokuda_1 = 900
                                                         evil_gokuda_2 = 1250
                                                         evil_napravlenie = 'left'
                                                         trigger_red_button.add(red_trigger_button_object)
                                                         walle.add(red_trigger_wall)
                                                         na_rasstrel.append(red_trigger_button_object)
                                                         na_rasstrel.append(red_trigger_wall)
                                 if location == 15:

                                  
                                    if progruzka_levela == 1:#2-7
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        try:
                                         elf.cur.close()
                                        except:
                                            pass
                                        try:
                                            ejsk_ball.kill()
                                            ejsh.kill()
                                        except:
                                            pass

                                        stand_boss = 50
                                        stand_boss_check = 0

                                        move_ball = 45
                                        move_ball_check = 0                                        

                                        in_ball_check = 0
                                        in_ball = 32
                                        nalichie_eja = False

                                        die_anim = 22
                                        die_anim_check = 0

                                        polojenie_eja_po_x = 980#потом для анимки тебе придётся это трогать, потому что структурная часть на тебе

                                        nahui_vashego_eja = 0
                                        level_number = 16

    
                                        spawn_gregory = 150
                                        spawn_gregory_check = 0
                                        speed_anim_gregory = 70
                                        speed_anim_gregory_check = 0
                                        napravlenie_eja = 1
                                        kuda_letim = 1
                                        otbivania = 0
                                        hp_boss = 5
                                        background_loca_2.kill()
                                        background_loca_2 = Hero_sprite(x,y, 'Data/images/backgrounds/pen_bg.png')
                                        polozhenie_personazha(200,450)
                                        floor_loca = Hero_sprite(x,y+325, 'Data/images/backgrounds/pol_pen.png')
                                        floor_loca1 = Hero_sprite(x,y-325, 'Data/images/backgrounds/pen_floor.png')
                                        walle.add(floor_loca)
                                        na_rasstrel.append(floor_loca)
                                        walle.add(floor_loca1)
                                        na_rasstrel.append(floor_loca1)
                                        progruzka_levela = 0
                                        wall = Hero_sprite(10, 350, 'Data/images/walls/pen_wall.png')
                                        jiv = 1
                                        walle.add(wall)
                                        shar_sozdan = 0
                                        na_rasstrel.append(wall)
                                        shar_y = 400
                                        shar_x = 900
                                        wall2 = Hero_sprite(1290, 350, 'Data/images/walls/pen_wall.png')
                                        wall24 = Hero_sprite(1290, 350, 'Data/images/walls/pen_wall.png')
                                        na_rasstrel.append(wall24)
                                        walle.add(wall24)
                                        perehod_x = 12000
                                        boss_ozidanie = 0
                                        walle.add(wall2)
                                        shar = 'netu'
                                        na_rasstrel.append(wall2)
                                        bil_udar = 0
                                        platform = Hero_sprite(70, 490, 'Data/images/walls/pen_platform_right.png')
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform1 = Hero_sprite(1240, 490, 'Data/images/walls/pen_platform_left.png')
                                        text_frame = Hero_sprite(700, 200, 'Data/images/walls/frame_loca_2.png')
                                        Grisha_frame = Hero_sprite(250, 200, 'Data/images/characters/Grisha_frame.png')
                                        na_rasstrel.append(Grisha_frame)
                                        na_rasstrel.append(text_frame)
                                        dialoge_grisha = 0
                                        walle.add(platform1)
                                        na_rasstrel.append(platform1)
                                        boss_collison.add(wall)
                                        boss_collison.add(floor_loca1)
                                        boss_collison.add(floor_loca)
                                        boss_collison.add(wall2)
                                        y_dollot = 0
                                        text_color = ((153, 146, 113))
                                        x_dollot = 0

                                 if location == 16:
                                  if progruzka_levela == 1:#3-1
                                    self.conn = sqlite3.connect('gameinfo.db')
                                    self.cur = self.conn.cursor()
                                    if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                    elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                    else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                    self.conn.commit()
                                    self.cur.close()
                                               
                                    progruzka_levela = 0
                                    polozhenie_personazha(100,500)
                                    
                                    perehod_x = 1250
                                    level_number = 17
                                    floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_3.png')  
                                    wall = Hero_sprite(10, 350, 'Data/images/walls/wall_loca_3.png')
                                    wall2 =   Hero_sprite(1275,250, 'Data/images/walls/wall_loca_3_pre_exit.png')    
                                    wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_3.png')         
                                    na_rasstrel.append(wall)
                                    na_rasstrel.append(wall2)
                                    na_rasstrel.append(wall3)
                                    na_rasstrel.append(floor_loca_1)
                                    walle.add(floor_loca_1)
                                    walle.add(wall)
                                    walle.add(wall2)
                                    walle.add(wall3) 
                                 if location == 17:
                                    #try:
                                    #    beatle.kill()#
                                    #    
                                    #except:
                                    #    pass
                                    try:
                                        beatle.kill()
                                        
                                    except:
                                        pass
                                    try:
                                        if beatle_killed == False:
                                          if move_beatle_right == True:
                                              sranaya_proverka_na_x +=1
                                              if sranaya_proverka_na_x == 1200:
                                                  move_beatle_right = False
                                                  anim_bucashka_check = 0
                                          elif move_beatle_right == False:
                                              sranaya_proverka_na_x -=1
                                              if sranaya_proverka_na_x == 920:
                                                  anim_bucashka_check = 0
                                                  move_beatle_right = True
                                    except:
                                        move_beatle_right = True
                                        anim_bucashka = 70
                                        die_anim_beatle_check = 0
                                        die_anim_beatle = 400
                                        beatle_killed = False
                                        anim_bucashka_check = 0
                                        sranaya_proverka_na_x = 925
                                    if beatle_killed == False:
                                        if move_beatle_right == True:
                                            if anim_bucashka_check < anim_bucashka // 7 * 1:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_1.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 2:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_2.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 3:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_3.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 4:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_4.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 5:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_5.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 6:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_6.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 7:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_7.png')
                                            else:
                                                anim_bucashka_check = 0
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_1.png')
                                            na_rasstrel.append(beatle)
                                            evil.add(beatle)    
                                        else:
                                            if anim_bucashka_check < anim_bucashka // 7 * 1:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_left/beatle_walk_1.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 2:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_left/beatle_walk_2.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 3:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_left/beatle_walk_3.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 4:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_left/beatle_walk_4.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 5:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_left/beatle_walk_5.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 6:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_left/beatle_walk_6.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 7:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_left/beatle_walk_7.png')
                                            else:
                                                anim_bucashka_check = 0
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_1.png')
                                            na_rasstrel.append(beatle)
                                            evil.add(beatle)    
                                        anim_bucashka_check +=1

                                        
                                    if  pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False) :
                                        for ii in na_rasstrel:
                                            ii.kill()
                                        
                                        progruzka_levela = 1
                                        die_sound.play()
                                    if pygame.sprite.spritecollide(beatle, attack_hero, False):
                                      if beatle_killed == False:
                                        if self.developer == True:
                                             
                                            print('Танец злобного гения')
                                        
                                        beatle.kill()
                                        if  sound_not_duplicated == 0:
                                            die_beatle.play()
                                            sound_not_duplicated =1
                                        beatle_killed = True
                                    
                                


                                    if progruzka_levela == 1:#3-2
                                            self.conn = sqlite3.connect('gameinfo.db')
                                            self.cur = self.conn.cursor()
                                            if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                            elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                            else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                            self.conn.commit()
                                            self.cur.close()
                                            
                                            progruzka_levela = 0
                                            polozhenie_personazha(100,500)
                                            perehod_x = 1250
                                            level_number = 18
                                            move_beatle_right = True
                                            anim_bucashka = 70
                                            die_anim_beatle_check = 0
                                            die_anim_beatle = 400
                                            beatle_killed = False
                                            anim_bucashka_check = 0
                                            sranaya_proverka_na_x = 925
                                            floor_loca_1 = Hero_sprite(x-500,y+325, 'Data/images/backgrounds/short_floor_loca_3.png')  
                                            floor_loca_2 = Hero_sprite(x+500,y+325, 'Data/images/backgrounds/short_floor_loca_3.png')  
                                            na_rasstrel.append(floor_loca_2)
                                            walle.add(floor_loca_2)
                                            wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_3.png')
                                            wall2 =   Hero_sprite(1275,250, 'Data/images/walls/wall_loca_3_pre_exit.png')    
                                            wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_3.png')
                                            spike = Hero_sprite(1150, 635, 'Data/images/spikes/sprite_spike_1.png')
                                            na_rasstrel.append(spike)
                                            evil.add(spike)
                                            platform = Hero_sprite(90, 475, 'Data/images/walls/platform_loca_3_1.png')
                                            na_rasstrel.append(platform)
                                            walle.add(platform)
                                            platform2 = Hero_sprite(655, 360, 'Data/images/walls/platform_loca_3_1.png')
                                            na_rasstrel.append(platform2)
                                            walle.add(platform2)
                                            platform3 = Hero_sprite(500, 360, 'Data/images/walls/platform_loca_3_1.png')
                                            na_rasstrel.append(platform3)
                                            walle.add(platform3)
                                            sound_not_duplicated =0

                                            platform4 = Hero_sprite(1110, 400, 'Data/images/walls/platform_loca_3_1.png')
                                            na_rasstrel.append(platform4)
                                            walle.add(platform4)
                                            platform5 = Hero_sprite(955, 400, 'Data/images/walls/platform_loca_3_1.png')
                                            na_rasstrel.append(platform5)
                                            walle.add(platform5)
                                            beatle_killed = False
                                            #beatle = Hero_sprite(925, 360, 'Data/images/enemies/beatle/walk_right/beatle_walk_1.png')
                                            na_rasstrel.append(beatle)
                                            evil.add(beatle)
                                            #move_beatle_right = True
                                            #sranaya_proverka_na_x = 925

                                            na_rasstrel.append(wall)
                                            na_rasstrel.append(wall2)
                                            na_rasstrel.append(wall3)
                                            na_rasstrel.append(floor_loca_1)
                                            walle.add(floor_loca_1)
                                            walle.add(wall)
                                            walle.add(wall2)
                                            walle.add(wall3)     
                                 if location == 18:
                                    try :
                                         if pygame.sprite.spritecollide(block, attack_hero, False)   :
                                             if kill_drevo == 0 :
                                                 breaking_tree_sound.play()
                                                 block.kill()
                                             kill_drevo =1
                                    except:
                                         pass
                                    try:
                                        snake.kill()
                                    except:
                                        start_x = 300
                                        alive_snake = True
                                        move_right = True
                                        speed_anim_snake = 150
                                        speed_anim_snake_check = 0
                                    if alive_snake == True:
                                        if move_right == True:
                                            start_x +=1
                                            if speed_anim_snake_check < speed_anim_snake // 10 * 1:
                                                snake = Hero_sprite(start_x, 457, 'Data/images/enemies/snake/walk_right/walk_1.png')
                                            elif speed_anim_snake_check < speed_anim_snake // 10 * 2:
                                                snake = Hero_sprite(start_x, 457, 'Data/images/enemies/snake/walk_right/walk_2.png')
                                            else:
                                                speed_anim_snake_check = 0
                                            speed_anim_snake_check += 1
                                            if start_x == 560:
                                                move_right = False
                                        elif move_right == False:
                                            start_x -=1
                                            if speed_anim_snake_check < speed_anim_snake // 10 * 1:
                                                snake = Hero_sprite(start_x, 457, 'Data/images/enemies/snake/walk_left/walk_1.png')
                                            elif speed_anim_snake_check < speed_anim_snake // 10 * 2:
                                                snake = Hero_sprite(start_x, 457, 'Data/images/enemies/snake/walk_left/walk_2.png')
                                            else:
                                                speed_anim_snake_check = 0
                                            speed_anim_snake_check += 1
                                            if start_x == 300:
                                                move_right = True
                                        evil.add(snake)
                                        na_rasstrel.append(snake)

                                        if  pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False) :
                                            for ii in na_rasstrel:
                                                ii.kill()
                                            
                                            progruzka_levela = 1
                                            die_sound.play()
                                        if pygame.sprite.spritecollide(snake, attack_hero, False):
                                            snake.kill()
                                            if self.developer == True:    
                                                print('На страницах произведения.')
                                            die_snake.play()
                                            alive_snake = False
                                    if progruzka_levela == 1:#3-3
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        sound_not_duplicated = 0
                                        start_x = 300
                                        alive_snake = True
                                        move_right = True
                                        speed_anim_snake = 150
                                        speed_anim_snake_check = 0
                                        progruzka_levela = 0
                                        start_x = 300
                                        polozhenie_personazha(100,400)
                                        alive_snake = True
                                        speed_anim_snake = 150
                                        speed_anim_snake_check = 0
                                        background_loca_3.kill()
                                        background_loca_3 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_3_2.png')
                                        floor_loca_2 = Hero_sprite(x+700,y+325, 'Data/images/backgrounds/short_floor_loca_3_2.png')  
                                        na_rasstrel.append(floor_loca_2)
                                        walle.add( floor_loca_2)
        

                                        perehod_x = 1250
                                        level_number = 19
                                        platform = Hero_sprite(90, 560, 'Data/images/walls/platform_loca_3_2.png')
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_3_2.png')
                                        wall2 =   Hero_sprite(1275,150, 'Data/images/walls/wall_loca_3_pre_exit_2.png')    
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_3_2.png')         
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        na_rasstrel.append(wall)
                                        na_rasstrel.append(wall2)
                                        na_rasstrel.append(wall3)
                                        
                                        walle.add(wall)
                                        walle.add(wall2)
                                        walle.add(wall3)
                                        block = Hero_sprite(900, 370, 'Data/images/walls/crushed_stoun.png')
                                        walle.add(block)
                                        platform2 = Hero_sprite(350, 500, 'Data/images/walls/platform_loca_3_2.png')            
                                        walle.add(platform2)
                                        na_rasstrel.append(platform2)
                                        platform4 = Hero_sprite(850, 500, 'Data/images/walls/platform_loca_3_2.png')            
                                        walle.add(platform4)
                                        na_rasstrel.append(platform4)
                                        platform3 = Hero_sprite(505, 500, 'Data/images/walls/platform_loca_3_2.png')            
                                        walle.add(platform3)
                                        na_rasstrel.append(platform3)
                                        kill_drevo = 0
                                        decoration.add(block)
                                        na_rasstrel.append(block)
                                 if location == 19:
                                    try:
                                                   #---------------------------------------------------------------------------механику кнопок которые спавнят стену брать от сюда-----------------------
                                                   if pygame.sprite.spritecollide(red_trigger_button_object, attack_hero, False)  :   
                                                               
                                                               red_trigger_button_object.kill()
                                                               red_trigger_wall.kill()
                                                               
                                                               red_click_trigger_button_object = Hero_sprite(645,200, 'Data/images/walls/clicked_trigger_red_button_vertical_left_1.png')
                                                               trigger_red_wall1 = Hero_sprite(800,9000, 'Data/images/walls/trigger_red_wall_gorizontal_1.png')

                                                               walle.add(trigger_red_wall1)
                                                               trigger_red_button.add(red_click_trigger_button_object)
                                                               na_rasstrel.append(red_click_trigger_button_object)
                                                               na_rasstrel.append(trigger_red_wall1)
                                  
                                    except:
                                                   pass 
                                    try :
                                         if pygame.sprite.spritecollide(block, attack_hero, False)   :
                                             if kill_drevo == 0 :
                                                 breaking_tree_sound.play()
                                                 block.kill()
                                             kill_drevo =1
                                    except:
                                         pass
                                        
                                    if progruzka_levela == 1:#3-4
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        
                                        progruzka_levela = 0
                                        polozhenie_personazha(50,400)
                                     
                                        floor_loca_2 = Hero_sprite(x+900,y+325, 'Data/images/backgrounds/floor_loca_3_2.png')  
                                        na_rasstrel.append(floor_loca_2)
                                        walle.add( floor_loca_2)

                                        perehod_x = 1300
                                        level_number = 20
                                        
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_3_2.png')
                                        wall2 =   Hero_sprite(1275,150, 'Data/images/walls/wall_loca_3_pre_exit_2.png')    
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_3_2.png')
                                        wall4 =   Hero_sprite(675,50, 'Data/images/walls/wall_loca_3_pre_exit_2.png')
                                     
                                        na_rasstrel.append(wall)
                                        na_rasstrel.append(wall2)
                                        na_rasstrel.append(wall3)
                                        na_rasstrel.append(wall4)
                                        floor_loca_2 = Hero_sprite(x-900,y+325, 'Data/images/backgrounds/floor_loca_3_2.png')  
                                        na_rasstrel.append(floor_loca_2)
                                        walle.add(floor_loca_2)
                                        walle.add(wall)
                                        walle.add(wall2)
                                        walle.add(wall3)
                                        walle.add(wall4)
                                        block = Hero_sprite(1230, 520, 'Data/images/walls/crushed_stoun.png')
                                        walle.add(block)
                                        platform2 = Hero_sprite(350, 470, 'Data/images/walls/platform_loca_3_2.png')            
                                        walle.add(platform2)
                                        na_rasstrel.append(platform2)
                                        red_trigger_button_object = Hero_sprite(640,200, 'Data/images/walls/trigger_red_button_vertical_left_1.png')
                                        red_trigger_wall = Hero_sprite(1280,500, 'Data/images/walls/trigger_red_wall_vertical_1.png')
                                        if trigger_red_button_check == False:
                                                             try:
                                                                 red_click_trigger_button_object.kill()
                                                             except:
                                                                 pass
                                                             
                                                             
                                                             trigger_red_button.add(red_trigger_button_object)
                                                             walle.add(red_trigger_wall)
                                                             na_rasstrel.append(red_trigger_button_object)
                                                             na_rasstrel.append(red_trigger_wall)
                                        platform3 = Hero_sprite(490, 350, 'Data/images/walls/platform_loca_3_2.png')            
                                        walle.add(platform3)
                                        na_rasstrel.append(platform3)
                                        kill_drevo = 0
                                        decoration.add(block)
                                        na_rasstrel.append(block)
                                 if location == 20:
                                    try:
                                        beatle.kill()
                                        
                                    except:
                                        pass
                                    try:

                                        if move_beatle_right == True:
                                            sranaya_proverka_na_x +=1
                                            if sranaya_proverka_na_x == 600:
                                                move_beatle_right = False
                                                anim_bucashka_check = 0
                                        elif move_beatle_right == False:
                                            sranaya_proverka_na_x -=1
                                            if sranaya_proverka_na_x == 360:
                                                anim_bucashka_check = 0
                                                move_beatle_right = True
                                    except:
                                        move_beatle_right = True
                                        anim_bucashka = 70
                                        die_anim_beatle_check = 0
                                        die_anim_beatle = 400
                                        beatle_killed = False
                                        anim_bucashka_check = 0
                                        sranaya_proverka_na_x =360 
                                    if beatle_killed == False:
                                        if move_beatle_right == True:
                                            if anim_bucashka_check < anim_bucashka // 7 * 1:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_right/beatle_walk_1.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 2:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_right/beatle_walk_2.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 3:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_right/beatle_walk_3.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 4:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_right/beatle_walk_4.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 5:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_right/beatle_walk_5.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 6:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_right/beatle_walk_6.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 7:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_right/beatle_walk_7.png')
                                            else:
                                                anim_bucashka_check = 0
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_right/beatle_walk_1.png')
                                            anim_bucashka_check +=1
                                            na_rasstrel.append(beatle)
                                            evil.add(beatle)    
                                        else:
                                            if anim_bucashka_check < anim_bucashka // 7 * 1:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_left/beatle_walk_1.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 2:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_left/beatle_walk_2.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 3:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_left/beatle_walk_3.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 4:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_left/beatle_walk_4.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 5:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_left/beatle_walk_5.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 6:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_left/beatle_walk_6.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 7:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_left/beatle_walk_7.png')
                                            else:
                                                anim_bucashka_check = 0
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 610, 'Data/images/enemies/beatle/walk_left/beatle_walk_1.png')
                                            anim_bucashka_check +=1
                                            na_rasstrel.append(beatle)
                                            evil.add(beatle)    

                                        
                                    if  pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False) :
                                        for ii in na_rasstrel:
                                            ii.kill()
                                        
                                        progruzka_levela = 1
                                        die_sound.play()
                                    if pygame.sprite.spritecollide(beatle, attack_hero, False):
                                        beatle.kill()
                                        if self.developer == True:    
                                            print('Это - игра, без сомнения,')
                                        if  sound_not_duplicated == 0:
                                            die_beatle.play()
                                            sound_not_duplicated =1
                                    
                                        beatle_killed = True
                                    ###триггерная кнопка::
                                    try:
                                        if pygame.sprite.spritecollide(red_button, attack_hero, False) :
                                            red_button.kill()
                                            red_button =  Hero_sprite(1070,535, 'Data/images/walls/clicked_trigger_red_button_vertical_left_1.png')
                                            na_rasstrel.append(red_button)
                                            decoration.add(red_button)
                                            red_wall_2.kill()
                                            red_wall.kill()
                                    except:
                                        pass

                                    if progruzka_levela == 1:#3-5
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        self.locationsave=location
                                        
                                        sound_not_duplicated =0
                                        move_beatle_right = True
                                        anim_bucashka = 70
                                        die_anim_beatle_check = 0
                                        die_anim_beatle = 400
                                        beatle_killed = False
                                        anim_bucashka_check = 0
                                        sranaya_proverka_na_x =360 
                                        sranaya_proverka_na_x =360 
                                        anim_bucashka = 80
                                        anim_bucashka_check = 0
                                        beatle_killed = False
                                        die_anim_beatle = 0
                                        die_anim_beatle_check = 80
                                        polozhenie_personazha(50,400)
                                        progruzka_levela = 0
                                        level_number = 22
                                        floor_loca_2 = Hero_sprite(x-1100,y+325, 'Data/images/backgrounds/floor_loca_3_3.png')  
                                        na_rasstrel.append(floor_loca_2)
                                        walle.add( floor_loca_2)
                                        floor_loca_3 = Hero_sprite(x+1100,y+325, 'Data/images/backgrounds/floor_loca_3_3.png')  
                                        na_rasstrel.append(floor_loca_3)
                                        walle.add( floor_loca_3)
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_3_3.png')
                                        na_rasstrel.append(wall)
                                        walle.add(wall)
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_3_3.png')
                                        na_rasstrel.append(wall3)
                                        walle.add(wall3)
                                        wall2 =   Hero_sprite(1275,150, 'Data/images/walls/wall_loca_3_pre_exit_3.png')    
                                        walle.add(wall2)
                                        na_rasstrel.append(wall2)
                                        wall4 =   Hero_sprite(1100,500, 'Data/images/walls/wall_loca_3_pre_exit_3.png')    
                                        walle.add(wall4)
                                        na_rasstrel.append(wall4)
                                        red_wall = Hero_sprite(1100,200, 'Data/images/walls/trigger_red_wall_vertical_1.png')   
                                        na_rasstrel.append(red_wall)
                                        walle.add(red_wall)
                                        platform = Hero_sprite(400, 650, 'Data/images/walls/platform_loca_3_3.png')    
                                        na_rasstrel.append(platform)
                                        walle.add(platform) 
                                        platform2 = Hero_sprite(555, 650, 'Data/images/walls/platform_loca_3_3.png')    
                                        na_rasstrel.append(platform2)
                                        walle.add(platform2) 
                                        red_wall_2 = Hero_sprite(925,680, 'Data/images/walls/active_trigger_red_wall_gorizontal_1.png')   
                                        na_rasstrel.append(red_wall_2)
                                        walle.add(red_wall_2)
                                        red_button =  Hero_sprite(1065,535, 'Data/images/walls/trigger_red_button_vertical_left_1.png')
                                        na_rasstrel.append(red_button)
                                        decoration.add(red_button)
                                        platform3 = Hero_sprite(675, 475, 'Data/images/walls/platform_loca_3_3.png')    
                                        na_rasstrel.append(platform3)
                                        walle.add(platform3) 
                                        platform5 = Hero_sprite(975, 330, 'Data/images/walls/platform_loca_3_3.png')    
                                        na_rasstrel.append(platform5)
                                        walle.add(platform5) 
                                        spike = Hero_sprite(1137, 637, 'Data/images/spikes/sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                 clock.tick(FPS)   
                                 if location == 21:
                                    try :
                                         if pygame.sprite.spritecollide(block, attack_hero, False)   :
                                             if kill_drevo == 0 :
                                                 breaking_tree_sound.play()
                                                 block.kill()
                                             kill_drevo =1
                                    except:
                                         pass
                                    try:
                                        snake.kill()
                                    except:
                                        start_x = 85
                                        alive_snake = True
                                        move_right = True
                                        speed_anim_snake = 150
                                        speed_anim_snake_check = 0
                                    if alive_snake == True:
                                        if move_right == True:
                                            start_x +=1
                                            if speed_anim_snake_check < speed_anim_snake // 10 * 1:
                                                snake = Hero_sprite(start_x, 255, 'Data/images/enemies/snake/walk_right/walk_1.png')
                                            elif speed_anim_snake_check < speed_anim_snake // 10 * 2:
                                                snake = Hero_sprite(start_x, 255, 'Data/images/enemies/snake/walk_right/walk_2.png')
                                            else:
                                                speed_anim_snake_check = 0
                                            speed_anim_snake_check += 1
                                            if start_x == 350:
                                                move_right = False
                                        elif move_right == False:
                                            start_x -=1
                                            if speed_anim_snake_check < speed_anim_snake // 10 * 1:
                                                snake = Hero_sprite(start_x, 255, 'Data/images/enemies/snake/walk_left/walk_1.png')
                                            elif speed_anim_snake_check < speed_anim_snake // 10 * 2:
                                                snake = Hero_sprite(start_x, 255, 'Data/images/enemies/snake/walk_left/walk_2.png')
                                            else:
                                                speed_anim_snake_check = 0
                                            speed_anim_snake_check += 1
                                            if start_x == 85:
                                                move_right = True
                                        evil.add(snake)
                                        na_rasstrel.append(snake)

                                        if  pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False) :
                                            for ii in na_rasstrel:
                                                ii.kill()
                                            
                                            progruzka_levela = 1
                                            die_sound.play()
                                        if pygame.sprite.spritecollide(snake, attack_hero, False):
                                            if self.developer == True:    
                                                print('Обречённых ждёт поражение')
                                            snake.kill()
                                            die_snake.play()
                                            alive_snake = False
                                    #анимка жука
                                    try:
                                        beatle.kill()
                                        
                                    except:
                                        pass
                                    try:

                                        if move_beatle_right == True:
                                            sranaya_proverka_na_x +=1
                                            if sranaya_proverka_na_x == 500:
                                                move_beatle_right = False
                                                anim_bucashka_check = 0
                                        elif move_beatle_right == False:
                                            sranaya_proverka_na_x -=1
                                            if sranaya_proverka_na_x == 245:
                                                anim_bucashka_check = 0
                                                move_beatle_right = True
                                    except:
                                        move_beatle_right = True
                                        anim_bucashka = 70
                                        die_anim_beatle_check = 0
                                        die_anim_beatle = 400
                                        beatle_killed = False
                                        anim_bucashka_check = 0
                                        sranaya_proverka_na_x =245
                                    if beatle_killed == False:
                                        if move_beatle_right == True:
                                            if anim_bucashka_check < anim_bucashka // 7 * 1:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_right/beatle_walk_1.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 2:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_right/beatle_walk_2.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 3:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_right/beatle_walk_3.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 4:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_right/beatle_walk_4.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 5:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_right/beatle_walk_5.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 6:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_right/beatle_walk_6.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 7:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_right/beatle_walk_7.png')
                                            else:
                                                anim_bucashka_check = 0
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_right/beatle_walk_1.png')
                                            anim_bucashka_check +=1
                                            na_rasstrel.append(beatle)
                                            evil.add(beatle)    
                                        else:
                                            if anim_bucashka_check < anim_bucashka // 7 * 1:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_left/beatle_walk_1.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 2:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_left/beatle_walk_2.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 3:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_left/beatle_walk_3.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 4:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_left/beatle_walk_4.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 5:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_left/beatle_walk_5.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 6:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_left/beatle_walk_6.png')
                                            elif anim_bucashka_check < anim_bucashka // 7 * 7:
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_left/beatle_walk_7.png')
                                            else:
                                                anim_bucashka_check = 0
                                                beatle = Hero_sprite(sranaya_proverka_na_x, 460, 'Data/images/enemies/beatle/walk_right/beatle_walk_1.png')
                                            anim_bucashka_check +=1
                                            na_rasstrel.append(beatle)
                                            evil.add(beatle)    

                                        
                                    if  pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False) :
                                        for ii in na_rasstrel:
                                            ii.kill()
                                        
                                        progruzka_levela = 1
                                        die_sound.play()
                                    if pygame.sprite.spritecollide(beatle, attack_hero, False):
                                        beatle.kill()
                                        if  sound_not_duplicated == 0:
                                            die_beatle.play()
                                            sound_not_duplicated =1
                                      
                                        beatle_killed = True
                                    try:
                                        if pygame.sprite.spritecollide(red_button, attack_hero, False) :
                                            red_button.kill()
                                            red_button =  Hero_sprite(56,150, 'Data/images/walls/clicked_trigger_red_button_vertical_1.png')
                                            na_rasstrel.append(red_button)
                                            decoration.add(red_button)
                                            red_wall2.kill()
                                            red_wall.kill()
                                            red_wall2 = Hero_sprite(650,675, 'Data/images/walls/active_trigger_red_wall_gorizontal_1.png')   
                                            na_rasstrel.append(red_wall2)
                                            walle.add(red_wall2)
                                    except:
                                        pass
                                    if progruzka_levela == 1:#3-5
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        move_beatle_right = True
                                        anim_bucashka = 70
                                        die_anim_beatle_check = 0
                                        die_anim_beatle = 400
                                        beatle_killed = False
                                        anim_bucashka_check = 0
                                        sranaya_proverka_na_x =245
                                        start_x = 85
                                        alive_snake = True
                                        move_right = True
                                        speed_anim_snake = 150
                                        speed_anim_snake_check = 0
                                        start_x = 85
                                        sranaya_proverka_na_x =245
                                        alive_snake = True
                                        speed_anim_snake = 150
                                        speed_anim_snake_check = 0
                                        sound_not_duplicated =0

                                        anim_bucashka = 80
                                        anim_bucashka_check = 0
                                        beatle_killed = False
                                        die_anim_beatle = 0
                                        die_anim_beatle_check = 80

                                        polozhenie_personazha(50,400)
                                        progruzka_levela = 0
                                        level_number = 21
                                        floor_loca_2 = Hero_sprite(x-1100,y+325, 'Data/images/backgrounds/floor_loca_3_3.png')  
                                        na_rasstrel.append(floor_loca_2)
                                        walle.add( floor_loca_2)
                                        floor_loca_3 = Hero_sprite(x+1100,y+325, 'Data/images/backgrounds/floor_loca_3_3.png')  
                                        na_rasstrel.append(floor_loca_3)
                                        walle.add( floor_loca_3)
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_3_3.png')
                                        na_rasstrel.append(wall)
                                        walle.add(wall)
                                        wall2 =   Hero_sprite(1275,150, 'Data/images/walls/wall_loca_3_pre_exit_3.png')    
                                        walle.add(wall2)
                                        na_rasstrel.append(wall2)
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_3_3.png')
                                        na_rasstrel.append(wall3)
                                        walle.add(wall3)
                                        red_wall = Hero_sprite(1300-25,500, 'Data/images/walls/trigger_red_wall_vertical_1.png')   
                                        na_rasstrel.append(red_wall)
                                        walle.add(red_wall)
                                        red_wall2 = Hero_sprite(650,675, 'Data/images/walls/trigger_red_wall_gorizontal_1.png')   
                                        na_rasstrel.append(red_wall2)
                                        decoration.add(red_wall2)
                                        wall4 =   Hero_sprite(650,250, 'Data/images/walls/wall_loca_3_pre_exit_3.png')    
                                        walle.add(wall4)
                                        na_rasstrel.append(wall4)
                                        platform = Hero_sprite(450, 500, 'Data/images/walls/platform_loca_3_3.png')    
                                        na_rasstrel.append(platform)
                                        walle.add(platform) 
                                        platform2 = Hero_sprite(295, 500, 'Data/images/walls/platform_loca_3_3.png')    
                                        na_rasstrel.append(platform2)
                                        walle.add(platform2) 
                                        platform3 = Hero_sprite(130, 300, 'Data/images/walls/platform_loca_3_3.png')    
                                        na_rasstrel.append(platform3)
                                        walle.add(platform3)
                                        platform4 = Hero_sprite(285, 300, 'Data/images/walls/platform_loca_3_3.png')    
                                        na_rasstrel.append(platform4)
                                        walle.add(platform4)
                                        red_button =  Hero_sprite(60,150, 'Data/images/walls/trigger_red_button_vertical_1.png')
                                        na_rasstrel.append(red_button)
                                        decoration.add(red_button)
                                        spike = Hero_sprite(1150, 635, 'Data/images/spikes/sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                 if location == 22:
                                     try:
                                                           if sprite_hero_walk_left_1.rect.y > niz_levela and len(pygame.sprite.spritecollide(sprite_hero_walk_left_2, walle, False)) >0:
                                                            for ii in na_rasstrel:
                                                             ii.kill()
                                                            progruzka_levela = 1
                                                            die_sound.play()   
                                     except:
                                                           pass
                                     try:
                                         if  pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False) :
                                            for ii in na_rasstrel:
                                                ii.kill()
                                            
                                            progruzka_levela = 1
                                            die_sound.play()
                                     except:
                                         pass
                                     try:
                                         if attaka2_vpered == 1 :
                                  
                                             
                                             if krab_est == 1 and podgotovka == 0:
                                                 if krab.rect.x  <  100 :
                                                     krab.rect.x  += 5
                                                     klesna_right.rect.x +=5
                                                     klesna_left.rect.x +=5
                                                    
                                                 if krab.rect.x >  100 :
                                                     krab.rect.x  -= 5
                                                     klesna_right.rect.x -=5
                                                     klesna_left.rect.x -=5
                                                 if krab.rect.y >  300 and x_dollot == 1 :
                                                     krab.rect.y  -= 5
                                                     klesna_right.rect.y -=5
                                                     klesna_left.rect.y -=5
                                                 if krab.rect.y == 400:
                                                     y_dollot = 1
                                                 if krab.rect.x == 100:
                                                      x_dollot = 1
                                                 if y_dollot == 1 and x_dollot == 1 and podgotovka == 0 :
                                                    klesna_right.rect.y +=1000
                                                    klesna_left.rect.y +=1000
                                                    podgotovka = 1
                                                 
                                                    reznya = Hero_sprite(krab.rect.x+130,krab.rect.y+100, 'Data/images/second_boss/pila.png')
                                                    evil.add(reznya )
                                                    na_rasstrel.append(reznya )

                                                    
                                        
                                                    
                                                        
                                     except:
                                         pass
                                     try:
                                         if podgotovka == 1:
                                         
                                                    
                                                    
                                                        if krab.rect.x <  800 :
                                                             klesna_right.rect.x +=1
                                                             klesna_left.rect.x +=1
                                                             krab.rect.x += 1
                                                             reznya.rect.x += 1
                                                               
                                                        if krab.rect.x ==  800:
                                                            reznya.kill()
                                                            attak_number = 9
                                                            attaka2_vpered = 2
                                                            attak1_podgotovka = 1
                                                            podgotovka = 0
                                                            
                                     except:
                                         pass
                                     try:
                                         if attak1_podgotovka == 1:
                                         
                                                    
                                                   
                                                            
                                                        if krab.rect.y<=  260:
                                                            attak_number = 0
                                                            
                                                            attaka2_vpered = 0
                                                            attak1_podgotovka = 0
                                                            x_dollot = 0
                                                            y_dollot = 0
                                                            ozidanie_pered_attakoy= 0
                                                            bil_udar = 0
                                                            klesna_right.rect.y -=1000
                                                            klesna_left.rect.y -=1000
                                                        else:
                                                            krab.rect.y -= 5
                                                            klesna_right.rect.y -=5
                                                            klesna_left.rect.y -=5.
                                                            
                                                            
                                     except:
                                         pass
                                     try:
                                         if attak_number < 4 and attaka2_vpered == 0 :
                                             if krab_est != 1 :
                                                 try:
                                                        reznya.kill()
                                                 except:
                                                        pass
                                                 try:
                                                     luch.kill()
                                                     portal_luch.kill()
                                                     portal_luch2.kill()
                                                     luch1.kill()
                                                     
                                                 except:
                                                     pass
                                       
                                                 krab.kill()
                                                 klesna_right.kill()
                                                 klesna_left.kill()
                                                 krab = Hero_sprite(evil_x,evil_y, 'Data/images/second_boss/krab.png')
                                                 evil.add(krab)
                                                 na_rasstrel.append(krab)
                                                 klesna_right = Hero_sprite(evil_x-125,evil_y+30, 'Data/images/second_boss/left_claw_closed.png')
                                                 evil.add(klesna_right)
                                                 na_rasstrel.append(klesna_right)
                                                 klesna_left = Hero_sprite(evil_x+125,evil_y+30, 'Data/images/second_boss/right_claw_closed.png')
                                
                                                 evil.add(klesna_left)
                                                 na_rasstrel.append(klesna_left)
                                                 krab_est = 1
                                             if krab_est == 1:
                                                 
                                                 if sprite_hero_walk_left_1.rect.x < krab.rect.x-30 and dlotelnost_ataki == 0 :
                                                     krab_napravlenie = 'right'
                                                 elif sprite_hero_walk_left_1.rect.x > krab.rect.x and dlotelnost_ataki== 0  :
                                                     krab_napravlenie = 'left'
                                                 if sprite_hero_walk_left_1.rect.x == krab.rect.x-30 and dlotelnost_ataki== 0:
                                                     pora_ataka = 1
                                                 if pora_ataka == 1  : 
                                                     if dlotelnost_ataki < 200000 and attak_number < 4:
                                                         dlotelnost_ataki += 1000
                                                         if dlotelnost_ataki == 1000 :
                                                             attak_number +=1
                                                         if dlotelnost_ataki == 110000 :
                                                             portal_luch = Hero_sprite(klesna_left.rect.x+40,klesna_left.rect.y+220, 'Data/images/second_boss/portal_laser.png')
                                                             portal_luch2 = Hero_sprite(klesna_right.rect.x+40,klesna_right.rect.y+220, 'Data/images/second_boss/portal_laser.png')
                                                             na_rasstrel.append(portal_luch)
                                                             na_rasstrel.append(portal_luch2)
                                                             evil.add(portal_luch)
                                                             evil.add(portal_luch2)
                                                             luch = Hero_sprite(klesna_left.rect.x+40,klesna_left.rect.y+350, 'Data/images/second_boss/laser.png')
                                                             evil.add(luch )
                                                             na_rasstrel.append(luch )
                                                             luch1 = Hero_sprite(klesna_right.rect.x+40,klesna_right.rect.y+350, 'Data/images/second_boss/laser.png')
                                                             evil.add(luch1 )
                                                             na_rasstrel.append(luch1 )
                                                             laser_atk.play()
                                                     else :
                                                         try:
                                                             luch.kill()
                                                             portal_luch.kill()
                                                             portal_luch2.kill()
                                                             luch1.kill()
                                                             
                                                         except:
                                                             pass
                                                         dlotelnost_ataki = 0
                                                         pora_ataka = 0
                                                 if dlotelnost_ataki == 0:
                                                     
                                                     if  krab_napravlenie == 'right'  :
                                                                     
                                                                                                                 
                                                         klesna_right.rect.x-=5
                                                         klesna_left.rect.x-=5
                                                         krab.rect.x-=5
                                                     else:
                                                         klesna_right.rect.x+=5
                                                         klesna_left.rect.x+=5
                                                         krab.rect.x+=5
                                                
                                           
                                             
                                             
                                     except:
                                         pass
                                     
                                     try:
                                         if  attak_number == 4 :
                                         
                                                 
                                                 
                                                 if krab.rect.x <  500 :
                                                         
                                                         krab_napravlenie = 'left'
                                                    
                                                 if krab.rect.x >  500 :
                                                         krab_napravlenie = 'right'
                                                      
                                                 if  krab_napravlenie == 'right'  :
                                                                     
                                                                                                                 
                                                         klesna_right.rect.x-=5
                                                         klesna_left.rect.x-=5
                                                         krab.rect.x-=5
                                                 if  krab_napravlenie == 'left':
                                                     
                                                         klesna_right.rect.x+=5
                                                         klesna_left.rect.x+=5
                                                         krab.rect.x+=5
                                                 if  krab_napravlenie == 'down':
                                                         klesna_right.rect.y+=5
                                                         klesna_left.rect.y+=5
                                                         krab.rect.y+=5
                                                 if krab.rect.y <  500 and x_dollot == 1 :
                                                         krab_napravlenie = 'down'
                                                         
                                                 if  krab.rect.y >=  500   :
                                                     y_dollot = 1
                                                     krab_napravlenie = 'stop'
                                                 if krab.rect.x  == 500 :
                                                     
                                                     x_dollot = 1
                                                 if y_dollot == 1 and x_dollot == 1:
                                                    if ozidanie_pered_attakoy == 1000000:
                                                        attaka2_vpered = 1
                                                        attak_number = 0
                                                        x_dollot = 0
                                                        y_dollot = 0
                                                    ozidanie_pered_attakoy+=1000
                                            
                                     except:
                                         pass
                                     try :
                                         if pygame.sprite.spritecollide(krab, attack_hero, False)  or   pygame.sprite.spritecollide(klesna_left, attack_hero, False) or   pygame.sprite.spritecollide(klesna_right, attack_hero, False):
                                             if bil_udar == 0:
                                                
                                                hp_boss -=1
                                                bil_udar = 1
                                                hp_bar.kill()
                                                if hp_boss == 3:
                                                    hp_bar =  Hero_sprite(evil_x-90,evil_y-140, 'Data/images/decorations/hp bar second boss/hp_bar_3of4.png')
                                                    na_rasstrel.append(hp_bar)
                                                    decoration.add(hp_bar)
                                                elif hp_boss == 2:
                                                    hp_bar =  Hero_sprite(evil_x-90,evil_y-140, 'Data/images/decorations/hp bar second boss/hp_bar_2of4.png')
                                                    na_rasstrel.append(hp_bar)
                                                    decoration.add(hp_bar)
                                                elif hp_boss == 1:
                                                    hp_bar =  Hero_sprite(evil_x-90,evil_y-140, 'Data/images/decorations/hp bar second boss/hp_bar_1of4.png')
                                                    na_rasstrel.append(hp_bar)
                                                    decoration.add(hp_bar)
                                                elif hp_boss == 0:
                                                    hp_bar =  Hero_sprite(evil_x-90,evil_y-140, 'Data/images/decorations/hp bar second boss/hp_bar_0of4.png')
                                                    na_rasstrel.append(hp_bar)
                                                    decoration.add(hp_bar)
                                                    krab.kill()
                                                    try:
                                                        krab.kill()
                                                    except:
                                                        pass
                                                    ixs = krab.rect.x
                                                    ygrek = krab.rect.y
                                                    krab = Hero_sprite(evil_x,evil_y, 'Data/images/second_boss/krab.png')
                                                    na_rasstrel.append(krab)
                                                    walle.add(krab)
                                                    dialoge_check = 0
                                                    die_animation = False
                                                
                                               
                                         if hp_boss == 0:
                                                 try:

                                                     portal_luch.kill()
                                                     portal_luch2.kill()

                                                     luch.kill()
                                                     luch1.kill()
                                                     reznya.kill()
                                                     klesna_right.kill()
                                                     klesna_left.kill()
                                                 except:
                                                     pass

                                                 attak_number = 9
                                                 attaka2_vpered = 2
                                                 attak1_podgotovka = 1
                                                 podgotovka = 0
                                                 attak1_podgotovka = 0
                                                 klesna_right.kill()
                                                 klesna_left.kill()
                                                 jiv = 0
                                                 perehod_x = 12000
                                                 if krab.rect.y < 500:
                                                    evil_y +=1
                                                    krab.rect.y = evil_y
                                                    dialoge_check = 0
                                                 if krab.rect.y <= 520 and dialoge_check == 0 and die_animation == False:#bamableyla pd
                                                    hp_bar.kill()
                                                    peremennaya = True
                                                    decoration.add(text_frame)
                                                    decoration.add(crab_frame)
                                                 if peremennaya == True:
                                                    if dialoge_check < 700:
            
                                                        dialoge_check +=1
                                                    else:
                                                            text_frame.kill()
                                                            portaliy = Hero_sprite(50,550, 'Data/images/decorations/portal/crab_portal.png')
                                                            text_frame =Hero_sprite(600, 200, 'Data/images/walls/crab_Frame_for_text2.png')
                                                            na_rasstrel.append(text_frame)
                                                            decoration.add(portaliy)
                                                            na_rasstrel.append(portaliy)
                                                            trigers.add(portaliy)
                                                            peremennaya = False
                                                            crab_frame.kill()
                                                            die_animation = True
                                                 if die_animation == True:
                                                    try:
                                                        crab_frame.kill()
                                                    except:
                                                        pass
                                                    krab.kill()
                                                    krab = Hero_sprite(evil_x,evil_y, 'Data/images/second_boss/in_sleep_5.png')
                                                    na_rasstrel.append(krab)
                                                    decoration.add(krab)
                                                 if pygame.sprite.spritecollide(sprite_hero_walk_left_2, trigers, False):
                                                    sc.blit(text_frame.image, text_frame.rect)

                                                    if keys[pygame.K_e]:
                                                        for ii in na_rasstrel:
                                                            ii.kill()
                                                        perehod_x = 1








                                     except:
                                         pass
                                     try:
                                        hp_bar.rect.x = krab.rect.x +20
                                        hp_bar.rect.y = krab.rect.y -70

                                     except:
                                        pass
                                     if progruzka_levela == 1:#3-6
                                            try:
                                                text_frame.kill()
                                            except:
                                                pass
                                            self.conn = sqlite3.connect('gameinfo.db')
                                            self.cur = self.conn.cursor()
                                            if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                            elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                            else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                            self.conn.commit()
                                            self.cur.close()
                                            try:
                                                   portal_luch.kill()
                                                   portal_luch2.kill()     
                                            except:
                                                pass
                                            try:
                                                   klesna_right.kill()
                                                   klesna_left.kill()    
                                            except:
                                                        pass
                                            try:
                                                        reznya.kill()
                                            except:
                                                        pass
                                            try:
                                                 
                                                 luch.kill()
                                                 portal_luch.kill()
                                                 portal_luch2.kill()
                                                 luch1.kill()
                                                 krab.kill()
                                                 klesna_right.kill()
                                                 klesna_left.kill()
                                            except:
                                                 pass
                                            try:
                                                hp_bar.kill()
                                            except:
                                                pass

                                            attaka2_vpered = 0
                                            x_dollot = 0
                                            y_dollot = 0
                                            ozidanie_pered_attakoy = 0
                                            attak_number = 0
                                            pora_ataka = 0
                                            attak_moment = 0
                                            dlotelnost_ataki = 0
                                            krab_est = 0
                                            evil_x = 800
                                            evil_y = 300
                                            bil_udar = 0


                                            anim_sleep = 100
                                            anim_sleep_check = 0
                                            die_animation = False

                                            krab_napravlenie = 'right'
                                            krab = Hero_sprite(evil_x,evil_y, 'Data/images/second_boss/krab.png')
                                            evil.add(krab)
                                            na_rasstrel.append(krab)
                                            klesna_right = Hero_sprite(evil_x-125,evil_y+50, 'Data/images/second_boss/left_claw_closed.png')
                                            hp_boss = 4 
                                            hp_bar =  Hero_sprite(evil_x-90,evil_y-140, 'Data/images/decorations/hp bar second boss/hp_bar_4of4.png')
                                            na_rasstrel.append(hp_bar)
                                            decoration.add(hp_bar)
                                            evil.add(klesna_right)
                                            na_rasstrel.append(klesna_right)
                                            klesna_left = Hero_sprite(evil_x+125,evil_y+50, 'Data/images/second_boss/right_claw_closed.png')
                                            podgotovka = 0
                                            attak1_podgotovka = 0
                                            evil.add(klesna_left)
                                            na_rasstrel.append(klesna_left)
                                            background_loca_3.kill()
                                            background_loca_3 = Hero_sprite(x,y, 'Data/images/backgrounds/bg_loca_3_2.png')
                                            progruzka_levela = 0
                                            polozhenie_personazha(100,500)
                                            platform2 = Hero_sprite(400, 470, 'Data/images/walls/platform_loca_3_3.png')    
                                            na_rasstrel.append(platform2)
                                            walle.add(platform2)
                                            platform3 = Hero_sprite(900, 470, 'Data/images/walls/platform_loca_3_3.png')    
                                            na_rasstrel.append(platform3)
                                            walle.add(platform3) 
                                            perehod_x = 1250
                                            level_number = 23
                                            floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_3_3.png')  
                                            wall = Hero_sprite(10, 350, 'Data/images/walls/wall_loca_3_3.png')
                                            wall2 =   Hero_sprite(1275,350, 'Data/images/walls/wall_loca_3_3.png')    
                                            wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_3_3.png')
                                            niz_levela = 520
        
                                            text_frame =Hero_sprite(700, 200, 'Data/images/walls/crab_Frame_for_text.png')
                                            na_rasstrel.append(text_frame)
                                            #decoration.add(text_frame)
                                            crab_frame = Hero_sprite(250, 200, 'Data/images/characters/crab_Frame.png')
                                            na_rasstrel.append(crab_frame)
                                            #decoration.add(crab_frame)
                                            dialoge_check = 0
                                            peremennaya = False
                                            try:
                                                krab.kill()
                                            except:
                                                pass
                                            try:
                                                krab.kill()
                                            except:
                                                pass
                                            na_rasstrel.append(wall)
                                            na_rasstrel.append(wall2)
                                            na_rasstrel.append(wall3)
                                            na_rasstrel.append(floor_loca_1)
                                            walle.add(floor_loca_1)
                                            walle.add(wall)
                                            walle.add(wall2)
                                            walle.add(wall3) 
                                 if location == 23:

                                    if progruzka_levela == 1:#4-1
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        perehod_x = 1250
                                        try:
                                            hp_bar.kill()
                                            klesna_left.kill()
                                            klesna_right.kill()
                                            beatle.kill()
                                        except:
                                            pass
                                        progruzka_levela = 0
                                        polozhenie_personazha(200, 500)
                                        floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_4.png')
                                        na_rasstrel.append(floor_loca_1)
                                        walle.add(floor_loca_1)
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_4.png')
                                        wall2 =   Hero_sprite(1275,150, 'Data/images/walls/wall_loca_4_pre_exit.png')    
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_4.png')   
                                        walle.add(wall)
                                        walle.add(wall2)
                                        walle.add(wall3)
                                        na_rasstrel.append(wall)
                                        na_rasstrel.append(wall2)  
                                        na_rasstrel.append(wall3)
                                        level_number = 24
                                 if location == 24:
                                    #скелет
                                    try:
                                        if skeleton_alive == True:
                                            if move_skelet == 'right':
                                                skeleton.kill()
                                                skelet_x +=1
                                                if move_skelet_anim_check <= move_skelet_anim // 4 * 1:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_1.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 2:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_2.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 3:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_3.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 4:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_4.png')

                                                if skelet_x == end_skeleton_x:
                                                    move_skelet = 'left'
                                                move_skelet_anim_check+=1
                                                if move_skelet_anim_check == move_skelet_anim:
                                                    move_skelet_anim_check = 0

                                            elif move_skelet == 'left':
                                                skeleton.kill()
                                                skelet_x -=1
                                                if move_skelet_anim_check <= move_skelet_anim // 4 * 1:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_1.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 2:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_2.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 3:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_3.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 4:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_4.png')
                                                if skelet_x == start_skelet_x:
                                                    move_skelet = 'right'
                                                move_skelet_anim_check+=1
                                                if move_skelet_anim_check == move_skelet_anim:
                                                    move_skelet_anim_check = 0

                                            evil.add(skeleton)
                                            na_rasstrel.append(skeleton)
                                            if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False):
                                                for ii in na_rasstrel:
                                                    ii.kill()
                                                progruzka_levela = 1
                                                die_sound.play()
                                            if pygame.sprite.spritecollide(skeleton, attack_hero, False):
                                                skeleton_alive = False
                                                die_skeleton.play()
                                                skeleton.kill()
                                    except:
                                        start_skelet_x = 775#начальная точка х
                                        start_skelet_y = 570#начальная точка у
                                        end_skeleton_x = 1200#при каком х поворачивать влево
                                        skelet_x = start_skelet_x#это для проверки на х
                                        skelet_y = start_skelet_y
                                        move_skelet = 'right'
                                        move_skelet_anim = 100
                                        move_skelet_anim_check = 0
                                        skeleton = Hero_sprite(start_skelet_x,start_skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_1.png')

                                    #кнопка
                                    try:
                                        if pygame.sprite.spritecollide(red_button, attack_hero, False):
                                            red_button.kill()
                                            red_button = Hero_sprite(619,240, 'Data/images/walls/clicked_trigger_red_button_vertical_left_1.png')
                                            na_rasstrel.append(red_button)
                                            decoration.add(red_button)
                                            wall_red.kill()
                                    except:
                                        clicked_but = False
                                    #конец кнопки
                                    if progruzka_levela == 1:#4-2 десять пятого
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        start_skelet_x = 775#начальная точка х
                                        start_skelet_y = 570#начальная точка у
                                        end_skeleton_x = 1200#при каком х поворачивать влево
                                        skelet_x = start_skelet_x#это для проверки на х
                                        skelet_y = start_skelet_y
                                        move_skelet = 'right'
                                        move_skelet_anim = 100
                                        move_skelet_anim_check = 0
                                        progruzka_levela = 0
                                        polozhenie_personazha(200, 500)
                                        skeleton_alive = True
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_4.png')
                                        wall2 =   Hero_sprite(1275,250, 'Data/images/walls/wall_loca_4_pre_exit.png')    
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_4.png')   
                                        wall4 =   Hero_sprite(650,250, 'Data/images/walls/wall_loca_4_pre_exit.png')    
                                        walle.add(wall)
                                        walle.add(wall2)
                                        walle.add(wall3)
                                        walle.add(wall4)
                                        na_rasstrel.append(wall)
                                        na_rasstrel.append(wall2)  
                                        na_rasstrel.append(wall3)
                                        na_rasstrel.append(wall4)
                                        level_number = 25
                                        platform =  Hero_sprite(130,480, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        platform2 =  Hero_sprite(550,340, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform2)
                                        na_rasstrel.append(platform2)  
                                        wall_red = Hero_sprite(650,600, 'Data/images/walls/trigger_red_wall_vertical_1.png')   
                                        walle.add(wall_red)
                                        na_rasstrel.append(wall_red) 
                                        floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_4.png')
                                        na_rasstrel.append(floor_loca_1)
                                        walle.add(floor_loca_1)
                                        red_button = Hero_sprite(615,240, 'Data/images/walls/trigger_red_button_vertical_left_1.png')
                                        decoration.add(red_button)
                                        na_rasstrel.append(red_button)
                                 if location == 25:
                                    try:
                                        if pygame.sprite.spritecollide(red_button, attack_hero, False):
                                            red_button.kill()
                                            red_button = Hero_sprite(994,500, 'Data/images/walls/clicked_trigger_red_button_vertical_left_1.png')
                                            na_rasstrel.append(red_button)
                                            decoration.add(red_button)
                                            wall_red.kill()
                                            wall_red = Hero_sprite(620,675, 'Data/images/walls/active_trigger_red_wall_gorizontal_1.png')
                                            walle.add(wall_red  )
                                            na_rasstrel.append(wall_red)
                                            red_wall.kill()
                                    except:
                                        clicked_but = False

                                    try:
                                        if skeleton_alive == True:
                                            if move_skelet == 'right':
                                                skeleton.kill()
                                                skelet_x +=1
                                                if move_skelet_anim_check <= move_skelet_anim // 4 * 1:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_1.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 2:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_2.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 3:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_3.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 4:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_4.png')

                                                if skelet_x == end_skeleton_x:
                                                    move_skelet = 'left'
                                                move_skelet_anim_check+=1
                                                if move_skelet_anim_check == move_skelet_anim:
                                                    move_skelet_anim_check = 0

                                            elif move_skelet == 'left':
                                                skeleton.kill()
                                                skelet_x -=1
                                                if move_skelet_anim_check <= move_skelet_anim // 4 * 1:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_1.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 2:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_2.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 3:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_3.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 4:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_4.png')
                                                if skelet_x == start_skelet_x:
                                                    move_skelet = 'right'
                                                move_skelet_anim_check+=1
                                                if move_skelet_anim_check == move_skelet_anim:
                                                    move_skelet_anim_check = 0

                                            evil.add(skeleton)
                                            na_rasstrel.append(skeleton)
                                            if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False):
                                                for ii in na_rasstrel:
                                                    ii.kill()
                                                progruzka_levela = 1
                                                die_sound.play()
                                            if pygame.sprite.spritecollide(skeleton, attack_hero, False):
                                                skeleton_alive = False
                                                die_skeleton.play()
                                                skeleton.kill()
                                    except:
                                        start_skelet_x = 400#начальная точка х
                                        start_skelet_y = 215#начальная точка у
                                        end_skeleton_x = 850#при каком х поворачивать влево
                                        skelet_x = start_skelet_x#это для проверки на х
                                        skelet_y = start_skelet_y
                                        move_skelet = 'right'
                                        move_skelet_anim = 100
                                        move_skelet_anim_check = 0
                                        skeleton = Hero_sprite(start_skelet_x,start_skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_1.png')
                                    if progruzka_levela == 1:#4-3
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        start_skelet_x = 400#начальная точка х
                                        start_skelet_y = 215#начальная точка у
                                        end_skeleton_x = 850#при каком х поворачивать влево
                                        skelet_x = start_skelet_x#это для проверки на х
                                        skelet_y = start_skelet_y
                                        move_skelet = 'right'
                                        move_skelet_anim = 100
                                        move_skelet_anim_check = 0
                                        progruzka_levela = 0
                                        level_number = 26
                                        skeleton_alive = True
                                        red_wall =  Hero_sprite(1025,150, 'Data/images/walls/trigger_red_wall_vertical_1.png')
                                        walle.add(red_wall)
                                        na_rasstrel.append(red_wall)
                                        polozhenie_personazha(200, 500)
                                        floor_loca_1 = Hero_sprite(150,675, 'Data/images/backgrounds/short_floor_loca_4.png')
                                        na_rasstrel.append(floor_loca_1)
                                        walle.add(floor_loca_1)
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_4.png')
                                        wall2 =   Hero_sprite(1275,250, 'Data/images/walls/wall_loca_4_pre_exit.png')    
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_4.png')    
                                        walle.add(wall)
                                        walle.add(wall2)
                                        walle.add(wall3)
                                        na_rasstrel.append(wall)
                                        na_rasstrel.append(wall2)  
                                        na_rasstrel.append(wall3)
                                        platform =  Hero_sprite(130,480, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        platform =  Hero_sprite(470,300, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        platform =  Hero_sprite(630,300, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        platform =  Hero_sprite(790,300, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        platform =  Hero_sprite(925,600, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        wall4 =   Hero_sprite(1025,450, 'Data/images/walls/wall_loca_4_pre_exit.png')
                                        walle.add(wall4)
                                        na_rasstrel.append(wall4)
                                        floor_loca_2 = Hero_sprite(1150,675, 'Data/images/backgrounds/short_floor_loca_4.png')
                                        na_rasstrel.append(floor_loca_2)
                                        walle.add(floor_loca_2)
                                        wall_red = Hero_sprite(620,675, 'Data/images/walls/trigger_red_wall_gorizontal_1.png')
                                        decoration.add(wall_red)
                                        na_rasstrel.append(wall_red) 
                                        red_button = Hero_sprite(990,500, 'Data/images/walls/trigger_red_button_vertical_left_1.png')
                                        na_rasstrel.append(red_button)
                                        decoration.add(red_button)
                                 if location == 26:
                                    

                                    try:
                                        if skeleton_alive == True:
                                            if move_skelet == 'right':
                                                skeleton.kill()
                                                skelet_x +=1
                                                if move_skelet_anim_check <= move_skelet_anim // 4 * 1:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_1.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 2:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_2.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 3:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_3.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 4:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_4.png')

                                                if skelet_x == end_skeleton_x:
                                                    move_skelet = 'left'
                                                move_skelet_anim_check+=1
                                                if move_skelet_anim_check == move_skelet_anim:
                                                    move_skelet_anim_check = 0

                                            elif move_skelet == 'left':
                                                skeleton.kill()
                                                skelet_x -=1
                                                if move_skelet_anim_check <= move_skelet_anim // 4 * 1:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_1.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 2:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_2.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 3:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_3.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 4:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_4.png')
                                                if skelet_x == start_skelet_x:
                                                    move_skelet = 'right'
                                                move_skelet_anim_check+=1
                                                if move_skelet_anim_check == move_skelet_anim:
                                                    move_skelet_anim_check = 0

                                            evil.add(skeleton)
                                            na_rasstrel.append(skeleton)
                                            
                                            if pygame.sprite.spritecollide(skeleton, attack_hero, False):
                                                skeleton_alive = False
                                                die_skeleton.play()
                                                skeleton.kill()
                                    except:
                                        start_skelet_x = 150#начальная точка х
                                        start_skelet_y = 160#начальная точка у
                                        end_skeleton_x = 1000#при каком х поворачивать влево
                                        skelet_x = start_skelet_x#это для проверки на х
                                        skelet_y = start_skelet_y
                                        move_skelet = 'right'
                                        move_skelet_anim = 100
                                        move_skelet_anim_check = 0
                                        skeleton = Hero_sprite(start_skelet_x,start_skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_1.png')
                                    
                                    if pygame.sprite.spritecollide(red_button, attack_hero, False):
                                            red_button.kill()
                                            red_button = Hero_sprite(56,140, 'Data/images/walls/clicked_trigger_red_button_vertical_1.png')
                                            na_rasstrel.append(red_button)
                                            decoration.add(red_button)
                                            red_wall.kill()
                                        
                                    
                                    
                                    try:
                                       if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False):
                                                for ii in na_rasstrel:
                                                    ii.kill()
                                                progruzka_levela = 1
                                                die_sound.play()
                                        
                                    except:
                                        pass
                                    if progruzka_levela ==1 :#4-4
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        start_skelet_x = 150#начальная точка х
                                        start_skelet_y = 160#начальная точка у
                                        end_skeleton_x = 1000#при каком х поворачивать влево
                                        skelet_x = start_skelet_x#это для проверки на х
                                        skelet_y = start_skelet_y
                                        move_skelet = 'right'
                                        move_skelet_anim = 100
                                        move_skelet_anim_check = 0
                                        progruzka_levela = 0
                                        level_number = 27
                                        skeleton_alive = True
                                        polozhenie_personazha(200, 500)
                                        red_wall =  Hero_sprite(1275,600, 'Data/images/walls/trigger_red_wall_vertical_1.png')
                                        walle.add(red_wall)
                                        na_rasstrel.append(red_wall)
                                        floor_loca_1 = Hero_sprite(650,675, 'Data/images/backgrounds/floor_loca_4.png')
                                        na_rasstrel.append(floor_loca_1)
                                        walle.add(floor_loca_1)
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_4.png')
                                        wall2 =   Hero_sprite(1275,250, 'Data/images/walls/wall_loca_4_pre_exit.png')    
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_4.png')    
                                        walle.add(wall)
                                        walle.add(wall2)
                                        walle.add(wall3)
                                        na_rasstrel.append(wall)
                                        na_rasstrel.append(wall2)  
                                        na_rasstrel.append(wall3)
                                        platform =  Hero_sprite(1170,440, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        platform =  Hero_sprite(1010,480, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        platform =  Hero_sprite(850,480, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        platform =  Hero_sprite(690,480, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)  
                                        platform =  Hero_sprite(530,480, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform) 
                                        platform =  Hero_sprite(370,480, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform) 
                                        platform =  Hero_sprite(120,250, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform) 
                                        platform =  Hero_sprite(290,250, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(450,250, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(610,250, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(770,250, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(930,250, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        red_button = Hero_sprite(60,140, 'Data/images/walls/trigger_red_button_vertical_1.png')
                                        na_rasstrel.append(red_button)
                                        decoration.add(red_button)
                                        spike = Hero_sprite(610, 465, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(930, 465, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                 if location == 27:
                                    try:
                                        if  crush_wall_on == True :
                                            perehod_x = 12500000
                                            if   Oleg.rect.x == 1250:
                                                for ii in na_rasstrel:
                                                    ii.kill()
                                                secret_bambaleyla = True
                                                progruzka_levela = 1
                                      
                                    
                                    except:
                                        pass
                                    if secret_bambaleyla == True :
                                        if progruzka_levela == 1 and no_two_bambaleyla != True: 
                                            no_two_bambaleyla = True
                                            polozhenie_personazha(160, 460)
                                            perehod_x = 1400
                                            anim_bambaleyla = 72
                                            anim_bambaleyla_check = 0
                                            polozhenie_personazha(160, 460)
                                            progruzka_levela = 0
                                            floor_loca_1 = Hero_sprite(650,675, 'Data/images/backgrounds/bambaleyla_floor_room.png')
                                            na_rasstrel.append(floor_loca_1)
                                            walle.add(floor_loca_1)
                                            wall = Hero_sprite(1300,350, 'Data/images/walls/bambaleyla_vertical_wall.png')
                                            walle.add(wall)
                                            na_rasstrel.append(wall)
                                            floor_loca_1 = Hero_sprite(650,25, 'Data/images/backgrounds/bambaleyla_floor_room.png')
                                            na_rasstrel.append(floor_loca_1)
                                            walle.add(floor_loca_1)
                                            wall = Hero_sprite(0,250, 'Data/images/walls/bambaleyla_vertical_wall_pre_exit.png')
                                            walle.add(wall)
                                            na_rasstrel.append(wall)
                                            bambaleyla = Hero_sprite(1100,535, 'Data/images/characters/bambaleyla_1.png')
                                            decoration.add(bambaleyla)
                                            na_rasstrel.append(bambaleyla)
                                            dialoge_check = 0
                                            dialoge_bambaleyla = False
                                            text_frame = Hero_sprite(650, 200, 'Data/images/walls/bambaleyla_Frame_for_text.png')
                                            na_rasstrel.append(text_frame)
                                            bambaleyla_frame = Hero_sprite(250, 200, 'Data/images/characters/bambaleyla_frame.png')
                                            na_rasstrel.append(bambaleyla_frame)
                                            bambaleyla_frame2 = Hero_sprite(600, 200, 'Data/images/walls/bambaleyla_Frame_for_text.png')
                                            na_rasstrel.append(bambaleyla_frame2)
                                            text_color = (225,225, 5)
                                            text = font.render("О! Приветствую, Путник!", True, (text_color))
                                            place = text.get_rect(center=(520, 200))
                                            place2 = text.get_rect(center=(470, 200))
                                            table = Hero_sprite(850, 600, 'Data/images/decorations/table.png')
                                            na_rasstrel.append(table)
                                            trigers.add(table)
                                            ashtray = Hero_sprite(850, 515, 'Data/images/decorations/ashtray.png')
                                            na_rasstrel.append(ashtray)
                                            trigers.add(ashtray)


                                        #bambaleyla.kill()
                                        if anim_bambaleyla_check == anim_bambaleyla // 4 * 1:
                                            bambaleyla.kill()
                                            bambaleyla = Hero_sprite(1100,535, 'Data/images/characters/bambaleyla_1.png')
                                            decoration.add(bambaleyla)
                                            na_rasstrel.append(bambaleyla)
                                        elif anim_bambaleyla_check == anim_bambaleyla// 4 * 2:
                                            bambaleyla.kill()
                                            bambaleyla = Hero_sprite(1100,535, 'Data/images/characters/bambaleyla_2.png')
                                            decoration.add(bambaleyla)
                                            na_rasstrel.append(bambaleyla)
                                        elif anim_bambaleyla_check == anim_bambaleyla// 4 * 3:
                                            bambaleyla.kill()
                                            bambaleyla = Hero_sprite(1100,535, 'Data/images/characters/bambaleyla_3.png')
                                            decoration.add(bambaleyla)
                                            na_rasstrel.append(bambaleyla)
                                        elif anim_bambaleyla_check == anim_bambaleyla // 4 * 4:
                                            bambaleyla.kill()
                                            bambaleyla = Hero_sprite(1100,535, 'Data/images/characters/bambaleyla_2.png')
                                            decoration.add(bambaleyla)
                                            na_rasstrel.append(bambaleyla)
                                        anim_bambaleyla_check +=1
                                        if anim_bambaleyla_check == anim_bambaleyla:
                                            anim_bambaleyla_check = 0
                                        if pygame.sprite.spritecollide(sprite_hero_walk_left_2, decoration, False) and dialoge_check == 0 and dialoge_bambaleyla == False:
                                                    dialoge_bambaleyla = True
                                                    can_moving = False
                                        if dialoge_bambaleyla == True:
                                            sc.blit(text_frame.image, text_frame.rect)
                                            sc.blit(bambaleyla_frame.image, bambaleyla_frame.rect)
                                            sc.blit(text, place)
                                            dialoge_check+=1
                                            if dialoge_check == 700:
                                                text = font.render("Давненько ко мне не заходили люди", True, (text_color))
                                            elif dialoge_check == 700 *2:
                                                text = font.render("Ты не обращай внимания на грязь...", True, (text_color))
                                            elif dialoge_check == 700 *3:
                                                text = font.render("Я не ждал гостей", True, (text_color))
                                            elif dialoge_check == 700 *4:
                                                text = font.render("Не хочешь закурить?", True, (text_color))
                                            elif dialoge_check == 700 *5:
                                                text = font.render("В жестяной банке есть бесконечная сигарета", True, (text_color))
                                            elif dialoge_check == 700 *6:
                                                text = font.render("Если хочешь расслабиться - возьми её", True, (text_color))
                                            elif dialoge_check == 700 *7:
                                                text = font.render("*отрыжка*", True, (text_color))
                                                fart_bambaleyla.play()
                                            elif dialoge_check == 700 *8:
                                                dialoge_bambaleyla = False
                                                text = font.render("*Нажмите Е, чтобы взять сигарету*", True, (text_color))
                                                can_moving = True
                                            elif dialoge_check == 700 *9:
                                                dialoge_bambaleyla = False
                                                can_moving = True
                                        if dialoge_check == 700 * 8:
                                            if pygame.sprite.spritecollide(sprite_hero_walk_left_2, trigers, False):
                                                sc.blit(bambaleyla_frame2.image, bambaleyla_frame2.rect)
                                                sc.blit(text, place2)
                                                if keys[pygame.K_e]:#Артефакт бамбалейлы
                                                    #save
                                                    Oleg_sigara = True#Арт бамбы
                                                    if self.choosencharacter==1:
                                                        self.conn = sqlite3.connect('gameinfo.db')
                                                        self.cur =self.conn.cursor()
                                                        self.cur.execute("UPDATE Saves SET Bambaleyla=? WHERE ID = 1", ((1,)))
                                                        self.conn.commit()
                                                        self.cur.close()
                                                        if self.developer == True:    
                                                            print("save 1: Bambaleyla's artifact was collected")
                                                    elif self.choosencharacter==2:
                                                        self.conn = sqlite3.connect('gameinfo.db')
                                                        self.cur =self.conn.cursor()
                                                        self.cur.execute("UPDATE Saves SET Bambaleyla=? WHERE ID = 2", ((1,)))
                                                        self.conn.commit()
                                                        self.cur.close()
                                                        if self.developer == True:    
                                                            print("save 2: Bambaleyla's artifact was collected")
                                                    elif self.choosencharacter==3:
                                                        self.conn = sqlite3.connect('gameinfo.db')
                                                        self.cur =self.conn.cursor()
                                                        self.cur.execute("UPDATE Saves SET Bambaleyla=? WHERE ID = 3", ((1,)))
                                                        self.conn.commit()
                                                        self.cur.close()
                                                        if self.developer == True:    
                                                            print("save 3: Bambaleyla's artifact was collected")
                                                    else:
                                                        if self.developer == True:    
                                                            print("\n")
                                                    dialoge_bambaleyla = True
                                                    can_moving = False
                                                    text =font.render("Ты встала на кривую дорожку... как и я в твоём возрасте", True, (text_color))
                                                    bunch_bambaleyla.play()
                                                    ashtray.kill()
                                                    ashtray = Hero_sprite(850, 515, 'Data/images/decorations/ashtray_2.png')
                                                    na_rasstrel.append(ashtray)
                                                    trigers.add(ashtray)





                                    else:
                                        if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False):
                                                    for ii in na_rasstrel:
                                                        ii.kill()
                                                    progruzka_levela = 1
                                                    die_sound.play()
                                        try:
                                            if no_two_bambaleyla == False:
                                                if pygame.sprite.spritecollide(crush_wall, attack_hero, False):
                                                            crush_wall.kill()
                                                            crush_wall_bambaleyla.play()
                                                            crush_wall_on = True
                                        except:
                                            pass
                                            
                                        if progruzka_levela ==1 and secret_bambaleyla == False:# and Oleg_sigara == False:#4-5
                                            self.conn = sqlite3.connect('gameinfo.db')
                                            self.cur = self.conn.cursor()
                                            if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                            elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                            else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                            self.conn.commit()
                                            self.cur.close()
                                            try:
                                                crush_wall.kill()
                                            except:
                                                pass
                                            
                                            progruzka_levela = 0
                                            perehod_x = 1250
                                            level_number = 28
                                            skeleton_alive = True
                                            polozhenie_personazha(160, 460)
                                            crush_wall = Hero_sprite(1275,175, 'Data/images/walls/crushed_wall.png')
                                            na_rasstrel.append(crush_wall)
                                            walle.add(crush_wall)    
                                            wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_4.png')
                                            wall2 =   Hero_sprite(1275,375, 'Data/images/walls/wall_loca_4_pre_exit_mini.png')    
                                            wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_4.png')    
                                            walle.add(wall)
                                            walle.add(wall2)
                                            walle.add(wall3)
                                            na_rasstrel.append(wall)
                                            na_rasstrel.append(wall2)  
                                            na_rasstrel.append(wall3)
                                            wall2 =   Hero_sprite(705,440, 'Data/images/walls/wall_loca_4_pre_exit.png')   
                                            walle.add(wall2)
                                            na_rasstrel.append(wall2) 
                                            wall2 =   Hero_sprite(705,580, 'Data/images/walls/wall_loca_4_pre_exit.png')   
                                            walle.add(wall2)
                                            na_rasstrel.append(wall2) 
                                            wall2 =   Hero_sprite(495,480, 'Data/images/walls/wall_loca_4_pre_exit.png')   
                                            walle.add(wall2)
                                            na_rasstrel.append(wall2) 
                                            platform =  Hero_sprite(130,640, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(300,500, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(600,670, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(130,300, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(440,280, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(810,340, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(1170,440, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(1000,520, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(810,700, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(970,700, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(1030,700, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(1190,700, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            platform =  Hero_sprite(1350,700, 'Data/images/walls/platform_loca_4.png') 
                                            walle.add(platform)
                                            na_rasstrel.append(platform)
                                            spike = Hero_sprite(350, 486, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(150, 286, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(430, 266, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(673, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(660, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(647, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(634, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(621, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(608, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(595, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(582, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(569, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(556, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(543, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(530, 656, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(880, 326, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(1180, 426, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(1000, 506, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                            spike = Hero_sprite(1180, 686, 'Data/images/spikes/mini_sprite_spike_1.png')
                                            evil.add(spike)
                                            na_rasstrel.append(spike)
                                 if location == 28:

                                    try:
                                        if skeleton_alive == True:
                                            if skelet_x == start_skelet_x:
                                                    move_skelet = 'right'
                                            if skelet_x == end_skeleton_x:
                                                    move_skelet = 'left'
                                            if move_skelet == 'right':
                                                skeleton.kill()
                                                skelet_x +=1
                                                if move_skelet_anim_check <= move_skelet_anim // 4 * 1:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_1.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 2:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_2.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 3:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_3.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 4:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_4.png')

                                                if skelet_x == end_skeleton_x:
                                                    move_skelet = 'left'
                                                move_skelet_anim_check+=1
                                                if move_skelet_anim_check == move_skelet_anim:
                                                    move_skelet_anim_check = 0

                                            elif move_skelet == 'left':
                                                skeleton.kill()
                                                skelet_x -=1
                                                if move_skelet_anim_check <= move_skelet_anim // 4 * 1:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_1.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 2:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_2.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 3:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_3.png')
                                                elif move_skelet_anim_check <= move_skelet_anim // 4 * 4:
                                                    skeleton = Hero_sprite(skelet_x,skelet_y, 'Data/images/enemies/skeleton/walk_left/walk_4.png')
                                                if skelet_x == start_skelet_x:
                                                    move_skelet = 'right'
                                                move_skelet_anim_check+=1
                                                if move_skelet_anim_check == move_skelet_anim:
                                                    move_skelet_anim_check = 0
                                             
                                            else:
                                                move_skelet = 'right'

                                            evil.add(skeleton)
                                            na_rasstrel.append(skeleton)
                                            
                                            if pygame.sprite.spritecollide(skeleton, attack_hero, False):
                                                skeleton_alive = False
                                                die_skeleton.play()
                                                skeleton.kill()
                                    except UnboundLocalError:
                                        print('fuck')
                                        start_skelet_x = 570#начальная точка х
                                        start_skelet_y = 155#начальная точка у
                                        end_skeleton_x = 1025#при каком х поворачивать влево
                                        skelet_x = start_skelet_x#это для проверки на х
                                        skelet_y = start_skelet_y
                                        move_skelet = 'right'
                                        move_skelet_anim = 100
                                        move_skelet_anim_check = 0
                                        skeleton = Hero_sprite(start_skelet_x,start_skelet_y, 'Data/images/enemies/skeleton/walk_right/walk_1.png')
                                    try:
                                        if pygame.sprite.spritecollide(red_button, attack_hero, False):
                                                red_button.kill()
                                                red_button_click = Hero_sprite(1245,140, 'Data/images/walls/clicked_trigger_red_button_vertical_left_1.png')
                                                decoration.add(red_button_click)
                                                na_rasstrel.append(red_button_click)
                                               
                                               
                                                red_wall.kill()
                                    except:
                                        pass
                                    
                                    try:
                                        if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False):
                                                for ii in na_rasstrel:
                                                    ii.kill()
                                                progruzka_levela = 1
                                                die_sound.play()
                                        
                                    except:
                                        pass
                                    if pygame.sprite.spritecollide(sprite_hero_walk_left_2, evil, False):
                                                for ii in na_rasstrel:
                                                    ii.kill()
                                                progruzka_levela = 1
                                                die_sound.play()
                                    if progruzka_levela ==1 :#4-6
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        start_skelet_x = 570#начальная точка х
                                        start_skelet_y = 155#начальная точка у
                                        end_skeleton_x = 1025#при каком х поворачивать влево
                                        skelet_x = start_skelet_x#это для проверки на х
                                        skelet_y = start_skelet_y
                                        move_skelet = 'right'
                                        move_skelet_anim = 100
                                        move_skelet_anim_check = 0
                                        red_wall =  Hero_sprite(1275,550, 'Data/images/walls/trigger_red_wall_vertical_1.png')
                                        walle.add(red_wall)
                                        na_rasstrel.append(red_wall)
                                        wall2 =   Hero_sprite(750,450, 'Data/images/walls/wall_loca_4_pre_exit.png') 
                                        walle.add(wall2)
                                        na_rasstrel.append(wall2)
                                        floor_loca_1 = Hero_sprite(650,675, 'Data/images/backgrounds/floor_loca_4.png')
                                        na_rasstrel.append(floor_loca_1)
                                        walle.add(floor_loca_1)
                                        progruzka_levela = 0
                                        level_number = 29
                                        skeleton_alive = True
                                        polozhenie_personazha(160, 460)
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_4.png')
                                        wall2 =   Hero_sprite(1275,220, 'Data/images/walls/wall_loca_4_pre_exit.png')    
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_4.png')    
                                        walle.add(wall)
                                        walle.add(wall2)
                                        walle.add(wall3)
                                        na_rasstrel.append(wall)
                                        na_rasstrel.append(wall2)  
                                        na_rasstrel.append(wall3)
                                        platform =  Hero_sprite(130,400, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(290,400, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(645,490, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(645,240, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(805,240, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(965,240, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        red_button = Hero_sprite(1240,140, 'Data/images/walls/trigger_red_button_vertical_left_1.png')
                                        na_rasstrel.append(red_button)
                                        decoration.add(red_button)
                                        platform =  Hero_sprite(1170,410, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        platform =  Hero_sprite(980,490, 'Data/images/walls/platform_loca_4.png') 
                                        walle.add(platform)
                                        na_rasstrel.append(platform)
                                        spike = Hero_sprite(210, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)    
                                        spike = Hero_sprite(197, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(184, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(171, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(158, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(145, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(132, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)    
                                        spike = Hero_sprite(119, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(106, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike) 
                                        spike = Hero_sprite(93, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(80, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(67, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(54, 386, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)      
                                        spike = Hero_sprite(680, 476, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)   
                                        spike = Hero_sprite(693, 476, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)
                                        spike = Hero_sprite(706, 476, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)   
                                        spike = Hero_sprite(719, 476, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)       
                                        spike = Hero_sprite(1244, 396, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike)  
                                        spike = Hero_sprite(1231, 396, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike) 
                                        spike = Hero_sprite(1218, 396, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike) 
                                        spike = Hero_sprite(783, 642, 'Data/images/spikes/mini_sprite_spike_1.png')
                                        evil.add(spike)
                                        na_rasstrel.append(spike) 
                                 if location == 29:
                                    #Для начала диалога
                                    try:
                                      if sprite_hero_walk_left_2.rect.x > 600 and can_talk_to_grisha == True:
                                          can_moving = False
                                          dialoge_grisha = True
                                    except:
                                      pass
                                    #===============


                                    #Диалог только с гришей
                                    try:
                                      if dialoge_grisha == True:
                                          dialoge_check +=1
                                          sc.blit(Grisha_frame.image, Grisha_frame.rect)
                                          sc.blit(text_frame_grisha.image, text_frame_grisha.rect)
                                          sc.blit(text, place)
                                          if dialoge_check == 750:
                                            text = font.render("Почему я не чувствую, что ты убила Крабоида?", True, (text_color_grisha))
                                            can_talk_to_grisha = False
                                          elif dialoge_check == 1500:
                                            dialoge_grisha = False
                                    #============


                                    #Появление портала
                                      if dialoge_check == 1500:
                                        if speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 1:
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_0%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 2:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_10%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 3:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_20%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 4:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_30%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 5:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_40%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 6:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_50%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 7:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_60%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 8:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_70%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 9:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_80%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 10:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_90%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 11:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_100%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                          dialoge_check = 1501
                                          crab = Hero_sprite(evil_x,evil_y, 'Data/images/second_boss/krab.png')
                                          decoration.add(crab)
                                          na_rasstrel.append(crab)
                                          moving_crab = True
                                          text = font.render("Но... Почему ты его не убилa?", True, (text_color_grisha))
                                          speed_anim_spawn_portal_check = 0
                                        speed_anim_spawn_portal_check +=1
                                        

                                    except:
                                      pass
                                    #============


                                    #ходьба краба и небольшие баги текстур для портала
                                    try:
                                      if evil_x > 900 and moving_crab == True and catscene_anim_check <1:
                                        evil_x -=1
                                        crab.rect.x = evil_x
                                        speed_anim_spawn_portal_check += 1
                                        if speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 1:
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_100%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 2:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_90%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 3:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_80%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 4:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_70%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 5:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_60%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 6:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_50%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 7:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_40%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 8:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_30%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 9:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_20%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 10:
                                          portal.kill()
                                          portal = Hero_sprite(1250,550, 'Data/images/decorations/portal/crab_portal_10%.png')
                                          decoration.add(portal)
                                          na_rasstrel.append(portal)
                                        elif speed_anim_spawn_portal_check == speed_anim_spawn_portal // 10 * 11:
                                          portal.kill()
                                        if evil_x <= 900:
                                          moving_crab = False
                                          dialoge_crab = True
                                    except:
                                      pass 
                                    #==========

                                    #диалог с крабом и Гришей
                                    try:
                                      if dialoge_crab == True:                      
                                        dialoge_check +=1
                                        if dialoge_check <= 2250:
                                          sc.blit(Grisha_frame.image, Grisha_frame.rect)
                                          sc.blit(text_frame_grisha.image, text_frame_grisha.rect)
                                          sc.blit(text, place)
                                        if dialoge_check == 2251:
                                          text = font.render("Она практически одолела меня, но я притворился, что погиб", True, (text_color_crab))
                                        elif dialoge_check == 3000:
                                          text = font.render("Олег, разве ты не видишь? Он же просто манипулирует тобой!", True, (text_color_crab))
                                        elif dialoge_check == 3750:
                                          text = font.render("Он хочет уничтожить мир, и готов ради этого поработить любого!", True, (text_color_crab))
                                        elif dialoge_check == 4500:
                                          text = font.render("Он твоими руками возвращает себе его великую потерянную силу.", True, (text_color_crab))
                                        elif dialoge_check == 5250:
                                          text = font.render("Вспомни же его безумства, очнись ото сна!!", True, (text_color_crab))
                                        elif dialoge_check == 5250:
                                          text = font.render("Вспомни же его безумства, очнись ото сна!!", True, (text_color_crab))
                                        elif dialoge_check == 6000:
                                          text = font.render("Не верь ему! Он всё лжёт! УБЕЙ ЕГО, ОЛЕГ!", True, (text_color_grisha))
                                        elif dialoge_check == 7500:
                                          text = font.render("РААААААААААААААР", True, (text_color_grisha))
                                        elif dialoge_check == 8250:
                                          text = font.render("ОН ОБЕЗУМЕЛ! САДИСЬ НА МЕНЯ, ЖИВО!", True, (text_color_crab))
                                        elif dialoge_check == 9000:

                                          dialoge_crab = False
                                          catscene2 = True
                                          
                                        if dialoge_check > 2250 and dialoge_check < 6000:
                                          sc.blit(crab_frame.image, crab_frame.rect)
                                          sc.blit(text_frame_crab.image, text_frame_crab.rect)
                                          sc.blit(text, place)
                                        if dialoge_check >5999 and dialoge_check < 6750:
                                          sc.blit(Grisha_frame.image, Grisha_frame.rect)
                                          sc.blit(text_frame_grisha.image, text_frame_grisha.rect)
                                          sc.blit(text, place)
                                        if dialoge_check == 6750:
                                          catscene = True
                                          dialoge_crab = False
                                        if dialoge_check > 6750 and dialoge_check < 7500:
                                          sc.blit(oleg_frame.image, oleg_frame.rect)
                                          sc.blit(text_frame_oleg.image, text_frame_oleg.rect)
                                          sc.blit(text, place)
                                        if dialoge_check >7499 and dialoge_check < 8250:
                                          sc.blit(Grisha_frame.image, Grisha_frame.rect)
                                          sc.blit(text_frame_grisha.image, text_frame_grisha.rect)
                                          sc.blit(text, place)
                                        if dialoge_check >8249 and dialoge_check < 9000:
                                          sc.blit(crab_frame.image, crab_frame.rect)
                                          sc.blit(text_frame_crab.image, text_frame_crab.rect)
                                          sc.blit(text, place)
                                          

                                    except:
                                      pass
                                    #===========



                                    #катсцены
                                    try:
                                      if catscene == True:
                                        catscene_anim_check += 1
                                        if catscene_anim_check == catscene_anim // 20 * 1:
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_0%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 2:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_5%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 3:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_10%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 4:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_15%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 5:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_20%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 6:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_25%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 7:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_30png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 8:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_35%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 9:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_40%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 10:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_45%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 11:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_50%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 12:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_55%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 13:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_60%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 14:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_65%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 15:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_70%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 16:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_75%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 17:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_80%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 18:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_85%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 19:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_90%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 20:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_95%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 21:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_100%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 23:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/catscene_1.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 123:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/catscene_2.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 223:
                                          dark.kill()
                                          catscene = False
                                          dialoge_check == 6751
                                          dialoge_crab = True  
                                          catscene_anim_check = 0
                                          text = font.render("Я вспомнил... Злодейства Гриши, Крабоида...", True, (text_color_oleg))  
                                      elif catscene2 == True:
                                        catscene_anim_check += 1
                                        if catscene_anim_check == catscene_anim // 20 * 1:
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_0%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 2:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_5%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 3:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_10%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 4:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_15%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 5:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_20%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 6:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_25%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 7:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_30png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 8:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_35%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 9:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_40%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 10:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_45%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 11:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_50%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 12:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_55%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 13:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_60%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 14:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_65%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 15:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_70%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 16:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_75%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 17:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_80%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 18:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_85%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 19:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_90%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif catscene_anim_check == catscene_anim // 20 * 20:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_95%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        if self.developer == True:    
                                            print('aaa')
                                        elif catscene_anim_check == catscene_anim // 20 * 21:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/win_catscene_100%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                          for ii in na_rasstrel:
                                            ii.kill()
                                          perehod_x = 1


                                    except:
                                      pass

                                    #===========
                                    

                                    if progruzka_levela == 1:#4-7
                                        self.conn = sqlite3.connect('gameinfo.db')
                                        self.cur = self.conn.cursor()
                                        if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                        elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                        else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                        self.conn.commit()
                                        self.cur.close()
                                        speed_anim_spawn_portal = 200
                                        jump_oleg = False

                                        evil_x = 1300
                                        evil_y = 550
                                        speed_anim_spawn_portal_check = 0
                                        can_talk_to_grisha = True
                                        catscene = False
                                        catscene2 = False
                                        catscene_anim = 200
                                        catscene_anim_check = 0
                                        moving_crab = False
                                        dialoge_crab = False
                                        progruzka_levela = 0
                                        can_moving = True
                                        dialoge_grisha = False
                                        polozhenie_personazha(200, 500)
                                        dialoge_check = 0
                                        floor_loca_1 = Hero_sprite(x,y+325, 'Data/images/backgrounds/floor_loca_4.png')
                                        na_rasstrel.append(floor_loca_1)
                                        walle.add(floor_loca_1)
                                        wall = Hero_sprite(25, 350, 'Data/images/walls/wall_loca_4.png')
                                        wall2 =   Hero_sprite(1275,350, 'Data/images/walls/wall_loca_4.png')    
                                        wall3 =   Hero_sprite(650, 25, 'Data/images/walls/ceiling_loca_4.png')   
                                        walle.add(wall)
                                        walle.add(wall2)
                                        walle.add(wall3)
                                        na_rasstrel.append(wall)
                                        na_rasstrel.append(wall2)  
                                        na_rasstrel.append(wall3)
                                        level_number = 30
                                        Grisha = Hero_sprite(700,575, 'Data/images/characters/Grisha_1.png')
                                        na_rasstrel.append(Grisha)
                                        decoration.add(Grisha) 
                                        text_frame_grisha = Hero_sprite(700, 200, 'Data/images/walls/frame_loca_2.png')
                                        Grisha_frame = Hero_sprite(250, 200, 'Data/images/characters/Grisha_frame.png')
                                        na_rasstrel.append(text_frame_grisha)
                                        na_rasstrel.append(Grisha_frame)
                                        text_frame_crab =Hero_sprite(700, 200, 'Data/images/walls/crab_Frame_for_text3.png')
                                        na_rasstrel.append(text_frame_crab)
                                        crab_frame = Hero_sprite(250, 200, 'Data/images/characters/crab_Frame.png')
                                        na_rasstrel.append(crab_frame)

                                        text_color_oleg = ((0,0,0))
                                        text_frame_oleg =Hero_sprite(700, 200, 'Data/images/walls/frame_loca_2.png')
                                        na_rasstrel.append(text_frame_oleg)
                                        oleg_frame = Hero_sprite(250, 200, 'Data/images/characters/Oleg_frame.png')
                                        na_rasstrel.append(oleg_frame)

                                        text_color_grisha = ((153, 146, 113))
                                        text = font.render("Что ты тут делаешь? Как ты сюда попала?", True, (text_color_grisha))
                                        text_color_crab = ((57, 77, 96))
                                        place = text.get_rect(center=(620, 200))
                                 if location == 30:
                                    
                                    if Grisha_alive == True:
                                      #Движение Олега и анимация (ну, недоанимация)    
                                      for_anim = None
                                      try:
                                        if keys[pygame.K_d]:
                                            if x_oleg  +1 < 1240:
                                                x_oleg +=1
                                                Oleg.rect.x = x_oleg
                                                Oleg_right.rect.x = x_oleg  
                                                Oleg_left.rect.x = x_oleg  
                                                for_anim = 'right'
                                        elif keys[pygame.K_a] or ispravlenye_x == True:
                                            ispravlenye_x = False
                                            if x_oleg  -1 > 0:
                                                x_oleg -=1
                                                Oleg.rect.x = x_oleg
                                                Oleg_right.rect.x = x_oleg  
                                                Oleg_left.rect.x = x_oleg  
                                                for_anim = 'left'  
                                        if keys[pygame.K_w] or ispravlenye_y == True:
                                            ispravlenye_y = False
                                            if y_oleg  -1 > 0:
                                                y_oleg -=1
                                                Oleg.rect.y = y_oleg  
                                                Oleg_right.rect.y = y_oleg  
                                                Oleg_left.rect.y = y_oleg  
                                        elif keys[pygame.K_s]:
                                            if y_oleg  +1 < 650:
                                                y_oleg +=1
                                                Oleg.rect.y = y_oleg  
                                                Oleg_right.rect.y = y_oleg  
                                                Oleg_left.rect.y = y_oleg  
                                      except:
                                        pass
                                      try:
                                        claw_left.rect.x = x_oleg - 10
                                        claw_left.rect.y = y_oleg - 20

                                        claw_right.rect.x = x_oleg + 55
                                        claw_right.rect.y = y_oleg - 20
                                      except:
                                        pass
                                      try:
                                        if for_anim == 'right':
                                          sc.blit(Oleg_right.image, Oleg_right.rect)
                                        elif for_anim == 'left':
                                          sc.blit(Oleg_left.image, Oleg_left.rect)
                                        elif for_anim == None:
                                          sc.blit(Oleg.image, Oleg.rect)
                                        sc.blit(claw_right.image, claw_right.rect)
                                        sc.blit(claw_left.image, claw_left.rect)
                                      except:
                                        pass
                                      #===================================

                                      #atk Oleg
                                      try:
                                        decoration_attack.draw(sc)
                                        if pressed[0]:
                                          if anim_claw_left_check == 0 and claw_left_check == True:
                                            claw_left_check = False
                                            if hp_gregory != -1:
                                              lazer_sound_2.play()
                                              laser = Hero_sprite(x_oleg, y_oleg  , 'Data/images/second_boss/laser_mini.png')
                                              decoration_attack.add(laser)
                                              
                                              attack_hero.add(laser)
                                              na_rasstrel.append(laser)
                                            anim_claw_left_check+=1
                                          claw_left_check = False
                                        else:
                                          claw_left_check = True

                                        if anim_claw_left_check >0:
                                          laser.rect.x = x_oleg-5
                                          laser.rect.y = y_oleg - 155
                                          anim_claw_left_check+=1
                                          if anim_claw_left_check == 50:
                                            anim_claw_left_check = 0
                                            laser.kill()

                                        if pressed[2]:
                                          if anim_claw_right_check == 0 and claw_right_check == True:
                                            if hp_gregory != -1:
                                              lazer_sound_2.play()
                                              laser1 = Hero_sprite(x_oleg, y_oleg  , 'Data/images/second_boss/laser_mini.png')
                                              decoration_attack.add(laser1)
                                              
                                              attack_hero.add(laser1)
                                              na_rasstrel.append(laser1)
                                            anim_claw_right_check+=1
                                          claw_right_check = False
                                        else:
                                          claw_right_check = True
                                        if anim_claw_right_check >0:
                                          laser1.rect.x = x_oleg+60
                                          laser1.rect.y = y_oleg - 155
                                          anim_claw_right_check+=1
                                          if anim_claw_right_check == 50:
                                            anim_claw_right_check = 0
                                            laser1.kill()
                                      except:
                                        pass
     #================================#======================================================================================================================================================================================================
                                      #atk Grisha Lasers(atk_Grisha == 0)
                                      try:
                                        if atk_Grisha == 0:
                                        
                                          if Grisha.rect.y > 75:
                                            Grisha.rect.y -= 4
                                          else:
                                            speed_spawn_particle_atk_0_check +=1
                                            if speed_spawn_particle_atk_0_check == speed_spawn_particle_atk_0:
                                              speed_spawn_particle_atk_0_check= 0
                                              lazer_sound_4.play()
                                              particle_laser = Hero_sprite(Grisha.rect.x+28, Grisha.rect.y+35, 'Data/images/third_boss/laser atk/start_laser_1.png')
                                              perehod_from_atk_0 -= 1
                                              particle_laser.to_cord_x = (random.randint(0, 1300))
                                              na_rasstrel.append(particle_laser)
                                              decoration.add(particle_laser)
                                              parts_atk_0.append(particle_laser)
                                              if perehod_from_atk_0 == 0:
                                                perehod_from_atk_0 = 25
                                                list_atk_Grisha = [1,2,3]
                                                atk_Grisha = random.randint(list_atk_Grisha[0], list_atk_Grisha[-1])
                                        for i in parts_atk_0:
                                          #i.rect.y -=1
                                          if i.rect.x < i.to_cord_x:
                                            i.rect.x +=1
                                          elif i.rect.x > i.to_cord_x:
                                            i.rect.x -=1
                                          if i.rect.y == 25 or i.rect.x == i.to_cord_x:
                                            parts_atk_0.remove(i)
                                            parts_atk_0_in_laser.append(i)
                                            i.in_laser_speed_check = 0
                                        for i in parts_atk_0_in_laser:
                                          i.in_laser_speed_check +=1
                                          if i.in_laser_speed_check == 25:
                                            lazer = Hero_sprite(i.rect.x, i.rect.y, 'Data/images/third_boss/laser atk/laser_atk_1.png')
                                            lazer.anim = 0
                                            decoration.add(lazer)
                                            na_rasstrel.append(lazer)
                                            laser_atk_0_sprite_1.append(lazer)
                                            i.kill()
                                        for i in laser_atk_0_sprite_1: 
                                          i.anim +=1

                                          if i.anim == 30:
                                            lazer = Hero_sprite(i.rect.x, i.rect.y+1000, 'Data/images/third_boss/laser atk/laser_atk_2.png')
                                            lazer.anim = 30
                                            decoration.add(lazer)
                                            na_rasstrel.append(lazer)
                                            laser_atk_0_sprite_1.append(lazer)
                                            i.kill()
                                          elif i.anim == 60:
                                            lazer = Hero_sprite(i.rect.x, i.rect.y+1000, 'Data/images/third_boss/laser atk/laser_atk_3.png')
                                            lazer.anim = 60
                                            decoration.add(lazer)
                                            na_rasstrel.append(lazer)
                                            laser_atk_0_sprite_1.append(lazer)
                                            i.kill()
                                          elif i.anim == 90:
                                            i.kill()
                                            lazer_sound_2.play()


                                      except UnboundLocalError:
                                        pass
                                      #==============================

                                      #atk Grisha 1(выпад)
                                      try:
                                        if atk_Grisha == 1 and time_wait_for_jerk_check < time_wait_for_jerk and in_atk_1 == False:
                                          if Grisha.rect.y != Oleg.rect.y:
                                            if Grisha.rect.y > Oleg.rect.y:
                                              Grisha.rect.y -=1
                                            elif Grisha.rect.y < Oleg.rect.y:
                                              Grisha.rect.y +=1
                                          elif Grisha.rect.y == Oleg.rect.y:
                                            time_wait_for_jerk_check +=1

                                        if time_wait_for_jerk_check > time_wait_for_jerk -1 and in_atk_1 == False:
                                            time_wait_for_jerk_check +=1
                                        if time_wait_for_jerk_check == time_wait_for_jerk + 100:
                                              x_grisha = Grisha.rect.x
                                              if Oleg.rect.x > Grisha.rect.x:
                                                atk_1_move = 'right'
                                              else:
                                                atk_1_move = 'left'
                                              lazer_sound_1.play()
                                              y_grisha = Grisha.rect.y
                                              hp = Grisha.hp
                                              invulnerability = Grisha.invulnerability
                                              Grisha.kill()
                                              Grisha = Hero_sprite(x_grisha, y_grisha, 'Data/images/third_boss/jerk atk/jerk_atk_1.png')
                                              na_rasstrel.append(Grisha)
                                              decoration.add(Grisha)
                                              Grisha.hp = hp
                                              Grisha.invulnerability = invulnerability
                                              in_atk_1 = True
                                              time_wait_for_jerk_check = 0
                                        if in_atk_1 == True and atk_1_move == 'right':
                                          x_grisha +=3
                                          if speed_anim_jerk_check <= speed_anim_jerk // 3 * 1:
                                            Grisha.kill()
                                            Grisha = Hero_sprite(x_grisha, y_grisha, 'Data/images/third_boss/jerk atk/jerk_atk_1.png')
                                            na_rasstrel.append(Grisha)
                                            decoration.add(Grisha)
                                          elif speed_anim_jerk_check <= speed_anim_jerk // 3 * 2:
                                            Grisha.kill()
                                            Grisha = Hero_sprite(x_grisha, y_grisha, 'Data/images/third_boss/jerk atk/jerk_atk_2.png')
                                            na_rasstrel.append(Grisha)
                                            decoration.add(Grisha)
                                          elif speed_anim_jerk_check <= speed_anim_jerk // 3 * 3:
                                            Grisha.kill()
                                            Grisha = Hero_sprite(x_grisha, y_grisha, 'Data/images/third_boss/jerk atk/jerk_atk_3.png')
                                            na_rasstrel.append(Grisha)
                                            decoration.add(Grisha)
                                          speed_anim_jerk_check +=1
                                          if speed_anim_jerk_check == speed_anim_jerk:
                                            speed_anim_jerk_check = 0
                                          if x_grisha > 1250:
                                            in_atk1 = False
                                            time_wait_for_jerk_check = 0
                                            atk_1_move = None
                                            in_atk_1 = False
                                            atk_1_move = 'none'
                                            speed_anim_jerk = 60
                                            speed_anim_jerk_check = 0

                                            time_wait_for_jerk = 150
                                            time_wait_for_jerk_check = 0
                                            atk_Grisha = list_atk_Grisha = [0,2,3]
                                            atk_Grisha = random.randint(list_atk_Grisha[0], list_atk_Grisha[-1])

                                            Grisha.kill()
                                            Grisha = Hero_sprite(x_grisha, y_grisha, 'Data/images/third_boss/fly/fly_1.png')
                                            Grisha.hp = hp
                                            Grisha.invulnerability = invulnerability
                                            decoration.add(Grisha)
                                            na_rasstrel.append(Grisha)  
                                        elif in_atk_1 == True and atk_1_move == 'left':
                                          x_grisha -=3
                                          if speed_anim_jerk_check <= speed_anim_jerk // 3 * 1:
                                            Grisha.kill()
                                            Grisha = Hero_sprite(x_grisha, y_grisha, 'Data/images/third_boss/jerk atk/jerk_atk_left_1.png')
                                            na_rasstrel.append(Grisha)
                                            decoration.add(Grisha)
                                          elif speed_anim_jerk_check <= speed_anim_jerk // 3 * 2:
                                            Grisha.kill()
                                            Grisha = Hero_sprite(x_grisha, y_grisha, 'Data/images/third_boss/jerk atk/jerk_atk_left_2.png')
                                            na_rasstrel.append(Grisha)
                                            decoration.add(Grisha)
                                          elif speed_anim_jerk_check <= speed_anim_jerk // 3 * 3:
                                            Grisha.kill()
                                            Grisha = Hero_sprite(x_grisha, y_grisha, 'Data/images/third_boss/jerk atk/jerk_atk_left_3.png')
                                            na_rasstrel.append(Grisha)
                                            decoration.add(Grisha)
                                          speed_anim_jerk_check +=1
                                          if speed_anim_jerk_check == speed_anim_jerk:
                                            speed_anim_jerk_check = 0
                                          if x_grisha < 50:
                                            in_atk1 = False
                                            time_wait_for_jerk_check = 0
                                            atk_1_move = None
                                            in_atk_1 = False
                                            atk_1_move = 'none'
                                            speed_anim_jerk = 60
                                            speed_anim_jerk_check = 0

                                            time_wait_for_jerk = 150
                                            time_wait_for_jerk_check = 0
                                            list_atk_Grisha = [0,2,3]

                                            atk_Grisha = random.randint(list_atk_Grisha[0], list_atk_Grisha[-1])
                                            Grisha.kill()
                                            Grisha = Hero_sprite(x_grisha, y_grisha, 'Data/images/third_boss/fly/fly_1.png')
                                            Grisha.hp = hp
                                            Grisha.invulnerability = invulnerability
                                            decoration.add(Grisha)
                                            na_rasstrel.append(Grisha)  

                                      except:
                                        pass
                                      #==
                                      #atk Grisha 2(spikes)
                                      #try:
                                      if atk_Grisha == 2:
                                          if start_atk_2 == False:
                                            if Grisha.rect.x > 1180:
                                              Grisha.rect.x -=1
                                            elif Grisha.rect.x < 120:
                                              Grisha.rect.x +=1
                                            if Grisha.rect.y > 580:
                                              Grisha.rect.y -=1
                                            elif Grisha.rect.y < 120:
                                              Grisha.rect.y +=1
                                            else:
                                              start_atk_2 = True
                                          else:

                                            speed_spawn_spikes_atk_2_check +=1
                                            if speed_spawn_spikes_atk_3 == speed_spawn_spikes_atk_2_check:
                                              speed_spawn_spikes_atk_2_check = 0
                                              if spikes_atk_2_check == 0: 
                                                lazer_sound_3.play()
                                                spike = Hero_sprite(Grisha.rect.x+ 27, Grisha.rect.y- 40, 'Data/images/third_boss/spike atk/spike_atk_1.png')
                                                decoration.add(spike)
                                                na_rasstrel.append(spike)
                                              elif spikes_atk_2_check == 1: 
                                                lazer_sound_3.play()
                                                spike2 = Hero_sprite(Grisha.rect.x+ 27, Grisha.rect.y+ 115, 'Data/images/third_boss/spike atk/spike_atk_1.png')
                                                decoration.add(spike2)
                                                na_rasstrel.append(spike2)
                                              elif spikes_atk_2_check == 2: 
                                                lazer_sound_3.play()
                                                spike3 = Hero_sprite(Grisha.rect.x+ 70, Grisha.rect.y+ 90, 'Data/images/third_boss/spike atk/spike_atk_1.png')
                                                decoration.add(spike3)
                                                na_rasstrel.append(spike3)
                                              elif spikes_atk_2_check == 3: 
                                                lazer_sound_3.play()
                                                spike4 = Hero_sprite(Grisha.rect.x- 20, Grisha.rect.y+ 90, 'Data/images/third_boss/spike atk/spike_atk_1.png')
                                                decoration.add(spike4)
                                                na_rasstrel.append(spike4)
                                              elif spikes_atk_2_check == 4:
                                                lazer_sound_3.play()
                                                spike5 = Hero_sprite(Grisha.rect.x+ 70, Grisha.rect.y- 20, 'Data/images/third_boss/spike atk/spike_atk_1.png')
                                                decoration.add(spike5)
                                                na_rasstrel.append(spike5)
                                              elif spikes_atk_2_check == 5:
                                                lazer_sound_3.play()
                                                spike6 = Hero_sprite(Grisha.rect.x- 20, Grisha.rect.y- 20, 'Data/images/third_boss/spike atk/spike_atk_1.png')
                                                decoration.add(spike6)
                                                na_rasstrel.append(spike6)
                                              elif spikes_atk_2_check == 6:
                                                lazer_sound_3.play()
                                                spike7 = Hero_sprite(Grisha.rect.x+ 90, Grisha.rect.y+ 35, 'Data/images/third_boss/spike atk/spike_atk_1.png')
                                                decoration.add(spike7)
                                                na_rasstrel.append(spike7)
                                              elif spikes_atk_2_check == 7:
                                                lazer_sound_3.play()
                                                spike8 = Hero_sprite(Grisha.rect.x- 40, Grisha.rect.y+ 35, 'Data/images/third_boss/spike atk/spike_atk_1.png')
                                                decoration.add(spike8)
                                                na_rasstrel.append(spike8)
                                              spikes_atk_2_check +=1
                                              if spikes_atk_2_check == 17:
                                                rect_x = spike.rect.x
                                                rect_y = spike.rect.y
                                                spike.move_x = Oleg.rect.x - rect_x
                                                spike.move_y = Oleg.rect.y - rect_y
                                                spike.move_x = spike.move_x // 7
                                                spike.move_y = spike.move_y // 7
                                                departure_sound.play()
                                                move_atk_2.append(spike)
                                              elif spikes_atk_2_check == 27:
                                                rect_x = spike2.rect.x
                                                rect_y = spike2.rect.y
                                                spike2.move_x = Oleg.rect.x - rect_x
                                                spike2.move_y = Oleg.rect.y - rect_y
                                                spike2.move_x = spike2.move_x // 7
                                                spike2.move_y = spike2.move_y // 7
                                                departure_sound.play()
                                                move_atk_2.append(spike2)
                                              elif spikes_atk_2_check == 37:
                                                rect_x = spike3.rect.x
                                                rect_y = spike3.rect.y
                                                spike3.move_x = Oleg.rect.x - rect_x
                                                spike3.move_y = Oleg.rect.y - rect_y
                                                spike3.move_x = spike3.move_x // 7
                                                spike3.move_y = spike3.move_y // 7
                                                departure_sound.play()
                                                move_atk_2.append(spike3)
                                              elif spikes_atk_2_check == 47:
                                                rect_x = spike4.rect.x
                                                rect_y = spike4.rect.y
                                                spike4.move_x = Oleg.rect.x - rect_x
                                                spike4.move_y = Oleg.rect.y - rect_y
                                                spike4.move_x = spike4.move_x // 7
                                                spike4.move_y = spike4.move_y // 7
                                                departure_sound.play()
                                                move_atk_2.append(spike4)
                                              elif spikes_atk_2_check == 57:
                                                rect_x = spike5.rect.x
                                                rect_y = spike5.rect.y
                                                spike5.move_x = Oleg.rect.x - rect_x
                                                spike5.move_y = Oleg.rect.y - rect_y
                                                spike5.move_x = spike5.move_x // 7
                                                spike5.move_y = spike5.move_y // 7
                                                departure_sound.play()
                                                move_atk_2.append(spike5)
                                              elif spikes_atk_2_check == 67:
                                                rect_x = spike6.rect.x
                                                rect_y = spike6.rect.y
                                                spike6.move_x = Oleg.rect.x - rect_x
                                                spike6.move_y = Oleg.rect.y - rect_y
                                                spike6.move_x = spike6.move_x // 7
                                                spike6.move_y = spike6.move_y // 7
                                                departure_sound.play()
                                                move_atk_2.append(spike6)
                                              elif spikes_atk_2_check == 77:
                                                rect_x = spike7.rect.x
                                                rect_y = spike7.rect.y
                                                spike7.move_x = Oleg.rect.x - rect_x
                                                spike7.move_y = Oleg.rect.y - rect_y
                                                spike7.move_x = spike7.move_x // 7
                                                spike7.move_y = spike7.move_y // 7
                                                departure_sound.play()
                                                move_atk_2.append(spike7)
                                              elif spikes_atk_2_check == 87:
                                                rect_x = spike8.rect.x
                                                rect_y = spike8.rect.y
                                                spike8.move_x = Oleg.rect.x - rect_x
                                                spike8.move_y = Oleg.rect.y - rect_y
                                                spike8.move_x = spike8.move_x // 7
                                                spike8.move_y = spike8.move_y // 7
                                                departure_sound.play()
                                                move_atk_2.append(spike8)

                                              for i in move_atk_2:

                                                rect_x = i.move_x
                                                rect_y = i.move_y
                                                i.rect.x += rect_x
                                                i.rect.y += rect_y
                                                if i.rect.x < -10 or i.rect.x > 1310 or i.rect.y > 710 or i.rect.y < -10:
                                                  i.kill()
                                              if spikes_atk_2_check == 110:
                                                if len(move_atk_2) > 0:
                                                  break_spikes.play()
                                                  for i in move_atk_2:
                                                    i.kill()
                                                move_atk_2 = []
                                                spikes_atk_2_check = 0
                                                list_atk_Grisha = [0,1,3]
                                                atk_Grisha = random.randint(list_atk_Grisha[0], list_atk_Grisha[-1])
                                                start_atk_2 = False
                                                #i.rect.y += i.move.y
                                      #========
                                      #Atk Grisha 3(ball lasers)
                                      if atk_Grisha == 3:
                                        if in_atk_3 == False:
                                          if Grisha.rect.x > 655:
                                            Grisha.rect.x -= 3
                                          elif Grisha.rect.x < 645:
                                            Grisha.rect.x += 3
                                          else:
                                            check_grisha_x = True
                                          if Grisha.rect.y > 335:
                                            Grisha.rect.y -= 3
                                          elif Grisha.rect.y < 325:
                                            Grisha.rect.y +=3
                                          else:
                                            check_grisha_y = True
                                            if check_grisha_y == True and check_grisha_x == True:
                                              in_atk_3 = True
                                        else:
                                          if check_lasers_atk_3 == 0:
                                            #ball_lazer = Hero_sprite(Grisha.rect.x+26, Grisha.rect.y, 'Data/images/third_boss/ball atk/laser_atk_1_vertical1.png')        
                                            ball_lazer = Hero_sprite(Grisha.rect.x+27, Grisha.rect.y+45, 'Data/images/third_boss/ball atk/start_lazer_1.png')
                                            lazer_sound_4.play()
                                            decoration.add(ball_lazer)
                                            na_rasstrel.append(ball_lazer)
                                            check_lasers_atk_3 += 1
                                            ball_lazer.speed_anim = 40
                                            ball_lazer.speed_anim_check = 0
                                            ball_lazer.cadr = 0
                                            anim_change_balls_atk_3.append(ball_lazer)
                                          for i in anim_change_balls_atk_3:
                                            i.speed_anim_check +=1
                                            if i.speed_anim_check == i.speed_anim:
                                              speed_anim = i.speed_anim
                                              rect_x = i.rect.x 
                                              rect_y = i.rect.y
                                              if i.cadr == 0:
                                                lazer_sound_4.play()
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_2.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 1
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 1:
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_3.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 2
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 2:
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_4.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 3
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 3:
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_5.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 4
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 4:
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_5.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 5
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 5:
                                                lazer_sound_2.play()
                                                lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/laser_atk_1_gorizontal1.png')
                                                lazer.speed_anim = 25
                                                lazer.speed_anim_check = 0
                                                lazer.cadr = 6
                                                lazer.gor = True
                                                anim_change_balls_atk_3.append(lazer)
                                                decoration.add(lazer)
                                                na_rasstrel.append(lazer)

                                                lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/laser_atk_1_vertical1.png')
                                                lazer.speed_anim = 25
                                                lazer.speed_anim_check = 0
                                                lazer.cadr = 6
                                                lazer.gor = False
                                                anim_change_balls_atk_3.append(lazer)
                                                decoration.add(lazer)
                                                na_rasstrel.append(lazer)
                                                if work_please == True:
                                                  lazer_sound_2.play()
                                                  work_please = False
                                                  ball_lazer = Hero_sprite(Grisha.rect.x+27, Grisha.rect.y+45, 'Data/images/third_boss/ball atk/start_lazer_1.png')
                                                  ball_lazer.first = 1
                                                  decoration.add(ball_lazer)
                                                  na_rasstrel.append(ball_lazer)
                                                  check_lasers_atk_3 += 1
                                                  ball_lazer.speed_anim = 40
                                                  ball_lazer.speed_anim_check = 0
                                                  ball_lazer.cadr = 0
                                                  ball_lazer.move_y = True
                                                  ball_lazer.move_up = True
                                                  move_atk_3_diagonal.append(ball_lazer)

                                                  ball_lazer = Hero_sprite(Grisha.rect.x+27, Grisha.rect.y+45, 'Data/images/third_boss/ball atk/start_lazer_1.png')
                                                  ball_lazer.first = 1
                                                  decoration.add(ball_lazer)
                                                  na_rasstrel.append(ball_lazer)
                                                  check_lasers_atk_3 += 1
                                                  ball_lazer.speed_anim = 40
                                                  ball_lazer.speed_anim_check = 0
                                                  ball_lazer.cadr = 0
                                                  ball_lazer.move_y = True
                                                  ball_lazer.move_up = False
                                                  move_atk_3_diagonal.append(ball_lazer)

                                                  ball_lazer = Hero_sprite(Grisha.rect.x+27, Grisha.rect.y+45, 'Data/images/third_boss/ball atk/start_lazer_1.png')
                                                  ball_lazer.first = 1
                                                  decoration.add(ball_lazer)
                                                  na_rasstrel.append(ball_lazer)
                                                  check_lasers_atk_3 += 1
                                                  ball_lazer.speed_anim = 40
                                                  ball_lazer.speed_anim_check = 0
                                                  ball_lazer.cadr = 0
                                                  ball_lazer.move_y = False
                                                  ball_lazer.move_left = True
                                                  move_atk_3_diagonal.append(ball_lazer)
                                                  lazers_atk_3.append(lazer)
                                                  ball_lazer = Hero_sprite(Grisha.rect.x+27, Grisha.rect.y+45, 'Data/images/third_boss/ball atk/start_lazer_1.png')
                                                  ball_lazer.first = 1
                                                  decoration.add(ball_lazer)
                                                  na_rasstrel.append(ball_lazer)
                                                  check_lasers_atk_3 += 1
                                                  ball_lazer.speed_anim = 40
                                                  ball_lazer.speed_anim_check = 0
                                                  ball_lazer.cadr = 0
                                                  ball_lazer.move_y = False
                                                  ball_lazer.move_left = False
                                                  move_atk_3_diagonal.append(ball_lazer)
                                                  lazers_atk_3.append(lazer)

                                                i.kill()
                                              elif i.cadr == 6:
                                                if i.gor == False:
                                                  lazer = Hero_sprite(rect_x+7, rect_y+1005, 'Data/images/third_boss/ball atk/laser_atk_1_vertical2.png')
                                                  lazer.gor = False
                                                else:
                                                  lazer = Hero_sprite(rect_x+1005, rect_y+7, 'Data/images/third_boss/ball atk/laser_atk_1_gorizontal2.png')
                                                  lazer.gor = True
                                                i.kill()
                                                lazers_atk_3.append(lazer)
                                                lazer.speed_anim = 25
                                                lazer.speed_anim_check = 0
                                                lazer.cadr = 7
                                                anim_change_balls_atk_3.append(lazer)
                                                decoration.add(lazer)
                                                na_rasstrel.append(lazer)
                                              elif i.cadr == 7:
                                                if i.gor == False:
                                                  lazer = Hero_sprite(rect_x+7, rect_y+1005, 'Data/images/third_boss/ball atk/laser_atk_1_vertical3.png')
                                                else:
                                                  lazer = Hero_sprite(rect_x+1005, rect_y+7, 'Data/images/third_boss/ball atk/laser_atk_1_gorizontal3.png')
                                                lazers_atk_3.append(lazer)
                                                lazer.speed_anim = 25
                                                i.kill()
                                                lazer.speed_anim_check = 0
                                                lazer.cadr = 8
                                                anim_change_balls_atk_3.append(lazer)
                                                decoration.add(lazer)
                                                na_rasstrel.append(lazer)
                                              elif i.cadr == 8:
                                                i.kill()
                                                check_final_lazer_atk_3+=1
                                                if check_final_lazer_atk_3 == 10:
                                                  list_atk_Grisha = [0,1,2]
                                                  atk_Grisha = random.randint(list_atk_Grisha[0], list_atk_Grisha[-1])
                                                  check_grisha_x = False
                                                  check_grisha_y = False
                                                  in_atk_3 = False
                                                  check_lasers_atk_3 = 0
                                                  anim_change_balls_atk_3 = []
                                                  anim_change_balls_atk_3_1 = []
                                                  move_atk_3_diagonal = []
                                                  work_please = True#its really work
                                                  check_final_lazer_atk_3 = 0
                                                  lazer_1_check = False
                                                  lazer_2_check = False
                                                  lazer_3_check = False
                                                  lazer_4_check = False
                                          for i in move_atk_3_diagonal:
                                                if i.move_y == True:
                                                  if i.move_up == True:
                                                    if i.rect.y < 606:
                                                      i.rect.y +=1
                                                    else:
                                                      if lazer_1_check == False:
                                                        anim_change_balls_atk_3_1.append(i)
                                                        lazer_1_check = True
                                                  elif i.move_up == False:
                                                    if i.rect.y > 50:
                                                      i.rect.y -=1
                                                    else:
                                                      if lazer_2_check == False:
                                                        anim_change_balls_atk_3_1.append(i)
                                                        lazer_2_check = True
                                                else:
                                                  if i.move_left == True:
                                                    if i.rect.x > 300:
                                                      i.rect.x -=1
                                                    else:
                                                      if lazer_3_check == False:
                                                        anim_change_balls_atk_3_1.append(i)
                                                        lazer_3_check = True
                                                  elif i.move_left == False:
                                                    if i.rect.x < 1000-28:
                                                      i.rect.x +=1
                                                    else:
                                                      if lazer_4_check == False:
                                                        anim_change_balls_atk_3_1.append(i)
                                                        lazer_4_check = True
                                          for i in anim_change_balls_atk_3_1:
                                            i.speed_anim_check +=1
                                            if i.speed_anim_check == i.speed_anim:
                                              speed_anim = i.speed_anim
                                              rect_x = i.rect.x 
                                              rect_y = i.rect.y
                                              if i.cadr == 0:
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_2.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 1
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 1:
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_3.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 2
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 2:
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_4.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 3
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 3:
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_5.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 4
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 4:
                                                i.kill()
                                                ball_lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/start_lazer_5.png')
                                                ball_lazer.speed_anim = 20
                                                ball_lazer.speed_anim_check = 0
                                                ball_lazer.cadr = 5
                                                anim_change_balls_atk_3.append(ball_lazer)
                                                decoration.add(ball_lazer)
                                                na_rasstrel.append(ball_lazer)
                                              elif i.cadr == 5:
                                                lazer_sound_2.play()
                                                lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/laser_atk_1_gorizontal1.png')
                                                lazer.speed_anim = 25
                                                lazer.speed_anim_check = 0
                                                lazer.cadr = 6
                                                lazer.gor = True
                                                anim_change_balls_atk_3.append(lazer)
                                                decoration.add(lazer)
                                                na_rasstrel.append(lazer)
                                                lazers_atk_3.append(lazer)
                                                lazer = Hero_sprite(rect_x+15, rect_y+15, 'Data/images/third_boss/ball atk/laser_atk_1_vertical1.png')
                                                lazer.speed_anim = 25
                                                lazer.speed_anim_check = 0
                                                lazer.cadr = 6
                                                lazer.gor = False
                                                anim_change_balls_atk_3.append(lazer)
                                                decoration.add(lazer)
                                                na_rasstrel.append(lazer)
                                                lazers_atk_3.append(lazer)
                                          
                                                i.kill()
                                              elif i.cadr == 6:
                                                if i.gor == False:
                                                  lazer = Hero_sprite(rect_x+7, rect_y+1005, 'Data/images/third_boss/ball atk/laser_atk_1_vertical2.png')
                                                  lazer.gor = False
                                                else:
                                                  lazer = Hero_sprite(rect_x+1005, rect_y+7, 'Data/images/third_boss/ball atk/laser_atk_1_gorizontal2.png')
                                                  lazer.gor = True
                                                i.kill()
                                                lazers_atk_3.append(lazer)
                                                lazer.speed_anim = 25
                                                lazer.speed_anim_check = 0
                                                lazer.cadr = 7
                                                anim_change_balls_atk_3.append(lazer)
                                                decoration.add(lazer)
                                                na_rasstrel.append(lazer)
                                              elif i.cadr == 7:
                                                if i.gor == False:
                                                  lazer = Hero_sprite(rect_x+7, rect_y+1005, 'Data/images/third_boss/ball atk/laser_atk_1_vertical3.png')
                                                else:
                                                  lazer = Hero_sprite(rect_x+1005, rect_y+7, 'Data/images/third_boss/ball atk/laser_atk_1_gorizontal3.png')
                                                lazer.speed_anim = 25
                                                i.kill()
                                                lazer.speed_anim_check = 0
                                                lazers_atk_3.append(lazer)
                                                lazer.cadr = 8
                                                anim_change_balls_atk_3.append(lazer)
                                                decoration.add(lazer)
                                                na_rasstrel.append(lazer)
                                              elif i.cadr == 8:
                                                i.kill()
                                                check_final_lazer_atk_3+=1



                                      #except:
                                      #  pass
                                      #=====

                                      #удар по Грише
                                      #ну типа да
                                    try:
                                      if pygame.sprite.spritecollide(Grisha, attack_hero, False) and Grisha.invulnerability == 0 and atk_Grisha != 1:
                                        hp_gregory -=1
                                        text = font.render('{}/30'.format(Grisha.hp + hp_gregory), True, (text_color))
                                        Grisha.invulnerability = 300
                                        if hp_gregory == -1:
                                          speed_spawn_particle_atk_0 = 150
                                          speed_spawn_particle_atk_0_check = 0
                                          parts_atk_0 = []
                                          parts_atk_0_in_laser = []
                                          Grisha_music.stop()
                                          laser_atk_0_sprite_1 = []
                                          atk_Grisha = 4
                                      if hp_gregory == -1:
                                          
                                          catscene_anim_check+=1
                                          if catscene_anim_check == catscene_anim // 20 * 1:
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_0%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 2:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_5%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 3:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_10%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 4:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_15%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 5:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_20%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 6:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_25%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 7:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_30png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 8:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_35%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 9:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_40%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 10:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_45%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 11:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_50%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 12:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_55%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 13:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_60%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 14:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_65%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 15:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_70%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 16:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_75%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 17:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_80%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 18:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_85%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 19:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_90%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 20:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_95%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 21:
                                            dark.kill()
                                            for i in na_rasstrel:
                                              i.kill()
                                            #location = 31
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_100%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)

                                          elif catscene_anim_check == catscene_anim // 20 * 80:
                                            dark.kill()
                                            dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/catscene_3.png')
                                            na_rasstrel.append(dark1)
                                            decoration.add(dark1)
                                          elif catscene_anim_check == catscene_anim // 20 * 160:
                                            titles_music.play()
                                            #dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_50%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 165:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_55%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 170:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_60%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 175:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_65%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 180:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_70%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 185:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_75%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 190:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_80%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 195:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_85%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 200:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_90%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 205:
                                            dark.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_95%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                          elif catscene_anim_check == catscene_anim // 20 * 210:
                                            dark.kill()
                                            dark1.kill()
                                            dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_100%.png')
                                            na_rasstrel.append(dark)
                                            decoration.add(dark)
                                            #if Oleg_amulet == True and Oleg_eye == True and Oleg_sigara == True:
                                            location = 31
                                            aivani_anim = 100
                                            ai_vani_anim_check = 0
                                            anim = 100
                                            ai_vani_drinking = 460
                                            ai_vani_drinking_check = 0
                                            time_pered_dialog = 500
                                            anim_check = 0
                                            for ii in na_rasstrel:
                                              ii.kill()
                                             




                                      if Grisha.invulnerability > 0:
                                        Grisha.invulnerability -=1


                                    except:
                                      pass

                                    #===========
                                    try:
                                        if Grisha.invulnerability == 0:
                                            sc.blit(hp_bar_1.image, hp_bar_1.rect)
                                            sc.blit(text, place)
                                        else:
                                            if Grisha.invulnerability > 265:
                                                sc.blit(hp_bar_2.image, hp_bar_2.rect)
                                            elif Grisha.invulnerability > 230:
                                                sc.blit(hp_bar_3.image, hp_bar_3.rect)
                                            elif Grisha.invulnerability > 195:
                                                sc.blit(hp_bar_4.image, hp_bar_4.rect)
                                            elif Grisha.invulnerability > 160:
                                                sc.blit(hp_bar_5.image, hp_bar_5.rect)
                                            else:
                                                sc.blit(hp_bar_1.image, hp_bar_1.rect)
                                                sc.blit(text, place)
                                                
                                    except:
                                        pass
                                    try:
                                      if pygame.sprite.spritecollide(Oleg, decoration, False) and hp_gregory != -1:
                                        die_sound.play()
                                       
##                                        for i in lazers_atk_3:
##                                          i.kill()
##                                        for i in parts_atk_0:
##                                          i.kill()
##                                        for i in parts_atk_0_in_laser:
##                                          i.kill()
##                                        for i in lazer_atk_0_sprite_1:
##                                          i.kill()
##                                        for i in move_atk_2:
##                                          i.kill()
##                                        for i in anim_change_balls_atk_3:
##                                          i.kill()
##                                        for i in anim_change_balls_atk_3_1:
##                                          i.kill()
##                                        for i in move_atk_3_diagonal:
##                                          i.kill()
                                        for ii in na_rasstrel:
                                          ii.kill()
                                          location = 30
                                          progruzka_levela = 1

                                    except:
                                      pass
                                    if progruzka_levela == 1:#4-8
                                      if play_music_grisha == False:
                                        music_loca_1[music_loca_1_check].stop()
                                        Grisha_music.play()

                                      play_music_grisha = True
                                      self.conn = sqlite3.connect('gameinfo.db')
                                      self.cur = self.conn.cursor()
                                      if self.choosencharacter==1:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 1", ((location,)))
                                                if self.developer == True:    
                                                    print("save 1 updated")
                                      elif self.choosencharacter==2:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 2", ((location,)))
                                                if self.developer == True:    
                                                    print("save 2 updated")
                                      else:
                                                self.cur.execute("UPDATE Saves SET last_loc=? WHERE ID = 3", ((location,)))
                                                if self.developer == True:    
                                                    print("save 3 updated")
                                      self.conn.commit()
                                      self.cur.close()
                                      try:
                                     
                                        sprite_hero_walk_left_1.kill()
                                        sprite_hero_walk_left_1_1.kill()
                                        sprite_hero_walk_left_1_2.kill()
                                        sprite_hero_walk_left_2.kill()

                                        sprite_hero_stand_1.kill()

                                        sprite_hero_walk_right_1.kill()
                                        sprite_hero_walk_right_1_1.kill()
                                        sprite_hero_walk_right_1_2.kill()
                                        perehod_x = 12000

                                        sprite_hero_falling_1.kill()
                                        Grisha.kill()
                                      except:
                                        pass
                                      try:
                                        laser1.kill()
                                        laser.kill()
                                        
                                      except:
                                        pass
                                      try:
                                        spike.kill()
                                        spike2.kill()
                                        spike3.kill()
                                        spike4.kill()
                                        spike5.kill()
                                        spike6.kill()
                                        spike7.kill()
                                        spike8.kill()
                                      except:
                                        pass
                                      try:
                                        ball_lazer.kill()
                                        
                                      except:
                                        pass
                                      try:
                                        lazer.kill()
                                      except:
                                        pass




                                      progruzka_levela = 0       
                                      x_oleg = 200
                                      y_oleg = 350
                                      perehod_from_atk_0 = 25
                                      Oleg = Hero_sprite(x_oleg, y_oleg  , 'Data/images/the main character/crab_with_Oleg.png')
                                      ispravlenye_x = True
                                      ispravlenye_y = True
                                      claw_left =  Hero_sprite(x_oleg - 10, y_oleg-20, 'Data/images/second_boss/left_claw_mini.png')
                                      claw_right =  Hero_sprite(x_oleg + 55, y_oleg-20, 'Data/images/second_boss/right_claw_mini.png')
                                      claw_left_check = True
                                      claw_right_check = True

                                      na_rasstrel.append(claw_right)
                                      na_rasstrel.append(claw_left)
                                      #decoration.add(claw_left)
                                      #decoration.add(claw_right)
                                      na_rasstrel.append(Oleg)

                                      Oleg_right = Hero_sprite(x_oleg, y_oleg  , 'Data/images/the main character/crab_with_Oleg_right.png')
                                      na_rasstrel.append(Oleg_right)
                                      Oleg_left = Hero_sprite(x_oleg, y_oleg  , 'Data/images/the main character/crab_with_Oleg_left.png')
                                      na_rasstrel.append(Oleg_left)
                                      
                                      list_atk_Grisha = [0,1,2,3]
                                      atk_Grisha = random.randint(list_atk_Grisha[0], list_atk_Grisha[-1])
                                      in_atk_1 = False
                                      atk_1_move = 'none'
                                      speed_anim_jerk = 60
                                      speed_anim_jerk_check = 0

                                      time_wait_for_jerk = 150
                                      time_wait_for_jerk_check = 0
                                      speed_spawn_particle_atk_0 = 150
                                      speed_spawn_particle_atk_0_check = 0

                                      parts_atk_0 = []
                                      parts_atk_0_in_laser = []
                                      laser_atk_0_sprite_1 = []


                                      speed_spawn_spikes_atk_3 = 12
                                      speed_spawn_spikes_atk_2_check = 0
                                      spikes_atk_2_check = 0
                                      start_atk_2 = False
                                      move_atk_2 = []

                                      check_grisha_x = False
                                      check_grisha_y = False
                                      in_atk_3 = False
                                      check_lasers_atk_3 = 0
                                      anim_change_balls_atk_3 = []
                                      anim_change_balls_atk_3_1 = []
                                      move_atk_3_diagonal = []
                                      lazers_atk_3 = []
                                      work_please = True#its really work
                                      check_final_lazer_atk_3 = 0
                                      lazer_1_check = False
                                      lazer_2_check = False
                                      lazer_3_check = False
                                      lazer_4_check = False
                                      Grisha = Hero_sprite(1100, 350, 'Data/images/third_boss/fly/fly_1.png')
                                      Grisha.hp = 1
                                      Grisha.invulnerability = 0
                                      Grisha_alive = True

                                      Grisha.anim = 40
                                      Grisha.anim_check = 0
                                      decoration.add(Grisha)
                                      na_rasstrel.append(Grisha)             

                                      anim_claw_left = 100
                                      anim_claw_left_check = 0   
                                      anim_claw_right_check = 0

                                      catscene_anim = 100
                                      catscene_anim_check = 0

                                      text_color = (0,0,0)
                                      hp_gregory = 29
                                      text = font.render('{}/30'.format(Grisha.hp + hp_gregory), True, (text_color))
                                      place = text.get_rect(center=(650, 625))
                                      hp_bar_1 = Hero_sprite(650, 625, 'Data/images/third_boss/hp bar/hp_bar_1.png')
                                      na_rasstrel.append(hp_bar_1)
                                      hp_bar_2 = Hero_sprite(650, 625, 'Data/images/third_boss/hp bar/hp_bar_2.png')
                                      na_rasstrel.append(hp_bar_2)
                                      hp_bar_3 = Hero_sprite(650, 625, 'Data/images/third_boss/hp bar/hp_bar_3.png')
                                      na_rasstrel.append(hp_bar_3)
                                      hp_bar_4 = Hero_sprite(650, 625, 'Data/images/third_boss/hp bar/hp_bar_4.png')
                                      na_rasstrel.append(hp_bar_4)
                                      hp_bar_5 = Hero_sprite(650, 625, 'Data/images/third_boss/hp bar/hp_bar_5.png')
                                      na_rasstrel.append(hp_bar_5)
                                 elif location == 31:
                                    #End №8
                                    if anim_check <=anim // 20 * 100:
                                      anim_check +=1
                                      if anim_check == anim // 20 * 5:
                                              dark.kill()
                                              if Oleg_amulet == True:
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              if Oleg_eye == True:
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)


                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_95%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                              if Oleg_amulet == True and Oleg_eye == True and Oleg_sigara== True:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end8.png')
                                              elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == True:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7.png')
                                              elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == True:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end6.png')
                                              elif Oleg_amulet == True and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end5.png')
                                              elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == True:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end4.png')
                                              elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end3.png')
                                              elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end2.png')
                                              elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end1.png')
                                          
                                              else:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7.png')
                                              na_rasstrel.append(dark1)
                                              decoration.add(dark1)
                                      elif anim_check == anim // 20 * 10:
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark.kill()
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_90%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 15:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_85%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                              f2 = open('Extra.txt')
                                              list = ''
                                              for i in f2:
                                                 list += i
                                              f2.close()
                                              f2 = open('Extra.txt', 'w')
                                              list = list.replace('Grisha = False', 'Grisha = True')
                                              list = list.replace('Aricius = False', 'Aricius = True')
                                              list = list.replace('Kraboid = False', 'Kraboid = True')
                                              list = list.replace('Oleg = False', 'Oleg = True')
                                              if Oleg_amulet == True:
                                                list = list.replace('Ai_vani = False', 'Ai_vani = True')
                                              if Oleg_eye == True:
                                                list = list.replace('Gfh = False', 'Gfh = True')
                                                list = list.replace('Guardian = False', 'Guardian = True')
                                              if Oleg_sigara == True:
                                                list = list.replace('Bambaleyla = False', 'Bambaleyla = True')
                                              f2.write(list)
                                              f2.close()
                                      elif anim_check == anim // 20 * 20:
                                              dark.kill()
                                              if Oleg_amulet == True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                                decoration.add(Ai_vani)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_80%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 25:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_75%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 30:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_70%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 35:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_65%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 40:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_60%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 45:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_55%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 50:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_50%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 55:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_45%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 60:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_40%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 65:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_35%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 70:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_30%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 75:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_25%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 80:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_20%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 85:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_15%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 90:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_10%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 95:
                                              dark.kill()
                                              if Oleg_amulet== True:
                                                Ai_vani.kill()
                                                Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                                decoration.add(Ai_vani)
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                na_rasstrel.append(bambaleyla)
                                                decoration.add(bambaleyla)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              na_rasstrel.append(Grisha)
                                              dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_5%.png')
                                              na_rasstrel.append(dark)
                                              decoration.add(dark)
                                      elif anim_check == anim // 20 * 100:
                                              dark.kill()
                                              Grisha.kill()
                                              if Oleg_eye == True:
                                                gfh.kill()
                                                gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                                decoration.add(gfh)
                                                na_rasstrel.append(gfh)
                                              Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                              decoration.add(Grisha)
                                              if Oleg_sigara == True:
                                                bambaleyla.kill()
                                                bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                                decoration.add(bambaleyla)
                                                na_rasstrel.append(bambaleyla)
                                    else:
                                      time_pered_dialog -=1
                                      if self.developer == True:    
                                        print(time_pered_dialog)

                                      if time_pered_dialog == 0:
                                        dark1.kill()
                                        if Oleg_amulet == True and Oleg_eye == True and Oleg_sigara== True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end8_text_20%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7_text_20%.png')
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end6_text_20%.png')
                                        elif Oleg_amulet == True and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end5_text_20%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == True:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end4_text_20%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end3_text_20%.png')
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end2_text_20%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end1_text_20%.png')
                                        else:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7.png')
                                        na_rasstrel.append(dark1)
                                        decoration.add(dark1)
                                        if Oleg_amulet == True:
                                          Ai_vani.kill()
                                          if ai_vani_anim_check < aivani_anim //2:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                          else:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                          decoration.add(Ai_vani)
                                          na_rasstrel.append(Ai_vani)
                                        Grisha.kill()
                                        if Oleg_eye == True:
                                          gfh.kill()
                                          gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                          decoration.add(gfh)
                                          na_rasstrel.append(gfh)
                                        if Oleg_sigara == True:
                                          bambaleyla.kill()
                                          bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                          decoration.add(bambaleyla)
                                          na_rasstrel.append(bambaleyla)
                                        Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                        decoration.add(Grisha)
                                        na_rasstrel.append(Grisha)
                                      elif time_pered_dialog == -50:
                                        dark1.kill()
                                        if Oleg_amulet == True and Oleg_eye == True and Oleg_sigara== True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end8_text_40%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7_text_40%.png')
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end6_text_40%.png')
                                        elif Oleg_amulet == True and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end5_text_40%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == True:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end4_text_40%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end3_text_40%.png')
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end2_text_40%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end1_text_40%.png')
                                        else:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7.png')
                                        na_rasstrel.append(dark1)
                                        decoration.add(dark1)
                                        if Oleg_amulet == True:
                                          Ai_vani.kill()
                                          if ai_vani_anim_check < aivani_anim //2:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                          else:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                          decoration.add(Ai_vani)
                                          na_rasstrel.append(Ai_vani)
                                        Grisha.kill()
                                        if Oleg_eye == True:
                                          gfh.kill()
                                          gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                          decoration.add(gfh)
                                          na_rasstrel.append(gfh)
                                        if Oleg_sigara == True:
                                          bambaleyla.kill()
                                          bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                          decoration.add(bambaleyla)
                                          na_rasstrel.append(bambaleyla)
                                        Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                        decoration.add(Grisha)
                                        na_rasstrel.append(Grisha)
                                      elif time_pered_dialog == -100:
                                        dark1.kill()
                                        if Oleg_amulet == True and Oleg_eye == True and Oleg_sigara== True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end8_text_60%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7_text_60%.png')
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end6_text_60%.png')
                                        elif Oleg_amulet == True and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end5_text_60%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == True:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end4_text_60%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end3_text_60%.png') 
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end2_text_60%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end1_text_60%.png')
                                        else:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7.png')
                                        na_rasstrel.append(dark1)
                                        decoration.add(dark1)
                                        if Oleg_amulet == True:
                                          Ai_vani.kill()
                                          if ai_vani_anim_check < aivani_anim //2:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                          else:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                          decoration.add(Ai_vani)
                                          na_rasstrel.append(Ai_vani)
                                        Grisha.kill()
                                        if Oleg_eye == True:
                                          gfh.kill()
                                          gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                          decoration.add(gfh)
                                          na_rasstrel.append(gfh)
                                        if Oleg_sigara == True:
                                          bambaleyla.kill()
                                          bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                          decoration.add(bambaleyla)
                                          na_rasstrel.append(bambaleyla)
                                        Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                        decoration.add(Grisha)
                                        na_rasstrel.append(Grisha)
                                      elif time_pered_dialog == -150:
                                        dark1.kill()
                                        if Oleg_amulet == True and Oleg_eye == True and Oleg_sigara== True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end8_text_80%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7_text_80%.png')
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end6_text_80%.png')
                                        elif Oleg_amulet == True and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end5_text_80%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == True:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end4_text_80%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end4_text_80%.png')
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end2_text_80%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end1_text_80%.png')
                                        else:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7.png')
                                        na_rasstrel.append(dark1)
                                        decoration.add(dark1)
                                        if Oleg_amulet == True:
                                          Ai_vani.kill()
                                          if ai_vani_anim_check < aivani_anim //2:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                          else:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                          decoration.add(Ai_vani)
                                          na_rasstrel.append(Ai_vani)
                                        Grisha.kill()
                                        if Oleg_eye == True:
                                          gfh.kill()
                                          gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                          decoration.add(gfh)
                                          na_rasstrel.append(gfh)
                                        if Oleg_sigara == True:
                                          bambaleyla.kill()
                                          bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                          decoration.add(bambaleyla)
                                          na_rasstrel.append(bambaleyla)
                                        Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                        decoration.add(Grisha)
                                        na_rasstrel.append(Grisha)
                                      elif time_pered_dialog == -200:
                                        dark1.kill()
                                        if Oleg_amulet == True and Oleg_eye == True and Oleg_sigara== True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end8_text_100%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7_text_100%.png')
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == True:
                                          dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end6_text_100%.png')
                                        elif Oleg_amulet == True and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end5_text_100%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == True:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end4_text_100%.png')
                                        elif Oleg_amulet == False and Oleg_eye == True and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end3_text_100%.png')
                                        elif Oleg_amulet == True and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end2_text_100%.png')
                                        elif Oleg_amulet == False and Oleg_eye == False and Oleg_sigara == False:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end1_text_100%.png')
                                        else:
                                                dark1 = Hero_sprite(x,y, 'Data/images/backgrounds/ends/end7.png')
                                        na_rasstrel.append(dark1)
                                        decoration.add(dark1)
                                        if Oleg_amulet == True:
                                          Ai_vani.kill()
                                          if ai_vani_anim_check < aivani_anim //2:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                          else:
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                          decoration.add(Ai_vani)
                                          na_rasstrel.append(Ai_vani)
                                        Grisha.kill()
                                        if Oleg_eye == True:
                                          gfh.kill()
                                          gfh = Hero_sprite(800,150, 'Data/images/characters/gfh_gray.png')
                                          decoration.add(gfh)
                                          na_rasstrel.append(gfh)
                                        if Oleg_sigara == True:
                                          bambaleyla.kill()
                                          bambaleyla = Hero_sprite(1100,150, 'Data/images/characters/bambaleyla_gray.png')
                                          decoration.add(bambaleyla)
                                          na_rasstrel.append(bambaleyla)
                                        Grisha = Hero_sprite(350,150, 'Data/images/characters/Grisha_gray.png')
                                        decoration.add(Grisha)
                                        na_rasstrel.append(Grisha)
                                      if Oleg_amulet == True:
                                        if ai_vani_drinking_check == 0:
                                          if ai_vani_anim_check == 0:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_1.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_anim_check == ai_vani_anim // 2:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Aivani_sit_2.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                        ai_vani_anim_check +=1
                                        if ai_vani_anim_check == ai_vani_anim:
                                          ai_vani_anim_check = 0
                                      if time_pered_dialog == -8600 or time_pered_dialog < -8600:
                                        ai_vani_drinking_check +=1
                                        if Oleg_amulet == True:
                                          if ai_vani_drinking_check == ai_vani_drinking // 23 * 1:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_1.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 2:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_2.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 3:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_3.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 4:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_4.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 5:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_5.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 6:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_6.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 7:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_7.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 8:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_8.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 9:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_9.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 10:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_10.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 11:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_11.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 12:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_12.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 13:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_13.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 14:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_14.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 15:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_15.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 16:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_16.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 17:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_17.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 18:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_18.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 19:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_19.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 20:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_20.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 21:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_21.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 22:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_22.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)
                                          elif ai_vani_drinking_check == ai_vani_drinking // 23 * 23:
                                            Ai_vani.kill()
                                            Ai_vani = Hero_sprite(175,150, 'Data/images/characters/Ai_vani drink/drink_23.png')
                                            decoration.add(Ai_vani)
                                            na_rasstrel.append(Ai_vani)

                                        if ai_vani_drinking_check == ai_vani_drinking // 23 * 30:
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_0%.png')
                                          ai_vani_drinking = 175
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 37:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_5%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 44:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_10%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 51:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_15%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 59:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_20%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 66:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_25%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 73:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_30%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 80:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_35%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 87:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_40%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 94:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_45%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 101:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_50%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 108:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_55%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 115:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_60%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 122:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_65%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 129:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_70%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 136:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_75%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 143:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_80%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 150:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_85%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 157:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_90%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 164:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_95%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 171:
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_100%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                        elif ai_vani_drinking_check == ai_vani_drinking // 23 * 180:
                                          #dark.kill()
                                          dark.kill()
                                          dark = Hero_sprite(x,y, 'Data/images/backgrounds/catscene/in_catscene_100_gray%.png')
                                          na_rasstrel.append(dark)
                                          decoration.add(dark)
                                          titles = Hero_sprite(x,3750, 'Data/images/backgrounds/ends/titles.png')  
                                          na_rasstrel.append(titles)
                                          decoration.add(titles)
                                        elif ai_vani_drinking_check > ai_vani_drinking // 23 * 180:
                                          titles.rect.y -= 1
                                          if pressed[0]:
                                              titles.rect.y -=2
                                          if self.developer == True:    
                                                print(titles.rect.y)
                                          if titles.rect.y < -7000:
                                                titles_music.stop()
                                                
                                           
                                                pygame.quit()
                                                
                                                
                                                #self.__init__()

                                     
                                                #potat = Potato()
                                                quit()
                                    #if Oleg_amulet == True and Oleg_eye == True and Oleg_sigara == True:
##                   exceif self.developer == True:pt:
##                              
##print('bye-bye')
##                          time.sleep(2)
##                          pygame.quit()
##                          quit()

potat = Potato()
potat.developer = False
root.mainloop()
