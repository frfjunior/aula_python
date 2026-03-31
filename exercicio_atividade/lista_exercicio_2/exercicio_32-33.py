kg_morango = float(input("Quantos Kg de morango você comprou? "))
kg_maca = float(input("Quantos Kg de maçã você comprou? "))

preco_morango = 0
if kg_morango <= 5:
  preco_morango = kg_morango * 2.50
else:
  preco_morango = kg_morango * 2.20

preco_maca = 0
if kg_maca <= 5:
  preco_maca = kg_maca * 1.80
else:
  preco_maca = kg_maca * 1.50

preco_total = preco_morango + preco_maca
kg_total = kg_morango + kg_maca
valor_final = preco_total

if kg_total > 8 or preco_total > 25.00:
  valor_final = preco_total * 0.90

print(f"O valor final a ser pago é: R$ {valor_final:.2f}")