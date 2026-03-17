# Remova o primeiro elemento da lista do exercício 1, o último
# da segunda lista e o elemento do meio da terceira lista. Depios
# exiba na tela.


import exercicio_1 as lista_nome
import exercicio_2 as lista_numero
import exercicio_3 as fruta

print("Listas Originais:")
print(f"Nomes: {lista_nome.lista_nome}")
print(f"Números: {lista_numero.lista_numero}")
print(f"Frutas: {fruta.lista_frutas}")
print("-" * 20) 


primeiro_nome_removido = lista_nome.lista_nome.pop(0)
print(f"Removido da lista de nomes: {primeiro_nome_removido}")

ultimo_numero_removido = lista_numero.lista_numero.pop()
print(f"Removido da lista de números: {ultimo_numero_removido}")

indice_meio = len(fruta.lista_frutas) // 2
fruta_meio_removida = fruta.lista_frutas.pop(indice_meio)
print(f"Removido da lista de frutas: {fruta_meio_removida}")
print("-" * 20)

# --- Exibe as listas modificadas na tela ---
print("Listas Modificadas:")
print(f"Nomes: {lista_nome.lista_nome}")
print(f"Números: {lista_numero.lista_numero}")
print(f"Frutas: {fruta.lista_frutas}")