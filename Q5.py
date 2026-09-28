# """
# Exercício 5 — Ranking de Artilheiros

# Crie uma lista de dicionários para armazenar informações de jogadores.

# O programa deverá perguntar quantos jogadores o usuário deseja cadastrar.

# Para cada jogador, solicite:

# Nome
# Seleção
# Quantidade de gols

# Cada jogador deverá ser armazenado como um dicionário dentro da lista.

# Ao final:

# Exiba todos os jogadores cadastrados.
# Informe qual jogador marcou mais gols.
# Informe a média de gols dos jogadores cadastrados.

# Desafio: utilize try/except para validar a quantidade de gols informada pelo usuário.
# """
while True:
    try:
        qtd_jogadores = int(input("Quantos jogadores você deseja cadastrar? "))
        if qtd_jogadores <= 0:
            print("Quantidade de jogadores não pode ser menor ou igual a zero.\n")
        else:
            break
    except ValueError:
        print("Quantidade de jogadores deve ser um número inteiro.\n")
lista_jogadores = []

for i in range(qtd_jogadores):
    dados_jogador = {}
    dados_jogador["nome"] = input(f"Qual o nome do {i+1}º jogador? ")
    dados_jogador["selecao"] = input(f"Qual a seleção do {dados_jogador['nome']}? ")
    while True:
        try:
            dados_jogador["qtd_gols"] = int(input(f"Qual a quantidade de gols do {dados_jogador['nome']}? "))
            if dados_jogador["qtd_gols"] < 0:
                print("Quantidade de gols não pode ser menor que zero.\n")
            else:
                break
        except ValueError:
            print("Quantidade de gols deve ser um número inteiro.\n")
    lista_jogadores.append(dados_jogador)
    print(f"{i+1}º jogador, {dados_jogador['nome']} cadastrado!\n")

# Exiba todos os jogadores cadastrados.
print("\nLista com todos os jogadores cadastrados:")
for jogador in lista_jogadores:
    print(jogador['nome'], jogador['selecao'], jogador['qtd_gols'])

# Informe qual jogador marcou mais gols.
melhores_jogadores = []
qtd_gols_melhores_jogadores = 0
for jogador in lista_jogadores:
    if jogador['qtd_gols'] == qtd_gols_melhores_jogadores:
        melhores_jogadores.append(jogador['nome'])
    elif jogador['qtd_gols'] > qtd_gols_melhores_jogadores:
        melhores_jogadores = []
        melhores_jogadores.append(jogador['nome'])
        qtd_gols_melhores_jogadores = jogador['qtd_gols']

if qtd_gols_melhores_jogadores == 0:
    print("\nNenhum jogador marcou nenhum gol.")
else:
    print(f"\nJogador(es) com mais gols: {', '.join(melhores_jogadores)}")


# Informe a média de gols dos jogadores cadastrados.
total_gols = 0
for jogador in lista_jogadores:
    total_gols += jogador['qtd_gols']
print(f"O total de gols é {total_gols}.")
media = round(total_gols / len(lista_jogadores), 3)
print(f"A média de gols por jogador é: {media}")