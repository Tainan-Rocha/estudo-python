# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Exemplo')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

# Exclui todas as pastas e arquivos do caminho
shutil.rmtree(NOVA_PASTA, ignore_errors=True)

# Copia todas as pastas e arquivos para um novo diretorio
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# Renomeia uma pasta
shutil.move(NOVA_PASTA, NOVA_PASTA + '_RENOMEADA')
