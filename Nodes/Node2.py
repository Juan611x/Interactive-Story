from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

from Node4 import Node4
from Node5 import Node5
from Node6 import Node6



def Negotiate():
    Text_Service.typing_effect("Decides que esta es una oportunidad para obtener más de lo que se había acordado. Te acercas al contacto ruso y comienzas a negociar, buscando obtener mejores términos para la operación. Sabes que esto puede ser arriesgado, pero la recompensa podría valer la pena.\n")
    Text_Service.Dialogue("Escucha, creo que podemos hacer un mejor trato. Lo que estás ofreciendo no es suficiente para el riesgo que estamos tomando.")
    print()
    Text_Service.typing_effect("El contacto ruso frunce el ceño, pero parece considerar tus palabras. Sus hombres intercambian miradas, y puedes sentir la tensión en el aire")

    Node6.Start()

def Rely():
    Text_Service.typing_effect("Decides que lo mejor es seguir con el plan original. Te acercas al contacto ruso con confianza, ignorando las señales de advertencia. Esperas que tu determinación y seguridad sean suficientes para llevar a cabo la operación sin problemas.\n")
    Text_Service.typing_effect("Al llegar al punto de encuentro, extiendes la mano para saludar al contacto ruso. Él te mira con desconfianza, pero finalmente estrecha tu mano. Sus hombres se mantienen alerta, observando cada uno de tus movimientos.")

    Node5.Start()

def Caution():
    Text_Service.typing_effect("Decides mantener la calma y observar cuidadosamente el entorno antes de actuar. Notas pequeños detalles que confirman tus sospechas: un hombre armado en la sombra, una señal de mano entre los rusos. Te preparas para cualquier eventualidad.\n")
    Text_Service.typing_effect("Te acercas lentamente, asegurándote de no hacer movimientos bruscos. Tus ojos escanean el área, buscando posibles rutas de escape y cualquier cosa que pueda ser usada como cobertura en caso de que las cosas se pongan feas.")

    Node4.Start()

def Actio_2():
    Text_Service.typing_effect("La noche es fría y oscura en los muelles de Nueva York. Las luces de los barcos parpadean a lo lejos mientras te acercas al punto de encuentro. El contacto ruso, un hombre de aspecto severo y ojos penetrantes, te espera junto a un contenedor. Sin embargo, algo en su postura y en la forma en que sus hombres te observan te hace sentir que algo no está bien.\n")
    Text_Service.typing_effect("El viento sopla con fuerza, llevando consigo el olor salado del mar y el eco distante de las bocinas de los barcos. Te detienes por un momento, observando el entorno. Los muelles están casi desiertos, pero puedes ver sombras moviéndose entre los contenedores y escuchar el murmullo de conversaciones en ruso.\n")

Node2 = ActionNode(Actio_2)
Desitions = {
    "Cautela": ActionNode(Caution),
    "Confiar": ActionNode(Rely),
    "Negociar": ActionNode(Negotiate)
}
Node2.set_SubNodes(Desitions)
