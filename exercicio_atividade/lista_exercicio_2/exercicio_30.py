print("Responda as perguntas com 'sim' ou 'nao'.")

respostas_positivas = 0

resposta = input("Telefonou para a vítima? ").lower()
if resposta == 'sim':
  respostas_positivas += 1

resposta = input("Esteve no local do crime? ").lower()
if resposta == 'sim':
  respostas_positivas += 1

resposta = input("Mora perto da vítima? ").lower()
if resposta == 'sim':
  respostas_positivas += 1

resposta = input("Devia para a vítima? ").lower()
if resposta == 'sim':
  respostas_positivas += 1

resposta = input("Já trabalhou com a vítima? ").lower()
if resposta == 'sim':
  respostas_positivas += 1

print("\nClassificação:")
if respostas_positivas == 5:
  print("Assassino")
elif respostas_positivas >= 3:
  print("Cúmplice")
elif respostas_positivas == 2:
  print("Suspeita")
else:
  print("Inocente")