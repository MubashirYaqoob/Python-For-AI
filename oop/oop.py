class student:
   # name = "mubashir"
    def __init__(self,fullname) :
        self.name = fullname
        print("addding new student in database...")
    
    

""" Constructor in Python with self parameter
we can pass multiple paramter as a constructor 
aisa data jo hr object ka alg hoga vh instance attribute kehlata he or self se define hota he vh 
if there is some data which may be same for all objecets  are called class attribute """
s1 = student("mubashir") # here we call constructor constructor always take an argument whcich is knows as self parameter
print(s1.name)