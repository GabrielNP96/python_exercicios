def square_root(number):
    square_root_value = number ** 2
    print(f'A raiz quadrada de {number} é {round(square_root_value, 2)}')

try:
    user_number = float(input('Digite um número: '))
    square_root(user_number)
except:
    print('Erro...\nNúmero inválido...')