# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

# Importando modulo
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('22/08/2024 12:00:00', fmt)
data_fim = datetime.strptime('20/08/2024 12:20:20', fmt)



delta = data_fim - data_inicio
print(delta.days) # Retorna a diferenca do delta
print(data_fim > data_inicio) # Comparar datas retorna bollean


delta = relativedelta(data_fim, data_inicio)  # Retorna a diferenca do delta
print(delta.days, delta.years)  # Retorna a diferenca do delta