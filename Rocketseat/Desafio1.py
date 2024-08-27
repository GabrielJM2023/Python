# Criando um dicionário de contatos vazio
Contatos = {}

def AdicionarContato():
    print("Para adicionar um novo contato, tenha em mãos o Nome, Telefone e Email.")
    
    novo_id = len(Contatos) + 1
    
    nome = input("Qual o nome do contato? ")
    telefone = input("Qual o telefone do contato? ")
    email = input("Qual o email do contato? ")
    favoritar = "X"
    Contatos[novo_id] = {"nome": nome, "telefone": telefone, "email": email, "favorito": favoritar}
    print("Contato adicionado com sucesso!")

def VizualizarContato():
    if len(Contatos) == 0:
        print("\nA lista está vazia\n")
    else:
        print("Id".ljust(3), "Nome".ljust(15), "Telefone".ljust(15), "Email".ljust(77), "Favorito")
        print("-" * 40)

        for id, contato in Contatos.items():
            print(str(id).ljust(3), contato["nome"].ljust(15), contato["telefone"].ljust(15), contato["email"].ljust(77), contato["favorito"])

def EditarContato():
    if len(Contatos) == 0:
        return
    
    VizualizarContato()
        
    try:
        contato_id = int(input("Digite o ID do contato que deseja editar: "))
        contato = Contatos[contato_id]
        
        print("Caso não deseje atualizar algum campo, pressione ENTER.")
        
        nome = input(f"Nome atual [{contato['nome']}]: ")
        telefone = input(f"Telefone atual [{contato['telefone']}]: ")
        email = input(f"Email atual [{contato['email']}]: ")
        
        if nome:
            contato['nome'] = nome
        if telefone:
            contato['telefone'] = telefone
        if email:
            contato['email'] = email
        
        print("Contato atualizado com sucesso!")
        
    except KeyError:
        print("Contato não encontrado.")
    except ValueError:
        print("ID inválido.")

def FavoritarContato():
    if len(Contatos) == 0:
        return
    
    VizualizarContato()
        
    try:
        contato_id = int(input("Digite o ID do contato que deseja favoritar: "))
        contato = Contatos[contato_id]                
        
        contato['favorito'] = "V"
        
        print("Contato Favoritado com sucesso!")
        
    except KeyError:
        print("Contato não encontrado.")
    except ValueError:
        print("ID inválido.")

def ApagarContato():
    VizualizarContato()
    
    if len(Contatos) == 0:
        return
    
    try:
        contato_id = int(input("Digite o ID do contato que deseja apagar: "))
        Contatos.pop(contato_id)
        print("Contato apagado com sucesso!")
        
    except KeyError:
        print("Contato não encontrado.")
    except ValueError:
        print("ID inválido.")

def Selecionado(opcao):
    if opcao == "1":
        AdicionarContato()
    elif opcao == "2":
        VizualizarContato()
    elif opcao == "3":
        EditarContato()
    elif opcao == "4":
        FavoritarContato()
    elif opcao == "5":
        ApagarContato()
    else:
        print("Seleção inválida")

while True:
    print("*-------------------------------------------*")
    print("1-Adicionar contato")
    print("2-Vizualizar Lista")
    print("3-Editar Contato")
    print("4-Marcar/Desmarcar um contato como favorito")
    print("5-Apagar contato")
    print("*-------------------------------------------*")
    
    selecao = input("Digite a opção desejada: ")
    Selecionado(selecao)
    
    continuar = input("Deseja finalizar? Digite 'sair' para finalizar ou ENTER para continuar: ")
    if continuar.lower() == "sair":
        break
