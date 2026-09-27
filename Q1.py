# """
# Exercício 1 — Cadastro de Figurinhas

# Você foi contratado para desenvolver um sistema simples para controlar um álbum de figurinhas da Copa do Mundo.

# O programa deve permitir que o usuário cadastre figurinhas até que ele digite a palavra "fim".

# Ao final, exiba:

# Todas as figurinhas cadastradas.
# A quantidade total de figurinhas.
# A primeira figurinha cadastrada.
# A última figurinha cadastrada.

# Desafio: não permita que o usuário cadastre uma figurinha vazia.
# """

lista_figurinhas = []

while True:
    nova_figurinha = input("Cadastre nova figurinha ou digite 'fim' para encerrar: ").strip()
    if nova_figurinha == "":
        print("O cadastro não pode ser em branco")
    elif nova_figurinha.lower() == "fim":
        if len(lista_figurinhas) == 0:
            print("A lista não pode ficar vazia.")
        else:
            break
    else:
        lista_figurinhas.append(nova_figurinha)

print(f"Todas as figurinhas cadastradas são: {lista_figurinhas}")
print(f"O total de figurinhas é {len(lista_figurinhas)}")
print(f"A primeira figurinha cadastrada é {lista_figurinhas[0]}")
print(f"A última figurinha cadastrada é {lista_figurinhas[-1]}")