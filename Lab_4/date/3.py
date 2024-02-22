# 3. Write a Python program to drop microseconds from datetime.

from datetime import datetime

current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Datetime without microseconds:", datetime_without_microseconds)