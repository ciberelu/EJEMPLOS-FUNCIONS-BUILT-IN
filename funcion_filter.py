##ejemplo de como utilizar la funcion filter
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pares (x):
    if x % 2 == 1:
        return True

##con filter tomamos cada iterador que devuelva True
resultado = filter(pares, numero)
##para imprimmir una lista se debe poner antes de la variable que contiene la lista la palabra list(variable)
print(list(resultado))

##ejemplo de filter para filtrar una lista string

nombres = ["pepe", "pepito", "elui"]

def obtenerpep (x):
    if x.startswith("pep"):
        return True  

nombresFiltrados = filter(obtenerpep, nombres)
print(list(nombresFiltrados))