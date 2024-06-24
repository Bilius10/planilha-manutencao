import pandas as pd
#recebe um texto, para estilizar o titulo
def titulo(msg):
    print("-"*42)
    print(msg.center(42))
    print("-"*42)
    print("")
#salvar as informações passadas no dataframe inserir
#concatena com as ultimas informações da tabela, e resalvamos ela
def cadastro(tabela_manutencao):
    inserir = pd.DataFrame({
            "Equipamento": [str(input("Nome do equipamento: "))],
            "Data": [str(input("Data de entrada do equipamento: "))],
            "Nome": [str(input("Nome do proprietario: "))],
            "Problema": [str(input("Problema: "))],
        })
    tabela_manutencao = pd.concat([tabela_manutencao, inserir], ignore_index=True)
    tabela_manutencao.to_excel("equipamento_manutencao.xlsx", index=False)
#printa o primeiro item da tabela manutenção
#inserimos as informações no df inserir, concatemos com as ultimas informações da tabela_prontos, e resalvamos
#excluimos a ultima linha da tabela_manutencao e resalvamos
def fechamento_manutencao(tabela_manutencao, tabela_prontos):
    print(f"Equipamento concertado : {tabela_manutencao['Equipamento'][0]}")
    inserir = pd.DataFrame({
        "equipamento": [tabela_manutencao['Equipamento'][0]],
        "Data": [str(input("Data de saida: "))],
        "Valor": [float(input("Valor do concerto: "))],
        "Tecnico": [str(input("Nome do Tecnico: "))],
        })
    tabela_prontos = pd.concat([tabela_prontos, inserir], ignore_index=True)
    tabela_prontos.to_excel("equipamento_pronto.xlsx", index=False)
    tabela_manutencao = tabela_manutencao.drop(index=0)
    tabela_manutencao.to_excel("equipamento_manutencao.xlsx", index=False)
#usando o for passamos de linha em linha da tabela(index), e exibimos as informações index e equipamento daquela linha
def fila(tabela_manutencao):
    for index, row in tabela_manutencao.iterrows():
        print(f'{index+1}° Equipamento: {row['Equipamento']}')
    sair = input("Enter para sair: ")
#printamos na tela, todos os nomes e equipamentos para o usuario usar de base
#o usuario digite o nome e o equipamento que esta procurando
#com isso sera printado na tela, todas as suas informações
def buscar_manutencao(tabela_manutencao):
    import os
    for index, row in tabela_manutencao.iterrows():
        print(f"Nome: {row['Nome']} Equipamento: {row['Equipamento']}")
    print(" ")
    buscar_1 = str(input("Digite o nome do proprietario : "))
    buscar = str(input("Digite o nome do equipamento: "))
    os.system('cls')
    if buscar in tabela_manutencao['Equipamento'].values and buscar_1 in tabela_manutencao['Nome'].values :
        print(tabela_manutencao.iloc[index-1].to_string())
        sair = input("Enter para sair: ")
    else:
        print("Equipamento não localizado")
#a funcao len é usada para devolver o numero de equipamentos que há no df
#com isso será usado, para mostrar quantos produtos tem em cada df
def status(tabela_manutencao, tabela_prontos):
    print(f'{len(tabela_manutencao)} equipamento(s) em manutenção')
    print(f'{len(tabela_prontos)} equipamento(s) prontos')
    sair = input("Enter para sair: ")
#o for vai de linha em linha do df, e usando o row, printamos na tela apenas o equipamento e o valor daquela linha
#nisso atribuimos o valor dessa linha  a variavel soma, aonde sera somado ao ultimo valor que tem nela 
def concertados(tabela_prontos):
    soma = int(0)
    for index, row in tabela_prontos.iterrows():
        print(f'Equipamento: {row['equipamento']} Valor: R${row['Valor']}')
        soma += tabela_prontos['Valor'][index]
    print(f'Valor Total: R$:{soma}')
    sair = input("Enter para sair: ")
#printamos na tela, todos os nomes e equipamentos para o usuario usar de base
#o usuario digite o nome e o equipamento que esta procurando
#com isso sera printado na tela, todas as suas informações
def buscar_prontos(tabela_pronto):
    import os
    for index, row in tabela_pronto.iterrows():
        print(f"Tecnico: {row['Tecnico']} Equipamento: {row['equipamento']}")
    buscar_1 = str(input("Digite o nome do tecnico : "))
    buscar = str(input("Digite o nome do equipamento: "))
    os.system('cls')
    if buscar in tabela_pronto['equipamento'].values and buscar_1 in tabela_pronto['Tecnico'].values :
        print(tabela_pronto.iloc[index-1])
        sair = input("Enter para sair: ")
    else:
        print("Equipamento não localizado")
