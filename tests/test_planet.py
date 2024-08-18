import unittest
from planet import Planet
from ursina import Ursina, load_texture
# see https://docs.python.org/3/library/unittest.html

class TestPlanet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Ursina()

    def test_set_shape(self):
        io = Planet.get_planet()
        
        io.set_shape("cube")
        self.assertEqual(str(io.model), 'render/scene/planet/cube')

        io.set_shape("sphere")
        self.assertEqual(str(io.model), "sphere")

        io.set_shape("cone")
        self.assertEqual(str(io.model), "mesh")
    
    def test_get_planet(self):
        mars = Planet.get_planet()
        self.assertEqual(Planet.instance, mars)
        self.assertEqual(str(mars.texture), str(load_texture("perlin_noise")))
        mars.texture="grass"
        mars2 = Planet.get_planet()
        self.assertEqual(mars, mars2)
        self.assertEqual(str(mars2.texture), str(load_texture("grass")))