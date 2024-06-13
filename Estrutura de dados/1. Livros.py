import os
from dataclasses import dataclass
os.system ("cls || clear")

LIVROS = 2

# Classe
@dataclass
class Livro:
    titulos : str
    autores : str
    numero_de_paginas : int
    preços : float

livros = []


# Solicitando dados para o usuário.
for i in range (LIVROS):
    titulo = input("\nDigite o título do livro: "),
    autor = input("Digite o autor: "),
    numero_de_pagina = int(input("Digite o número de páginas: ")),
    preço = float(input("Digite o preço do livro: "))

    dados = Livro(titulos = titulo, autores = autor, numero_de_paginas = numero_de_pagina, preços = preço)
    livros.append(dados)

for i in livros:
    print (f"\nTítulo do livro: {i.titulos}")
    print (f"Autor do livro: {i.autores}")
    print (f"Número de páginas do livro: {i.numero_de_paginas}")
    print (f"preço do livro: {i.preços}")