import math

try:
    circle_radius = float(input('Digite o raio do circulo: não use virgula use ponto ex: 1.8: '))
    area_of_the_circle = math.pi * (circle_radius ** 2)

    print(f'A área do círculo é {round(area_of_the_circle, 2)}')
except:
    print('Erro\nDigite um número valido.')