print("Informe o gabarito da prova (10 questões).")
gabarito = []
for i in range(1, 11):
    resposta = input(f"Gabarito da questão {i} (A-E): ").strip().upper()
    while resposta not in ("A", "B", "C", "D", "E"):
        resposta = input("Resposta inválida. Digite A, B, C, D ou E: ").strip().upper()
    gabarito.append(resposta)

maior_acerto = -1
menor_acerto = 11
total_alunos = 0
soma_notas = 0

while True:
    print("\nRespostas do aluno:")
    acertos = 0
    for i in range(1, 11):
        resposta = input(f"Questão {i} (A-E): ").strip().upper()
        while resposta not in ("A", "B", "C", "D", "E"):
            resposta = input("Resposta inválida. Digite A, B, C, D ou E: ").strip().upper()
        if resposta == gabarito[i - 1]:
            acertos += 1

    total_alunos += 1
    soma_notas += acertos
    if acertos > maior_acerto:
        maior_acerto = acertos
    if acertos < menor_acerto:
        menor_acerto = acertos

    continuar = input("Outro aluno vai utilizar o sistema? (s/n): ").strip().lower()
    if continuar != "s":
        break

print(f"\nMaior acerto: {maior_acerto}")
print(f"Menor acerto: {menor_acerto}")
print(f"Total de alunos: {total_alunos}")
print(f"Média das notas da turma: {soma_notas / total_alunos:.2f}")
