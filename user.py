#read JSON file to objects
class User:
    def __init__(self):
        self.uid = "-1"
        self.type = "donor"
        self.name = "Llama"
        self.supplyType = "mask"
        self.supplyNumber = "8"
        self.addr = "3411 Chestnut Stree"
        self.tel = "6786467287"
        self.email = "pqy@seas.upenn.edu"
        self.info = "Hi"
    
    def setAll(self, usrtype, name, supplyT, supplyN, addr, tel, email, info = "N/A"):
        self.type = usrtype
        self.name = name
        self.supplyType = supplyT
        self.supplyNumber = int(supplyN)
        self.addr = addr
        self.tel = tel
        self.email = email
        self.info = info
    
    def setUid(self, uid):
        self.uid = uid
    
    def intro(self):
        print("Hello! I'm " + self.name + " and I'm a " + self.type)

    def give(self, supplyType, n):
        num = int(self.supplyNumber)
        self.supplyNumber = str(num - n)
    
    def receive(self, supplyType, n):
        num = int(self.supplyNumber)
        self.supplyNumber = str(num + n)

def test():
    user = User()
    user.intro()
    print("I have " + user.supplyNumber + " " + user.supplyType)
    user.give("mask", 2)
    print("Now I have " + user.supplyNumber + " " + user.supplyType)
