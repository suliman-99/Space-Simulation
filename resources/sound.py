from pygame import mixer


def play_sountrack():
    # mixer.Channel(0).play(mixer.Sound(('./assets/sound/s3.mp3')))
    mixer.init()
    mixer.music.load('./assets/sound/s3.mp3')
    mixer.music.play(loops=-1)


def play_sountrack_collision():
    mixer.Channel(1).play(mixer.Sound(('./assets/sound/collision 1.mp3')))
    # mixer.init()
    # mixer.music.load('./assets/sound/collision 1.mp3')
    # mixer.music.play()


def mute():
    if mixer.music.get_volume == 0:
        mixer.music.set_volume(100)
    else:
        mixer.music.set_volume(0)
