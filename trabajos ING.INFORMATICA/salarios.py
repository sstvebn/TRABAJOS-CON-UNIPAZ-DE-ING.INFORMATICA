contador = input("Desea iniciar el programa Y/N: ")

while contador == "Y":
    salario = float(input("indique el salario del trabajador: "))

    if salario > 10000:
        aument = salario*1.15
    else:
        aument = salario*1.12

    print("El salario es ",aument)

    contador = input("Desea calcular otro salario? Y/N: ")

print("muchas gracias por usarme")