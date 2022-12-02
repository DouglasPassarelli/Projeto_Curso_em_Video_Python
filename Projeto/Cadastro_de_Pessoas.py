'''
Projeto de Cadastro de Pessoas simples pegando nome e idade e armazenando em um arquivo cursoemvideo.txt
#Funções na pasta listagem __init__.py e na pasta arquivo.

'''


from Projeto.listagem.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqexiste(arq):
    criararq(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        adicionararq(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Ate logo')
        break
    elif resposta == 4:
        cabecalho('Apagar registro')
        numerorRegistro = leiaint('Numero Registro')
        break
    else:
        print('\033[31mErro! Digite um opção valida.\033[m')
    sleep(2)


