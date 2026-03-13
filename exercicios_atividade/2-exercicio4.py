letra = str(input("Digite uma letra: "))

if letra in 'aeiouAEIOU':
        print("A letra é uma vogal.")
elif letra.isalpha():
        print("A letra é uma consoante.")
else:   print("Você não digitou uma letra válida.")