# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import calendar

import locale 

# Deixando a string vazio vai puxar a localizacao de acordo com seu sistema operacional
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') # Ou tambem pode especificar

# Atraves do comando 'local -a', consegue visualizar as localizacoes disponiveis para utilizacao.

print(calendar.calendar(2024))