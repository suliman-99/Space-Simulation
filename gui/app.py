import sys
import tkinter
from tkinter import Label, PhotoImage, Widget
from resources.sound import *
from core.environment import Environment
from core.file import save_as


class AppContext:
    def __init__(self):
        self.app = tkinter.Tk()
        self.environment = Environment()
        self.init_screen()

    def init_screen(self):
        self.app.geometry('600x400+0+0')
        self.app.title('Space Simulation')
        if sys.platform == 'linux':
            self.app.attributes('-zoomed', True)
        else:
            self.app.state('zoomed')


class TkinterApp:
    def __init__(self, home):
        self.context = AppContext()

        image = PhotoImage(file='./assets/image/background.png')
        background = Label(self.context.app, image=image,
                           width=2000, height=1100)
        background.place(x=0, y=0)
        mixer_init()
        play_sountrack()
        home(self.context)

    def get_widgets(self):
        widgets = []
        for i in dir(self):
            atterbute = getattr(self, i)
            if issubclass(type(atterbute), Widget):
                widgets.append(atterbute)
            elif issubclass(type(atterbute), list):
                for member in atterbute:
                    if issubclass(type(member), Widget):
                        widgets.append(member)
        return widgets

    def pop(self):
        for widget in self.get_widgets():
            widget.destroy()

    def run_environment(self):
        save_as(self.context.environment,'current_demo')
        self.context.app.destroy()
        self.context.environment.run()
