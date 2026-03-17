primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

divisao_numero = primeiro_numero / segundo_numero

resto_divisao = primeiro_numero % segundo_numero
resultado_par = primeiro_numero * segundo_numero
resultado_impar = primeiro_numero + segundo_numero

if resto_divisao == 0:
    pass
elif resto_divisao // 2 == 0:
    print(f"O resultado da multiplicação é: {resultado_par}")
else:
    print(f"O resultado da soma é: {resultado_impar}")