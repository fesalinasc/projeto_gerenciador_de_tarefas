# Estrutura de dados para armazenar tarefas
tasks = []
task_counter = 1  # Para gerar identificadores únicos


def create_task(title, description=""):
    """
    Cria uma nova tarefa e adiciona à lista de tarefas.

    Parâmetros:
        title (str): Título da tarefa.
        description (str): Descrição da tarefa (opcional).

    Retorna:
        dict: A tarefa criada.
    """
    global task_counter
    task = {
        "number": task_counter,
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    task_counter += 1
    return task


def list_tasks():
    """
    Retorna uma lista formatada das tarefas pendentes.

    Retorna:
        list: Lista de strings formatadas das tarefas pendentes.
    """
    pending_tasks = [task for task in tasks if not task["completed"]]
    formatted_tasks = []
    for task in pending_tasks:
        desc = f", Descrição: {task['description']}" if task["description"] else ""
        formatted_tasks.append(f"{task['number']}. Título: {task['title']}{desc}")
    return formatted_tasks


def mark_complete(task_number):
    """
    Marca a tarefa com o número especificado como concluída.

    Parâmetros:
        task_number (int): Número da tarefa a ser marcada como concluída.

    Retorna:
        bool: True se a tarefa foi marcada com sucesso, False se não foi encontrada.
    """
    for task in tasks:
        if task["number"] == task_number:
            task["completed"] = True
            return True
    return False


def remove_task(task_number):
    """
    Remove a tarefa com o número especificado.

    Parâmetros:
        task_number (int): Número da tarefa a ser removida.

    Retorna:
        bool: True se a tarefa foi removida com sucesso, False se não foi encontrada.
    """
    for task in tasks:
        if task["number"] == task_number:
            tasks.remove(task)
            return True
    return False
