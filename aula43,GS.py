""" Gerenciador de senhas """
começo = input(f'crie uma senha: ')
senha_salva = começo
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    
    repeticoes += 1
    if repeticoes >5:
        print('Você excedeu o limite de tentativas')
        break
    elif senha_digitada != senha_salva:
        print('Senha incorreta')
    elif senha_digitada == senha_salva:
        print('Senha correta, carregando')

