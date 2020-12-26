# Python Object Model

A repo to maintain the code for learning Python Object Module referred from <a href="https://www.youtube.com/watch?v=AmHE0kZhLIQ&ab_channel=CodingTech">Objectionable Content - James Powel</a>

## Key Learnings
1. Python object consumes lot of memory as there is lot of overhead
    1. To get performance back build a manager to separate computation domain
    2. In the example, "Resistor" is a business entity which is not needed for computation
    3. "Product" class represents a computation entity
        1. Takes a list of enities (Resistor)
        2. Extracts the information and stores in a Dataframe, which enables to perform operations effeciently
        3. __getitem__ constructs the entity(Resistor) for the required product
2. Basic Object Model
    1. To implement protocols
    2. __repr__ method to give a human understanble representation
    3. We can use signature method from inspect module to identify the class and its respective feilds to be printed out (helpful in printing subclasses)
3. Usage of dataclasses
    1. Module to automatically add generated special methods such as __init__() and __repr__() to the user defined classes
	
