x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
def changenumber(array):
    for i in range(len(array)):
        for x in range(len(array[i])):
            if array[i][x] == 10:
                array[i][x] = 15 #aca se pide que 10 cambie a 15
    print(array) #para imprimirlo,antes se debe recorrer el array del enunciado (x)
x = [ [5,2,3], [10,8,9] ] #resultado del array ,pero,previamente hay qe imprimirlo
changenumber(x) #para que me muestre la fx,debe haber un array definido para poder aplicarla (el que esta en x)


# En el directorio sports_directory, cambia 'Messi' a 'Andres'
# Camba el valor 20 en z a 30



# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
def changelastname(students):
    for student in students: #aqui se recorre la lista ,esta lista es de estudiantes,pero solo queremos modificar el last name de un estudiante
        #print (student ['last_name'])
        if student['last_name'] == "Jordan": #antes del cambio.Para hacer el cambio,como el parametro esta en una lista,
            #se debe recorrer para saber que parametro estan pidiendo que cambie.en este casoo,piden que cambie  el last name
            student['last_name'] = "Bryant" #cambio al final
            return student#piden cambiar el apellido del 1er alumno de jordan a bryant ,para eso,antes tengo que indicar el cambio a realizar
print (changelastname(students))



def changesoccer(sports_directory):
    for soccer in sports_directory: #aqui se recorre la lista ,esta lista es de estudiantes,pero solo queremos modificar el last name de un estudiante
        #print (student ['last_name'])
        if soccer[0] == "Messi": #antes del cambio.Para hacer el cambio,como el parametro esta en una lista,
            #se debe recorrer para saber que parametro estan pidiendo que cambie.en este casoo,piden que cambie  el last name
            soccer[0] = "Andres" #cambio al final
            return soccer #piden cambiar el apellido del 1er alumno de jordan a bryant ,para eso,antes tengo que indicar el cambio a realizar

sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
print ((sports_directory ["soccer"]))

