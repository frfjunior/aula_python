numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

while fim < inicio:
    print("Valor final não pode ser menor que o inicial.")
    inicio = int(input("Começar por: "))
    fim = int(input("Terminar em: "))

for i in range(inicio, fim + 1):
    print(f"{numero} X {i} = {numero * i}")
