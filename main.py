import os
import time
import random

from Listener_Service import Listener_Service
from Sound_Service import Sound_Service
from Enemy import Enemy
from Player import Player
import Text_Service

class Game:
    def __init__(self, *, enemies, player):
        self.listener = Listener_Service()
        self.Audio_Source = Sound_Service()
        
        self.location = 'entrance_hall'
        self.playing = True
        self.interactions = 0
        self.start_time = time.time()

        self.enemies = enemies
        self.player = player

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def change_Room(self):
        self.Audio_Source.set_Sound('closeDoor.wav')
        self.Audio_Source.Start(gain=0.5)

    def play(self):

        print("¡Bienvenido al Castillo de las Sombras!")
        print("Tu misión es encontrar la legendaria reliquia oculta en lo más profundo del castillo.")
        print("Tienes un mapa antiguo que marca seis cuartos. Explora, resuelve enigmas y sobrevive.")
        while self.playing:
            if self.location == 'entrance_hall':
                # self.clear()
                self.entrance_hall()
            elif self.location == 'armory':
                # self.clear()
                self.armory()
            elif self.location == 'library':
                # self.clear()
                self.library()
            elif self.location == 'dungeon':
                # self.clear()
                self.dungeon()
            elif self.location == 'throne_room':
                # self.clear()
                self.throne_room()
            elif self.location == 'secret_chamber':
                # self.clear()
                self.secret_chamber()
            elif self.location == 'end':
                # self.clear()
                self.end_game()
            self.check_health()

    def entrance_hall(self):
        self.change_Room()
        print("\nTe encuentras en el vestíbulo de entrada del castillo. La sala está llena de telarañas y el aire es frío.")
        print("Puedes ver puertas hacia el norte, este y oeste. Hay una escalera que desciende hacia el sur.")
        # action = input("¿Qué quieres hacer? (norte/este/oeste/sur/examinar): ").strip().lower()
        action =  Text_Service.Give_Options('¿Qué quieres hacer?', ['norte', 'este', 'oeste', 'sur', 'examinar'], player)
        self.interactions += 1
        if action == 'norte':
            self.location = 'throne_room'
        elif action == 'este':
            self.location = 'library'
        elif action == 'oeste':
            self.location = 'armory'
        elif action == 'sur':
            self.location = 'dungeon'
        elif action == 'examinar':
            print("Observas un cuadro antiguo colgado en la pared. En él aparece el retrato de un rey.")
            print("El cuadro parece mirarte fijamente.")
        else:
            print("No entiendes qué hacer.")
    
    def armory(self):
        self.change_Room()
        # self.enemy_encounter('armory')
        print("\nHas entrado en la armería. Las paredes están cubiertas con armaduras oxidadas y espadas antiguas.")
        # action = input("¿Qué quieres hacer? (examinar/tomar/volver): ").strip().lower()
        action = Text_Service.Give_Options('¿Qué quieres hacer', ['examinar', 'tomar', 'volver'], player)
        self.interactions += 1
        if action == 'examinar':
            print("Encuentras una espada que parece estar en mejor estado que las otras. También ves una linterna en un rincón.")
        elif action == 'tomar':
            if 'sword' not in self.player.inventory:
                print("Tomas la espada. Ahora tienes una espada en tu inventario.")
                self.player.inventory.append('sword')
            else:
                print("Ya tienes la espada.")
            if 'lantern' not in self.player.inventory:
                print("Tomas la linterna. Ahora tienes una linterna en tu inventario.")
                self.player.inventory.append('lantern')
            else:
                print("Ya tienes la linterna.")
        elif action == 'volver':
            self.location = 'entrance_hall'
        else:
            print("No entiendes qué hacer.")
    
    def library(self):
        self.change_Room()
        self.enemy_encounter('library')
        print("\nEntras en una antigua biblioteca. Los estantes están llenos de libros polvorientos.")
        print("Una vela encendida sobre una mesa sugiere que alguien estuvo aquí recientemente.")
        # action = input("¿Qué quieres hacer? (examinar/libro_secreto/volver): ").strip().lower()
        action = Text_Service.Give_Options('¿Qué quieres hacer?', ['examinar', 'libro_secreto', 'volver'], player)
        self.interactions += 1
        if action == 'examinar':
            print("Mientras examinas los libros, encuentras un diario que describe los secretos del castillo.")
            if 'diary' not in self.player.inventory:
                self.player.inventory.append('diary')
                print("El diario se ha añadido a tu inventario.")
            else:
                print("Ya has tomado el diario.")
        elif action == 'libro_secreto':
            print("Encuentras un libro que parece fuera de lugar. Lo jalas, y una puerta secreta se abre en la pared.")
            print("Pasas por la puerta y encuentras una cámara secreta.")
            self.location = 'secret_chamber'
        elif action == 'volver':
            self.location = 'entrance_hall'
        else:
            print("No entiendes qué hacer.")
    
    def dungeon(self):
        self.change_Room()
        self.enemy_encounter('dungeon')
        print("\nDesciendes a la mazmorra. Está oscura y húmeda, y puedes escuchar el eco de tu respiración.")
        print("Ves celdas vacías a ambos lados y una pesada puerta al final del pasillo.")
        # action = input("¿Qué quieres hacer? (explorar/abrir_puerta/volver): ").strip().lower()
        action = Text_Service.Give_Options('¿Qué quieres hacer?', ['explorar', 'abrir_puerta', 'volver'], player)
        self.interactions += 1
        if action == 'explorar':
            print("Exploras las celdas y encuentras un esqueleto que sostiene una llave en la mano.")
            if 'key' not in self.player.inventory:
                self.player.inventory.append('key')
                print("Tomas la llave. Quizás abre alguna puerta importante.")
            else:
                print("Ya has tomado la llave.")
        elif action == 'abrir_puerta':
            if 'key' in self.player.inventory:
                print("Usas la llave para abrir la pesada puerta. Detrás de ella encuentras un túnel.")
                print("Sigues el túnel y regresas al vestíbulo de entrada.")
                self.location = 'entrance_hall'
            else:
                print("La puerta está cerrada y no tienes la llave.")
        elif action == 'volver':
            self.location = 'entrance_hall'
        else:
            print("No entiendes qué hacer.")
    
    def throne_room(self):
        self.change_Room()
        self.enemy_encounter('throne_room')
        print("\nEntras en la sala del trono. Un gran trono dorado se encuentra al final de la sala.")
        print("Sin embargo, algo en el ambiente te pone nervioso. El lugar está lleno de una energía extraña.")
        # action = input("¿Qué quieres hacer? (examinar/sentar/volver): ").strip().lower()
        action = Text_Service.Give_Options('¿Qué quieres hacer?', ['examinar', 'sentar', 'volver'], player)
        self.interactions += 1
        if action == 'examinar':
            print("Mientras examinas el trono, encuentras un compartimiento secreto.")
            if 'ring' not in self.player.inventory:
                self.Audio_Source.set_Sound('logro.wav')
                self.Audio_Source.Start()
                print("Dentro del compartimiento encuentras un anillo dorado. Lo tomas y lo guardas.")
                self.player.inventory.append('ring')
            else:
                print("Ya has tomado el anillo.")
        elif action == 'sentar':
            print("Te sientas en el trono, pero una sensación de pesadez te invade. Decides levantarte rápidamente.")
        elif action == 'volver':
            self.location = 'entrance_hall'
        else:
            print("No entiendes qué hacer.")
    
    def secret_chamber(self):
        self.change_Room()
        self.enemy_encounter('secret_chamber')
        if all(enemy.isDefeated for enemy in enemies.values()):
            print("\nTe encuentras en la cámara secreta. El aire es denso, y el ambiente parece cargado de misterio.")
            print("En el centro de la sala hay un pedestal con una reliquia antigua, brillando con una luz propia.")
            # action = input("¿Qué quieres hacer? (examinar/tomar/volver): ").strip().lower()
            action = Text_Service.Give_Options('¿Qué quieres hacer?', ['examinar', 'tomar', 'volver'], player)
            self.interactions += 1
            if action == 'examinar':
                print("Te acercas al pedestal y ves que la reliquia está rodeada de inscripciones antiguas.")
                print("Parece ser la reliquia que buscabas, pero tomarla podría activar alguna trampa.")
            elif action == 'tomar':
                if 'relic' not in self.player.inventory:
                    print("Tomas la reliquia. Una sensación de logro te invade.")
                    self.player.inventory.append('relic')
                    self.location = 'end'
                else:
                    print("Ya has tomado la reliquia.")
            elif action == 'volver':
                self.location = 'library'
            else:
                print("No entiendes qué hacer.")
        else:
            print("No puedes tomar la reliquia hasta derrotar a todos los enemigos en el castillo.")
            self.location = 'library'

    def enemy_encounter(self, room):
        if not self.enemies[room].isDefeated:
            isCombat = True
            atack_p, Flee_p = 0.75, 0.6
            if self.enemies[room].isDiscovered == False:
                if 'lantern' in self.player.inventory:
                    # use = input('Deseas usar tu linterna ? (Si/No): ').strip().lower()
                    use = Text_Service.Give_Options('Deseas usar tu linterna ?', ['Si', 'No'], player)
                    if use == 'si':
                        print(f'Enemigo descubierto ({self.enemies[room].name})')
                        self.enemies[room].isDiscovered = True
                        print('Acabas de entrar en combate...')
            while isCombat:
                self.check_health()
                if self.player.health <= 0:
                    isCombat = False
                    continue
                if self.enemies[room].isDiscovered == False:
                    print(f'Aparecio el {self.enemies[room].name}')
                    print(f'El {self.enemies[room].name} te ataco, te quito una vida')
                    self.player.health -= 1
                    self.enemies[room].isDiscovered = True
                else:
                    print(f'Estas en combate contra {self.enemies[room].name}')
                    # action = input('Que deseas hacer ? (Atacar/Huir): ').strip().lower()
                    action = Text_Service.Give_Options('Que deseas hacer ?', ['Atacar', 'Huir'], player)
                    if action == 'atacar':
                        if 'sword' in self.player.inventory:
                            success = random.random() < atack_p
                            self.Audio_Source.set_Sound('ataque.wav') 
                            self.Audio_Source.Start(position=(1,0,0))
                            time.sleep(0.2)    
                            if success:
                                self.Audio_Source.set_Sound('golpeEspada.wav') 
                                self.Audio_Source.Start(position=(-1,0,0))
                                print(f'Derrotaste al {self.enemies[room].name}')
                                self.enemies[room].isDefeated = True
                                isCombat = False
                                self.player.health = 3
                            else:
                                print('Fallaste tu ataque!')
                                print('El enemigo te ataca y pierdes una vida')
                                self.player.health -= 1
                        else:
                            print('No tiene con que atacar, reciver un ataque del enemigo y te quita una vida')
                            self.player.health -= 1

                    else:  
                        success = random.random() < Flee_p
                        if success:
                            print(f'lograste huir del {self.enemies[room].name}')
                            isCombat = False
                            #TODO: Huir
                            self.location = 'entrance_hall'
                        else:
                            print('No lograste Huir!')
                            print('El enemigo te ataca y pierdes una vida')
                            self.player.health -= 1



    def check_health(self):
        if self.player.health <= 0:
            print("Te has quedado sin salud.")
            self.playing = False
            self.end_game()

    def end_game(self):
        self.playing = False
        elapsed_time = time.time() - self.start_time
        print("\nEl juego ha terminado.")
        print(f"Tuviste {self.interactions} interacciones y jugaste por {int(elapsed_time)} segundos.")
        print("Gracias por jugar.")
        exit(0)


player = Player()
player.inventory = []
player.health = 3

enemies = {
            'armory': Enemy('guardián de la armería'),
            'library': Enemy('espectro de la biblioteca'),
            'dungeon': Enemy('carcelero de la mazmorra'),
            'throne_room': Enemy('rey espectral'),
            'secret_chamber': Enemy('guardián de la reliquia')
        }
game = Game(enemies=enemies, player=player)
game.play()