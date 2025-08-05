



import datetime #esta es la forma de importar datetime para fecha sin hora
mi_hora = datetime.time(17,20,35)  # hora, minuto, segundo
print(mi_hora)
print(mi_hora.hour)

print('\n')
mi_dia = datetime.date(2025,10,17)  # año, mes, día
print(mi_dia)
print(mi_dia.year)
print(mi_dia.ctime())# formato de fecha en ingles
print(mi_dia.today())# fecha de hoy

import datetime
hoy = datetime.date.today()
print(hoy)

print('\n')
from datetime import datetime #esta es la forma correcta de importar datetime para fecha con hora

mi_fecha_hora = datetime(2025,10,17,17,20,35)  # año, mes, día, hora, minuto, segundo
mi_fecha_hora = mi_fecha_hora.replace(year=2024)  # Cambia el año a 2024, month o day
print(mi_fecha_hora)


print('\n')
# Ejemplo de diferencia entre dos fechas
from datetime import date
nacimiento = date(1995, 5, 15)  # año, mes, día
defuncion = date(2024, 10, 17)  # año, mes, día
diferencia = defuncion - nacimiento  # Resta de fechas
print(f'resta de dia entre nacimiento y defuncion: {diferencia.days}')# Días entre las dos fechas

print('\n')
from datetime import datetime
despierta = datetime(2024, 10, 17, 7, 0, 0)  # Despertar a las 7:00 AM
dormir = datetime(2024, 10, 17, 22, 0, 0)  # Dormir a las 10:00 PM
tiempo_dormido = dormir - despierta  # Tiempo dormido
print(f'Tiempo dormido: {tiempo_dormido}')  # Imprime el tiempo dormido
print(tiempo_dormido.seconds)# Imprime los segundos del tiempo dormido


from datetime import datetime
minutos = datetime.now().minute # Obtiene los minutos actuales
print(minutos)