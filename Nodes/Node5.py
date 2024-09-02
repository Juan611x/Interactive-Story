from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

from Node13 import Node13
from Node14 import Node14


def Bribe():
    Text_Service.typing_effect("Sabes que el dinero puede ser una poderosa herramienta. Ofreces una suma considerable a cambio de tu libertad.\n")

    Text_Service.Dialogue("Escucha, tengo dinero. Mucho dinero. Déjame ir y te haré rico.")
    Text_Service.Dialogue("¿Dinero, dices? Habla, ¿cuánto estamos hablando?", name= "Lider Ruso")
    print()

    Node14.Start()

def Escape():
    Text_Service.typing_effect("Observas que las cuerdas que te atan no están tan apretadas como pensabas. Podrías intentar soltarte y buscar una salida.\n")

    Text_Service.Dialogue("(Piensas)`Si puedo aflojar estas cuerdas, tal vez tenga una oportunidad.`")
    Text_Service.Dialogue("¿Qué estás haciendo? ¡No intentes nada estúpido!", name= "Lider Ruso")
    print()

    Node13.Start()

def Actio_5():
    print("Tu imprudencia te lleva a una trampa. Pierdes la carga y eres capturado.\n")

    Text_Service.typing_effect("Te encuentras en un almacén oscuro y húmedo, atado a una silla. La luz de una bombilla parpadeante ilumina apenas el rostro de tus captores. El líder, un hombre de aspecto rudo con una cicatriz en la mejilla, se acerca lentamente.\n")
    
    Text_Service.Dialogue("Así que pensaste que podías jugar con nosotros, ¿eh? Ahora, pagarás el precio.", name= "Lider Ruso")
    Text_Service.Dialogue("No sabía que esto iba a pasar. Solo seguía órdenes.")
    Text_Service.Dialogue("Órdenes… Siempre las órdenes. Pero ahora, tú decides tu destino.", name= "Lider Ruso")
    print()

Node5 = ActionNode(Actio_5)
Desitions = {
    "Escapar": ActionNode(Escape),
    "Sobornar": ActionNode(Bribe)
}
Node5.set_SubNodes(Desitions)
    