### Dates ###

from datetime import datetime


now = datetime.now()

print("Year:",now.year)
print("Month:",now.month)
print("Day:",now.day)
print("Hour:",now.hour)
print("Minute:",now.minute)
print("Second:",now.second)
print("Microsecond:",now.microsecond)

timestamp = now.timestamp()

print(timestamp)