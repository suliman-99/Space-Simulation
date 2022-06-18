from tkinter import Entry, Label, CENTER, Button, messagebox
from gui.app import TkinterApp, AppContext
from gui.screens.planet_info import PlanetInfoScreen


class PlanetNumberScreen(TkinterApp):
    def __init__(self, context: AppContext):
        self.label2 = None
        self.time_scale_entry = None
        self.pop_button = None
        self.button = None
        self.label1 = None
        self.planet_number_entry = None
        self.context = context
        self.initial_state()

    def initial_state(self):
        self.initial_widgets()
        self.initial_position()

    def initial_widgets(self):
        self.planet_number_entry = Entry(self.context.app)
        self.time_scale_entry = Entry(self.context.app)
        self.pop_button = Button(self.context.app, text='back', height=1, width=9, command=self.back)
        self.label1 = Label(self.context.app, text="planet number : ", width=12)
        self.label2 = Label(self.context.app, text="time scale : ", width=12)
        self.button = Button(self.context.app, text='next', height=1, width=15, command=self.next)

    def initial_position(self):
        self.pop_button.place(relx=.2, rely=.1, anchor=CENTER)
        self.label1.place(relx=0.45, rely=0.5, anchor=CENTER)
        self.label2.place(relx=0.45, rely=0.6, anchor=CENTER)
        self.planet_number_entry.place(relx=0.55, rely=0.5, anchor=CENTER)
        self.time_scale_entry.place(relx=0.55, rely=0.6, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def show_error(self):
        self.planet_number_entry.delete(0, 'end')
        self.time_scale_entry.delete(0, 'end')
        messagebox.showerror("Error", "enter a valid number between 1 and 100 please")

    def next(self):
        try:
            planet_number = int(self.planet_number_entry.get())
            self.context.environment.time_scale = int(self.time_scale_entry.get())
            self.context.environment.set_time_speed(1)
        except ValueError:
            self.show_error()
            return
        if planet_number < 1:
            self.show_error()
            return
        self.pop()
        PlanetInfoScreen(self.context, planet_number, 0)

    def back(self):
        self.pop()
        from gui.screens.home import HomeScreen
        HomeScreen(self.context)
