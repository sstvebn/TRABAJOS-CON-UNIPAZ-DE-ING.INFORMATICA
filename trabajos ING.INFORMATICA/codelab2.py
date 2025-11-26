N = int(input("ingrese el límite N: "))

suma_pares = 0
i = 1

while i <= N:
    if i % 2 == 0:
       suma_pares += i
    i += 1

print(f"La suma de los números pares hasta {N} es: {suma_pares}")


#el error es que faltaba la actualización del iterador i += 1 dentro del while sin esto el valor de i se vuelve infinito