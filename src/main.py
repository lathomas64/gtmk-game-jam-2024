## Entry point into whatever game we make
from ursina import *
from planet import *
from hud import HUD
from request import Request

if __name__ == "__main__":
    app = Ursina()
    ui = HUD()
    #world = Planet()
    Request()
    window.borderless = False
    app.run()

