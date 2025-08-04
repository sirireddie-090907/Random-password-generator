# RANDOM_PASSWORD_GENERATOR

import random
import string

pass_len = 10

charvalues = string.ascii_letters + string.digits + string.punctuation

# List comprehension (compact way)

password="".join([random.choice(charvalues) for i in range(pass_len)])

print("Here we go with your random password:",password)