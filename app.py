class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def __eq__(self, outro):
        # Dois livros são iguais se tiverem mesmo título e autor
        if isinstance(outro, Livro):
            return self.titulo == outro.titulo and self.autor == outro.autor
        return False
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano})"

# Instanciar objetos
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1900)  # Mesmo título e autor, ano diferente
livro3 = Livro("Memórias Póstumas", "Machado de Assis", 1881)  # Título diferente, mesmo autor
livro4 = Livro("O Cortiço", "Aluísio Azevedo", 1890)  # Completamente diferente

print("=== LIVROS CRIADOS ===")
print(f"Livro 1: {livro1}")
print(f"Livro 2: {livro2}")
print(f"Livro 3: {livro3}")
print(f"Livro 4: {livro4}")
print()

print("=== COMPARAÇÕES COM == (usa __eq__) ===")
print(f"livro1 == livro2: {livro1 == livro2}")  # True - mesmo título e autor
print(f"livro1 == livro3: {livro1 == livro3}")  # False - título diferente
print(f"livro1 == livro4: {livro1 == livro4}")  # False - tudo diferente
print(f"livro2 == livro3: {livro2 == livro3}")  # False - título diferente
print()

print("=== IDENTIDADE DOS OBJETOS (id()) ===")
print(f"id(livro1): {id(livro1)}")
print(f"id(livro2): {id(livro2)}")
print(f"id(livro3): {id(livro3)}")
print(f"id(livro4): {id(livro4)}")
print()

print("=== COMPARAÇÕES COM IS (identidade) ===")
print(f"livro1 is livro2: {livro1 is livro2}")  # False - objetos diferentes na memória
print(f"livro1 is livro1: {livro1 is livro1}")  # True - mesma referência
print()

print("=== ANÁLISE DOS RESULTADOS ===")
print("1. livro1 == livro2 retorna True porque:")
print("   - Ambos têm título 'Dom Casmurro'")
print("   - Ambos têm autor 'Machado de Assis'")
print("   - O método __eq__ ignora o ano de publicação")
print()
print("2. A identidade (id) é diferente para cada objeto:")
print("   - Cada instância criada com Livro() ocupa um espaço único na memória")
print("   - Mesmo que o conteúdo seja igual, são objetos distintos")
print()
print("3. O operador 'is' retorna False para livro1 is livro2:")
print("   - Eles são objetos diferentes na memória")
print("   - 'is' verifica se são o MESMO objeto, não se têm conteúdo igual")