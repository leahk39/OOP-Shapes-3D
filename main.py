from shapes3D import Torus 
import math

major_radius = int(input("What is the major radius"))
minor_radius = int(input("What is the minor radius"))

my_torus = Torus(
    "Torus",
    (127, 0, 255),
    (2, 4),
    major_radius,
    minor_radius
)

# Display the results
print("Volume:", my_torus.volume())
print("Surface area:", my_torus.surface_area())
