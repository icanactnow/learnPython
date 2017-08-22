from django.test import TestCase

# Create your tests here.
class Shuxing():
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize)
t  = Shuxing(100)
print(t.x)
print(t.getSize())