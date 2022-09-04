## sirven para crear ficheros de registro
##niveles de logging, info (no muestra nada), warning error critical debug 
##logger sirve para ir trazando los programas.
import logging
##con este no se muestra nada

logging.info("arrancando programa")
logging.warning("hace calor")

##se puede configurar los niveles para indicarle a partir del cual se pueden presentar los logginf, ejemplo

logging.basicConfig(level=logging.INFO)
logging.info("ahora si ya lo muestro")