class marks :
    def __init__(self,marks1,marks2,marks3):
        self.m = marks1
        self.m1 = marks2
        self.m3 = marks3


    def average(self) :
        sum = self.m + self.m1 + self.m3
        avg = sum / 3
        print(f"Average of this student is {avg}")

s1 = marks(10,20,30)
s1.average()