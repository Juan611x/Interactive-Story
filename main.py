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

        self.isVisited = {key: False for key in enemies}

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def change_Room(self):
        self.Audio_Source.set_Sound('closeDoor.wav')
        self.Audio_Source.Start(gain=0.5)

    def play(self):
        self.Audio_Source.set_Sound('Rayo.wav')
        self.Audio_Source.Start_async()
        # print("¡Bienvenido al Castillo de las Sombras!")
        # print("Tu misión es encontrar la legendaria reliquia oculta en lo más profundo del castillo.")
        # print("Tienes un mapa antiguo que marca seis cuartos. Explora, resuelve enigmas y sobrevive.")
        Text_Service.typing_effect("Una tormenta rugía en lo alto de la colina cuando te acercaste al imponente Castillo de las Sombras")
        Text_Service.typing_effect("El viento gélido azotaba tu rostro mientras te detienes frente a las puertas principales, forjadas en hierro negro, tan antiguas como el tiempo mismo.")
        Text_Service.typing_effect("Eres un cazador de reliquias, conocido en todo el reino por tu astucia y valor.")
        Text_Service.typing_effect("Sin embargo, esta misión es diferente. No es solo por la gloria o las riquezas. Hay algo personal que te impulsa, una promesa que hiciste hace mucho tiempo.")
        
        Text_Service.typing_effect("\nDe repente, una voz grave te saca de tus pensamientos:")
        Text_Service.typing_effect("\nVoz misteriosa: '¿Vas a entrar o dejarás que el miedo te consuma?'")
        Text_Service.typing_effect("Te giras rápidamente, buscando la fuente de la voz, pero no ves a nadie. Solo la oscuridad del castillo te da la bienvenida.")
        
        Text_Service.typing_effect("\nTe decides y empujas las puertas con esfuerzo. Crujen ruidosamente al abrirse, revelando el vestíbulo del castillo.")
        Text_Service.typing_effect("La sala está en penumbra, y las sombras parecen moverse por su cuenta.")
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
        if not self.isVisited[self.location]:
            self.isVisited[self.location] = True
            Text_Service.typing_effect("\nTe encuentras en el vestíbulo de entrada del castillo. La sala está llena de telarañas y el aire es frío.")


            Text_Service.typing_effect("El aire es pesado y antiguo, como si el tiempo mismo se hubiera detenido en este lugar.")
            Text_Service.typing_effect("Las enormes puertas de madera detrás de ti se cierran con un estruendo, y el eco de su cierre resuena en las paredes de piedra desnuda.")
            Text_Service.typing_effect("A tu alrededor, las sombras se arremolinan en las esquinas del vasto salón, ondeando como si tuvieran vida propia.")
            Text_Service.typing_effect("Los techos se elevan imposiblemente altos, desapareciendo en la penumbra. A lo lejos, un candelabro de hierro colgante oscila levemente, sus velas gastadas apenas iluminan el vasto espacio.")
            Text_Service.typing_effect("El suelo bajo tus pies, hecho de losas de piedra fría y gastada, muestra cicatrices de antiguas batallas, con marcas y grietas que cuentan historias olvidadas.")
            Text_Service.typing_effect("Te sientes pequeño ante la inmensidad del lugar, y una sensación de desasosiego se apodera de ti. Es como si el castillo mismo estuviera observándote, esperando a que des el siguiente paso.")
            Text_Service.typing_effect("El eco de tus propios movimientos es tu única compañía en este silencio sepulcral. La aventura comienza aquí, en un lugar donde muchos han entrado, pero pocos han salido con vida.")

            Text_Service.typing_effect("Puedes ver puertas hacia el norte, este y oeste. Hay una escalera que desciende hacia el sur.")
        else:
            Text_Service.typing_effect("\nTe encuentras en el vestíbulo de entrada del castillo. La sala está llena de telarañas y el aire es frío.")
            Text_Service.typing_effect("Puedes ver puertas hacia el norte, este y oeste. Hay una escalera que desciende hacia el sur.")
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
        if not self.isVisited[self.location]:
            self.isVisited[self.location] = True
            Text_Service.typing_effect("Ingresas a la Armería...")
            Text_Service.typing_effect("Las paredes están adornadas con armas de todo tipo, desde espadas hasta arcos, todas cubiertas por una gruesa capa de polvo.")
            Text_Service.typing_effect("En el centro de la sala, una figura alta y encapuchada afila una espada. El sonido del metal contra la piedra reverbera por toda la armería.")
            
            Text_Service.Dialogue('Pensé que no vendrías. Pero aquí estás, buscando lo que no debes.', name="Figura misteriosa")
            Text_Service.typing_effect("Levanta la vista y ves unos ojos brillantes debajo de la capucha.")

            action = Text_Service.Give_Options('¿Qué quieres hacer', ['hablar', 'ignorar'], player)
            if action == 'hablar':
                Text_Service.typing_effect("Te acercas a la figura. Al hacerlo, sientes que el aire se vuelve más denso.")
                Text_Service.Dialogue('No todos los que entran en este castillo salen con vida. ¿Qué te hace pensar que serás diferente?', name="Figura misteriosa")
                Text_Service.typing_effect("Le cuentas brevemente tu misión y por qué estás aquí. La figura asiente lentamente.")
                Text_Service.Dialogue('Si realmente buscas la reliquia, necesitarás algo más que acero afilado. Pero toma esto, te servirá.', name="Figura misteriosa")
                Text_Service.typing_effect("Te entrega una espada antigua, cuya hoja brilla con un fulgor azul.")
                if 'sword' not in self.player.inventory:
                    print("Tomas la espada. Ahora tienes una espada en tu inventario.")
                    self.player.inventory.append('sword')
        else:
            Text_Service.typing_effect("Estas de regreso en la Armería...")
            

        action = Text_Service.Give_Options('¿Qué quieres hacer', ['examinar', 'volver'], player)
        self.interactions += 1
        if action == 'examinar':
            self.Audio_Source.set_Sound('Arsenal.wav')
            self.Audio_Source.Start_async(position=(0,0,1))
            Text_Service.typing_effect("Encuentras una espada que parece estar en mejor estado que las otras. También ves una linterna en un rincón.")
            action = Text_Service.Give_Options('¿Qué quieres hacer', ['tomar', 'dejar'], player)
            if action == 'tomar':
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
        if not self.isVisited[self.location]:
            self.isVisited[self.location] = True
            Text_Service.typing_effect("Entras en la antigua biblioteca del Castillo de las Sombras.")
            Text_Service.typing_effect("Los estantes, que se elevan hasta el techo, están repletos de libros cuyas tapas están cubiertas de polvo y misterios.")
            Text_Service.typing_effect("A medida que avanzas, notas que algunos libros flotan suavemente en el aire, moviéndose entre los estantes como si fueran mariposas, sus páginas susurrando secretos olvidados.")
            Text_Service.typing_effect("El ambiente es denso con la energía de siglos de conocimiento y magia acumulada, y una tenue luz azulada parece emanar de los mismos libros.")
            Text_Service.typing_effect("En el centro de la biblioteca, una mesa de madera oscura, con intrincados grabados, sostiene una vela encendida que parpadea suavemente, sugiriendo que alguien estuvo aquí no hace mucho.")
            Text_Service.typing_effect("Cerca de la mesa, un sillón de terciopelo rojo invita a sentarse, ofreciendo un raro momento de tranquilidad en este lugar ominoso.")
        else:
            Text_Service.typing_effect("Estas de regreso en la antigua biblioteca del Castillo de las Sombras.")

        self.enemy_encounter('library')
        # action = input("¿Qué quieres hacer? (examinar/libro_secreto/volver): ").strip().lower()
        action = Text_Service.Give_Options('¿Qué quieres hacer?', ['examinar', 'volver'], player)
        self.interactions += 1
        if action == 'examinar':
            Text_Service.typing_effect("Tus ojos se detienen en un libro que parece fuera de lugar, más brillante y menos polvoriento que los demás.")
            Text_Service.typing_effect("Lo jalas con cuidado, y de repente, escuchas un clic. Una sección de la pared se desplaza, revelando una puerta secreta.")
  
            action = Text_Service.Give_Options('¿Qué quieres hacer?', ['continuar', 'regresar'], player)
            if action == 'continuar':
                self.location = 'secret_chamber'
        elif action == 'volver':
            self.location = 'entrance_hall'
        else:
            print("No entiendes qué hacer.")
    
    def dungeon(self):
        self.change_Room()
        if not self.isVisited[self.location]:
            self.isVisited[self.location] = True
            Text_Service.typing_effect("Desciendes a la mazmorra, y una sensación de opresión te invade al instante. El aire es denso y frío, y la oscuridad es casi tangible.")
            Text_Service.typing_effect("Las paredes de piedra están cubiertas de musgo, goteando con la humedad que se filtra desde lo alto. El eco de tu respiración resuena en el pasillo estrecho, amplificado por el silencio abrumador.")
            Text_Service.typing_effect("A medida que avanzas, tus pasos hacen crujir el suelo de piedra bajo tus pies. A ambos lados del corredor, ves celdas abandonadas, sus rejas oxidadas por el tiempo.")
            Text_Service.typing_effect("Dentro de las celdas, puedes distinguir las sombras de lo que una vez fueron prisioneros, ahora reducidos a simples huesos que descansan en la penumbra.")
            Text_Service.typing_effect("Al final del pasillo, una pesada puerta de hierro se alza como una barrera ominosa, su superficie rugosa parece haber soportado siglos de tormento.")
        else:
            print("Estas de regreso en la mazmorra..")

        self.enemy_encounter('dungeon')
        action = Text_Service.Give_Options('¿Qué quieres hacer?', ['explorar', 'abrir_puerta', 'volver'], player)
        self.interactions += 1
        
        if action == 'explorar':
            Text_Service.typing_effect.typing_effectnt("Te acercas a las celdas, examinando cada una con detenimiento. En una de ellas, encuentras un esqueleto encorvado en un rincón oscuro.")
            Text_Service.typing_effect("Sus huesos están frágiles por el tiempo, pero en su mano huesuda sostiene algo brillante. Con cautela, te inclinas y descubres que es una llave, desgastada pero aún intacta.")
            if 'key' not in self.player.inventory:
                self.player.inventory.append('key')
                Text_Service.typing_effect("Tomas la llave con cuidado, sintiendo el frío metal en tu mano. Quizás esta llave abra la pesada puerta al final del pasillo.")
            else:
                Text_Service.typing_effect("Ya has tomado la llave. No hay nada más que puedas llevar de aquí.")
        elif action == 'abrir_puerta':
            if 'key' in self.player.inventory:
                Text_Service.typing_effect("Con la llave en mano, te diriges hacia la puerta de hierro. La introduces en la cerradura y, con un esfuerzo considerable, logras girarla.")
                Text_Service.typing_effect("La puerta se abre con un chirrido ensordecedor, revelando un túnel oscuro que parece extenderse hacia la distancia.")
                Text_Service.typing_effect("Sin otra opción, decides seguir el túnel, esperando que te lleve de regreso a una parte más familiar del castillo.")
                self.location = 'entrance_hall'
            else:
                Text_Service.typing_effect("Intentas abrir la puerta, pero la cerradura está firme. Necesitas una llave para continuar.")
        elif action == 'volver':
            Text_Service.typing_effect("Decides regresar por donde viniste, dejando la oscuridad de la mazmorra detrás.")
            self.location = 'entrance_hall'
        else:
            print("No entiendes qué hacer.")

    
    def throne_room(self):
        self.change_Room()
        if not self.isVisited[self.location]:
            self.isVisited[self.location] = True
            Text_Service.typing_effect("Cruzando el umbral, entras en la sala del trono. Es un espacio vasto y majestuoso, con altos techos abovedados decorados con intrincados frescos.")
            Text_Service.typing_effect("En el extremo opuesto, un gran trono dorado se erige como el centro de atención, su resplandor apenas amortiguado por la penumbra de la sala.")
            Text_Service.typing_effect("El aire está cargado de una energía extraña, palpable, que parece hacer eco de los susurros de las almas que alguna vez ocuparon este lugar. Cada paso que das resuena en el silencio sepulcral, y una sensación de inquietud se apodera de ti.")
        else:
            Text_Service.typing_effect("Estas de regreso en la sala del trono...")

        self.enemy_encounter('throne_room')

        action = Text_Service.Give_Options('¿Qué quieres hacer?', ['examinar', 'sentar', 'volver'], player)
        self.interactions += 1
        
        if action == 'examinar':
            Text_Service.typing_effect("Te acercas al trono con cautela, observando cada detalle. Las tallas doradas relucen bajo la poca luz, pero algo más llama tu atención.")
            Text_Service.typing_effect("Alrededor del asiento, tus dedos tropiezan con un borde irregular. Después de una inspección más cercana, descubres un compartimiento secreto.")
            if 'ring' not in self.player.inventory:
                self.Audio_Source.set_Sound('logro.wav')
                self.Audio_Source.Start()
                Text_Service.typing_effect("Dentro del compartimiento, tus ojos se posan en un pequeño anillo dorado. Lo tomas con reverencia, sintiendo una energía poderosa que emana de él, y lo guardas en tu inventario.")
                self.player.inventory.append('ring')
            else:
                print("Ya has tomado el anillo. No encuentras nada más en el compartimiento.")
        
        elif action == 'sentar':
            Text_Service.typing_effect("Te sientas con cierta reticencia en el trono, pero tan pronto como lo haces, una abrumadora sensación de pesadez te invade.")
            Text_Service.typing_effect("Tu corazón comienza a latir descontroladamente, como si estuviera a punto de explotar en tu pecho.")
            Text_Service.typing_effect("Es como si el trono intentara imponerte su voluntad. Un miedo inexplicable te recorre la columna vertebral, y decides levantarte rápidamente, antes de que esa energía te consuma por completo.")
        
        elif action == 'volver':
            self.location = 'entrance_hall'
        
        else:
            print("No entiendes qué hacer.")
    
    def secret_chamber(self):
        self.change_Room()
        
        if not self.isVisited[self.location]:
            self.isVisited[self.location] = True
            Text_Service.typing_effect("Pasas por la puerta y te encuentras en una cámara oculta, iluminada por la suave luz de antorchas mágicas que parecen flotar en el aire.")
            Text_Service.typing_effect("La habitación es pequeña pero está repleta de objetos antiguos y extraños, colocados cuidadosamente en estantes de piedra.")
            Text_Service.typing_effect("En el centro de la cámara, sobre un pedestal tallado con runas antiguas, hay un hueco perfectamente esculpido, como si estuviera esperando que algo encaje en él.")
            Text_Service.typing_effect("Te acercas con cautela, observando el pedestal más de cerca. Las runas que lo decoran brillan con un resplandor tenue, irradiando una energía misteriosa.")
            Text_Service.typing_effect("Aunque no puedes leer las inscripciones, el diseño del hueco sugiere que está destinado a albergar una espada, tal vez la tuya.")
        else:
            Text_Service.typing_effect("Regresa a la camara secreta, te encuentras nuevamente frente al pedestal..")
        self.enemy_encounter('secret_chamber')

        action = Text_Service.Give_Options('¿Qué quieres hacer?', ['insertar', 'volver'], player)
        if action == 'insertar':
            if 'sword' in self.player.inventory: 
                if all(enemy.isDefeated for enemy in enemies.values()):
                    Text_Service.typing_effect("Con un movimiento decidido, insertas la espada en el hueco del pedestal. De inmediato, las runas comienzan a brillar con una intensidad cegadora.")
                    Text_Service.typing_effect("Un viento sobrenatural se levanta en la cámara, y ves como las almas de los enemigos que derrotaste empiezan a emerger de la espada, transformándose en etéreos espectros.")
                    Text_Service.typing_effect("Uno por uno, los espectros son absorbidos por el pedestal, fusionándose con la energía antigua que lo envuelve.")
                    Text_Service.typing_effect("De repente, el pedestal se agrieta y se abre, revelando un camino oculto que lleva a una sala secreta.")
                    Text_Service.typing_effect("Cuando entras, tus ojos se agrandan ante la visión que se despliega ante ti: una cámara repleta de tesoros inimaginables, con montones de oro, joyas y objetos de un valor incalculable.")
                    Text_Service.typing_effect("El resplandor del tesoro ilumina la sala, reflejando en las paredes y llenándote de una sensación de logro indescriptible.")
                    Text_Service.typing_effect("Has encontrado el mayor tesoro que jamás hayas visto, la recompensa final por todas tus victorias y sacrificios.")
                    self.playing = False
                    self.end_game()
            else:
                print('No tines una espada..')
        else:
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
                    if 'ring' in self.player.inventory:
                        print("El ataque es repelido, pero el anillo se rompe en el proceso, desapareciendo de tu mano en fragmentos dorados. Aunque has perdido el anillo, has evitado el daño.")
                        self.player.inventory.remove('ring')
                    else:
                        print("pierdes una vida...")
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
                                self.player.health += 1
                                Text_Service.typing_effect("El alma del enemigo derrotado es absorbida por tu espada, imbuyéndola con un poder oscuro y antiguo")
                            else:
                                print('Fallaste tu ataque!')
                                print(f'El {self.enemies[room].name} te ataca')
                                if 'ring' in self.player.inventory:
                                    print("El ataque es repelido, pero el anillo se rompe en el proceso, desapareciendo de tu mano en fragmentos dorados. Aunque has perdido el anillo, has evitado el daño.")
                                    self.player.inventory.remove('ring')
                                else:
                                    print("pierdes una vida...")
                                    self.player.health -= 1
                        else:
                            print(f'No tiene con que atacar, reciver un ataque del {self.enemies[room].name}')
                            if 'ring' in self.player.inventory:
                                print("El ataque es repelido, pero el anillo se rompe en el proceso, desapareciendo de tu mano en fragmentos dorados. Aunque has perdido el anillo, has evitado el daño.")
                                self.player.inventory.remove('ring')
                            else:
                                print("pierdes una vida...")
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