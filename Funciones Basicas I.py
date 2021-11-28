#1
def a():
    return 5
print(a())

#el resultado predice 5,ya que si retorna 5,se imprime 5,en la funcion no hay nada definido

#2
def a():
    return 5
print(a()+a())

# el resultado predice 10,ya que a() es 5 y se pide sumar a() cn a()

#3
def a():
    return 5
    return 10
print(a())
#en pyhton el 1er retorno es 5


#4
def a():
    return 5
    print(10)

#retorna 5 no se porque
la identacion del print esta dentro y no reconoce la funcion.Si hubiese estado fuera,ahi reconoce el print

#5
def a():
    print(5)
x = a()
print(x)
#el 1er es igual a 5,y no retorna nada


#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
print(b+c) #no puede sumar nada mas nada
#el resultado imprime 3 y 5 . no suma porque no tiene un retorno despues del 
# print 

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#imprime 25 (son string y se multiplica)

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#100,10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(5,3)) 
print(a(2,3) + a(5,3))

#retorna 14,21 

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
 # imprime 8 (lo que dice el print)

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
 # 500,500,300,500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#500,300,500,500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#500,500,300,500

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#1,3,2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#1,3,5,10
