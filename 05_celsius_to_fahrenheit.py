def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}° = {round(fahrenheit, 2)}°')

try:
    celsius = float(input('Digite a quantidade de Celsius para converter para Fahrenheit: '))
    celsius_to_fahrenheit(celsius)
except:
    print('Erro...\nO valor não é um número.')