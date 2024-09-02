from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

from Node17 import Node17	
from Node16 import Node16

def Kill():
    Text_Service.typing_effect("Decides que la traición no puede ser tolerada. Te enfrentas a Luca en privado y lo eliminas sin más preámbulos.\n")

    Node16.Start()

def UseIt():
    Text_Service.typing_effect("Decides que es mejor mantener a tus enemigos cerca. Le haces saber a Luca que estás al tanto de su traición, pero en lugar de matarlo en ese momento, Decides sacaele toda la informacion que puedas.\n")

    Node17.Start()


def Actio_6():
    Text_Service.typing_effect("Llegas al  sótano de un club nocturno que usas como base de operaciones. Uno de tus hombres de confianza, Marco, te ha informado que otro miembro de tu equipo, Luca, ha estado pasando información a los rusos. Estás solo con Marco y sientes la rabia acumulándose dentro de ti.\n")

    Text_Service.Dialogue("Jefe, odio ser el que te lo diga, pero Luca ha estado hablando con los rusos. Les ha pasado algo grande. No sé exactamente qué, pero no podemos dejarlo pasar.", name="Marco")
    Text_Service.Dialogue("¿Estás seguro de esto, Marco? Luca siempre ha sido leal... aunque últimamente, algo me olía mal.")
    Text_Service.Dialogue("Lo vi con mis propios ojos. Si no hacemos algo pronto, estaremos en serios problemas.", name="Marco")

Node6 = ActionNode(Actio_6)
Desitions = {
    "Eliminarlo": ActionNode(Kill),
    "Interrogarlo": ActionNode(UseIt)
}
Node6.set_SubNodes(Desitions)

