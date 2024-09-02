from openal import *
import os
import threading
import time

class Sound_Service:
    def __init__(self, path):
        self.set_Sound(path)

    def Start(self, *, gain = 1, position = (0,0,0), looping = False):
        self.Sound.set_looping = looping
        self.Sound.set_position(position)
        self.Sound.set_gain(gain)
        self.Sound.play()
        while self.Sound.get_state() == AL_PLAYING:
            pass

    def Start_async(self, *, gain = 1, position = (0,0,0), sleep = 0, looping = False):
        time.sleep(sleep)
        thread = threading.Thread(target=self.Start, kwargs={'gain': gain, 'position': position, 'looping':looping})
        thread.start()

    def set_Sound(self, path):
        RUTA = os.getcwd()
        self.Sound = oalOpen(RUTA + '\\Sound_Efects\\' + path)
    
    def set_position(self, x, y, z):
        self.Sound.set_position((x, y, z))

    # def set_orientation(self,frontX, frontY, frontZ, upX, upY, upZ):
    #     self.Sound.set_looping

