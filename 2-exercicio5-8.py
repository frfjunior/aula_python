nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))

media_final = (nota_1 + nota_2) / 2


if media_final < 7:
    print("Reprovado")
elif media_final >= 7 and media_final < 10:
    print("Aprovado")
else:
    print("Aprovado com Distinção")