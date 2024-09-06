class Enemy:
    def __init__(self, name, sound):
        self.isDefeated = False
        self.isDiscovered = False
        self.name = name
        self.sound = sound