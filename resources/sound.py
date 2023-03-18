from pygame import mixer

channel_idx = 0
channel_number = 5


def mixer_init():
    mixer.init()
    mixer.set_num_channels(channel_number+1)


def play_sountrack():
    mixer.Channel(0).play(mixer.Sound(('./assets/sound/music.mp3')), -1)


def play_sountrack_collision():
    global channel_idx
    if mixer.Channel(channel_idx % channel_number+1).get_busy():
        mixer.Channel(channel_idx % channel_number+1).pause()
    mixer.Channel(channel_idx % channel_number+1).set_volume(50)
    mixer.Channel(channel_idx % channel_number +
                  1).play(mixer.Sound(('./assets/sound/collision.mp3')))
    channel_idx += 1


def mute():
    if mixer.Channel(0).get_volume() == 0.0:
        mixer.Channel(0).set_volume(1.0)
    else:
        mixer.Channel(0).set_volume(0)
