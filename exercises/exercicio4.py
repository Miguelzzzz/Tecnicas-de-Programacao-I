def calcularImc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = calcularImc(peso, altura)
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")