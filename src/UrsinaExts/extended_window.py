from ursina.window import Window

class ExtendedWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("extended window called...")
        self.original_size = Window.size

    def register_size_change_listener(self, listener):
        if not hasattr(self, 'size_change_listeners'):
            self.size_change_listeners = []
        self.size_change_listeners.append(listener)

    def unregister_size_change_listener(self, listener):
        if hasattr(self, 'size_change_listeners'):
            self.size_change_listeners.remove(listener)

    def notify_size_change(self, new_size):
        if hasattr(self, 'size_change_listeners'):
            for listener in self.size_change_listeners:
                listener(new_size)
    
    def update_aspect_ratio(self):
        super().update_aspect_ratio()
        self.notify_size_change(self.size)