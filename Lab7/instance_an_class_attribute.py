class Product:

    tax_rate = 2.5

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def product_with_tax(self):
        tax_amount = self.price * self.tax_rate/100
        return self.price + tax_amount


product1 = Product("Laptop", 1999)
product2 = Product("Mouse", 300)
product3 = Product("PenDrive", 780)

print("Before tax rate update: Price with Tax rate:", product1.product_with_tax(),
      product2.product_with_tax(), product3.product_with_tax())

Product.tax_rate = 10

print("After Tax rate update: Price with Tax: ", product1.product_with_tax(),
      product2.product_with_tax(), product3.product_with_tax())

product3.tax_rate = 9.2

print("Different tax rate:", product1.tax_rate,
      Product.tax_rate, product3.tax_rate)
