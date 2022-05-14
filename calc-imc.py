while True:
  print("CALCULADORA IMC")
  print(" ")

  # VALORES

  altura = float(input("INFORME UMA ALTURA: "))
  print(" ")
  peso = float(input("INFORME UM PESO: "))
  print(" ")

  # IMC

  imc = round(peso / altura ** 2, 2)
  print (f"SEU IMC É {imc}")

  # CALC

  if imc < 18.5:
    print("ABAIXO DO PESO")

  elif imc >= 18.5 and imc <= 24.9:
    print("PESO NORMAL")

  elif imc >= 25.0 and imc <= 29.9:
    print("SOBREPESO")

  elif imc >= 30.0 and imc <= 34.9:
    print("OBESIDADE GRAU I")

  elif imc >= 35.0 and imc <= 39.9:
    print("OBESIDADE GRAU II")

  elif imc >= 40.0 and imc > 40.0:
    print("OBESIDADE GRAU III OU MÓRBIDA")
    print(" ")

  # REPETIÇÃO

  print(" ")
  nova_calc = input("1/ NOVAMENTE 2/ SAIR: ")
  if nova_calc == '1':
    os.system('cls')

  elif nova_calc == '2':

    print("ATÉ MAIS")
    os.system('cls')
    break
