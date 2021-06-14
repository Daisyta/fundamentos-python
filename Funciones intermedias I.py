# 1-debería imprimir un número aleatorio entre 0 a 100
import random
def randInt(min= 0 , max= 100):
    num = random.randint (min,max)  #aqui se define la variable de minimo y maximo, la funcion randint arroja un numero entero
    if num < min or num > max: #este es el rango en el que estará ese numero aleatorio,pero,para que se muestre,
        #antes tengo que guardar ese numero aleatorio en una variable.
        num = random.random()  #random.ramdom va a dar un numero aleatorio.Entonces,como me dicen que debe estar entre un rango,le tengo que dar esa condicion antes
    return round (num) #la funcion round retorna un numero entero
print(randInt(0,100))



# debería imprimir un número aleatorio entre 0 a 50


import random
def randInt(min= 0 , max= 50):
    num = random.randint(min,max)
    if num < min or num > max: #este es el rango en el que estará ese numero aleatorio,pero,para que se muestre,antes tengo que guardar ese numero aleatorio en una variable.
        num = random.random()  #random.ramdom va a dar un numero aleatorio.Entonces,como me dicen que debe estar entre un rango,le tengo que dar esa condicion antes
    return num
print(randInt(max=50))



# debería imprimir un número aleatorio entre 50 a 100
import random
def randInt(min= 0 , max= 50):
    num = random.randint(min,max)
    if num < min or num > max: #este es el rango en el que estará ese numero aleatorio,pero,para que se muestre,antes tengo que guardar ese numero aleatorio en una variable.
        num = random.random()  #random.ramdom va a dar un numero aleatorio.Entonces,como me dicen que debe estar entre un rango,le tengo que dar esa condicion antes
    return num
print(randInt(50,100))


# debería imprimir un número aleatorio entre 50 y 500
import random
def randInt(min= 0, max= 500):
    num = random.random()*max + min
    while (num < min) or (num > max):
        num = random.random()*max
    return round(num)
print(randInt(50,500)) 


 

