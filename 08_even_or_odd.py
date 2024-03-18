def even_or_odd(number):
    if number % 2 == 0:
        return print(f'{number} é par')
    return print(f'{number} é ímpar')

try:
    number = float(input('Digite um número: '))
    even_or_odd(number)
except:
    print('Erro...\nDigite apenas números...')
