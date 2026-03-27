vogais = ['a', 'e', 'i', 'o', 'u']

frase = "Lingua inglesa interessante"

contar_vogais = 0
for letra in frase:
    if letra.lower() in vogais:
        contar_vogais += 1
print(f"A frase contém {contar_vogais} vogais.")