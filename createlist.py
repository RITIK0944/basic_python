class MeraList:
    def __init__(self):
        self.size=1
        self.n=0
        # create a C type array with size = self.size
        self.A= self.__make_array(self.size)
    def __len__(self):
        return self.n
    def append(self,item):
        return self
    def __make_array(self, capacity):
        # create a C type array(ststic,referential) with size capacity
        return (capacity * ctypes.py_object)()
    l= [10,20,30,40,20]
    print(len(MeraList()))

    print(len(l))