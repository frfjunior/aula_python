mais_alto = {"codigo": None, "altura": 0}
mais_baixo = {"codigo": None, "altura": float("inf")}
mais_gordo = {"codigo": None, "peso": 0}
mais_magro = {"codigo": None, "peso": float("inf")}

total_altura = 0
total_peso = 0
quantidade = 0

while True:
    codigo = int(input("Código do cliente (0 para encerrar): "))
    if codigo == 0:
        break

    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))

    quantidade += 1
    total_altura += altura
    total_peso += peso

    if altura > mais_alto["altura"]:
        mais_alto = {"codigo": codigo, "altura": altura}
    if altura < mais_baixo["altura"]:
        mais_baixo = {"codigo": codigo, "altura": altura}
    if peso > mais_gordo["peso"]:
        mais_gordo = {"codigo": codigo, "peso": peso}
    if peso < mais_magro["peso"]:
        mais_magro = {"codigo": codigo, "peso": peso}

if quantidade == 0:
    print("Nenhum cliente informado.")
else:
    print(f"Mais alto: código {mais_alto['codigo']} - {mais_alto['altura']:.2f} m")
    print(f"Mais baixo: código {mais_baixo['codigo']} - {mais_baixo['altura']:.2f} m")
    print(f"Mais gordo: código {mais_gordo['codigo']} - {mais_gordo['peso']:.2f} kg")
    print(f"Mais magro: código {mais_magro['codigo']} - {mais_magro['peso']:.2f} kg")
    print(f"Média das alturas: {total_altura / quantidade:.2f} m")
    print(f"Média dos pesos: {total_peso / quantidade:.2f} kg")
