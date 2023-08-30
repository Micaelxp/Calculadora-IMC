nome = input ("Digite seu nome")
peso = input ("DIgite seu peso")
altura = input ("Digite sua altura em Cm: ")
alturaMetros = float (altura) / 100
imc =  float (peso) / (float(alturaMetros) * float (alturaMetros)) 
if imc < 18.49:
    print(f'{nome}, seu imc e: {imc:.2f}, Seu imc está abaixo do peso')
elif imc >= 18.5 or imc<= 24.5:
   print(f'{nome}, seu imc e: {imc:.2f}, Seu imc está normal')
else:
    print(f'{nome}, seu imc e: {imc:.2f}, Seu imc está acima do peso')
print ("Parabéns por se preocupar com sua saúde!!!")