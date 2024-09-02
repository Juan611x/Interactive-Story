from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

from Node10 import Node10
from Node11 import Node11

def Counter():
    Text_Service.typing_effect("Decides que la mejor defensa es un buen ataque. Reúnes a tus hombres y planeas un contraataque para enviar un mensaje claro a los rusos: no se metan contigo.\n")

    Node10.Start()

def Escape():
    Text_Service.typing_effect("Sabes que la situación es peligrosa y decides que lo mejor es informar al Don sobre lo ocurrido. Escapas rápidamente y vuelves a la base para planear tu próximo movimiento con el apoyo de tu jefe.\n")

    Node11.Start()


def Actio_4():
    Text_Service.typing_effect("Gracias a tu precaución, lograste evitar una emboscada. Los rusos habían planeado tenderte una trampa, pero tus instintos te alertaron a tiempo. Mientras te movías con sigilo, notaste a varios hombres armados escondidos entre los contenedores, listos para atacarte. Sin perder tiempo, te escabulliste por una ruta alternativa, logrando escapar ileso. Sin embargo, ahora sabes que has hecho enemigos poderosos\n")
    Text_Service.typing_effect("Mientras te alejabas, el sonido de tus pasos resonaba en el silencio de la noche. La adrenalina corría por tus venas, y cada sombra parecía esconder un nuevo peligro. Te detuviste un momento para recuperar el aliento y evaluar la situación. Desde tu posición elevada, podías ver a los rusos moviéndose con cautela, buscando cualquier rastro de tu presencia. Sabías que no podías quedarte mucho tiempo en un solo lugar.\n")
    Text_Service.typing_effect("Decidiste moverte hacia un viejo almacén abandonado que habías visto en tu camino. El lugar estaba oscuro y lleno de escombros, pero ofrecía un refugio temporal. Te escondiste detrás de unas cajas y escuchaste atentamente. Los rusos estaban cada vez más cerca, sus voces se oían más claras. Respiraste hondo y trataste de calmarte, sabiendo que cualquier error podría ser fatal. Con cuidado, te deslizaste hacia una salida trasera y continuaste tu huida, consciente de que la caza apenas había comenzado.\n")


Node4 = ActionNode(Actio_4)
Desitions = {
    "Contraatacar": ActionNode(Counter),
    "Escapar": ActionNode(Escape)
}
Node4.set_SubNodes(Desitions)

