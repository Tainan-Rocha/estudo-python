# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6

import calendar 

# Exibe calendario do ano que deseja
print(calendar.calendar(2024))

# Exibe o calendario de um mes 
print(calendar.month(2024, 8))

primeiro_dia_mes, ultimo_dia_mes = calendar.monthrange(2024, 8)

# Retorna o dia semana e o ultimo dia do mes
print(primeiro_dia_mes, ultimo_dia_mes)