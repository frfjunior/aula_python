numero = int(input("Vou montar a tabuada de: "))
inicio = int(input("Começando em: "))
fim = int(input("Terminando em: "))

while fim < inicio:
    print("Obs: o final não pode ser menor que o inicial.")
    inicio = int(input("Começando em: "))
    fim = int(input("Terminando em: "))

print(f"\nTabuada de {numero} de {inicio} até {fim}:")
for i in range(inicio, fim + 1):
    print(f"{numero} X {i} = {numero * i}")
