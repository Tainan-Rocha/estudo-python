# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.

import os 

# Criando um caminho para um arquivo ou pasta
caminho = os.path.join('Home', 'Documentos', 'curso', 'arquivo.txt')
print(caminho) # Retorna -> Home/Documentos/curso/arquivo.txt

# Retorna o diretorio e o nome do arquivo separados
diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo) # Retorna Home/Documentos/curso arquivo.txt

# Retorna o nome do arquivo e sua extensao separados
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo) # Retorna -> arquivo .txt

# Retorna bolleano true ou falso, caso caminho exista
print(os.path.exists('/home/tainan/Área de Trabalho/python/Modulo os/caminhos.py'))

# Retorna o caminho da pasta que esta executando o comando abaixo
print(os.path.abspath('.'))

# Retorna a ultimo caminho, seja pasta ou arquivo
print(os.path.basename(caminho)) # -> arquivo.txt

# Retorna o caminho das pastas e nao retorna o arquivo
print(os.path.dirname(caminho)) # -> Home/Documentos/curso