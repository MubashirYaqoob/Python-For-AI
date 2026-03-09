words = ["apple", "banana", "apple", "orange", "banana", "apple"]

result = {}

for i in words :
    result[i] = result.get(i,0) + 1 