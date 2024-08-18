from ursina import *

class Planet(Entity):
    shapes = ["cube","sphere","cone"]
    instance = None
    def __init__(self):
        self.shape = random.choice(Planet.shapes)
        super().__init__(rotation=30, texture="perlin_noise")
        self.set_shape(self.shape)

    def update(self):
        self.rotate((0, 10 * time.dt, 0))
    
    def set_shape(self, shape):
        self.shape = shape
        match shape:
            case "cone":
                self.model = Cone(10)
            case _:
                self.model = self.shape
    
    @classmethod
    def get_planet(cls):
        if cls.instance == None:
            cls.instance = Planet()
        return cls.instance
