preco_pao = float(input("Preço do pão: R$ "))

while preco_pao <= 0:
    preco_pao = float(input("Valor inválido. Digite um preço maior que 0: R$ "))

print("Panificadora Pão de Ontem - Tabela de preços")
for i in range(1, 51):
    print(f"{i} - R$ {i * preco_pao:.2f}")
