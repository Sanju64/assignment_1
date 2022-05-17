# class Sanju:
#     d = 12
#     print("this is sanju")
#     def display(self):
#         a = 10
#         b = 20
#         print(a,b)
# obj = Sanju()
# obj.display()
# print(obj.d)


class Mobile:
    def __init__(self, Brand,ram,camera,price):
        self.Brand = Brand
        self.ram = ram
        self.camera = camera
        self.price = price
    def display(self):
        print("Brand :",self.Brand)
        print("Ram :",self.ram)
        print("Camera :",self.camera)
        print("Price :",self.price)


obj1 = Mobile ("Samsung","12Gb","60MP","60K")
obj1.display()
obj1 = Mobile ("Apple","8Gb","30MP","100K")
obj1.display()
obj1 = Mobile ("Samsung","12Gb","60MP","60K")
obj1.display()
obj1 = Mobile ("Apple","8Gb","30MP","100K")
obj1.display()