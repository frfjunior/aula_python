quantidade_turmas = int(input("Digite a quantidade de turmas: "))

while quantidade_turmas <= 0:
    quantidade_turmas = int(input("Valor inválido. Digite um número maior que 0: "))

total_alunos = 0
for i in range(1, quantidade_turmas + 1):
    alunos = int(input(f"Quantidade de alunos da turma {i} (máximo 40): "))
    while alunos < 0 or alunos > 40:
        alunos = int(input("Valor inválido. Digite entre 0 e 40: "))
    total_alunos += alunos

media = total_alunos / quantidade_turmas
print(f"Média de alunos por turma: {media:.2f}")
