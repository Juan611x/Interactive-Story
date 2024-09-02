from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode


def Acept():
    Text_Service.typing_effect("Decides que no es prudente cuestionar más al Don y aceptas su explicación. Sigues sus órdenes, manteniendo tu lealtad intacta, pero a costa de tu curiosidad.\n")

    Text_Service.Dialogue("Entiendo, Don. Confiaré en su juicio. Mi lealtad sigue siendo para usted.")
    Text_Service.Dialogue("Así me gusta. Ahora, ve y haz lo que mejor sabes hacer. Que esto quede entre nosotros.", name= "Don Graziano")
    
    ##TODO: GO TO NODE 37

def Press():
    Text_Service.typing_effect("No te conformas con la respuesta del Don y lo presionas para obtener más información. Esto podría fortalecer tu posición o ponerte en peligro.\n")
    
    Text_Service.Dialogue("Entendido, Don. Pero quizá este conocimiento podría ser útil para ambos... si sabemos cómo jugarlo.")
    Text_Service.Dialogue("Veo que tienes ambición. Veamos si sabes cómo manejarla sin que te consuma.", name= "Don Graziano")
    
    ##TODO: GO TO NODE 38

def Betray():
    Text_Service.typing_effect("Decides que no puedes confiar en el Don y comienzas a planear cómo traicionarlo, utilizando la información que tienes para debilitar su poder.\n")

    Text_Service.Dialogue("Lo entiendo, Don, pero si esto puede poner en peligro a la familia, creo que merezco saberlo todo.")
    Text_Service.Dialogue("Estás jugando con fuego, chico. Muy bien, si quieres saber más, prepara tu alma. Este conocimiento viene con un precio.", name= "Don Graziano")
    
    ##TODO: GO TO NODE 39

def Actio_21():
    Text_Service.typing_effect("Inquieto por lo que has descubierto, decides confrontar al Don sobre el verdadero contenido del paquete. Sabes que estás jugando un juego peligroso, pero sientes que necesitas respuestas para protegerte a ti y a tu familia.\n")

    Text_Service.typing_effect("Te diriges a la mansión del Don en medio de la noche, el aire está cargado de tensión. Al entrar, te recibe su asistente, un hombre de pocas palabras que siempre parece estar a punto de sacar una pistola.\n")

    Text_Service.Dialogue("El Don te está esperando en su estudio. No te demores.", name= "Asistente")
    print()

    Text_Service.typing_effect("Caminas por el largo pasillo, las paredes están decoradas con fotos antiguas de hombres poderosos, hombres como el Don, que han gobernado el submundo durante décadas. Las sombras parecen alargarse mientras te acercas a la gran puerta de madera que lleva al estudio del Don. Tomas un respiro profundo y tocas la puerta.\n")

    Text_Service.Dialogue("Entra.", name= "Don Graziano")
    print()

    Text_Service.typing_effect("El Don está sentado detrás de un enorme escritorio de caoba, con una copa de vino en una mano y un cigarro en la otra. Te hace un gesto para que te sientes. El silencio en la habitación es casi ensordecedor.\n")

    Text_Service.Dialogue("Me han dicho que has estado preguntando por el paquete.", name= "Don Graziano")
    Text_Service.Dialogue("Sí, Don. Después de la entrega, comencé a escuchar cosas... cosas que me preocupan. Quiero saber la verdad sobre lo que llevaba.")
    print()

    Text_Service.typing_effect("El Don toma un trago de su vino, mirándote fijamente. Luego, con un gesto calmado, apaga el cigarro en un cenicero de cristal.\n")
    
    Text_Service.Dialogue("¿La verdad? La verdad es que la curiosidad mata al gato, chico. Pero... te respeto lo suficiente para decirte esto: no era tu preocupación lo que había en ese paquete. Hiciste tu trabajo, y eso es todo lo que necesitas saber.", name= "Don Graziano")
    print()

    Text_Service.typing_effect("Sientes un nudo en el estómago, pero decides insistir\n")

    Text_Service.Dialogue("Don, si lo que llevaba puede ponernos a todos en peligro, creo que tengo el derecho de saberlo. No quiero que mi lealtad se vea comprometida por algo que desconozco.")
    print()

    Text_Service.typing_effect("El Don se inclina hacia adelante, sus ojos, que antes parecían calmados, ahora tienen un brillo peligroso.\n")
    
    Text_Service.Dialogue("¿Lealtad? ¿Estás cuestionando mi juicio? Escucha, muchacho, en este negocio, a veces es mejor no saberlo todo. Pero si realmente insistes...", name= "Don Graziano")
    print()

    Text_Service.typing_effect("El Don hace una pausa, como si estuviera decidiendo qué hacer contigo. Finalmente, deja escapar un suspiro y se reclina en su silla.\n")
    
    Text_Service.Dialogue("Ese paquete contenía documentos que podrían derribar a un hombre muy poderoso... alguien que podría causarnos más problemas de los que imaginas. ¿Ahora entiendes por qué era mejor que no lo supieras?", name= "Don Graziano")
    print()

    Text_Service.typing_effect("Tu mente corre a mil por hora. Los rumores eran ciertos, y ahora te das cuenta de lo profundo que estás en este juego. Tienes que decidir cómo proceder.\n")


Node21 = ActionNode(Actio_21)()
Desitions = {
    "Aceptar": ActionNode(Acept),
    "Presionar": ActionNode(Press),
    "Traicionar": ActionNode(Betray)
}
Node21.set_SubNodes(Desitions)

