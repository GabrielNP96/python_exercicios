def triangle_area(number_1, number_2):
    triangle_area = (number_1 * number_2) / 2
    print(f'A área do triângulo é {round(triangle_area, 2)}')

try:
    base = float(input('Digite a base do triângulo: '))
    height = float(input('Digite a altura ddo triângulo: '))

    triangle_area(base, height)
except:
    print('Erro...\nDigite apenas números...')