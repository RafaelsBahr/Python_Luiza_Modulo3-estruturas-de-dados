# x = ["a", "b", 55, 20]

# print(x[-2])
# print(x[3])

# y = ("a", "b", 55, 20)
# z = "a", "b", 55, 20

# print(type(y))
# print(type(z))

# a = {10, 5, 10, 8}
# print(a)

# jogadores = [
#     "Alisson",
#     "Marquinhos",
#     "Gabriel Magalhães",
#     "Bruno Guimarães",
#     "Raphinha",
#     "Rodrygo",
#     "Vini Jr.",
# ]

# for indice, jogador in enumerate(jogadores):
#     print(f" - {jogador} | Posição: {indice}")

# autores_gols = [
#     "Vini Jr.",
#     "Rodrygo",
#     "Vini Jr.",
# ]

# quantidade_gols = len(autores_gols)

# print(quantidade_gols)

# jogadores_que_marcaram_gols = set(autores_gols)

# print(f"quantos jogadores marcaram gols? {len(jogadores_que_marcaram_gols)}")

# gols_por_jogador = {}
# for jogador in autores_gols:
#     if jogador not in gols_por_jogador:
#         gols_por_jogador[jogador] = 1
#     else:
#         gols_por_jogador[jogador] += 1
# print(gols_por_jogador)

# for jogador in gols_por_jogador:
#     print(jogador)


# x = {10, 11, 10, 12}
# print(type(x))
# print(x)
# print(len(x))

lista_jogadores = [{'nome': 'Rafael', 'Seleção': 'Brasil', 'Quantidade de gols': 3}, {'nome': 'Sabrina', 'Seleção': 'USA', 'Quantidade de gols': 3}, {'nome': 'Gustavo', 'Seleção': 'China', 'Quantidade de gols': 2}]

# print(x[0]['nome'])

# for jogador in lista_jogadores:
#     print(jogador['nome'])

# total_gols = 0
# for jogador in lista_jogadores:
#     total_gols += jogador['Quantidade de gols']
# print(total_gols)

melhor_jogador = []
qtd_gols_melhor_jogador = 0
for jogador in lista_jogadores:
    if jogador['Quantidade de gols'] >= qtd_gols_melhor_jogador:
        melhor_jogador.append(jogador['nome'])
        qtd_gols_melhor_jogador = jogador['Quantidade de gols']

if melhor_jogador
for jogador in melhor_jogador:
    print
print(melhor_jogador)