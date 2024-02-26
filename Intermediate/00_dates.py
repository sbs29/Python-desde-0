### Dates ###

# datetime usado para fecha y hora
from datetime import datetime

now = datetime.now()    # Creacion de una variable datetime

timestamp = now.timestamp()     # Formato de postal

print("Timestamp:",timestamp)

year_2024 = datetime(2024, 5, 6)    # Minimo para declarar un año

print(year_2024)

def print_date(date):
    print("Year:",date.year)
    print("Month:",date.month)
    print("Day:",date.day)
    print("Hour:",date.hour)
    print("Minute:",date.minute)
    print("Second:",date.second)
    print("Microsecond:",date.microsecond)

print_date(now)


# time usado para horas
from datetime import time

current_time = time(hour=10,minute=45,second=35)

print("Hour:",current_time.hour)
print("Minute:",current_time.minute)
print("Second:",current_time.second)


# date usado para fechas
from datetime import date

current_date = date.today()

print("Year:",current_date.year)
print("Month:",current_date.month)
print("Day:",current_date.day)

current_date = date(24,5,6)

print("Year:",current_date.year)
print("Month:",current_date.month)
print("Day:",current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date)

diff = year_2024 - now                      # Forma de operar con datetime si son del mismo import
print(diff)

diff = year_2024.date() - current_date      # Forma de operar con date si son del mismo import
print(diff)

#diff = year_2024.time() - current_time      # No se puede operar con time
#print(diff)



# timedelta usado para operar con franjas de fechas
from datetime import timedelta

init_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - init_timedelta)   #   Es valido
print(end_timedelta + init_timedelta)   #   Es valido
#print(end_timedelta * init_timedelta)   #   No es valido
#print(end_timedelta / init_timedelta)   #   No es valido
