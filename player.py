from dfplayermini import Player

from time import sleep

music = Player(pin_TX=8, pin_RX=9)

#music.module_reset()
music.module_wake()
#music.volume(20)
music.play(1)
#sleep(5)
#music.stop()

#music.module_sleep()