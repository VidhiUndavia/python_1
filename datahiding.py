class myclass:
    __num=0
    num2=0
    def increment(self,inc):
        self.__num+=1
        self.num2+=inc
        print("Num1 = ",self.__num)
        print("Num2 = ",self.num2)
m1=myclass()
m1.increment(2)
print("----------------------------------")
print("Num2 = ",m1.num2*m1.num2)
print("Num2 = ",m1._myclass__num)
