import math

radius = float(input("Enter a radius of a circle in cm: "))
circumference = radius * 2 * math.pi
area = radius * radius * math.pi

print(f"The circumference of this circle is "
      f"{round(circumference,2)}cm and the "
      f"area is {round(area,2)}cm^2")