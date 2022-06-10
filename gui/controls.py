import logging

from environment import *
from gui.config import MAX_SPEED, MIN_SPEED


class Controls:
    def __init__(self, environment):
        self.environment = environment
        self.button = None
        self.slider_value = 1

    def on_changed(self, s):
        logging.debug(f'{s.value}')
        self.slider_value = s.value
        self.environment.change_time_flow(self.slider_value)

    def on_pressed(self):
        if self.environment.time_speed == 0:
            self.button.text = '<b>Pause</b>'
            self.environment.change_time_flow(self.slider_value)
        else:
            self.button.text = '<b>Resume</b>'
            self.environment.change_time_flow(0)

    def render(self):
        scene.append_to_caption('\n\n')
        self.button = button(bind=self.on_pressed, text='<b>Pause</b>', color=color.purple)
        scene.append_to_caption('    ')
        slider(bind=self.on_changed, value=1, min=MIN_SPEED, max=MAX_SPEED, length=1200)
