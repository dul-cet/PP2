# 4. Write a Python program to calculate two date difference in seconds.

from datetime import datetime

date1 = datetime(2023, 6, 15, 10, 30, 0)
date2 = datetime(2023, 6, 20, 14, 45, 0)

difference_seconds = abs((date2 - date1).total_seconds())
print("Difference in seconds:", difference_seconds)