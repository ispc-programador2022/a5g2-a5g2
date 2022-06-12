def suma(a, b, c):
    return (a + b + c)

print('Hola. Ingresa tres valores para obtener el resultado de su suma.')
num1 = int(input('Ingresa el primer valor: '))
num2 = int(input('Ingresa el segundo valor: '))
num3 = int(input('Ingresa el tercer valor: '))

resultado = suma(num1, num2, num3)

print('El resultado es: ', resultado)