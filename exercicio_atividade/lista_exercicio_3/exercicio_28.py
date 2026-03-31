quantidade_cds = int(input("Digite a quantidade de CDs: "))

while quantidade_cds <= 0:
    quantidade_cds = int(input("Valor inválido. Digite um número maior que 0: "))

total_investido = 0
for i in range(1, quantidade_cds + 1):
    valor = float(input(f"Digite o valor do CD {i}: R$ "))
    while valor < 0:
        valor = float(input("Valor inválido. Digite novamente: R$ "))
    total_investido += valor

media = total_investido / quantidade_cds
print(f"Valor total investido: R$ {total_investido:.2f}")
print(f"Valor médio por CD: R$ {media:.2f}")
