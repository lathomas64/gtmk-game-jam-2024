## Entry point into whatever game we make
from UrsinaExts.extended_ursina import create_extended_ursina
from planet import *
from hud import HUD
from request import Request

if __name__ == "__main__":
    app = create_extended_ursina()
    ui = HUD()
    #world = Planet()
    Request()

    window.borderless = False

    app.run()
