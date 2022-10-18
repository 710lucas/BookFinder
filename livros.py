
class Livros:
    def __init__(self, a, n, p, g):        
        self.autor = a
        self.nome = n
        self.paginas = p
        self.genero = g

livros = []
def criar_livros():
    
    livro = Livros("Johnny John John", "Searching Jon", 80, ["drama"])
    livros.append(livro)

    livro = Livros("Mauricio de souza", "Almanaque Chico Bento 1", 60, ["comedia"])
    livros.append(livro)

    livro = Livros("Ziraldo", "O menino maluquinho 1", 45, ["comedia"])
    livros.append(livro)

    livro = Livros("Antoine de saint exupery", "O pequeno principe", 120, ["drama"])
    livros.append(livro)

    livro = Livros("Silvia Plath", "A redoma de vidro", 80, ["romance", "autobiografia"])
    livros.append(livro)

    livro = Livros("ALbert Camus", "L'etranger", 120, ["romance", "filosofia"])
    livros.append(livro)

criar_livros()
livro_busca = input("Digite alguma informação sobre o livro (autor, nome, paginas ou genero): ").lower()

livros_index = []

for i in range(len(livros)):
    if( livro_busca in livros[i].autor.lower() or livro_busca in livros[i].nome.lower()
            or livro_busca in livros[i].genero and not livro_busca.isnumeric()) :
        livros_index.append(livros[i])
    elif(livro_busca.isnumeric() and int(livro_busca) == livros[i].paginas):
        livros_index.append(livros[i])

if(len(livros_index) > 0):
    print("Livros que satisfazem a sua pesquisa: ")
    for i in range(len(livros_index)):
        print(livros_index[i].nome)
        print("\tAutor(a):", livros_index[i].autor)
        print("\tPaginas:", livros_index[i].paginas)
        print("\tGenero: ", livros_index[i].genero)
