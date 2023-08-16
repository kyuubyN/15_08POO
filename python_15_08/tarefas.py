import time
tarefas = {}
id = 0
while True: 
    print("****Gerenciador de Tarefas****")
    print("1 - Criar")
    print("2 - Visualizar")
    print("3 - Excluir tarefas")
    print("4 - Sair")
    print("*******************************")

    opcao = int(input("Entre com a opção desejada: "))
    if opcao == 1:
        ##
        descricao = input("Entre com a tarefa: ")
        tarefas[id] = descricao
        id += 1
    elif opcao == 2:
        ##
        print("****Visualizar Tarefas****")
        for k,v in tarefas.items():
            print(k,v)
    elif opcao == 3:
        ##
        idExclusao = int(input("Enter com o id da tarefa para ser excluida: "))
        if idExclusao in tarefas: 
            del tarefas[idExclusao]
        else:
            print("Id inválido ou não encontrado")
    elif opcao == 4:
        ##
        sair = input("Deseja sair: 'Sim' ou 'Não'")
        if(sair.lower() != "n" or sair.lower() != "nao" or sair.lower() != "não"):
            break
        else:
            continue
    else:
        print("Opção errada")
        time.sleep(3)
        continue

