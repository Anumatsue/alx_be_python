import math

class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    def __init__(self,length:float, width:float):
        self.length = length
        self.width = width
    def area(self):
        self.area = self.length * self.width
        return self.area
        
    
class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius

    def area(self):
        self.area = self.radius**2 * math.pi
        return self.area
        


    

