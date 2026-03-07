## add two list arguments 

nums = [1, 2, 3, 4, 5]
nums1 = [2,3, 4, 5, 5]
final = list(map(lambda x,y : x + y, nums,nums1))

print(final)