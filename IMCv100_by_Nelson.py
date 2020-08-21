print('-----CALCULADORA DE IMC-----')
altura = float(input('Digite a sua altura (em metros): '))
peso = float(input('Digite o seu peso (em quilos): '))

imc = peso / altura**2

print('O seu IMC é: {}'.format(imc))

if imc < 18.5:
    print('Seu peso está abaixo do recomendado. Procure um nutricionista!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso recomendado, parabéns!')
elif imc >= 25 and imc < 30:
    print('Você está em pré-obesidade, precisa emagrecer.')
elif imc >= 30 and imc < 35:
    print('Você está em Obesidade nível 1, procure seu médico.')
elif imc >= 35 and imc < 40:
    print('Você está com Obesidade nível 2, procure seu médico urgentemente!')
else:
    print('Você está com obesidade nível 3, procure seu médico... Pra ontem!!!')