n = int(input("Digite a quantidade de pessoas: "))

while n <= 0:
    n = int(input("Valor inválido. Digite um número maior que 0: "))

soma_idades = 0
for i in range(1, n + 1):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    while idade < 0:
        idade = int(input("Idade inválida. Digite novamente: "))
    soma_idades += idade

media = soma_idades / n
if media <= 25:
    turma = "jovem"
elif media <= 60:
    turma = "adulta"
else:
    turma = "idosa"

print(f"Média de idade: {media:.2f}")
print(f"A turma é {turma}.")
