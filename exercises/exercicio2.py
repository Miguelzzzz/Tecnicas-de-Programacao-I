numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "zero"

bitTresLigado = bool(numero & (1 << 3))

if bitTresLigado:
    bit = "e o terceiro bit está ligado."
else:
    bit = "e o terceiro bit não está ligado."

print(f"O número é {paridade}, {sinal}, {bit}")