tarefas= []


def adicionar_tarefa():
    tarefa = input ("Digite uma nova tarefa: ")
    tarefas.append(tarefa)
    print ("tarefa executada")
    
    
    def eliminar_tarefa ():
        tarefa = int(input("Digite a tarefa que deseja eliminar:"))-1
        if tarefa < len(tarefas):
            tarefas.pop(tarefa)
            print("tarefa eliminada")
        else:
            print("A tarefa não existe na lista ")
            
            
            def mostrar_tarefas ():
                if tarefas:
                    print("Lista de tarefas: ")
                    for i, tarefa in enumerate(tarefas,1):
                        print (f"{i}. {tarefas}")
                    else:
                        print("não há tarefas na lista")
                        
                        def main ():
                            opcao= 0
                            
                            while opcao != 4:                           
                                print("/n --- Lista de tarefas---")
                                print ("1. Adicionar tarefa")
                                print ("2. Eliminar tarefa")
                                print ("3. Mostrar tarefa")
                                print ("4.Sair")
                            
                            opcao = int(input("Selecione uma opcao: "))
                            
                            if opcao == 1:
                                adicionar_tarefa()
                            elif opcao == 2:
                                eliminar_tarefa()
                            elif opcao == 3:
                                mostrar_tarefas()
                            elif opcao == 4:
                                print("lista concluída!!!")
                            else:
                                print("opcao nao válida")
                                
                                if __name__== "__main__":
                                 main()
                    
                            
                            
                    
                
    
        







        