
def c_a_f(c):
    return c * 9/5 + 32

def f_a_c(f):
    return (f - 32) * 5/9

def c_a_k(c):
    return c + 273.15

def k_a_c(k):
    return k - 273.15

def f_a_k(f):
    return (f - 32) * 5/9 + 273.15

def k_a_f(k):
    return (k - 273.15) * 9/5 + 32


print("=== Conversor de Temperaturas ===")
print("1) De °C a °F")
print("2) De °F a °C")
print("3) De °C a K")
print("4) De K a °C")
print("5) De °F a K")
print("6) De K a °F")

opcion = input("Selecciona una opción (1-6): ")
num = float(input("Introduce la temperatura: "))

if opcion == "1":
    print(f"{num}°C equivalen a {c_a_f(num):.2f}°F")
elif opcion == "2":
    print(f"{num}°F equivalen a {f_a_c(num):.2f}°C")
elif opcion == "3":
    print(f"{num}°C equivalen a {c_a_k(num):.2f} K")
elif opcion == "4":
    print(f"{num} K equivalen a {k_a_c(num):.2f}°C")
elif opcion == "5":
    print(f"{num}°F equivalen a {f_a_k(num):.2f} K")
elif opcion == "6":
    print(f"{num} K equivalen a {k_a_f(num):.2f}°F")
else:
    print("Esa opción no existe.")
