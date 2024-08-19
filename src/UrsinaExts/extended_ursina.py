from ursina import Ursina
from ursina import window
from UrsinaExts.extended_window import ExtendedWindow
import types

def create_extended_ursina(*args, **kwargs):
    print("Creating extended ursina")
    app = Ursina(*args, **kwargs)
    
    # Create a new instance of ExtendedWindow
    extended_window = ExtendedWindow()
    
    # Update the existing window instance with our extended functionality
    for attr, value in extended_window.__dict__.items():
        if not attr.startswith('__'):  # Skip Python special attributes
            setattr(window, attr, value)
    
    # Properly bind the methods to the window instance
    setattr(window, 'register_size_change_listener', 
            types.MethodType(ExtendedWindow.register_size_change_listener, window))
    setattr(window, 'unregister_size_change_listener', 
            types.MethodType(ExtendedWindow.unregister_size_change_listener, window))
    
    # Ensure the size_change_listeners attribute exists
    if not hasattr(window, 'size_change_listeners'):
        window.size_change_listeners = []
    
    print("Register method: ", window.register_size_change_listener)
    return app
