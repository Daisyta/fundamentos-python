 #coding=utf-8
#print("Hello World!")

#print("esta es una cadena de muestra")
#nombre = "Zen"
#print("Mi nombre es", nombre)


#first_name = "Zen"
#last_name = "Coder"
#age = 27
#print("Mi nombre es {} {} y tengo {} años.".format(first_name,last_name, age))
# salida: Mi nombre es Zen Coder y tengo 27 años.
#print("Mi nombre es {} {} y tengo {} años.".format(age, first_name,last_name))
# salida: Mi nombre es 27 Zen y soy Coder años.


# 1. TAREA: imprimir "Hola mundo"
print( "Hola mundo" )
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Dai"
print("Hola, " + name)	# con una coma
# 3. imprimir "Hola 42!" con un numero en una variable
num = 42
print( f"Hola {num} !")	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( ("Me encanta comer {} y {}".format(fave_food1, fave_food2))) # con .format()

fave_food1 = "sushi"
fave_food2 = "pizza"
print (f"Me encanta comer {fave_food1} and {fave_food2}") # con una cadena f


EJERCICIO GRUPO 1:

crea una función que tome una lista y devuelva el primer y el último valor de la lista. Si la longitud de la lista es menor que 2, haga que devuelva False.

def ejercicio(lista=[]):
    if len(lista) < 2:
        return False, False
    else:
        primer = lista[0]
        ultimo = lista[-1]
        #ultimo = lista[len(lista)+1]
        return primer, ultimo
    
lista_prueba1 = [1, 2, 3, 4]
lista_prueba2 = [2]
primer, ultimo = ejercicio(lista_prueba1)
print(f"el primero es {primer} y el ultimo es {ultimo}")


- Crea una funcion que dado una palabra diga si es palindroma o no.

igual, aux = 0, 0
texto = "ANA":
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
     igual += 1
     aux   += 1
if len(texto) == igual:
  print("El texto es palindromo!")
else:
  print("El texto no es palindromo!")
  
  
igual, aux = 0, 0
texto = "ANA"
for ind in reversed(range(0, len(texto))):
    if texto[ind].lower() == texto[aux].lower():
        igual += 1
        aux += 1
if len(texto) == igual:
    print("El texto es palindromo!")
else:
    print("El texto no es palindromo!")
    
    
  - Crea una función que tome una lista y devuelva un diccionario con su mínimo, máximo, promedio y sum

