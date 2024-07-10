class User:
    
    def __init__(self, firstname):
        print("Имя: " + firstname) 

    def Lastname(self, lastname):
        print("Фамилия: "+ lastname)
    
    def FullName(self, fullname):
        print("Имя и Фамилия: " + fullname)
                 
User1 = User("Kate")
User1.Lastname("Strong")
User1.FullName("Kate" + " " + "Strong")   


