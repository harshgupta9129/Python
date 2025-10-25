class vector_2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class vector_3d(vector_2d):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

v1 = vector_3d(1,2,3)
print(f"{v1.x}i + {v1.y}j + {v1.z}k")