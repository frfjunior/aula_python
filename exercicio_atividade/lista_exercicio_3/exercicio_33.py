temperaturas = []

while True:
    valor = input("Digite uma temperatura (ou 'fim' para encerrar): ").strip().lower()
    if valor == "fim":
        break
    temperaturas.append(float(valor))

if len(temperaturas) == 0:
    print("Nenhuma temperatura informada.")
else:
    menor = min(temperaturas)
    maior = max(temperaturas)
    media = sum(temperaturas) / len(temperaturas)
    print(f"Menor temperatura: {menor:.2f}")
    print(f"Maior temperatura: {maior:.2f}")
    print(f"Média das temperaturas: {media:.2f}")
