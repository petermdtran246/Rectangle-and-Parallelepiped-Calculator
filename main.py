class Rectangle():

    # Initialize the rectangle with its length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Calculates the perimeter of the rectangle
    def perimeter(self):
        return 2* (self.length+ self.width)

    # Calculates the area of the rectangle
    def area(self):
        return self.width * self.length

# Child class Parallelepiped inheriting from Rectangle
class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        # Calls the Rectangle constructor
        super().__init__(length, width)
        self.height = height
    # Calculates the volume of the parallelepiped
    def volume(self):
        return self.length * self.width * self.height

# Prompts the user to select a shape in a loop
while 1:
    print(f'Select a shape Rectangle or Parallelepiped: ')
    choice = input().lower()

    # Check if the user's choice is rectangle
    if choice == 'rectangle':
        # Prompt user to input numbers
        length = int(input('Input a Length: '))
        width = float(input('Input a Width: '))
        # Create an object to access the class
        rectangle = Rectangle(length, width)
        # Print area of the rectangle
        print(f'Rectangle Area is: {int(rectangle.area())}')
        # Print perimeter of the rectangle
        print(f'Rectangle Perimeter is: {int(rectangle.perimeter())}\n')
    # Check if the user's choice is parallelepiped
    elif choice == 'parallelepiped':
        length = int(input('Input a Length: '))
        width = float(input('Input a Width: '))
        height = int(input('Input a Height: '))
        parallelepipe = Parallelepiped(length, width, height)
        print(f'Parallelepiped Volume is: {int(parallelepipe.volume())}\n')
    # Check if the user's choice is invalid
    else:
        print('Invalid input. Please enter Rectangle or Parallelepiped')










