def average(user_number_list):
    numbers_sum = 0
    for number in user_number_list:
        numbers_sum += number
    
    average = numbers_sum / 3

    print(f'A média é {round(average, 2)}')

user_numbers = []

try:
    number_one = float(input('Digite um número: '))
    number_two = float(input('Digite outro número: '))
    number_three = float(input('Digite um último número número: '))
except:
    print('Erro...\nValor não é um número...')

user_numbers.append(number_one)
user_numbers.append(number_two)
user_numbers.append(number_three)

average(user_numbers)