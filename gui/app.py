import tkinter
from tkinter.ttk import Progressbar

from resources.config import MAXIMIZE
from environment import Environment
from tkinter import Label, PhotoImage, Widget, CENTER

from resources.sound import play_sountrack


class AppContext:
    def __init__(self):
        self.app = tkinter.Tk()
        self.environment = Environment()
        self.init_screen(MAXIMIZE)

    def init_screen(self, screen_status):
        self.app.geometry('600x400+0+0')
        self.app.title('Space Simulation')
        self.app.attributes(screen_status, True)


class TkinterApp:
    def __init__(self, home):
        self.context = AppContext()

        image = PhotoImage(file='./assets/image/background2.png')
        background = Label(self.context.app, image=image, width=2000, height=1100)
        background.place(x=0, y=0)

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
        self.context.environment.run()
