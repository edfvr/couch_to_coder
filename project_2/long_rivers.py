#----Base Task----

rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]

for river in rivers:
    print(river['name'])


total_length = 0

for river in rivers:
    total_length += river['length']

print(f"\nTotal length of the rivers = {total_length}")

#print(4157 + 3434 + 2310 + 2290 + 2540 + 3915)