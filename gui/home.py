import logging
import tkinter

from pygame import mixer
from enviroment import Enviroment
from gui.config import MAXIMIZE
from testing.debug import mesure_time
from tkinter import CENTER, Label, PhotoImage, Button

class HomeScreen():
    def __init__(self):
        self.layout = tkinter.Tk()
        self.environment = Enviroment()
                
        self.init_screen(MAXIMIZE)
        
        image = PhotoImage(file = './assets/image/background2.png')
        background = Label(self.layout, image = image, width = 2000, height = 1100)
        background.place(x = 0,y = 0)
        
        self.inital_options()
        
        self.play_sountrack()
        
        self.layout.mainloop()
    
    def inital_options(self):
        self.button1 = Button(self.layout, text='Run Demo From File', height = 2, width = 20,command=self.choose_demo)
        self.button2 = Button(self.layout, text='Input Demo Data', height = 2, width = 20)
        self.button1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.button2.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        
    def init_screen(self, screen_status):
        self.layout.geometry('600x400+0+0')
        self.layout.title('Space Simulation')
        self.layout.attributes(screen_status, True) 
    
    def play_sountrack(self):
        mixer.init()
        mixer.music.load('./assets/sound/soundtrack.mp3')
        mixer.music.play(loops=-1)
    
    def pop_home_screen(self):
        self.button1.destroy()
        self.button2.destroy()
        
    def demo_buttons(self):
        self.button1 = Button(self.layout, text='colliosion 1', height = 2, width = 20, command= lambda : self.run_demo(1))
        self.button2 = Button(self.layout, text='colliosion 2', height = 2, width = 20, command= lambda : self.run_demo(2))
        self.button3 = Button(self.layout, text='colliosion 3', height = 2, width = 20, command= lambda : self.run_demo(3))
        self.button4 = Button(self.layout, text='colliosion 4', height = 2, width = 20, command= lambda : self.run_demo(4))
        self.button5 = Button(self.layout, text='could be flower', height = 2, width = 20, command= lambda : self.run_demo(8))
        self.button6 = Button(self.layout, text='could be flower 2', height = 2, width = 20, command= lambda : self.run_demo(9))
        self.button7 = Button(self.layout, text='solar system', height = 2, width = 20, command= lambda : self.run_demo(6))
        self.button8 = Button(self.layout, text='old one', height = 2, width = 20, command= lambda : self.run_demo(7))
        
        self.button1.place(relx = 0.4, rely = 0.4, anchor = CENTER)
        self.button2.place(relx = 0.4, rely = 0.5, anchor = CENTER)
        self.button3.place(relx = 0.4, rely = 0.6, anchor = CENTER)
        self.button4.place(relx = 0.4, rely = 0.7, anchor = CENTER)
        self.button5.place(relx = 0.6, rely = 0.4, anchor = CENTER)
        self.button6.place(relx = 0.6, rely = 0.5, anchor = CENTER)
        self.button7.place(relx = 0.6, rely = 0.6, anchor = CENTER)
        self.button8.place(relx = 0.6, rely = 0.7, anchor = CENTER)
        
    def choose_demo(self):
        self.pop_home_screen()
        self.demo_buttons()
        
    def pop_demo_buttons(self):
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        self.button7.destroy()
        self.button8.destroy()
        
    def run_demo(self, index):
        logging.debug(f'{index}')
        mesure_time(self.environment.scan_from_file, file_number=index)
        self.run()
    
    def run(self):
        # self.layout.destroy()
        # loading = PhotoImage(file = './assets/animation/loading.gif', format="gif -index 2")
        # background = Label(self.layout, image = loading, width = 2000, height = 1100)
        # background.place(x = 0,y = 0)
        # background.configure()
        self.environment.run()