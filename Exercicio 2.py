print('|'.ljust(5)+'°Conversão Celsius para Fahrenheit ou Fahrenheit para Celsius°')
print('|')
print('|'.ljust(2)+'Digite C para Celcius e F para Fahrenheit!')
Escolha=str(input('|'.ljust(2)+'Qual Conversão necessita fazer?(C/F): '))
if Escolha =='C' or Escolha =='c':
    Celsius=int(input('|'.ljust(2)+'Informe a Temperatura em Celsius: '))
    Fahrenheit= ((Celsius*9)/5 +32)
    if Celsius > 50:
        print('|'.ljust(2)+'🔥Chame os Bombeiro Ramal 193🔥')
    if Fahrenheit!=0:
        print('|'.ljust(2)+f'Sua Temperatura Convertida para Fahrenheit: {Fahrenheit}°F')
elif Escolha =='F'or Escolha=='f':
    Fahrenheit=int(input('|'.ljust(2)+'Informe sua Temperatura em Fahrenheit: '))
    Celsius=((Fahrenheit-32)*5/9)
    print('|'.ljust(2)+f'Sua Temperatura convertida em Celsius:{Celsius}°C ')