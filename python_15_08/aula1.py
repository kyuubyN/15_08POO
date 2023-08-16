tarefas = {"1":"enviar relatorio","2":"corrigir bugs","3":"reunião as 10h"}

print(tarefas.get("2"))

for k,v in tarefas.items():
    print(k,v)

lista = [1,2,3,4]
for i in lista:
    print()
