valor_hora = float(input("Quanto você ganha por hora? R$"))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * horas_trabalhadas

percentual_ir = 0
if salario_bruto > 2500:
    percentual_ir = 20
elif salario_bruto > 1500:
    percentual_ir = 10
elif salario_bruto > 900:
    percentual_ir = 5

desconto_ir = (salario_bruto * percentual_ir) / 100
desconto_sindicato = (salario_bruto * 3) / 100
fgts = (salario_bruto * 11) / 100
total_descontos = desconto_ir + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print(f"\nSalário Bruto      : R$ {salario_bruto:.2f}")
print(f"(-) IR ({percentual_ir}%)         : R$ {desconto_ir:.2f}")
print(f"(-) Sindicato (3%)   : R$ {desconto_sindicato:.2f}")
print(f"FGTS (11%)          : R$ {fgts:.2f}")
print(f"Total de descontos  : R$ {total_descontos:.2f}")
print(f"Salário Liquido     : R$ {salario_liquido:.2f}")