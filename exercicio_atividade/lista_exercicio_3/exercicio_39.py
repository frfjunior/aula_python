salario = float(input("Digite o salário inicial (1995): R$ "))
ano_atual = int(input("Digite o ano atual: "))

while salario <= 0:
    salario = float(input("Salário inválido. Digite novamente: R$ "))
while ano_atual < 1995:
    ano_atual = int(input("Ano inválido. Digite um ano maior ou igual a 1995: "))

percentual = 0.015
for ano in range(1996, ano_atual + 1):
    salario += salario * percentual
    percentual *= 2

print(f"Salário em {ano_atual}: R$ {salario:.2f}")
