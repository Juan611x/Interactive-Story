from openal import *
import os
import threading
import time

class Sound_Service:
    # def __init__(self, ):
    #     self.set_Sound(path)

    def Start(self, *, gain = 1, position = (0,0,0), looping = False, duration = 0):
        self.Sound.set_looping = looping
        self.Sound.set_position(position)
        self.Sound.set_gain(gain)
        self.Sound.play()
        if duration == 0:
            while self.Sound.get_state() == AL_PLAYING:
                pass
        else:
            count = duration * 100
            while count > 0:
                time.sleep(0.01)
                count -= 1
                if looping and not self.Sound.get_state() == AL_PLAYING:
                    self.Sound.play()


    def Start_async(self, *, gain = 1, position = (0,0,0), sleep = 0, looping = False, duration = 0):
        time.sleep(sleep)
        thread = threading.Thread(target=self.Start, kwargs={'gain': gain, 'position': position, 'looping':looping, 'duration':duration})
        thread.start()

    def set_Sound(self, path):
        RUTA = os.getcwd()
        self.Sound = oalOpen(RUTA + '\\Sound_Efects\\' + path)
    
    def set_position(self, x, y, z):
        self.Sound.set_position((x, y, z))

    # def set_orientation(self,frontX, frontY, frontZ, upX, upY, upZ):
    #     self.Sound.set_looping




# Audio_Source4 = Sound_Service()
# Audio_Source4.set_Sound('pasos.wav')
# Audio_Source4.Start_async(duration=10, looping=True)