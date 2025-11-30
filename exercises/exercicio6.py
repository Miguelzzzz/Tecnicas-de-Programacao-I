def lerInteiros(arquivo):
    numeros = []
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                try:
                    n = int(linha.strip())
                    numeros.append(n)
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []
    
    return numeros

nomeArquivo = input("Digite o nome do arquivo: ")
nums = lerInteiros(nomeArquivo)

if nums:
    print("Soma:", sum(nums))
    print("Média:", sum(nums) / len(nums))
else:
    print("Nenhum número válido foi lido.")