while True:
    nome = input("Nome (mais de 3 caracteres): ").strip()
    if len(nome) > 3:
        break
    print("Nome inválido.")

while True:
    idade = int(input("Idade (0 a 150): "))
    if 0 <= idade <= 150:
        break
    print("Idade inválida.")

while True:
    salario = float(input("Salário (maior que 0): "))
    if salario > 0:
        break
    print("Salário inválido.")

while True:
    sexo = input("Sexo ('f' ou 'm'): ").strip().lower()
    if sexo in ("f", "m"):
        break
    print("Sexo inválido.")

while True:
    estado_civil = input("Estado civil ('s', 'c', 'v', 'd'): ").strip().lower()
    if estado_civil in ("s", "c", "v", "d"):
        break
    print("Estado civil inválido.")

print("Dados válidos informados com sucesso.")
