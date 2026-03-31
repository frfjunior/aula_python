dia = int(input("Digite o dia (dd): "))
mes = int(input("Digite o mês (mm): "))
ano = int(input("Digite o ano (aaaa): "))

data_valida = True

if mes < 1 or mes > 12 or ano <= 0:
  data_valida = False
elif mes in (1, 3, 5, 7, 8, 10, 12):
  if dia < 1 or dia > 31:
    data_valida = False
elif mes in (4, 6, 9, 11):
  if dia < 1 or dia > 30:
    data_valida = False
else:
  if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    if dia < 1 or dia > 29:
      data_valida = False
  else:
    if dia < 1 or dia > 28:
      data_valida = False

if data_valida:
  print(f"A data {dia}/{mes}/{ano} é válida.")
else:
  print(f"A data {dia}/{mes}/{ano} é inválida.")