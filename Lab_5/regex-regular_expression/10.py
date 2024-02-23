# 10. Write a Python program to insert spaces between words starting with capital letters.

import re

def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

print(camel_to_snake("SeventeenBtsStrayKids"))  
# seventeen_bts_stray_kids