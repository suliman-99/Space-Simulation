from vpython import scene, button, slider, checkbox, color
import resources.config
from file import save_as


class Controls:
    def __init__(self, environment):
        self.environment = environment
        self.button = None
        self.slider_value = 1

    def on_changed(self, s):
        self.slider_value = s.value
        self.environment.set_time_speed(self.slider_value)

    def on_pressed(self):
        if self.environment.time_speed == 0:
            self.button.text = '<b>Pause</b>'
            self.environment.set_time_speed(self.slider_value)
        else:
            self.button.text = '<b>Resume</b>'
            self.environment.set_time_speed(0)

    def on_saved(self):
        save_as(self.environment.planets_array,
                self.environment.time_scale, 'saved_state')

    def on_cheked(self, value):
        self.environment.set_trail_state(value.checked)

    def restart_demo(self):
        self.environment.isActive = False
        self.slider.value = 1
        self.slider_value = 1
        self.checkbox.checked = False
        self.button.text = '<b>Pause</b>'

    def render(self):
        button(bind=self.restart_demo, text='<b>Restart</b>', color=color.black)
        button(bind=self.on_saved, text='<b>Save State</b>', color=color.blue)
        self.button = button(bind=self.on_pressed,
                             text='<b>Pause</b>', color=color.purple)
        self.slider = slider(bind=self.on_changed, value=1,
                             min=resources.config.MIN_SPEED, max=resources.config.MAX_SPEED, length=1100)
        scene.append_to_caption('\n\n')
        self.checkbox = checkbox(
            bind=self.on_cheked, text='Show Trail', checked=False)
