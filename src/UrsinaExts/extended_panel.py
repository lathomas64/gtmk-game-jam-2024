from ursina.prefabs.window_panel import WindowPanel
from ursina import window

class ExtendedPanel(WindowPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        window.register_size_change_listener(self)

        self.percentage_width = kwargs.get('percentage_width', None)

    def on_window_resize(self, new_size):
        self.layout()

    def on_destroy(self):
        window.unregister_size_change_listener(self)

    def layout(self):
        super().layout()
        if (self.percentage_x):
            self.x = self.percentage_x * window.size[0]
        
