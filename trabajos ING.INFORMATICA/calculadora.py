
print("=== Calculadora ===")
print("1) Sumar")
print("2) Restar")
print("3) Multiplicar")
print("4) Dividir")

op = input("Elige una opción (1-4): ")

n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))

if op == "1":
    print("Resultado:", n1 + n2)
elif op == "2":
    print("Resultado:", n1 - n2)
elif op == "3":
    print("Resultado:", n1 * n2)
elif op == "4":
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("No se puede dividir entre cero")
else:
    print("Opción inválida")
