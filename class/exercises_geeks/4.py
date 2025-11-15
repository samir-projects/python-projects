'''
 Create a class MaxFinder that identifies the largest number in a list.
 '''
class Maxfinder:
    def __init__(self,numbers):
        self.numbers=numbers

    def find_max(self):
        if not self.numbers:
            return "The list is empty"
        return max(self.numbers)

max1=Maxfinder([1,43,321,45,23,45,756,65,45,46])
print(max1.find_max())
