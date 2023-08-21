print('-' * 40)
print('Calculando IMC')
print('-' * 40)
#Cabeçalho

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 24.9:
    print('Peso ideal')
elif imc < 29.9:
    print('Acima do peso')
elif imc < 34.9:
    print('Obesidade nível 1')
elif imc < 39.9:
    print('Obesidade nível 2')
else:
    print('Obesidade nível 3')
