import os
import time
import random
from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

# from Node2 import Node2
# from Node3 import Node3

def Decline():
    Text_Service.Dialogue("Lo siento, tío, pero no puedo aceptar este trabajo. Es demasiado arriesgado.")
    Text_Service.Dialogue("Me decepcionas, sobrino. Espero que no te arrepientas de esta decisión.")

    # Node3.Start()

def Negotiate():
    Text_Service.Dialogue("Estoy dispuesto a hacerlo, pero quiero una mayor participación en las ganancias. Este riesgo merece una recompensa adecuada.")
    Text_Service.Dialogue("Eres ambicioso, sobrino. Muy bien, tendrás tu parte, pero recuerda, la lealtad es lo más importante.", name= "Don Graziano")
    
    # Node2.Start()

def Acept():
    Text_Service.Dialogue("Haré lo que sea necesario, tío. Puedes contar conmigo.")
    Text_Service.Dialogue("Sabía que podía confiar en ti. No me decepciones.", name= "Don Graziano")

    # Node2.Start()

def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

def print_horses(horses):
    for i, horse in enumerate(horses):
        print(f"Caballo {i+1}: {'-' * horse}")

def race():
    horses = [0] * 6
    while max(horses) < 50:
        for i in range(len(horses)):
            horses[i] += random.randint(1, 5)
        print_horses(horses)
        time.sleep(0.5)
        # print("\n" * 10)
        clear()
    return horses.index(max(horses)) + 1

def horce_raice():
    print("¡La carrera ha comenzado!")
    winner = race()
    if winner == 5:
        print(f"¡El caballo {winner} ha ganado! ¡Ganaste tu apuesta!")
    else:
        print(f"¡El caballo {winner} ha ganado! Perdiste tu apuesta.")

def Actio_1():
    Text_Service.typing_effect('Bienvenido a esta historia...')

    print()
    Text_Service.typing_effect('Eres Tony "El Lobo" Graziano, un miembro en ascenso en la organización mafiosa de los Graziano en los años 90, basada en Nueva York. ')
    Text_Service.typing_effect("Tu objetivo es tomar el control total de la organización, enfrentarte a rivales, tomar decisiones clave que definirán tu destino, y tal vez incluso cuestionar tus propias lealtades.")
    Text_Service.typing_effect("Esta historia se desarrolla en un ambiente oscuro y peligroso, donde cada decisión puede acercarte más al poder o a la ruina.\n")

    Text_Service.typing_effect("Te encuentras en la casa de apuestas, un lugar bullicioso y lleno de humo, donde la mafia realiza todas sus operaciones. Las paredes están decoradas con fotos de caballos campeones y antiguos ganadores. Estás sentado en una mesa, observando con atención una carrera de caballos en la que has apostado una buena suma de dinero al caballo #5. El ambiente está cargado de tensión y emoción.\n")
    
    time.sleep(1.5)
    clear()
    horce_raice()
    
    Text_Service.typing_effect("De repente, un hombre de confianza de tu tío se acerca y te susurra al oído que Don Graziano quiere verte en su despacho.\n")

    Text_Service.typing_effect("Te levantas y caminas por el pasillo oscuro, pasando por varias puertas cerradas hasta llegar al despacho de Don Graziano. El lugar está lleno de antigüedades que reflejan el poder y la historia de tu familia. El aire está cargado de humo de cigarro y el aroma a cuero viejo. Don Graziano, tu tío, está sentado detrás de un gran escritorio de caoba, con una expresión seria en su rostro.\n")

    Text_Service.Dialogue("Ah, sobrino, me alegra que hayas venido. Tengo una oportunidad que podría cambiar tu vida… y la nuestra. Quiero que te encargues de una operación de contrabando de armas. Es un trabajo delicado, pero confío en ti.", name="Don Graziano")
    print()

Node1 = ActionNode(Actio_1)
Desitions = {
    'Aceptar': ActionNode(Acept),
    'Negociar': ActionNode(Negotiate),
    'Rechazar': ActionNode(Decline)
}
Node1.set_SubNodes(Desitions)
Node1.Start()

