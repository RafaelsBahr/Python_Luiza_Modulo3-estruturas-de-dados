# """
# Exercício 4 — Menu do Álbum

# Desenvolva um programa que simule um álbum de figurinhas.

# Utilize uma lista para armazenar as figurinhas e exiba o seguinte menu:

# 1 - Adicionar figurinha
# 2 - Remover figurinha
# 3 - Buscar figurinha
# 4 - Mostrar álbum
# 5 - Encerrar

# O menu deve permanecer sendo exibido até que o usuário escolha a opção 5.

# Regras:

# Ao adicionar, a figurinha deve ser inserida no final da lista.
# Ao remover, informe caso a figurinha não exista.
# Na busca, informe se a figurinha está ou não no álbum.
# Ao mostrar o álbum, exiba todas as figurinhas utilizando um for.

# Desafio: utilize if, elif, else e while.
# """

lista_figurinhas = []
dicionario_acoes = {1: "Adicionar figurinha",
    2: "Remover figurinha",
    3: "Buscar figurinha",
    4: "Mostrar álbum",
    5: "Encerrar"
    }

while True:
    for chave, valor in dicionario_acoes.items():
        print(chave, "->", valor)
    acao_usuario = input("Digite o número da ação você quer fazer: ")
    try:
        acao_usuario = int(acao_usuario)
    except ValueError:
        print("Você não digitou um número válido.")
        continue
    if acao_usuario == 1:
        nova_figurinha = input("Qual o nome da nova figurinha? ")
        lista_figurinhas.append(nova_figurinha)
        print(f"Você adicionou a figurinha {nova_figurinha}.")
    elif acao_usuario == 2:
        try:
            remover_figurinha = input("Qual figurinha você quer remover? ")
            lista_figurinhas.remove(remover_figurinha)
            print(f"Você removeu a figurinha {remover_figurinha}.")
        except ValueError:
            print("Você tentou remover uma figurinha que não está no álbum")
    elif acao_usuario == 3:
        figurinha_pesquisada = input("Qual figurinha você quer buscar? ")
        if figurinha_pesquisada in lista_figurinhas:
            print(f"A figurinha {figurinha_pesquisada} está na lista.")
        else:
            print(f"A figurinha {figurinha_pesquisada} não está na lista.")
    elif acao_usuario == 4:
        if not lista_figurinhas:
            print("O álbum não tem nenhuma figurinha.")
        else:
            for figurinha in lista_figurinhas:
                print(figurinha)
    elif acao_usuario == 5:
        print("Encerrando programa.")
        break
    else:
        print("Tente novamente.")