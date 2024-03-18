def value_and_weight():
    try:
        add_numbers = input('Quer adiconar novos números para calcular a media ponderada?: S para sim N para não ')
        add_numbers = add_numbers.upper()
        list_value_and_weight = []

        if add_numbers == 'S':
            while(add_numbers == 'S'):
                value = float(input('Digite um número: '))
                weight = float(input('Digite um peso para o número: '))
                list_value_and_weight.append([value, weight])
                
        else:
            print('Finalizando...')
    except:
        print('Erro...\nDigite apenas números...')