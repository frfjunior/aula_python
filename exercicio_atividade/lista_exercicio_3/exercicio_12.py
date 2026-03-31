while True:
    numero = int(input("Digite um número inteiro entre 1 e 10: "))
    if 1 <= numero <= 10:
        break
    print("Valor inválido.")

print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")
