total_eleitores = int(input("Digite o número total de eleitores: "))

while total_eleitores <= 0:
    total_eleitores = int(input("Valor inválido. Digite um número maior que 0: "))

votos = [0, 0, 0]

for i in range(1, total_eleitores + 1):
    voto = int(input(f"Eleitor {i}, vote no candidato (1, 2 ou 3): "))
    while voto not in (1, 2, 3):
        voto = int(input("Voto inválido. Digite 1, 2 ou 3: "))
    votos[voto - 1] += 1

print(f"Votos candidato 1: {votos[0]}")
print(f"Votos candidato 2: {votos[1]}")
print(f"Votos candidato 3: {votos[2]}")
