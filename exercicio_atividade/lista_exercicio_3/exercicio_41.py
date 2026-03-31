maior_indice = -1
menor_indice = float("inf")
cidade_maior = None
cidade_menor = None

total_veiculos = 0
acidentes_menos_2000 = 0
qtd_cidades_menos_2000 = 0

for i in range(1, 6):
    codigo = input(f"Código da cidade {i}: ").strip()
    veiculos = int(input("Número de veículos de passeio: "))
    acidentes = int(input("Número de acidentes com vítimas: "))

    while veiculos <= 0 or acidentes < 0:
        print("Dados inválidos. Informe novamente.")
        veiculos = int(input("Número de veículos de passeio: "))
        acidentes = int(input("Número de acidentes com vítimas: "))

    indice = acidentes / veiculos
    total_veiculos += veiculos

    if indice > maior_indice:
        maior_indice = indice
        cidade_maior = codigo
    if indice < menor_indice:
        menor_indice = indice
        cidade_menor = codigo

    if veiculos < 2000:
        acidentes_menos_2000 += acidentes
        qtd_cidades_menos_2000 += 1

print(f"Maior índice de acidentes: {maior_indice:.4f} (cidade {cidade_maior})")
print(f"Menor índice de acidentes: {menor_indice:.4f} (cidade {cidade_menor})")
print(f"Média de veículos nas 5 cidades: {total_veiculos / 5:.2f}")

if qtd_cidades_menos_2000 > 0:
    media_acidentes = acidentes_menos_2000 / qtd_cidades_menos_2000
    print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes:.2f}")
else:
    print("Nenhuma cidade com menos de 2000 veículos.")
