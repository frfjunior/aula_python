base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente (inteiro não negativo): "))

while expoente < 0:
    expoente = int(input("Expoente inválido. Digite um inteiro não negativo: "))

resultado = 1
for _ in range(expoente):
    resultado *= base

print(f"{base} elevado a {expoente} = {resultado}")
