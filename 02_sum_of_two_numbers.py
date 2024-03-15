def sum_of_two_numbers(number_one, number_two):
    print(f'{number_one} + {number_two} = {number_one + number_two} ')

try:
    first_user_number = float(input('Digite um número: '))
    second_user_number = float(input('Digite outro número: '))

    sum_of_two_numbers(first_user_number, second_user_number)

except:
    print('Erro...\nValor inválido...')