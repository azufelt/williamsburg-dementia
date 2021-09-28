import math
print()
print('This program computes and outputs the volume of tires')
print()
width=float(input('Enter the width of the tire in mm (ex205);'))
ratio=float(input('Enter the aspect ratio of the tire (ex 60):'))
diameter=float(input('Enter the diameter of the wheel in inches (ex 15):'))

(f'The area of the circle is: {float (math.pi * (width ** 2))} mm^2 or {float ((math.pi * (diameter ** 2)) * 1/10000)}')