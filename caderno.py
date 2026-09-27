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

autores_gols = [
    "Vini Jr.",
    "Rodrygo",
    "Vini Jr.",
]

quantidade_gols = len(autores_gols)

# print(quantidade_gols)

jogadores_que_marcaram_gols = set(autores_gols)

# print(f"quantos jogadores marcaram gols? {len(jogadores_que_marcaram_gols)}")

gols_por_jogador = {}
for jogador in autores_gols:
    if jogador not in gols_por_jogador:
        gols_por_jogador[jogador] = 1
    else:
        gols_por_jogador[jogador] += 1
# print(gols_por_jogador)

for jogador in gols_por_jogador:
    print(jogador)