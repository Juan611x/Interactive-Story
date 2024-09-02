from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode


def Use():
    Text_Service.typing_effect("Usar la información para ganar influencia en la familia\n")

    Text_Service.Dialogue("(pensando en voz alta) “Si juego bien mis cartas, esta información podría darme una posición más fuerte dentro de la familia.”")
    Text_Service.Dialogue("(pensando en voz alta) “Debo ser cuidadoso y estratégico. Esta es mi oportunidad para ascender.”")

    ##TODO: GO TO NODE 51

def Share():
    Text_Service.typing_effect("Compartir la información con el Don\n")

    Text_Service.Dialogue("(pensando en voz alta) “Debo llevar esto directamente a Don Graziano. Él sabrá qué hacer con esta información.”")
    Text_Service.Dialogue("(pensando en voz alta) “La lealtad es lo más importante. El Don debe saber que puede confiar en mí.”")

    ##TODO: GO TO NODE 24

def Sell():
    Text_Service.typing_effect("Vender la información a otro grupo\n")

    Text_Service.Dialogue("(pensando en voz alta) “Esta información vale una fortuna. Podría venderla a otro grupo y hacerme rico.”")
    Text_Service.Dialogue("(pensando en voz alta) “Es arriesgado, pero la recompensa podría ser enorme. Debo encontrar al comprador adecuado.”")

    ##TODO: GO TO NODE 52

def Actio_20():
    Text_Service.typing_effect("Después de recoger el paquete, te diriges a un lugar seguro para examinar su contenido. Al abrirlo, descubres documentos y fotografías que revelan información crucial sobre un rival de la mafia. Este conocimiento tiene el potencial de cambiar el equilibrio de poder en la ciudad. Te das cuenta de la importancia de esta información y de las diferentes maneras en que podrías utilizarla.\n")

    Text_Service.Dialogue("(pensando en voz alta) “Esto es más grande de lo que imaginaba. Con esta información, podría cambiar muchas cosas… pero, ¿cómo debería usarla?”")

Node20 = ActionNode(Actio_20)
Desitions = {
    "Usar": ActionNode(Use),
    "Compartir": ActionNode(Share),
    "Vender": ActionNode(Sell)
}
Node20.set_SubNodes(Desitions)

