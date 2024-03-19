def value_and_weight():
    try:

        add_numbers = input('Deseja adiconar números para calcular a media ponderada?: S para sim N para não ')
        add_numbers = add_numbers.upper()
        list_value_and_weight = []


        if add_numbers == 'S':
            while(add_numbers == 'S'):
                value = float(input('Digite um número: '))
                weight = float(input('Digite um peso para o número: '))
                list_value_and_weight.append([value, weight])
                add_numbers = input('Deseja adiconar outros números para calcular a media ponderada?: S para sim N para não ')
                add_numbers = add_numbers.upper()

        else:
            print('Finalizando...')

        return list_value_and_weight
    except:
        print('Erro...\nDigite apenas números...')

numbers_list = value_and_weight()

def weighted_average_calculation(numbers_list):
    sum_weight = 0
    sum_numbers_of_value_and_weight = 0
    numbers_list_multiplied = []

    for numbers in numbers_list:
        numbers_list_multiplied.append(numbers[0] * numbers[1])
        sum_weight += numbers[1]

    for numbers in numbers_list_multiplied:
        sum_numbers_of_value_and_weight += numbers

    answer = sum_numbers_of_value_and_weight / sum_weight

    return round(answer, 2)

answer_average = weighted_average_calculation(numbers_list)

def answer(number):
    if number > 0:
        print(f'O resultado da média ponderada é {number}')
answer(answer_average)
