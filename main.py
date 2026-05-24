def adicionar_item(lista_de_tarefas, tarefa):
    """Adiciona um novo item à lista de tarefas."""
    tarefa = {"nome_da_tarefa": tarefa, "status_da_tarefa": False}
    lista_de_tarefas.append(tarefa)


def visualizar_itens_da_lista(lista_de_tarefas):
    """Exibe todos os itens da lista com seu status."""
    if not lista_de_tarefas:
        print("A lista está vazia!")
        return
    for indice, tarefa in enumerate(lista_de_tarefas, start=1):
        status = "v" if tarefa["status_da_tarefa"] else " "
        print(f"[{status}] {indice}. {tarefa['nome_da_tarefa']}")


def alterar_item_da_lista(lista_de_tarefas, indice, novo_nome_da_tarefa):
    """Altera o nome de um item da lista pelo índice."""
    indice_ajustado = indice - 1
    lista_de_tarefas[indice_ajustado]["nome_da_tarefa"] = novo_nome_da_tarefa


def completar_tarefa(lista_de_tarefas, indice):
    """Marca uma tarefa como completada pelo índice."""
    indice_ajustado = indice - 1
    lista_de_tarefas[indice_ajustado]["status_da_tarefa"] = True
    print(f"Tarefa {indice} completada com sucesso!")


def excluir_tarefas_completadas(lista_de_tarefas):
    """Remove todas as tarefas marcadas como completadas."""
    lista_de_tarefas[:] = [t for t in lista_de_tarefas if not t["status_da_tarefa"]]
    print("As tarefas completadas foram removidas!")


# --- Programa principal ---
lista_de_tarefas = []

while True:
    print("""
        1. Adicionar uma tarefa a lista.
        2. Visualizar a lista de tarefas.
        3. Alterar uma tarefa da lista.
        4. Completar uma tarefa da lista.
        5. Excluir tarefas completadas.
        6. Encerrar programa.""")

    try:
        resposta = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if resposta == 1:
        tarefa = input("Escreva a tarefa que deseja adicionar: ")
        adicionar_item(lista_de_tarefas, tarefa)
    elif resposta == 2:
        visualizar_itens_da_lista(lista_de_tarefas)
    elif resposta == 3:
        visualizar_itens_da_lista(lista_de_tarefas)
        indice = int(input("Qual tarefa da lista deseja substituir? "))
        novo_nome_da_tarefa = input("Digite o novo nome da tarefa: ")
        alterar_item_da_lista(lista_de_tarefas, indice, novo_nome_da_tarefa)
        print("Tarefa alterada com sucesso!")
    elif resposta == 4:
        visualizar_itens_da_lista(lista_de_tarefas)
        indice = int(input("Qual tarefa deseja completar? "))
        completar_tarefa(lista_de_tarefas, indice)
    elif resposta == 5:
        excluir_tarefas_completadas(lista_de_tarefas)
    elif resposta == 6:
        print("Programa Encerrado!")
        break
    else:
        print("Opção inválida! Digite um número de 1 a 6.")