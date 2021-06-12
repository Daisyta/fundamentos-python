#1 Básico : imprime todos los enteros del 0 al 150.
for x in range (151):
  print (x)

#2 Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range (1000):
    if x % 5 == 0:
        print (x)
    
#3Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar.
#  Si es divisible por 10, imprima "Coding Dojo".
for x in range (100):
  if x % 10 == 0:
    print("Coding Dojo");
    elif x % 5 == 0:
      print ("Coding")

#4¡Uf, Eso es bastante grande!: 
# suma enteros impares de 0 a 500,000 e imprime la suma final.

numeros = []
numero = 0
while numero<500001:
    numero+=1
    if numero%2 != 0:
        numeros.append(numero)#Añade el numero al array
print(sum(numeros))


for x in range (500000):
    if x % 2 == 1:
        print (x)

#5Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, 
# restando 4 en cada iteración.


for x in range (2018,0,-4): #empieza en 2018 porque es cuenta regresiva
    print (x)


#6 Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2,
#  highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)


#from collections import counter  #para contar los valores de una lista o palabra en python,se usa la clase counter y hay que importar una libreria
#print (counter)


lowNum = 2
highNum = 9
mult = 3
if 9 % 3 == 0:
  return True
else:
  return False

for i in range (2,9,*3):
    print (i)




