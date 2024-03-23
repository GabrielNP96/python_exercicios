def factorial(number):
    arr_numbers = []
    i = number
    while(i > 0):
        arr_numbers.append(i)
        i -= 1
        
    product = 1
    for number in arr_numbers:
        product *= number
    
    print(f'O fatorial de {arr_numbers[0]} é {round(product, 2)}')

try:
    user_number = float(input('Digite um número para calcular o fatorial: '))
    factorial(user_number)
except:
    print('Erro...\n Você não digitou um número.')