class Student :
    def __init__(self,name,marks) :
        self.name = name
        self.marks = marks
 
    def get_avg(self) :
     sum = 0
     for i in self.marks :
        sum += i
        print("your marks is ",sum/3)

s1 = Student("mubashir",[90,45,32])
s1.get_avg()