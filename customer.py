from order import order


class customer:
    def __init__(self,name):
        self.name = name


        @property
        def name(self):
            return self._name
        

        @name.setter
        def name(self,value):
            if not (value,str):
                raise TypeError ("Name must be a string.")
            if not (1 <=len(value) <=15):
                raise ValueError("Name Must Be Between 1 and 15 characters.")
            
            self.name=value
        def order(self):
          return [order for order in order.all() if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self,coffee,price):

        return order(self,coffee,price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order

        customer_totals = {}

        for order in Order.all():
            if order.coffee == coffee:
                customer = order.customer
                customer_totals[customer] = customer_totals.get(customer, 0) + order.price

        if not customer_totals:
            return None  

        
        return max(customer_totals, key=customer_totals.get)
    

    