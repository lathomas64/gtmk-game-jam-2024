from ursina import Ursina, window
from UrsinaExts.extended_window import extend_window

def create_extended_ursina(*args, **kwargs):
    app = Ursina(*args, **kwargs)
    extend_window(window)
    return app
