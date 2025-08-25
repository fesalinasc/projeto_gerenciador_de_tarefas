import task_manager

def main():
    print("Bem-vindo ao Gerenciador de Tarefas!\n")

    while True:
        print("\n1. Criar tarefa")
        print("2. Listar tarefas pendentes")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        try:
            option = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if option == 1:
            title = input("Título da tarefa: ")
            description = input("Descrição (opcional): ")
            task = task_manager.create_task(title, description)
            print(f"Tarefa '{task['title']}' criada com sucesso!")

        elif option == 2:
            tasks = task_manager.list_tasks()
            if not tasks:
                print("Nenhuma tarefa pendente.")
            else:
                print("Tarefas pendentes:")
                for task_str in tasks:
                    print(task_str)

        elif option == 3:
            try:
                task_number = int(input("Número da tarefa a marcar como concluída: "))
                if task_manager.mark_complete(task_number):
                    print("Tarefa marcada como concluída!")
                else:
                    print("Tarefa não encontrada.")
            except ValueError:
                print("Por favor, insira um número válido.")

        elif option == 4:
            try:
                task_number = int(input("Número da tarefa a remover: "))
                if task_manager.remove_task(task_number):
                    print("Tarefa removida com sucesso!")
                else:
                    print("Tarefa não encontrada.")
            except ValueError:
                print("Por favor, insira um número válido.")

        elif option == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha entre 1 e 5.")

if __name__ == "__main__":
    main()
