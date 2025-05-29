import math

def calculate_circle_perimeter(radius):
    """Calculate the perimeter (circumference) of a circle."""
    if radius < 0:
        return "Radius cannot be negative."
    perimeter = 2 * math.pi * radius
    return perimeter

try:
    r = float(input("Enter the radius of the circle: "))
    result = calculate_circle_perimeter(r)
    print(f"The perimeter of the circle is: {result}")
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")
