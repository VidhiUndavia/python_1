class area:
    def computeArea(self,length=None,width=None):
        if length!=None and width!=None:
            print("Area of rectangle = ",length*width)
        elif length!=None:
            print("Area of Square = ",length*length)
        else:
            print("Invalid input")

a1=area()
a1.computeArea()
a1.computeArea(45)
a1.computeArea(20,30)
