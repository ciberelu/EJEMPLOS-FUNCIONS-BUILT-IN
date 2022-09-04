##funcion map
## aplica una funcion a todos los elementos iterables

cuadradoLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def cuadrado(x):
    return x*x



resultado = map(cuadrado, cuadradoLista)

print(list(resultado))

##funcion reduce

from functools import reduce
from subprocess import CREATE_NEW_PROCESS_GROUP

def suma (a, b):
    return a + b

##ejecuta de forma recursiva una funcion sobre la lista hasta que la lista se quede con un unico elemento
##las funciones con reduce, necesitan dos parametros
res = reduce(suma, cuadradoLista)
print(res)