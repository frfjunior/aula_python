def galoes_necessarios(area):
    litros_necessarios = area / 6
    galoes = litros_necessarios / 3.6
    return galoes

def latas_necessarias(area):
    litros_necessarios = area / 6
    latas = litros_necessarios / 18
    return latas

def mistura_latas_galoes(area):
    litros_necessarios = area / 6
    litros_com_folga = litros_necessarios * 1.1
    latas = int(litros_com_folga / 18)
    litros_restantes = litros_com_folga - (latas * 18)
    galoes = int(litros_restantes / 3.6) + (1 if litros_restantes % 3.6 > 0 else 0)
    return latas, galoes

area_a_pintar = float(input("Insira o tamanho da área a ser pintada em metros quadrados: "))
galoes = galoes_necessarios(area_a_pintar)
latas = latas_necessarias(area_a_pintar)
latas_mistura, galoes_mistura = mistura_latas_galoes(area_a_pintar)
print("Quantidade de galões de 3,6 litros necessários: ", round(galoes, 2))
print("Quantidade de latas de 18 litros necessárias: ", round(latas, 2))
print("Quantidade de latas de 18 litros necessárias na mistura: ", round(latas_mistura, 2))
print("Quantidade de galões de 3,6 litros necessários na mistura: ", round(galoes_mistura, 2))