from queue import Empty


class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """
    
    def __init__(self):
        self.container = []
        
    def add(self, value: int) -> None:
        """
        Adds the specified value to the container

        :param value: int
        """
        # TODO: implement this method
        if value > 0:
            self.container.append(value)
        return self.container
    
    
    def delete(self, value: int):
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        # TODO: implement this method
        self.value = value
        if self.value in self.container:
            self.container.remove(self.value)
            return True
        return False

    def get_median(self):
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle 
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        from statistics import median
        
        if self.container:
            self.container.sort()
            medianNumb = median(self.container)
            print("sorte", self.container)
            return medianNumb
        else:
            return None
        


container = Container()
# print(container.add(3))
# print(container.add(2))
# print(container.add(4))
# print(container.add(5))
# print(container.add(5))
# print(container.add(7))
# print(container.delete(8))
print(container.get_median())


