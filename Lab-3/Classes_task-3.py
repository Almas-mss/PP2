class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("Enter length of rectangle: "))
        self.width = int(input("Enter width of rectangle: "))

    def area(self):
        print(self.length * self.width)

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
        print("[3] Create rectangle")
        subchoice = int(input())
        if subchoice == 1:
            s1 = Square()
        elif subchoice == 2:
            s1 = Triangle()
        elif subchoice == 3:
            s1 = Rectangle()
        s1.area()
    elif choice == 0:
        break