divida = float(input("Digite o valor da dívida: R$ "))

while divida <= 0:
    divida = float(input("Valor inválido. Digite novamente: R$ "))

tabela = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]

print("Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
for parcelas, juros_percentual in tabela:
    juros_valor = divida * (juros_percentual / 100)
    valor_total = divida + juros_valor
    valor_parcela = valor_total / parcelas
    print(
        f"R$ {valor_total:10.2f} | "
        f"R$ {juros_valor:10.2f} | "
        f"{parcelas:22d} | "
        f"R$ {valor_parcela:10.2f}"
    )
