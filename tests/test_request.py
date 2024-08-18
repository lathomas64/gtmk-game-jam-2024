import unittest
from request import Request
from ursina import Ursina, load_texture
# see https://docs.python.org/3/library/unittest.html

class TestRequest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Ursina()
    
    def process_event(self, *args):
        event = args[0]
        request = args[1]
        self.assertEqual(event, "new_request") # TODO this should start failing once we have new events update the test
        self.assertIsInstance(request, Request)
        self.event_processed = True


    def test_events(self):
        self.event_processed = False
        Request.register_listener(self.process_event)
        Request()
        self.assertTrue(self.event_processed)

    def test_init(self):
        request = Request()
        self.assertIn(request.aesthetic, Request.aesthetics)
        self.assertIn(request.diet, Request.diets)
        self.assertEqual(len(request.description.split(".")), 3) # EXPECTED: sentences + 1
        self.assertIn(request, Request.queue)