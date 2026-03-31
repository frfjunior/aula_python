faixa_0_25 = 0
faixa_26_50 = 0
faixa_51_75 = 0
faixa_76_100 = 0

while True:
    numero = float(input("Digite um número positivo (negativo para encerrar): "))
    if numero < 0:
        break

    if 0 <= numero <= 25:
        faixa_0_25 += 1
    elif 26 <= numero <= 50:
        faixa_26_50 += 1
    elif 51 <= numero <= 75:
        faixa_51_75 += 1
    elif 76 <= numero <= 100:
        faixa_76_100 += 1

print(f"[0-25]: {faixa_0_25}")
print(f"[26-50]: {faixa_26_50}")
print(f"[51-75]: {faixa_51_75}")
print(f"[76-100]: {faixa_76_100}")
