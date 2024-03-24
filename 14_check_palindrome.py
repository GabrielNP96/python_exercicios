def check_palindrome(str):

    list_str = list(str)
    list_str.reverse()

    reverse_str = ''.join(list_str)

    if reverse_str == str:
        print(f'A palavra {str} é um palíndromo')
    else:
        print(f'A palavra {str} não é um palíndromo')

string = input('Digite uma palavra: ')

try:
    if float(string) or int(string):
        print('Erro...\nVocê digitou números')
except:
    check_palindrome(string)