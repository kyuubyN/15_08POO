reserva = {"Sala 1": "Disponivel","Sala 2": "Disponivel","Sala 3": "Disponivel","Sala 4": "Disponivel"}
while True:
    print('\n****Opções de reserva****')
    print('1 - Listar salas disponiveis')
    print('2 - Reservar uma sala')
    print('3 - Cancelar reserva')
    print('4 - Sair')
    print('*************************\n')

    selecao = int(input("Escolha uma opção: "))
    if selecao == 1:
        ##
        for k,v in reserva.items():
            print(k,v)
    elif selecao == 2:
        ##
        sala = input("Escolha uma sala de 1 até 4: ")
        strsala = "Sala "+ sala
        if strsala in reserva:
            reserva[strsala] = "Reservado"
        else:
            print("Sala invalida")
            continue
    elif selecao == 3:
        ##
        sala = input("Escolha uma sala de 1 até 4: ")
        strsala = "Sala "+ sala
        if strsala in reserva:
            reserva[strsala] = "Disponivel"
        else:
            print("Sala invalida")
            continue

    elif selecao == 4:
        sair = input("Deseja sair: 'Sim' ou 'Não' ")
        if(sair.lower() != "n" or sair.lower() != "nao" or sair.lower() != "não"):
            break
        else:
            continue
        ##
    else:
        print("OPÇÃO ERRADA")
        continue

