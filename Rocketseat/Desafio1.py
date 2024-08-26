Contato = {"id","nome", "telefone","email"}

def AdicionarContato():
    print("Para adicionar um novo contato, tenha em mãos o Nome, Telefone e Email")
    
    print("Qual o nome do contato?")
    Contato["nome"] = input("")
    
    print("Qual o telefone do contato?")
    Contato["telefone"] = input("")    
    
    print("Qual o email do contato?")
    Contato["email"] = input("")

def VizualizarContato():    
    print("Id", Contato["id"], "Nome", Contato["nome"],"Telefone", Contato["telefone"],"Email", Contato["email"],)

def EditarContato():        
    print("Qual contato deseja Editar?")
    VizualizarContato()
    input("")

    print("Caso não deseje atualizar algum campo é só pressionar o ENTER")

    print("Qual o nome do contato?")
    Contato["nome"] = input("")
    
    print("Qual o telefone do contato?")
    Contato["telefone"] = input("")    
    
    print("Qual o email do contato?")
    Contato["email"] = input("")    
    
def FavoritarContato():            
    print("Qual contato deseja Favoritar?")
    VizualizarContato()
    input("")
    
def ApagarContato():                
    print("Qual contato deseja Apagar?")
    VizualizarContato()
    input("")
    
def Selecionado(opcao):
    if opcao == 1:
        AdicionarContato()
    elif opcao == "2":
        VizualizarContato()
    elif opcao == 3:        
        EditarContato()
    elif opcao == 4:
        FavoritarContato()
    elif opcao == 5:    
        ApagarContato()
    else:
        print("Seleção inválida")

i = 0
print("Digite o número correspondente a opção desejada")
while i == 0:
    print("*-------------------------------------------*")
    print("1-Adicionar contato")
    print("2-Vizualizar Lista")
    print("3-Editar Contato")
    print("4-Marcar/Desmarcar um contato como favorito")
    print("5-Apagar contato")
    print("*-------------------------------------------*")
    selecao = input("Digite a opção desejada: ")

    Selecionado(selecao)


        
