

from shapes3D import Torus 
from shapes3D import Cone
import math

major_radius = int(input("What is the major radius of the torus: "))
minor_radius = int(input("What is the minor radius of the torus: "))

radius = int(input("What is the radius of the cone: "))
height = int(input("What is the height of the cone: "))

my_torus = Torus(
    "Torus",
    (127, 0, 255),
    (2, 4, 6),
    major_radius,
    minor_radius,
)

my_cone = Cone(
    "Cone",
    (255, 0, 0),
    (0, 5, 0),
    radius,
    height
)

# Display the results
print("\nThis is your torus:")
print("Volume:", my_torus.volume())
print("Surface area:", my_torus.surface_area())
print("Colour:", my_torus.get_colour())
print("Location:", my_torus.get_location())
print("Draw:", my_torus.draw())
print("\n")

print("This is your cone:")
print("Volume:", my_cone.volume())
print("Surface area:", my_cone.surface_area())
print("Colour:", my_cone.get_colour())
print("Location:", my_cone.get_location())
print("Draw:", my_cone.draw())
