#palindrome method 

pln = [1,2,3] #List 


copy = pln.copy() # this will create the shallow copy of list 

copy.reverse()

if(pln == copy) :
    print("this is palindrome ")
else:
    print("This is not palindrome")
