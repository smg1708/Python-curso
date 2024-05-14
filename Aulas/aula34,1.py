"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = True

while condicao:
    nome = input('Qual seu nome: ')
    print(f'Seu nome é {nome}')
    if nome == ('Meggie'):
        print('Você entrou Miggui')
        break
    if nome == ('Violet'):
        print('Você entrou Vualit')
        break
    elif nome == ('sair'):
        print('Você saiu')
        break
    elif nome == ('Magnus'):
        print('Incorreto')
    