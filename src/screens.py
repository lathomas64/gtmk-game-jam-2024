from ursina import *
from planet import Planet

class AestheticScreen(Entity):
    def on_enable(self):
        Planet.getPlanet().enable()
    def on_disable(self):
        Planet.getPlanet().disable()