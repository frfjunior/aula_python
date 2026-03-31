a, b = 0, 1
serie = []

while a <= 500:
    serie.append(a)
    a, b = b, a + b

print("Série de Fibonacci até passar de 500:")
print(*serie, sep=", ")
