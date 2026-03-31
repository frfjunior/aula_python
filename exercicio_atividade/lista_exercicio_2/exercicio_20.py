lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
  print("Os lados podem formar um triângulo.")
  if lado1 == lado2 and lado2 == lado3:
    print("É um Triângulo Equilátero.")
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("É um Triângulo Isósceles.")
  else:
    print("É um Triângulo Escaleno.")
else:
  print("Os lados NÃO podem formar um triângulo.")