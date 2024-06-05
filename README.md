# Shape Calculator
This Python script allows the user to calculate the area and perimeter of a rectangle, as well as the volume of a parallelepiped. The program continuously prompts the user to select a shape and input the necessary dimensions to perform the calculations

## Classes
### Rectangle
The Rectangle class represents a rectangle and provides methods to calculate its perimeter and area.

#### Methods
  -  __init__(self, length, width): Initializes the rectangle with its length and width.
  -  perimeter(self): Calculates the perimeter of the rectangle.
  -  area(self): Calculates the area of the rectangle.

### Parallelepiped
The Parallelepiped class inherits from the Rectangle class and represents a parallelepiped. It adds an additional dimension (height) and provides a method to calculate its volume.

#### Methods
  -  __init__(self, length, width, height): Initializes the parallelepiped with its length, width, and height. Calls the Rectangle constructor to set the length and width.
  -  volume(self): Calculates the volume of the parallelepiped.
