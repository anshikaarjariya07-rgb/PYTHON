#5.	Write a lambda function to find volume of cone.
import math

volume_cone = lambda r, h: (1/3) * math.pi * r * r * h

print(volume_cone(3,5))