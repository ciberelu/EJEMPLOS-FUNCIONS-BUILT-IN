##ejemplo de programacion multihilo

import _thread
from concurrent.futures import thread
import time

def horaActual(nomnbrethread, tiempo_de_espera):
        count = 0
        while count < 5:
                count += 1
                
                time.sleep(tiempo_de_espera)
                print(f"hilo: {nomnbrethread} - {time.ctime(time.time())}")

##cuando se ejecuta codigo multihilo, se tiene que bloquear el programa para que se ejecute codigo paralelo
##por ejemplo con un time.sleep(aqui se pone el tiempo)
_thread.start_new_thread(horaActual,("thread 1", 1))
_thread.start_new_thread(horaActual,("thread 2", 2))

print ("ya dispare los hilos")

while True:
        pass