#1Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def big(lista):
    for x in range(len(lista)):
        if lista[x] > 1: #numeros positivos
            lista[x] = "Big"
    print(lista)
big([- 1, 3, 5, -5])

#2-Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
#Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve

def contar(array):
    contar = 0
    for x in range (len(array)):
        if array[x]>0:
            contar = contar +1 #como no se cuales seran los valores positivos del array,solo se puede establecer una condcion que indique que si en el array hay valores positivos,se cuenten entre ellos
    array[len(array)-1] = contar #cambia el ultimo valor con el nimero de valores
    #positivos (contar sera el numero positivo que este en el array).no puedo colocar por ej,la posicion x3
    #  o la x1 para que sea positivo,porqie solo funcinara cn estos arrays del ejercicio y no con cualquiera
    print(array)

contar([-1,1,1,1])
contar([1,6, -4, -2, -7, -2])



#3-Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sum_total(array):
  suma= 0
  for x in range (len(array)):
    suma += array[x] # aqui se suman los valores de un array,para eso,debo crearlo antes,no se cuantos valores tiene el array,solo se que es un array
  print (suma)  #devuelve la suma,para eso,antes deben sumarse los valores de un array
sum_total([1,2,3,4])
sum_total([6,3, -2]) 


#4-Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promediofinal(array):
  promedio = 0
  for x in range (len(array)):
      promedio += array[x]
  promedio = promedio/ len(array) #el promediofinal se calcula con la suma de los valores dividido en la cantidad de valres del array
  print (promedio)
promediofinal ([1,2,3,4])

#5-Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0

# def longitud(array):
#   long = 0
#   for x in range(len(array)): aca no es necesario recorrer un arreglo para saber la longitud,solo basta con el indice.
#   long = len(array)
# print (long)
# longitud ([37,2,1, -9])

def long(array):
    longitud= len(array)
    print(longitud)
long([37,2,1, -9])
long([])

# #6-Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista.
#  Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False

def minimo(array):
    if len(array) == 0: #lista vacia
        print("False") 
        return 'false'
    else:
        min=array[0]
        for x in range (len(array)): 
            if array[x]<min: # valor minimo del array
                min = array[x] #valor minimo del array generado
        print(min) #devuelve el valor minimo,para eso,debe haber un array y este debe tener un valor minimo
minimo([37,2,1, -9])
minimo([])


# 7-Máximo : crea una función que toma una lista y devuelve 
# el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False

def maximo(array):
    if len(array) == 0: #lista vacia
        print("False") 
        return 'false'
    else:
        max=array[0]
        for x in range (len(array)): 
            if array[x]>max: # valor minimo del array
                max = array[x] #valor minimo del array generado
        print(max) #devuelve el valor minimo,para eso,debe haber un array y este debe tener un valor minimo
maximo([37,2,1, -9])
maximo([])


# 8-Análisis final : crea una función que tome una lista y devuelva un diccionario que 
# tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver 
# {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def analisisfinal(array):
    suma=0
    prom = 0
    min = 0
    max = 0
    long = len(array)
    for x in range(len(array)):
        suma += array[x]
        if min > array[x]:
            min = array[x]
        elif max < array[x]:
            max = array[x]
    prom = suma /len(array)
    print({'total': suma, 'promedio': prom, 'minimo': min, 'maximo': max, 'longitud': long}) #fx que tome una lista y devuelva dict.para eso,debo hacer antes de
    #un array,pero en el que se pueda sumar,promediar,min,max y ongitud.
analisisfinal([37,2,1, -9])


# 9-Lista inversa : crea una función que tome una lista y la devuelva 
# con los valores invertidos. Haz esto sin crear una segunda lista. 
# (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

def reverse_list():
return()

print [-9,1,2,37]
reverse_list ([37,2,1, -9])

def reverse_list(lista):
    return lista[::-1] 
mylist = [1, 2, 3, 4,] 
mylist2 = [6, 3, -2]   
print(reverse_list(mylist))
print(reverse_list(mylist2))

def reverse_list(array):
    array2 = []
    for x in range(len(array)-1, -1, -1):
        array2.append(array[x])
    print(array2)
reverse_list([37,2,1, -9])

def reverse_list(array):
    temp = 0
    long = int(len(array)/2)
    for x in range(long):
        temp = array[x]
        array[x] = array[len(array) -1- x]
        array[len(array) -1 - x] = temp
    print(array)
reverse_list([37,2,1,-9])

