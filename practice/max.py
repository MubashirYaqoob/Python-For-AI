num = int(input("Enter first number"))
print("You enter this ",num)

num2 =int(input("Enter any second number"))
print("You entered this ",num2)

num3 = int(input("Enter any third number"))
print("you entered this number",num3)


# now we are finding largest number 
maxnum =  num
if maxnum <= num2 :
    maxnum = num2
    print("max number is ",maxnum)
elif maxnum <= num3:
    maxnum = num3
    print("max number is ",maxnum)
else :
    print("max number is ",maxnum)