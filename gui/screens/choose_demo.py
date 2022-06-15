import logging
from tkinter import CENTER, Button
from gui.app import TkinterApp, AppContext

from testing.debug import mesure_time


class ChooseDemoScreen(TkinterApp):
    def __init__(self, context: AppContext) -> None:
        self.pop_button = None
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None
        self.button5 = None
        self.button7 = None
        self.button6 = None
        self.button8 = None
        self.context = context

        self.initial_state()

    def initial_state(self):
        self.initial_widgets()
        self.initial_position()

    def initial_widgets(self):
        self.pop_button = Button(self.context.app, text='back', height=1, width=9, command=self.back)
        self.button1 = Button(self.context.app, text='colliosion 1', height=2, width=20,
                              command=lambda: self.run_demo(1))
        self.button2 = Button(self.context.app, text='colliosion 2', height=2, width=20,
                              command=lambda: self.run_demo(2))
        self.button3 = Button(self.context.app, text='colliosion 3', height=2, width=20,
                              command=lambda: self.run_demo(3))
        self.button4 = Button(self.context.app, text='colliosion 4', height=2, width=20,
                              command=lambda: self.run_demo(4))
        self.button5 = Button(self.context.app, text='could be flower', height=2, width=20,
                              command=lambda: self.run_demo(8))
        self.button6 = Button(self.context.app, text='could be flower 2', height=2, width=20,
                              command=lambda: self.run_demo(9))
        self.button7 = Button(self.context.app, text='solar system', height=2, width=20,
                              command=lambda: self.run_demo(6))
        self.button8 = Button(self.context.app, text='old but gold', height=2, width=20,
                              command=lambda: self.run_demo(7))

    def initial_position(self):
        self.pop_button.place(relx=.2, rely=.1, anchor=CENTER)
        self.button1.place(relx=.4, rely=.4, anchor=CENTER)
        self.button2.place(relx=.4, rely=.5, anchor=CENTER)
        self.button3.place(relx=.4, rely=.6, anchor=CENTER)
        self.button4.place(relx=.4, rely=.7, anchor=CENTER)
        self.button5.place(relx=.6, rely=.4, anchor=CENTER)
        self.button6.place(relx=.6, rely=.5, anchor=CENTER)
        self.button7.place(relx=.6, rely=.6, anchor=CENTER)
        self.button8.place(relx=.6, rely=.7, anchor=CENTER)

    def run_demo(self, index):
        logging.debug(f'{index}')
        mesure_time(self.context.environment.scan_from_file, file=index)
        self.run()

    def run(self):
        # loading = PhotoImage(file = './assets/animation/loading.gif', format="gif -index 2")
        # background = Label(self.context.app, image = loading, width = 2000, height = 1100)
        # background.place(x = 0,y = 0)
        # background.configure()
        self.run_environment()

    def back(self):
        self.pop()
        from gui.screens.home import HomeScreen
        HomeScreen(self.context)
