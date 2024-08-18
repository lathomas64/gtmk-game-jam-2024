from ursina import Ursina
from ursina import window
from UrsinaExts.extended_window import ExtendedWindow

def create_extended_ursina(*args, **kwargs):
    app = Ursina(*args, **kwargs)
    
    # Create a new instance of ExtendedWindow
    extended_window = ExtendedWindow()
    
    # Update the existing window instance with our extended functionality
    for attr, value in extended_window.__dict__.items():
        if not attr.startswith('__'):  # Skip Python special attributes
            setattr(window, attr, value)
    
    return app
