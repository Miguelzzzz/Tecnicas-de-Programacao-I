# 🧩 Lista de Exercícios — Programação em Python

Versão com instruções completas para exercícios práticos que cobrem I/O, operadores, listas, funções, dicionários e tratamento de exceções.

## 🎯 Objetivo

Praticar a construção de pequenos programas completos, cada um abordando um tópico essencial de lógica e programação.

## ⚙️ Estrutura do arquivo

* Cada exercício traz:

  * Tópicos abordados
  * Requisitos funcionais
  * Exemplos de entradas/saídas quando aplicável

# 🧠 Exercício 1 — Conversor de Temperatura com Verificação

**Tópicos:** tipos de dados, I/O, operadores, `if`

### Requisitos

1. Peça ao usuário uma temperatura em **graus Celsius** (número real).
2. Converta para Fahrenheit usando a fórmula:

```text
F = C * 9/5 + 32
```

3. Mostre o valor em Fahrenheit (formatado com casas decimais a critério do implementador).
4. Se a temperatura em Celsius for menor que `0`, mostre também a mensagem:

> "Abaixo do ponto de congelamento da água."

# 🧠 Exercício 2 — Classificador de Número com Operações Lógicas e Bit a Bit

**Tópicos:** inteiros, operadores lógicos e bit a bit, condicionais

### Requisitos

1. Peça ao usuário um número inteiro.
2. Informe se o número é **par** ou **ímpar** (use `%`).
3. Informe se o número é **positivo**, **negativo** ou **zero**.
4. Verifique, usando operador bit a bit (`&`), se o **3º bit** (contando a partir de 0) está ligado.

   * Exemplo: `8` → binário `1000` → 3º bit ligado.

### Exemplo de saída

> "O número é par, positivo e o 3º bit está ligado."

# 🧠 Exercício 3 — Estatísticas de Notas com Listas

**Tópicos:** listas, laços, processamento de dados

### Requisitos

1. Leia notas (valores `float`) em loop até que o usuário digite `-1`.
2. Armazene as notas lidas em uma lista (não incluir o `-1`).
3. Ao final, mostre:

   * quantidade de notas digitadas
   * média das notas
   * maior e menor nota
4. Se nenhuma nota válida for informada, mostre uma mensagem dizendo que não há dados para calcular.

# 🧠 Exercício 4 — Função de Cálculo de IMC com Classificação

**Tópicos:** funções, valores booleanos, condicionais

### Requisitos

1. Implementar a função:

```python
def calcular_imc(peso: float, altura: float) -> float:
    """Retorna o IMC (peso / altura**2)."""
```

2. No programa principal:

   * Peça `peso` (kg) e `altura` (m) ao usuário.
   * Use `calcular_imc` para obter o IMC.
   * Mostre o IMC com duas casas decimais.
   * Classifique o IMC conforme as faixas:

| IMC             | Classificação  |
| --------------- | -------------- |
| < 18.5          | Abaixo do peso |
| 18.5 ≤ IMC < 25 | Peso normal    |
| 25 ≤ IMC < 30   | Sobrepeso      |
| ≥ 30            | Obesidade      |


# 🧠 Exercício 5 — Catálogo de Produtos com Dicionário e Tuplas

**Tópicos:** dicionários, tuplas, laços, processamento de listas

### Requisitos

1. Defina um dicionário onde a **chave** é o nome do produto e o **valor** é uma tupla `(preco, estoque)`.

Exemplo:

```python
produtos = {
    "arroz": (5.50, 20),
    "feijao": (7.20, 15),
}
```

2. Peça ao usuário o nome de um produto.
3. Se o produto existir, mostre:

   * preço
   * quantidade em estoque
4. Caso não exista, mostre mensagem apropriada.
5. Percorra o dicionário e mostre o **valor total em estoque** (soma de `preco * estoque`).


# 🧠 Exercício 6 — Leitura de Arquivo com Tratamento de Exceções

**Tópicos:** I/O, exceções, funções

### Requisitos

1. Implemente a função:

```python
def ler_inteiros(arquivo: str) -> list[int]:
    """Lê inteiros de um arquivo (um por linha). Retorna lista de inteiros válidos."""
```

2. A função deve:

   * receber o nome de um arquivo texto
   * tentar abrir o arquivo dentro de `try/except`
   * ler linha a linha e converter para `int`
   * ignorar linhas que não puderem ser convertidas (sem interromper o processamento)
   * se o arquivo não existir, exibir uma mensagem amigável e retornar lista vazia

3. No programa principal, após chamar `ler_inteiros`, calcule e mostre:

   * a soma dos inteiros lidos
   * a média (somente se a lista não estiver vazia)