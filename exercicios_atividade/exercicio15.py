IR = 0.11
INSS = 0.08
SINDICATO = 0.05

def valor_desconto():
    valor_hora = float(input("Insira o valor da hora trabalhada: "))
    horas_trabalhadas = float(input("Insira o número de horas trabalhadas: "))
    salario_bruto = valor_hora * horas_trabalhadas
    desconto_ir = salario_bruto * IR
    desconto_inss = salario_bruto * INSS
    desconto_sindicato = salario_bruto * SINDICATO
    salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato
    print("Salário bruto: ", salario_bruto)
    print("Desconto INSS: ", desconto_inss)
    print("Desconto IR: ", desconto_ir)
    print("Desconto Sindicato: ", desconto_sindicato)
    print("Salário líquido: ", salario_liquido)