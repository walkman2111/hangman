class Rectangle:
    recs = []
    def __init__(self,w,l):
        self.width = w
        self.length = l
        self.recs.append((self.width,self.length))
    def print_size(self):
        print("{} by {} ." .format(self.width,self.length))

r1 = Rectangle(10,24)
r2 = Rectangle(20,40)
r3 = Rectangle(100,200)

print(Rectangle.recs)
print(r1.recs)



class Square():
    square_list = []
    def __init__(self,w):
        self.width = w
        self.square_list.append(self)
    def __repr__(self):
        return "{}by{}by{}by{}".format(self.width,self.width,self.width,self.width)
    def calculate_primeter(self):
        primeter = self.width**2
        return primeter
    def change_size(self,value):
        self.width += value

s1 = Square(10)
s2 = Square(20)
print(s1)
print(Square.square_list)

def same_obj_checker(param1,param2):
    print(param1 is param2)

same_obj_checker(s1,s1)
same_obj_checker(s1,s2)