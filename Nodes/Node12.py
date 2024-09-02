from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

def Actio_12():
    Text_Service.typing_effect("Decides que la mejor manera de manejar los rumores es silenciar a aquellos que los propagan. Mandas un mensaje claro: nadie cuestiona al jefe.\n")
    Text_Service.typing_effect("Con cada hombre que haces callar, sientes que una parte de ti se endurece, pero también comienza a apagarse. Ya no te satisface el poder que alguna vez tanto ansiabas. Te vuelves cada vez más frío, más distante. Al final, te conviertes en uno más de la organización, perdiendo la chispa que te llevó a escalar.\n")

Node12 = ActionNode(Actio_12)
