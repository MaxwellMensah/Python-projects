# Music player in python

from pygame import mixer

mixer.init()
# --------------------------Path of your music
mixer.music.load("Fugees_-_Ready_Or_Not_.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    print("Press 'p' to pause")
    print("Press 'r' to resume")
    print("Press 'v' set volume")
    print("Press 'e' to exit")
    print()

    button = input("['p','r','v','e'] |>> ")
    if button == "p":
        mixer.music.pause()
        print()
    elif button == "r":
        mixer.music.unpause()
        print()
    elif button == "v":
        v = float(input("Enter volume(0 to 1): "))
        mixer.music.set_volume(v)
        print()
    elif button == "e":
        mixer.music.stop()
        break