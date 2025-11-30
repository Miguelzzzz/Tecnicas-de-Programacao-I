produtos = {
    "arroz": (5.50, 20),
    "feijao": (7.20, 15),
    "massa": (4.80, 30),
    "frango": (6.90, 60),
}

nome = input("Digite o nome do produto: ").lower()

if nome in produtos:
    preco, estoque = produtos[nome]
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque} unidades")
    print(f"Valor total deste item em estoque: R$ {preco * estoque:.2f}")
else:
    print("Produto não encontrado.")

total = 0
for preco, quantidade in produtos.values():
    total += preco * quantidade

print()
print(f"Valor total dos itens no estoque: R$ {total:.2f}")