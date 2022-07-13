class Flower:
    """Flower class"""
    
    def __init__(self, name, price, petalcount=0):
        """Creates an instance of the flower
        
        name    is the name of the flower
        price   is the amount of the flower
        petalcount  is the amount of petals a flower has default is 0
        """
        
        self._name = name
        self._price = price
        self._petalcount = petalcount
        
    def get_flower(self):
        """Returns name of flower"""
        return self._name
    
    def get_price(self):
        """Returns the price amount of the flower"""
        return self._price
    
    def get_petal_Count(self):
        """Returns the petal count of the flower"""
        return self._petalcount
    
    def change_flower_price(self, amount):
        """Updates the flower price"""
        self._price = amount
        return self._price 
    
    
if __name__ == '__main__':
    
    rose = Flower('Pink rose', 100.00, 30)
    print(rose.get_price())
    rose.change_flower_price(450)
    print(rose.get_price())