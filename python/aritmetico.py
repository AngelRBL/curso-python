print('Ingresa el primer valor')
num1 = int(input())
print('Ingresa el segundo valor')
num2 = int(input())

# Al sumarlos sucede un error y es concatenacion(en vez de sumarlo los une)
# Par aresolverlo tenemos que poner el input() dentro de int() 
resultado = num1 / num2
print(resultado)