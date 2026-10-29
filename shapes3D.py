import math

class Shape3D:
    # methods
    def volume(self):
        return None

    def surface_area(self):
        return None

    # constructor
    def __init__(self, type, colour, location):
        self.type = type
        self.colour = colour
        self.location = location

    # getters
    def get_type(self):
        return self.type
    
    def get_colour(self):
        return self.colour
    
    def get_location(self):
        return self.location

    # setters
    def set_type(self, type):
        self.type = type

    def set_colour(self, colour):
        self.colour = colour

    def set_location(self, location):
        self.location = location 

    def draw(self):
        return None
        


class Torus(Shape3D):
    # constructors
    def __init__(self, type, colour, location, major_radius, minor_radius):
        self.major_radius = major_radius
        self.minor_radius = minor_radius
        super().__init__(type, colour, location)
        
    def surface_area(self):
        surface_area = 4*math.pi**2*self.major_radius*self.minor_radius
        return surface_area
        
    def volume(self):
        volume = 2*math.pi**2*self.major_radius*self.minor_radius**2
        return volume
        
    # getters
    def get_major_radius(self):
        return self.major_radius
        
    def get_minor_radius(self):
        return self.minor_radius
        
    # setters
    def set_major_radius(self, major_radius):
        self.major_radius = major_radius
        
    def set_minor_radius(self, minor_radius):
        self.minor_radius = minor_radius
