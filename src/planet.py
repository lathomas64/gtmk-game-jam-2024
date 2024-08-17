from ursina import *

class Planet(Entity):
    shapes = {
        "cube":"cube",
        "sphere":"sphere",
         "cone": Cone(10)
    }
    instance = None
    def __init__(self):
        self.shape = random.choice(list(Planet.shapes.keys()))
        print(self.shape)
        super().__init__(model=Planet.shapes[self.shape], rotation=30, texture="perlin_noise")

    def update(self):
        self.rotate((0, 10 * time.dt, 0))
    
    @classmethod
    def getPlanet(cls):
        if cls.instance == None:
            cls.instance = Planet()
        return cls.instance
