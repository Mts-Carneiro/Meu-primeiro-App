import pandas as pd

xls = pd.read_excel("Lista de Compras uramaki.xlsx", skiprows=1, usecols=[0, 1, 2, 3, 4, 5, 6])
"""Nesta parte ficará a lista de itens e o estoque estoque minimoEx: Arroz(Item): 10(Nº do estoque minimo)"""

lista_compra = []
"""Nesta lista será salva os itens que estão em estoque baixo"""


def add_item(lista_para_item):
    """Função que adiciona um item a lista de compra"""

    item_adic = str(input('Informe o nome do item a ser adicionado: '))
    item_est = int(input(f'Informe o estoque minimo para {item_adic}: '))
    lista_para_item[item_adic] = item_est
    print(f'O item {item_adic} foi adicionado!')


def make_list(none):
    """Função que faz a lista de compras"""
    lista = open('listacompras.txt', 'w+')
    for cell in range(0, 147):
        estoque_medio = float(f' {(xls["E.M."][cell])} ')
        estoque_real = float(input(f'Insira a quantidade do item {(xls["Item"][cell])}(Referencia de medida: '
                                   f'{(xls["Medida"][cell])}): '))
        if estoque_real < estoque_medio:
            lista.write(xls["Item"][cell])

    lista.close()


def menu(lista_itens):
    """Função para Menu"""

    texto_menu = 'APP LISTA URAMKI PRIME'
    tt = int(len(texto_menu) + 6)
    print(f'-' * tt)
    print(f'{texto_menu:^{tt}}')
    print(f'-' * tt)
    print(f'=' * tt)
    print(f'{"Menu":^{tt}}')
    print('1 - Fazer a lista de compras')
    print('2 - Adicionar um item na lista')
    print('9 - Fechar o App')

    while True:
        print('')
        escolha = int(input('O que deseja fazer hoje?: '))

        if escolha == 1:
            make_list(lista_itens)

        elif escolha == 2:
            add_item(lista_itens)

        elif escolha == 9:
            print('Obrigado e ate a proxima!')

            break


menu(xls)

print(xls)
