# """
# Exercício 3 — Seleções Classificadas

# Durante a fase de grupos, várias seleções foram sendo classificadas.

# Peça ao usuário para informar o nome de 8 seleções.

# Armazene essas seleções em um set.

# Ao final:

# Exiba todas as seleções classificadas.
# Informe quantas seleções diferentes foram cadastradas.

# Depois pergunte ao usuário o nome de uma seleção e informe se ela está classificada utilizando o operador in.

# Desafio: explique por que, mesmo digitando uma seleção repetida, ela aparece apenas uma vez no conjunto.
# """

selecoes_classificadas = set()

for i in range(8):
    selecao_em_registro = input("Digite uma nova seleção classificada: ")
    selecoes_classificadas.add(selecao_em_registro)
print(selecoes_classificadas)
print(f"Foram cadastradas {len(selecoes_classificadas)} seleções diferentes.")

teste_classificadas = input("Digite uma seleção para saber se foi classificada: ")
if teste_classificadas in selecoes_classificadas:
    print(f"A seleção {teste_classificadas} foi classificada!")
else:
    print(f"A seleção {teste_classificadas} não foi classificada!")

# Resposta desafio: Porque a classe set não aceita objetos repetidos dentro dela.