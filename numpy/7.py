numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(filter(lambda x: x % 2 == 0,numbers))

square = list(map(lambda x : x * x , new_list))

print(square)