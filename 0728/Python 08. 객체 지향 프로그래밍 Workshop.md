# Python 08. 객체 지향 프로그래밍 Workshop



### 1. 도형 만들기

    

```python
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Rectangle():
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)

    def get_perimeter(self):
        return (self.p2.x - self.p1.x) + (self.p1.y - self.p2.y)

    def is_square(self):
        if (self.p2.x - self.p1.x) == (self.p1.y - self.p2.y):
            return True
        else:
            return False



p1 = Point(1, 2)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square)

p3 = Point(3, 7) #2
p4 = Point(6, 4) #3
r2 = Rectangle(p3,p4)

print(r2.get_area()) #9
print(r2.get_perimeter()) #6
print(r2.is_square)


```


