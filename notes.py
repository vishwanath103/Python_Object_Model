class Resistor:
    def __init__(self, number, manufacturer, resistance):
        self.number = number
        self.manufacturer = manufacturer
        self.resistance = resistance

r = Resistor('10-232-1412', 'honhai', 10)
print(f'{r.__dict__ = }')

from sys import getsizeof
print(f'{getsizeof(Resistor(None,None,None)) = }')

# put things into a restricted computation domain which might look like a manager class

from pandas import DataFrame
class Resistor:
    def __init__(self, number, manufacturer, resistance):
        self.number = number
        self.manufacturer = manufacturer
        self.resistance = resistance

class Product:
    def __init__(self, *components):
        self.components = DataFrame([
            [x.manufacturer, x.resistance]
            for x in components
            ], columns=['manufacturer', 'resistance'], index=[x.number for x in components])

    def __getitem__(self, number):
        x = self.components.loc[number]
        return Resistor(number, x.manufacturer, x.resistance)

p = Product(Resistor('10-423-1234', 'honhai', 1),
            Resistor('10-423-1249', 'samsung', 5),
            Resistor('10-423-1230', 'honhai', 10))

print(f'{p.components.resistance.mean() = }')
print(f'{p["10-423-1234"] = }')
