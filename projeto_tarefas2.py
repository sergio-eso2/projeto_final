banco_de_dados = []
tarefa = {'Status': False}
          

def criar_tarefa():
    tarefa = {}
    tarefa['Nome'] = input('Digite o nome da tarefa: ')
    tarefa['Descricao'] = input('Digite a descriçao: ')
    tarefa['Categoria'] = input('Digite a categoria: ')
    tarefa['Prioridade'] = int(input('Digite a prioridade(1-3): '))
    tarefa['Status'] = False
    banco_de_dados.append(tarefa)
    print('Tarefa adicionada com sucesso')

def listar_tarefas():
    for i in banco_de_dados:
        for chave, valor in i.items():
         print(f'{chave}: {valor}')


def listar_categorias():
    listar = input('Listar por categoria ou prioridade ')
    for i in banco_de_dados:
        if listar == 'Categoria':
            print(i['Categoria'])
        elif listar == 'Prioridade':
            print(i['Prioridade'])    

           
def concluir_tarefas ():
    conclusao = input('Qual tarefa voce concluiu? ')
    for i in banco_de_dados:
        if i['Nome'] == conclusao:
                i['Status'] = True

def deletar_tarefas ():
    deletar = input('Qual tarefa voce deseja deletar? ? ')
    for i in banco_de_dados:
        if i['Nome'] == deletar:
                del(i['Nome'])   
                del(i['Categoria'])
                del(i['Descricao'])
                del(i['Prioridade'])
                del(i['Status'])            
                print('Tarefa Deletada')

           
while True:
    print('Bem vindo ao AppTask')   
    print('1-Criar tarefa')
    print('2-Listar tarefa') 
    print('3-Filtrar Tarefas') 
    print('4-Marcar concluir tarefa') 
    print('5-Deletar tarefa') 
    print('6-Encerrar APP')    
    op = int(input('-> '))
    if op == 1:
        criar_tarefa()
    elif op == 2:
        listar_tarefas()
    elif op == 3:
        listar_categorias()    
    elif op == 4:
        concluir_tarefas()   
    elif op == 5:
        deletar_tarefas()         
    elif op == 6:
        print('App Encerrado')
        break    