n = int(input("Digite a quantidade de notas (N): "))

while n <= 0:
    n = int(input("Valor inválido. Digite N maior que 0: "))

soma = 0
for i in range(1, n + 1):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

media = soma / n
print(f"Média aritmética: {media:.2f}")
