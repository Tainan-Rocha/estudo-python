# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

# Importando modulo
from datetime import datetime

from pytz import timezone

data_str_data = '2024/08/23 10:50:23'
data_str_data = '23/08/2024'
data_str_fmt = '%d/%m/%Y'

data = datetime.strptime(data_str_data, data_str_fmt)

print(data) # Retorna data formatada 2024-08-23 00:00:00    

data_agora = datetime.now()
print(data_agora) # Retorna a data e hora atual do computador

data_outro_lugar = datetime.now(timezone('Asia/Tokyo'))
print(data_outro_lugar) # Retorna a data e hora de um local especifico