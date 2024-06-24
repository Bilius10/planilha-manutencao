import funcoes
import os
import pandas as pd
#atribuição das tabelas para dataframes
tabela_manutencao = pd.read_excel("equipamento_manutencao.xlsx")
tabela_prontos = pd.read_excel("equipamento_pronto.xlsx")
funcoes.titulo("Bem-Vindo ao sistema de manutenção")
#menu de opções
while True:
    print('''
1-Cadastro novo equipamento
2-Registro da Última Manutenção 
3-Fila de atendimento
4-Buscar equipamento em manutenção
5-Status da fila
6-Equipamento concertados/valor total
7-Buscar equipamento prontos
8-Sair''')
    opcao = int(input('Digite uma opção: '))
    os.system('cls')
    #opcao 1, puxamos a def titulo, para criação do titulo
    #puxamos a def cadastro, para enviarmos as informações ao excel euipamento_manutencao
    if opcao == 1:
        funcoes.titulo("Cadastro novo equipamento")
        funcoes.cadastro(tabela_manutencao)
    #opcao 2, puxamos a def titulo, para criação do titulo
    #puxamos a def proxima_manutencao, aonde sera repassado ao usuario a ultima manutencao, inserimos informações e excluiremos 
    #ela da tabela_manutencao e passamos para para a tabela_pronto
    elif opcao == 2:
        funcoes.titulo("Proximo equipamento para manutenção")
        funcoes.fechamento_manutencao(tabela_manutencao, tabela_prontos)
    #opcao 3, puxamos a def titulo, para criação do titulo
    #puxamos a def fila aonde printamos todos os equipamentos e os index da tabela_manutencao
    elif opcao == 3:
        funcoes.titulo("Fila de atendimento")
        funcoes.fila(tabela_manutencao)
    #opcao 4, puxamos a def titulo, para criação do titulo
    #puxamos a def buscar_manutencao, aonde buscaremos um equipamento especifico na tabela_manutencao
    #e sera printado todas as suas informações
    elif opcao == 4:
        funcoes.titulo("Buscar equipamento em manutenção")
        funcoes.buscar_manutencao(tabela_manutencao)
    #opcao 5, puxamos a def titulo, para criação do titulo
    #puxamos a def status, aonde sera printado na tela, quantidade de euipamentos na tabela_manutencao e 
    #na tabela_pronto
    elif opcao == 5:
        funcoes.titulo("Status da fila")
        funcoes.status(tabela_manutencao, tabela_prontos)
    #opcao 6, puxamos a def titulo, para criação do titulo
    #puxamos a def concertados, aonde sera exibido na tela todos os equipamentos e seus valores
    # e sera mostrado o valor total dos concertos
    elif opcao == 6:
        funcoes.titulo("Equipamento concertados/valor total")
        funcoes.concertados(tabela_prontos)
    #opcao 7, puxamos a def titulo, para criação do titulo
    #puxamos a def buscar_prontod, aonde buscaremos um equipamento especifico na tabela_prontos
    #e sera printado todas as suas informações
    elif opcao == 7:
        funcoes.titulo("Buscar equipamento prontos")
        funcoes.buscar_prontos(tabela_prontos)
    #opcao 8, puxamos a def titulo, para criação do titulo
    #break usado para interromper o while True
    elif opcao == 8:
        funcoes.titulo("Finalizando")
        break



