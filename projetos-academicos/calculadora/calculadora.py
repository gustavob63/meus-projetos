a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print(f"1- Soma\n2- Subtração\n3- Divisão\n4- Multiplicação")

operação = int(input("Qual o código da operação?: "))
if operação == 1 :
    print(a + b)
elif operação == 2 :
    print(a - b)
elif operação == 3 :
    print(a / b)
elif operação == 4 :
    print(a * b)
else:
    print("Código inválido")