from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode


def Safe():
    Text_Service.typing_effect("Decides mantener esta información en secreto, pensando que puede ser útil más adelante.\n")

    ##TODO: GO TO NODE 22

def Use():
    Text_Service.typing_effect("Decides actuar rápidamente y usar la información para extorsionar al político y obtener un gran beneficio.\n")

    ##TODO: GO TO NODE 23

def Inform():
    Text_Service.typing_effect("Decides que es mejor no jugar con fuego y le informas al Don sobre lo que has descubierto.\n")

    ##TODO: GO TO NODE 24

def Actio_8():
    Text_Service.typing_effect("Después de investigar, descubres que el paquete contenía documentos que podrían destruir la carrera de un político influyente. Te das cuenta del poder que tienes ahora en tus manos.\n")

    Text_Service.Dialogue("Esto podría cambiarlo todo. Con esta información, podría tener el control de un político... o mi propia cabeza podría estar en peligro.")
    Text_Service.Dialogue("¿Qué vas a hacer con esto? Es oro puro, pero también una bomba de tiempo.", name= "Aliado")

Node8 = ActionNode(Actio_8)
Desitions = {
    "Guardar": ActionNode(Safe),
    "Usar": ActionNode(Use),
    "Informar": ActionNode(Inform)
}
Node8.set_SubNodes(Desitions)

