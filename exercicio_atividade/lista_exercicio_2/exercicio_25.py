nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Sua média foi: {media:.2f}")

if media == 10:
  print("Aprovado com Distinção")
elif media >= 7:
  print("Aprovado")
else:
  print("Reprovado")