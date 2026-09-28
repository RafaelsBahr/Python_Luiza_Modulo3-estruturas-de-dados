# """
# Desafio Final — Sistema da Copa do Mundo

# Desenvolva um programa para cadastrar partidas da Copa do Mundo.

# O programa deverá permanecer em execução até que o usuário decida encerrá-lo.

# Para cada partida, solicite:

# Seleção mandante
# Seleção visitante
# Gols da seleção mandante
# Gols da seleção visitante

# Cada partida deverá ser armazenada em um dicionário, e todos os dicionários deverão ser armazenados em uma lista.

# Ao finalizar o cadastro, exiba:

# A quantidade de partidas cadastradas.
# Todas as partidas registradas.
# Quantas partidas terminaram empatadas.
# A partida com o maior número total de gols.
# A média de gols por partida.

# Requisitos:

# Utilize listas e dicionários.
# Utilize while para controlar o cadastro.
# Utilize for para percorrer as partidas.
# Utilize if, elif e else para identificar o resultado de cada jogo.
# Utilize try/except para validar os gols informados.
# Utilize len() para calcular a quantidade de partidas cadastradas.
# """
n_partida = 0
lista_partidas = []

while True:
    n_partida += 1
    selecao_mandante = input(f"Qual a seleção mandante do jogo {n_partida}? ")
    while True:
        selecao_visitante = input(f"Qual a seleção visitante do jogo {n_partida}? ")
        if selecao_visitante.lower().strip() == selecao_mandante.lower().strip():
            print("As 2 seleções não podem ser iguais.")
        else:
            break
    while True:
        try:
            gols_mandante = int(input(f"Quantos gols a seleção {selecao_mandante} fez no jogo {n_partida}? "))
            if gols_mandante < 0:
                print("Placar não pode ser menor que zero.")
            else:
                break
        except ValueError:
            print("Preencher gols com número inteiro.")
    while True:
        try:
            gols_visitante = int(input(f"Quantos gols a seleção {selecao_visitante} fez no jogo {n_partida}? "))
            if gols_visitante < 0:
                print("Placar não pode ser menor que zero.")
            else:
                break
        except ValueError:
            print("Preencher gols com número inteiro.")
    dados_partida = {}
    dados_partida['n_partida'] = n_partida
    dados_partida['selecao_mandante'] = selecao_mandante
    dados_partida['selecao_visitante'] = selecao_visitante
    dados_partida['gols_mandante'] = gols_mandante
    dados_partida['gols_visitante'] = gols_visitante
    lista_partidas.append(dados_partida)
    encerrar = input("\nQuer encerrar lançamentos de partidas? ")
    if encerrar.lower().strip() == "sim" or encerrar.lower().strip() == "s":
        break

# A quantidade de partidas cadastradas.
if len(lista_partidas) == 1:
    print("A quantidade de partidas cadastradas foi 1")
else:
    print(f"A quantidade de partidas cadastradas foi: {len(lista_partidas)}")
      
# Todas as partidas registradas.
for partida in lista_partidas:
    print(f"{partida['selecao_mandante']} {partida['gols_mandante']} X {partida['gols_visitante']} {partida['selecao_visitante']}")
# Quantas partidas terminaram empatadas.
contador_empate = 0
for partida in lista_partidas:
    if partida['gols_mandante'] == partida['gols_visitante']:
        contador_empate += 1
print(f"{contador_empate} partida(s) empataram")

# A partida com o maior número total de gols.

lista_partidas_gols = []
for partida in lista_partidas:
    total_gols_por_partida = {}
    total_gols_da_partida = partida['gols_mandante'] + partida['gols_visitante']
    total_gols_por_partida['n_partida'] = partida['n_partida']
    total_gols_por_partida['total_gols_da_partida'] = total_gols_da_partida
    lista_partidas_gols.append(total_gols_por_partida)

maior_numero_gols = 0
lista_partidas_mais_gols = []
for partida in lista_partidas_gols:
    if partida['total_gols_da_partida'] > maior_numero_gols:
        maior_numero_gols = partida['total_gols_da_partida']
        lista_partidas_mais_gols=[]
        lista_partidas_mais_gols.append(partida['n_partida'])
    elif partida['total_gols_da_partida'] == maior_numero_gols:
        lista_partidas_mais_gols.append(partida['n_partida'])

if maior_numero_gols == 0:
    print("Nenhuma partida marcou gols.")
else:
    print(f"O maior número de gols foi {maior_numero_gols}. Foi na partida(s):")
    for partida in lista_partidas_mais_gols:
        for i in lista_partidas:
            if i['n_partida'] == partida:
                print(f"{i['selecao_mandante']} {i['gols_mandante']} X {i['gols_visitante']} {i['selecao_visitante']}")

# A média de gols por partida.
total_gols = 0
for partida in lista_partidas:
    total_gols += partida['gols_mandante']
    total_gols += partida['gols_visitante']
media = round(total_gols / len(lista_partidas), 3)
print(f"A média de gols por partida é: {media}.")