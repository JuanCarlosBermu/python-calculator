import math

print ("Calculadora de python")
def sumar(a, b): # Aqui se definen la suma, a y b son los parametros que se les pasaran a la funcion sumar
    return a + b

def restar(a, b): # Aqui se definen la resta, a y b son los parametros que se les pasaran a la funcion restar
    return a - b

def multiplicar(a, b): # Aqui se definen la multiplicacion, a y b son los parametros que se les pasaran a la funcion multiplicar
    return a * b

def dividir(a, b): # Aqui se definen la division, a y b son los parametros que se les pasaran a la funcion dividir
    if b != 0:     # Este if valida que b no sea un cero, y asi no haya errores en la division. Ejemplo: 5/0 = error
        return a / b
    else:
        return "Error: División por cero"
def raiz(x, n): 
    if x <= 0: 
        return "Error: El grado de la raíz debe ser mayor que 0."
    if x < 0 and n % 2 == 0:
        return "Error: No se puede calcular la raíz par de un número negativo."
    else:
        return x ** (1 / n)
def potencia(base, exponente):
    if base == 0 and exponente < 0:
        return "Error: No se puede elevar 0 a un exponente negativo"
    else:
        return math.pow(base, exponente)


def calculadora(): # Esta funcion indica al user que numeros corresponden a que operacion, y el user debera elegir cual usar
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raiz cuadrada")
    print("6. Exponenciacion")

    while True:
        operacion = input("Ingresa el número de la operación (1/2/3/4/5/6): ")

        if operacion in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if operacion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif operacion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif operacion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif operacion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            elif operacion == '5':
                print(f"la raiz {num2} de {num1} es {raiz(num1, num2)}") #num1 es x, num2 es n
            elif operacion == '6':
                print(f"{num1} ^ {num2} = {potencia(num1, num2)}")  
        else:
            print("Operación inválida. Por favor, elige una operación válida.")

        otra = input("¿Quieres realizar otra operación? (si/no): ")
        if otra.lower() != 'si':
            break

if __name__ == "__main__":
    calculadora()
