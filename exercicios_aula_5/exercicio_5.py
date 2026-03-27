precos = [10.50, 150.00, 45.00, 210.90, 85.00, 300.00]
produtos_premium = []
for preco in precos:
    if preco > 100.00:
        produtos_premium.append(preco)
print("Produtos premium:", produtos_premium)
