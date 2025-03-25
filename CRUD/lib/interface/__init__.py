def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO. digite um numero inteiro.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mO usuario preferiu não digitar este numero. \033m[')
            return 0
        else:
            return n

def linha(tam = 50):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc
