# Los operadores de comparacion siempre vienen acompanados por los operadores de condicion o mejor conocidos como sentencias hacen que cambie el rumbo de nuestro programa.

# Por ejemplo:

# Si un usuario ingresa un numero mayor a 10 y la sentencia es correcta, entoces ingresa un bloque de codigo especifico siempre habra un caso contrario que no se cumpla y aqui tambien podemos ingresar a un bloque de codigo diferente.

print('Ingresa tu edad')
edad = int(input())
if edad < 18:
  print('Eres menor de edad')
else:
  print('Eres mayor de edad')
