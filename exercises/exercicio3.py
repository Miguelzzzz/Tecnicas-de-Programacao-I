notas = []

while True:
    valor = float(input("Digite uma nota (-1 para sair): "))
    if valor == -1:
        break
    notas.append(valor)

if len(notas) == 0:
    print("Nenhuma nota válida foi informada.")
else:
    print("Quantidade de notas:", len(notas))
    print("Média:", sum(notas) / len(notas))
    print("Maior nota:", max(notas))
    print("Menor nota:", min(notas))