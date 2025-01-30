class Car:
    def __init__(self, make=None, model=None, year=None, price=None):
        """Default and parameterized constructor"""
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}")

    def apply_discount(self, discount_percent):
        if self.price:
            discount_amount = self.price * (discount_percent / 100)
            self.price -= discount_amount
            print(f"New price after {discount_percent}% discount: ${self.price}")
        else:
            print("Price not set.")
