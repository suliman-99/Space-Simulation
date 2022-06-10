from pygame import mixer


def play_sountrack():
    mixer.init()
    mixer.music.load('./assets/sound/soundtrack.mp3')
    mixer.music.play(loops=-1)


def mute():
    if mixer.music.get_volume == 0:
        mixer.music.set_volume(100)
    else:
        mixer.music.set_volume(0)
