employees = [
    ("Ali", 30000),
    ("Ahmed", 55000),
    ("Sara", 70000),
    ("Zain", 45000)
]

new_list = list(filter(lambda x : x[1] > 50000,employees))

bonus = list(map(lambda x : x[1] *  10 ,new_list))

print(bonus)