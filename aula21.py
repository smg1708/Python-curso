# Operadores lógicos
# and (e) or (ou not (não))
# and - todas as condições precisam ser
#verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira sera avaliada
# São consideradis falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if True:
# ...
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')