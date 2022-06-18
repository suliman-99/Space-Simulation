from tkinter import Button, CENTER, messagebox, filedialog

from file import save_on_file
from gui.app import TkinterApp, AppContext


class SaveDemoScreen(TkinterApp):
    def __init__(self, context: AppContext):
        self.button2 = None
        self.button1 = None
        self.pop_button = None
        self.context = context
        self.initial_state()

    def initial_state(self):
        self.initial_widgets()
        self.initial_position()

    def initial_widgets(self):
        self.pop_button = Button(self.context.app, text='back', height=1, width=9, command=self.back)
        self.button1 = Button(self.context.app, text='save simulation', height=2, width=20, command=self.save)
        self.button2 = Button(self.context.app, text='run simulation', height=2, width=20, command=self.run)

    def initial_position(self):
        self.pop_button.place(relx=.2, rely=.1, anchor=CENTER)
        self.button1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.button2.place(relx=0.5, rely=0.6, anchor=CENTER)

    def back(self):
        planet_number = self.context.environment.planets_array.__len__()
        self.context.environment.planets_array.pop()
        self.pop()
        from gui.screens.planet_info import PlanetInfoScreen
        PlanetInfoScreen(self.context, planet_number, planet_number - 1)

    def save(self):
        output_file = filedialog.asksaveasfile(filetypes=(("Text Files", "*.txt"),), initialdir='./demos')
        save_on_file(self.context.environment.planets_array, output_file, self.context.environment.time_scale)
        messagebox.showinfo("SUCCESS", "Simulation saved successfuly")

    def run(self):
        self.run_environment()
