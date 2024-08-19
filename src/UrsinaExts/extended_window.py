from ursina import Vec2

def extend_window(window):
    def register_size_change_listener(self, listener):
        if not hasattr(self, 'size_change_listeners'):
            self.size_change_listeners = []
        self.size_change_listeners.append(listener)

    def unregister_size_change_listener(self, listener):
        if hasattr(self, 'size_change_listeners'):
            self.size_change_listeners.remove(listener)

    def notify_size_change(self, new_size):
        print("Notifying size change listeners")
        if hasattr(self, 'size_change_listeners'):
            for listener in self.size_change_listeners:
                listener(new_size)

    window.register_size_change_listener = register_size_change_listener.__get__(window)
    window.unregister_size_change_listener = unregister_size_change_listener.__get__(window)
    window.notify_size_change = notify_size_change.__get__(window)

    # Store the original size getter and setter
    original_size = window.__class__.size

    def size_getter(self):
        return original_size.__get__(self)

    def size_setter(self, value):
        original_size.__set__(self, value)
        self.notify_size_change(value)

    # Create a new property with our custom getter and setter
    new_size_property = property(size_getter, size_setter)

    # Set the new property on the window instance
    setattr(window.__class__, 'size', new_size_property)
