"""
Python é uma linguagem de programação de alto nível, conhecida por sua simplicidade e legibilidade. Criada por Guido van Rossum e lançada pela primeira vez em 1991, Python foi desenvolvida com o objetivo de ser fácil de aprender e usar, o que a tornou popular tanto entre iniciantes quanto entre desenvolvedores experientes.

### Principais características do Python:
- **Sintaxe simples e clara**: A sintaxe do Python é intuitiva, semelhante à linguagem natural, o que facilita a leitura e escrita do código.
- **Tipagem dinâmica**: Python é uma linguagem de tipagem dinâmica, ou seja, não é necessário declarar o tipo das variáveis explicitamente.
- **Interpretada**: Python é uma linguagem interpretada, o que significa que o código é executado linha por linha, sem a necessidade de compilar antes.
- **Versátil**: Python é utilizado em diversas áreas, como desenvolvimento web, ciência de dados, inteligência artificial, automação, e muito mais.
- **Bibliotecas e frameworks**: Python possui uma vasta coleção de bibliotecas e frameworks, como Django e Flask para web, Pandas e NumPy para ciência de dados, TensorFlow e PyTorch para aprendizado de máquina, entre outros.

### Exemplos de uso:
- **Desenvolvimento Web**: Criação de sites e aplicativos web.
- **Automação**: Scripts para automação de tarefas repetitivas.
- **Data Science**: Análise e visualização de dados.
- **Machine Learning**: Desenvolvimento de modelos de aprendizado de máquina e inteligência artificial.

Python é amplamente utilizado devido à sua flexibilidade e poder, o que o torna uma escolha popular para muitos tipos de projetos.
"""
# - comentario de uma linha 

"""
Comentario de varias linhas 
"""
# Declaração de variaveis padrão de linguagens, sem caracter especial no inicio da variavel, python é caseSensitive  e tem tipagem dinamica
nome = 1

nome = "Gabriel" +" "+ \
"Jardim"

# "\" é uma quebra de linha, se tirar da erro, porém, pode fazer com """" aspas duplas """" 

# Python não tem um final especifico, ele utiliza a identação 

if nome == "Gabriel":
    print(nome)
else:
    if nome == "Gabriel Jardim":
        print(nome)


#Em Python, tanto listas quanto tuplas são tipos de dados que podem armazenar uma coleção de itens, mas elas têm algumas diferenças importantes:
""" 
1. **Mutabilidade**:
   - **Listas**: São mutáveis, ou seja, podem ser alteradas após serem criadas. Você pode adicionar, remover ou modificar elementos em uma lista.
   - **Tuplas**: São imutáveis, o que significa que, uma vez criadas, não podem ser modificadas. Nenhum elemento pode ser adicionado, removido ou alterado.
"""
   # Lista
lista = [1, 2, 3]
lista[0] = 10  # Modifica o primeiro elemento
lista.append(4)  # Adiciona um novo elemento

# Tupla
tupla = (1, 2, 3)
tupla[0] = 10  # Isso causará um erro

""" 
    2. **Sintaxe**:
    - **Listas**: São definidas usando colchetes `[]`.
    - **Tuplas**: São definidas usando parênteses `()`.
""" 

lista = [1, 2, 3]  # Lista
tupla = (1, 2, 3)  # Tupla
"""    
3. **Uso e Desempenho**:
   - **Listas**: São preferidas quando você precisa de uma coleção de itens que pode mudar durante a execução do programa.
   - **Tuplas**: São mais rápidas que listas e consomem menos memória. São usadas quando você deseja garantir que os dados permaneçam constantes, como em pares de coordenadas, chaves de dicionários, etc.

4. **Operações Disponíveis**:
   - **Listas**: Oferecem uma ampla gama de métodos, como `append()`, `remove()`, `sort()`, entre outros.
   - **Tuplas**: Oferecem poucos métodos, como `count()` e `index()`.

""" 
lista = [1, 2, 3]
lista.append(4)  # Funciona

tupla = (1, 2, 3)
tupla.append(4)  # Isso causará um erro

""" 
5. **Quando Usar Cada Um**:
   - Use **listas** quando você precisar de uma coleção de elementos que possa mudar.
   - Use **tuplas** para dados constantes que não devem ser modificados após a criação.

Essas características fazem as listas e tuplas adequadas para diferentes cenários em Python.
""" 


# Para construir classes no python 
# É obrigatório o __init__, que é o construtor
# Para criar atributos, utiliza-se o self e tem q passar por parametro

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
pessoa = Pessoa("Arthur", 25)
pessoa.apresentar()