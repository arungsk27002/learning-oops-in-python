class Order:
    def __init__(self,items,price):
        self.items=items
        self.price =price
        
    def __gt__(self,order2):
        return self.price>order2.price
order1=Order("apple",200)
order2=Order("orange",150)
print(order1>order2)