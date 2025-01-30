class Shape:

    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = int(input("Enter length of square: "))
    def area(self):
        print(self.length * self.length)
class Triangle(Shape):
    def __init__(self):
        self.length = int(input("Enter length of triangle: "))
    def area(self):
        print(self.length ** 2 * 1.71 / 4)

while(True):
    print("[1] Create Shape ")
    print("[0] Exit")
    choice = int(input())
    if choice == 1:
        s1 = Shape()
        print("[1] Create square")
        print("[2] Create triangle")
        subchoice = int(input())
        if subchoice == 1:
            s1 = Square()
        elif subchoice == 2:
            s1 = Triangle()
        s1.area()
    elif choice == 0:
        break