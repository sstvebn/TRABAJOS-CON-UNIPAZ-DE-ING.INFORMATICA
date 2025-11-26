zona = input("ingrese zona (A/B)):  ").upper()
peso = float(input("ingrese peso (kg): "))

tarifa = 0

if zona == "A":
    if peso <= 10:
        tarifa = 5.00
    else:
        tarifa = 12.00
elif zona == "B":
    if peso <= 10:
        tarifa = 7.00
    else:
        tarifa = 15.00
else:
    print("zona inválida")

if tarifa > 0:
    print(f"La tarifa es: ${tarifa: .2f}")