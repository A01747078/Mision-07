# Alex Fernando Leyva Martínez - A01747078 - Grupo: 04
# Estye programa consiste en resolver problemas empleando el uso del ciclo While

# Esta función consiste en hacer una división imprimiendo el cociente y residuo
def dividir(dividendo, divisor):
    cociente = 0
    residuo = dividendo
    while residuo >= divisor:
        if divisor > 0:
            residuo = residuo - divisor
            cociente += 1
        elif divisor < 0:
            print("No acepta números negativos")
            print("----------")
            break
        elif divisor == 0:
            print("Math Error")
            print("----------")
            break
    if divisor > 0 and divisor != 0:
        print("----------")
        print("%d / %d = %d, sobra %d" % (dividendo, divisor, cociente, residuo))


#Esta función encuentra el número máximo de un conjunto de números
def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor")
    numeroMayor = 0
    numero = 0
    while numero != -1:
        numero = int(input("Teclea un numero [-1 para salir]: "))
        if numero > numeroMayor:
            numeroMayor = numero
        elif numero < numeroMayor:
                numeroMayor = numeroMayor
    if numero == numeroMayor and numero == 0:
        print("No hay valor mayor")
        print("----------")
    if numero == -1 and numeroMayor == 0:
        print("No hay valor mayor")
        print("----------")
    if numeroMayor > 0:
        print("El mayor es: ", numeroMayor)
        print("----------")


#Esta función despliega el menú de opciones y llama a la elegida
def main():
    opcion = 0
    while opcion != 3:
        print("Mision 07. Ciclos While")
        print("Autor: Alex Fernando Leyva Martinez")
        print("Matrícula: A01747078")
        print("1. Calcular Divisiones")
        print("2. Encontrar el mayor")
        print("3. Salir")
        opcion = int(input("Teclea tu opción: "))
        if opcion == 1:
            print("----------")
            dividendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            dividir(dividendo, divisor)
        elif opcion == 2:
            print("----------")
            encontrarMayor()
        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto")
        else:
            print("ERROR, teclea 1, 2 ó 3")
            print("----------")

# Función Principal
main()
