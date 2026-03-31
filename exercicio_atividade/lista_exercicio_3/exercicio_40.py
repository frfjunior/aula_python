mais_alto_numero = None
mais_alto_altura = -1
mais_baixo_numero = None
mais_baixo_altura = float("inf")

for i in range(1, 11):
    numero_aluno = int(input(f"Digite o número do aluno {i}: "))
    altura = float(input(f"Digite a altura do aluno {i} (cm): "))

    if altura > mais_alto_altura:
        mais_alto_altura = altura
        mais_alto_numero = numero_aluno
    if altura < mais_baixo_altura:
        mais_baixo_altura = altura
        mais_baixo_numero = numero_aluno

print(f"Aluno mais alto: {mais_alto_numero} - {mais_alto_altura:.2f} cm")
print(f"Aluno mais baixo: {mais_baixo_numero} - {mais_baixo_altura:.2f} cm")
