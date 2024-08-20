from ursina import *

class Planet(Entity):
    shapes = ["cube","sphere","cone"]
    instance = None
    def __init__(self):
        self.shape = random.choice(Planet.shapes)
        super().__init__(rotation=30, texture="perlin_noise")
        self.set_shape(self.shape)
        self.buildings = {}
        self.atmosphere = 0
        self.aether = 0
        self.biomass = 0

    def update(self):
        self.rotate((0, 10 * time.dt, 0))
        if "atmosphere_generator" in self.buildings:
            self.atmosphere += time.dt * self.buildings["atmosphere_generator"]
        if "aetheric_condensor" in self.buildings:
            self.aether += time.dt * self.buildings["aetheric_condensor"]
        if "primordial_cauldron" in self.buildings:
            self.biomass += time.dt * self.buildings["primordial_cauldron"]
        if len(self.buildings) > 0:
            print(self.atmosphere, self.aether, self.biomass)
    
    def set_shape(self, shape):
        self.shape = shape
        match shape:
            case "cone":
                self.model = Cone(10)
            case _:
                self.model = self.shape
    
    def add_building(self, name):
        if name not in self.buildings:
            self.buildings[name] = 1
        else:
            self.buildings[name] += 1
    def reset_resources(self):
        self.buildings = {}
        self.atmosphere = 0
        self.aether = 0
        self.biomass = 0
        #TODO maybe a resources dictionary like buildings?
    @classmethod
    def get_planet(cls):
        if cls.instance == None:
            cls.instance = Planet()
        return cls.instance
