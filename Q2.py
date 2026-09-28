# """
# Exercício 2 — Estatísticas da Partida

# Crie um programa que solicite ao usuário as seguintes informações de uma partida:

# Seleção mandante
# Seleção visitante
# Gols da seleção mandante
# Gols da seleção visitante

# Armazene essas informações em um dicionário.

# Depois:

# Exiba todas as informações utilizando um for com .items().
# Informe qual seleção venceu a partida.
# Caso os gols sejam iguais, informe que a partida terminou empatada.

# Desafio: utilize try/except para garantir que a quantidade de gols seja um número inteiro válido.
# """

selecao_mandante = input("Qual a seleção mandante? ")
selecao_visitante = input("Qual a seleção visitante? ")
while True:
    try:
        gols_mandante = int(input(f"Quantos gols fez o(a) {selecao_mandante}? "))
        if gols_mandante < 0:
            print("A quantidade de gols não pode ser negativa!")
        else:
            break
    except ValueError:
        print("Os gols devem ser um número inteiro")

while True:
    try:
        gols_visitante = int(input(f"Quantos gols fez o(a) {selecao_visitante}? "))
        if gols_visitante < 0:
            print("A quantidade de gols não pode ser negativa!")
        else:
            break
    except ValueError:
        print("Os gols devem ser um número inteiro")


dados_partida = {
    "selecao_mandante": selecao_mandante, 
    "selecao_visitante": selecao_visitante, 
    "gols_mandante": gols_mandante, 
    "gols_visitante": gols_visitante
    }

for chave, valor in dados_partida.items():
    print(f"{chave}: {valor}")

if dados_partida["gols_mandante"] > dados_partida["gols_visitante"]:
    print(f"{selecao_mandante} venceu a partida!")
elif dados_partida["gols_mandante"] < dados_partida["gols_visitante"]:
    print(f"{selecao_visitante} venceu a partida!")
else:
    print("A partida terminou empatada")