class Fibs:
    def __init__(self):
        self.a=1
    def __iter__(self):
        return self
    def __next__(self):
        return self.a+1
    
