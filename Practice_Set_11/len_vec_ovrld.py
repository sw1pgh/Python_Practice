# Override the __len__() method on vector of Problem 5 to display the dimension of the Vector

class Vector:
    def __init__(self, list):
        self.list = list
    
    def __len__(self):
        return len(self.list)


Vector_1 = Vector([1, 2, 3])

print(f"Length of Vector_1: {len(Vector_1)}")