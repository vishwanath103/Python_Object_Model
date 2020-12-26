'''
class Resistor:
    def __init__(self, number, manufacturer, resistance):
        self.number = number
        self.manufacturer = manufacturer
        self.resistance = resistance

    def __repr__(self):
        return f'Resistor({self.number!r}, {self.manufacturer!r}, {self.resistance!r})'

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

# print object in human understable format
print(f'{r = }')
'''

# Create you own protocols and object system
from inspect import signature

class Resistor:
    def __init__(self, number, manufacturer, resistance):
        self.number = number
        self.manufacturer = manufacturer
        self.resistance = resistance

    def __repr__(self):
        fields = signature(self.__init__).parameters
        values = ', '.join(repr(getattr(self,f)) for f in fields)
        return f'{type(self).__name__}({values})'

class Potentiometer(Resistor):
    def __init__(self, number, manufacturer, resistance, min_resistance, max_resistance):
        if not min_resistance <= resistance <= max_resistance:
            raise ValueError('resistance out of bounds')
        self.min_resistance = min_resistance
        self.max_resistance = max_resistance
        super().__init__(number, manufacturer, resistance)

r = Potentiometer('10-232-1412', 'honhai', 15, 10, 20)
print(f'{r = }')

