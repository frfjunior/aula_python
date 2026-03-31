candidatos = {
    1: "Jose",
    2: "João",
    3: "Maria",
    4: "Ana",
}

votos_candidatos = {1: 0, 2: 0, 3: 0, 4: 0}
votos_nulos = 0
votos_brancos = 0
total_votos = 0

print("Digite 0 para finalizar a votação.")

while True:
    voto = int(input("Vote (1-4 candidato, 5 nulo, 6 branco): "))
    if voto == 0:
        break
    if voto in votos_candidatos:
        votos_candidatos[voto] += 1
        total_votos += 1
    elif voto == 5:
        votos_nulos += 1
        total_votos += 1
    elif voto == 6:
        votos_brancos += 1
        total_votos += 1
    else:
        print("Código inválido.")

for codigo, nome in candidatos.items():
    print(f"{codigo} - {nome}: {votos_candidatos[codigo]} votos")

print(f"Votos nulos: {votos_nulos}")
print(f"Votos em branco: {votos_brancos}")

if total_votos > 0:
    print(f"% nulos: {(votos_nulos / total_votos) * 100:.2f}%")
    print(f"% brancos: {(votos_brancos / total_votos) * 100:.2f}%")
else:
    print("Nenhum voto computado.")
