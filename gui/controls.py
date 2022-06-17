from vpython import scene, button, slider, checkbox, color
import resources.config


class Controls:
    def __init__(self, environment):
        self.environment = environment
        self.button = None
        self.slider_value = 1

    def on_changed(self, s):
        self.slider_value = s.value
        self.environment.set_time_speed(self.slider_value * self.environment.initial_time)

    def on_pressed(self):
        if self.environment.time_speed == 0:
            self.button.text = '<b>Pause</b>'
            self.environment.set_time_speed(self.slider_value)
        else:
            self.button.text = '<b>Resume</b>'
            self.environment.set_time_speed(0)

    def on_cheked(self, value):
        self.environment.set_trail_state(value.checked)

    def render(self):
        scene.append_to_caption('\n\n')
        self.button = button(bind=self.on_pressed,
                             text='<b>Pause</b>', color=color.purple)
        scene.append_to_caption('    ')
        slider(bind=self.on_changed, value=1,
               min=resources.config.MIN_SPEED, max=resources.config.MAX_SPEED, length=1200)
        scene.append_to_caption('\n\n')
        checkbox(bind=self.on_cheked, text='Show Trail',
                 checked=self.environment.trail_state)
