## Entry point into whatever game we make
from UrsinaExts.extended_ursina import ExtendedUrsina, window
from planet import *
from hud import HUD
from request import Request
import random

if __name__ == "__main__":
    app = ExtendedUrsina()
    ui = HUD()
    #world = Planet()
    for i in range(random.randint(1,3)):
        Request()

    window.borderless = False

    app.run()
