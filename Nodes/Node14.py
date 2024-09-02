from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode


def Confess():
    Text_Service.typing_effect("Decides ser honesto con el Don sobre lo sucedido.\n")

    Text_Service.Dialogue("Tío, he perdido parte de nuestros recursos. Lo siento.")
    Text_Service.Dialogue("Esto es inaceptable. Pero aprecio tu honestidad.", name= "Don Graziano")

    ##TODO: GO TO NODE 37

def Recover():
    Text_Service.typing_effect("Decides encontrar una forma de recuperar lo que perdiste antes de informar al Don. Te reunes con los alidos que sobrevivieron.\n")

    Text_Service.Dialogue("Debo recuperar lo perdido antes de que el Don se entere.")
    Text_Service.Dialogue("Tengo algunas ideas. Vamos a trabajar en ello.", name= "Aliado")

    ##TODO: GO TO NODE 38

def Lie():
    Text_Service.typing_effect("Decides ocultar la verdad y mentir al Don sobre lo sucedido.\n")

    Text_Service.Dialogue("Todo salió bien, tío. No hubo problemas.")
    Text_Service.Dialogue("Me alegra escuchar eso. Buen trabajo.", name= "Don Graziano:")

    ##TODO: GO TO NODE 39

def Actio_14():
    Text_Service.typing_effect("Tus captores aceptan el soborno y te liberan, pero has perdido parte de tus recursos.\n")

    Text_Service.typing_effect("Te encuentras libre, pero con menos recursos. Debes decidir cómo proceder.")

    Text_Service.Dialogue("El dinero está bien. Puedes irte, pero no olvides que nos debes.", name= "Lider Ruso")
    Text_Service.Dialogue("Lo recordaré. Gracias.")

Node14 = ActionNode(Actio_14)
Desitions = {
    "Confesar": ActionNode(Confess),
    "Recuperar": ActionNode(Recover),
    "Mentir": ActionNode(Lie)
}
Node14.set_SubNodes(Desitions)

