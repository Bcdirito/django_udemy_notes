# Example

class Dog():
    
    # Class Object Attributes
    # Always go up top
    species = "Mammal"

    # initializing with attributes
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


# can be done without mass assignment
my_dog = Dog("German Shepherd", "Louis")

# can be done with mass assignment
other_dog = Dog(breed = "Huskie", name="Hughie")

print(my_dog.breed, my_dog.species)
print(other_dog.name)


# Example 2

class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius**2

    def set_radius(self, new_r):
        self.radius = new_r
        
default_circle = Circle()
print(default_circle.radius)

my_circle = Circle(3)
print(my_circle.area())