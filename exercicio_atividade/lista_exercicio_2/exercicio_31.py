litros = float(input("Quantos litros foram vendidos? "))
tipo = input("Qual o tipo de combustível? (A-álcool, G-gasolina): ").upper()

preco_gasolina = 2.50
preco_alcool = 1.90
valor_a_pagar = 0

if tipo == 'A':
  valor_bruto = litros * preco_alcool
  if litros <= 20:
    valor_a_pagar = valor_bruto * 0.97
  else:
    valor_a_pagar = valor_bruto * 0.95
elif tipo == 'G':
  valor_bruto = litros * preco_gasolina
  if litros <= 20:
    valor_a_pagar = valor_bruto * 0.96
  else:
    valor_a_pagar = valor_bruto * 0.94
else:
    print("Tipo de combustível inválido!")

if valor_a_pagar > 0:
    print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")