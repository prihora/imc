massa = float(input("Qual é o seu peso em kg? "))
altura = float(input("Qual é a a sua altura em metros? "))
imc = massa/(altura * altura)

resultado = print("O seu IMC é: %.2f" % imc,"kg/m²")
if imc < 18.5:
  print("Portanto, é classificado como: Magreza.")
elif imc >= 18.5 and imc <= 24.9:
  print("Portanto, é classificado como: Normal.")
elif imc >= 25 and imc <= 29.9:
  print("Portanto, é classificado como: Sobrepeso.")
elif imc >= 30 and imc <=34.9:
  print("Portanto, é classificado como: Obesidade grau I.")
elif imc >= 35 and imc <= 39.9:
  print("Portanto, é classificado como: Obesidade grau II.")
elif imc > 40:
  print("Portanto, é classificado como: Obesidade grau III.")