from customer import Customer
from coffee import Coffee
from order import order

# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create some coffee
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = order(alice, latte, 3.5)
order2 = order(bob, espresso, 4.0)
order3 = order(alice, latte, 5.0)

# Check associations
print("Alice's coffees:", [c.name for c in alice.coffees()])
print("Latte customers:", [c.name for c in latte.customers()])

# Use class methods
print("Number of orders for Latte:", latte.num_orders())
print("Average price for Latte:", latte.average_price())

# Check most aficionado
most = Customer.most_aficionado(latte)
print("Customer who spent most on Latte:", most.name if most else "None")
