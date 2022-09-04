##combina una lista con una tupla
cursos = ["java", "python", "git"]
asitentes = (15, 20, 4)

demo = zip(cursos, asitentes)
print(list (demo))

## palabras reservadas all() y any()

##sirve para verificar que todas las condiciones  de una lista se cumplan o que una condicion se cumpla

listaA =[1==1, 2==2, 3==4]
resultado = any(listaA)
print(resultado)
resultadoAll = all(listaA)
print(resultadoAll)

##funcion round
##sirve para redondear flotantes

a = 5.5
b= 5.4
c = 7.7

print(round(a))
print(round(b))


##funcion para ordenar lista 

listaLetras = ["z", "b", "d"]
ordenada = sorted(listaLetras, reverse=True)
print(list(ordenada))

##funcion input
##permite preguntar al usuario por datos

a= input("como te llamas")
print(f"hola: {a}")