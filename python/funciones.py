# Como trabaja una funcion?
# las funciones estan definidas con un conjunto de lineas de codigo las cuales realizan una accion expecifica, las funciones nos permiten descomponer los problemas que tengamos en tareas pequenas la cual podemos resolverlas en 1 a 1.
# Las funciones son acciones especificas para nuestro programa.

# def saludar():
#   print('Hola Bienvenido al juego de Cody')
# saludar()

#-------------------------------------------------------------------------------//
# Los argumentos nos van a permitir a recibir valores del exterior ya sea que el usuario lo ingrese o lo metamos desde nuestro codigo.

def saludar(nombre):
 return 'Hola {} Bienvenido al juego de Cody'.format(nombre)

print('Ingresa tu nombre')
nombre = input()
print(saludar(nombre))
