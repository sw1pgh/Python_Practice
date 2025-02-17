# Create a class (2-D Vector) and use it to create another class representing a 3-D vector

class _2DVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show_2D_Vector(self):
        print(f"2D Vector is: {self.i}i + {self.j}j")
        
class _3DVector(_2DVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show_3D_Vector(self):
        print(f"3D Vector is: {self.i}i + {self.j}j + {self.k}k")
        
_2Dobj = _2DVector(1, 2)
_2Dobj.show_2D_Vector()

_3Dobj = _3DVector(1, 2, 3)
_3Dobj.show_3D_Vector()