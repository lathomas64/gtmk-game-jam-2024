from ursina.window import Window as UrsinaWindow

class ExtendedWindow(UrsinaWindow):
    def __init__(self):
        super().__init__()
        self.size_change_listeners = []

    def register_size_change_listener(self, entity):
        if entity not in self.size_change_listeners:
            self.size_change_listeners.append(entity)

    def unregister_size_change_listener(self, entity):
        if entity in self.size_change_listeners:
            self.size_change_listeners.remove(entity)

    @property
    def size(self):
        return super().size

    @size.setter
    def size(self, value):
        old_size = self.size
        super(CustomWindow, self.__class__).size.fset(self, value)
        if old_size != value:
            self.notify_size_change(value)

    def notify_size_change(self, new_size):
        for entity in self.size_change_listeners:
            if hasattr(entity, 'on_window_resize'):
                entity.on_window_resize(new_size)
