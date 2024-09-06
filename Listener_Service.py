import ctypes
from openal import *
import threading
import time

class Listener_Service:
    _instance = None
    
    def __new__(cls,  *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Listener_Service, cls).__new__(cls, *args, **kwargs)
        return cls._instance
        
    def __init__(self):
        self.device = alc.alcOpenDevice(None)
        if not self.device:
            print("Error al abrir el dispositivo de audio.")
            exit(1)

        self.context = alc.alcCreateContext(self.device, None)
        alc.alcMakeContextCurrent(self.context)
        self.listener = oalGetListener()

        self.listener.set_position((0, 0, 0))  # Posición del listener
        self.listener.set_orientation((0, 0, -1, 0, 1, 0))

    def Stop(self):
        alc.alcMakeContextCurrent(None)
        alc.alcDestroyContext(self.context)
        alc.alcCloseDevice(self.device) 
                
