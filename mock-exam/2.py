numbers = [15,22,8,45,30,12,55,18]

new_number = list(filter(lambda x : x > 20,numbers))

print(new_number)


lsquare = list(map(lambda x : x * x,new_number))
print(lsquare)