print("Tipos de carne: File Duplo, Alcatra, Picanha")
tipo_carne = input("Qual tipo de carne você quer? ").lower()
quantidade_kg = float(input("Quantos quilos? "))
pagamento_cartao = input("Pagamento com cartão Tabajara? (sim/nao) ").lower()

preco_por_kg = 0
nome_carne = ""
carne_valida = True

if tipo_carne == "file duplo":
    nome_carne = "File Duplo"
    if quantidade_kg <= 5:
        preco_por_kg = 4.90
    else:
        preco_por_kg = 5.80
elif tipo_carne == "alcatra":
    nome_carne = "Alcatra"
    if quantidade_kg <= 5:
        preco_por_kg = 5.90
    else:
        preco_por_kg = 6.80
elif tipo_carne == "picanha":
    nome_carne = "Picanha"
    if quantidade_kg <= 5:
        preco_por_kg = 6.90
    else:
        preco_por_kg = 7.80
else:
    print("Tipo de carne inválido!")
    carne_valida = False

if carne_valida:
    preco_total = quantidade_kg * preco_por_kg
    valor_desconto = 0
    tipo_pagamento = "Outro"

    if pagamento_cartao == 'sim':
        valor_desconto = preco_total * 0.05
        tipo_pagamento = "Cartão Tabajara"

    valor_a_pagar = preco_total - valor_desconto

    print("\n--- Cupom Fiscal ---")
    print(f"Carne: {nome_carne}")
    print(f"Quantidade: {quantidade_kg} Kg")
    print(f"Preço total: R$ {preco_total:.2f}")
    print(f"Tipo de pagamento: {tipo_pagamento}")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")