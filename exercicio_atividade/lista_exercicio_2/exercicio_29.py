num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação deseja realizar? (+, -, *, /): ")

resultado = 0
calculou_com_sucesso = True

if operacao == '+':
  resultado = num1 + num2
elif operacao == '-':
  resultado = num1 - num2
elif operacao == '*':
  resultado = num1 * num2
elif operacao == '/':
  resultado = num1 / num2
else:
  print("Operação inválida!")
  calculou_com_sucesso = False

if calculou_com_sucesso:
    print(f"\nO resultado da operação é: {resultado}")
    if resultado % 2 == 0:
      print("- É um número par.")
    else:
      print("- É um número ímpar.")
    if resultado >= 0:
      print("- É um número positivo.")
    else:
      print("- É um número negativo.")
    if resultado == round(resultado):
      print("- É um número inteiro.")
    else:
      print("- É um número decimal.")