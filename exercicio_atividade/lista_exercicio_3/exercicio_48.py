nome = input("Atleta: ").strip()
while nome == "":
    nome = input("Nome inválido. Digite o nome do atleta: ").strip()

notas = []
for i in range(1, 8):
    nota = float(input(f"Nota {i}: "))
    notas.append(nota)

melhor = max(notas)
pior = min(notas)
media = (sum(notas) - melhor - pior) / 5

print("\nResultado final:")
print(f"Atleta: {nome}")
print(f"Melhor nota: {melhor:.1f}")
print(f"Pior nota: {pior:.1f}")
print(f"Média: {media:.2f}")
