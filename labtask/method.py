class Book :
    def __init__(self,title,author):
        self.title = title
        self.author = author
    

    def display(self):
        print(self.author)
        print("\n",self.title)


b1 = Book("My home","Mubashir yaqoob")
b1.display()