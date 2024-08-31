# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

# Retorna o home do PC.
HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

# Cria uma nova pasta 
os.makedirs(NOVA_PASTA, exist_ok=True) # exist_ok e para nao ter excesao caso a pasta ja exista

# Copia as pastas 
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_in in dirs: 
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_in)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    # Copia os arquivos
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)