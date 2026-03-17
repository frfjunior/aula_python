# Crie uma lista que armazene 10 nomes de pessoas e depois
# exiba na tela somente os nomes cujos indices sejam impares.


lista_nome = ["João", "Maria", "Pedro", "Ana", "Carlos", "Fernanda", "Lucas", "Sofia", "Rafael", "Isabela"]

nome_indice_impar = [1, 3, 5, 7, 9]

print("Nomes nos índices ímpares:")
for indice in nome_indice_impar:
    print(lista_nome[indice])
