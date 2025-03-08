class FiveFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing")
    def OddEven():
        num = int(input("Enter a number:"))
        if(num%2==1):
            print(num, "is Odd number")
        else:
            print(num, "is Even number")
    def Elegible():
        Gender = input("Enter the gender:")
        age = int(input("Enter the age:"))
        if((Gender =="Male")&(age>=21)):
            print("ELIGIBLE")
        elif((Gender =="Female")&(age>=18)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def percentage(): 
        SUB1 = int(input("Subject1 ="))
        SUB2 = int(input("Subject2 ="))
        SUB3 = int(input("Subject3 ="))
        SUB4 = int(input("Subject4 ="))
        SUB5 = int(input("Subject5 ="))
        Total= SUB1+SUB2+SUB3+SUB4+SUB5
        print("Total :",Total)
        Per = Total/5;
        print("Percentage :", Per)
    def triangle():
        Height= int(input("Height:"))
        Breadth= int(input("Breadth:"))
        Area = (Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",Area)
        Height1= int(input("Height1:"))
        Height2= int(input("Height2:"))
        Breadth1= int(input("Breadth1:"))
        Perimeter_formula = Height1+Height2+Breadth1
        print("Perimeter formula: Height1+Height2+Breadth1")
        print("Perimeter of Triangle:",Perimeter_formula)    