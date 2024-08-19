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
        if hasattr(self, 'size_change_listeners'):
            for listener in self.size_change_listeners:
                listener(new_size)

    window.register_size_change_listener = register_size_change_listener.__get__(window)
    window.unregister_size_change_listener = unregister_size_change_listener.__get__(window)
    window.notify_size_change = notify_size_change.__get__(window)

    # Store the original size getter and setter
    original_size_getter = window.__class__.size.fget
    original_size_setter = window.__class__.size.fset

    @property
    def size(self):
        # Use the original getter to avoid recursion
        return original_size_getter(self)

    @size.setter
    def size(self, value):
        # Use the original setter
        original_size_setter(self, value)
        # Notify listeners after the size has been set
        self.notify_size_change(value)

    # Replace the size property
    window.__class__.size = size
