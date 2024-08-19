from ursina.prefabs.window_panel import WindowPanel
from ursina import  ThinSlider, camera, ButtonList
from ui_utils import percentage_to_x_coordinate, percentage_to_y_coordinate
from UrsinaExts.extended_ursina import window

class ExtendedPanel(WindowPanel):
    def __init__(self, **kwargs):
        self.percentage_x = kwargs.get('percentage_x', None)
        self.percentage_y = kwargs.get('percentage_y', None)
        super().__init__(**kwargs)

        window.register_size_change_listener(self.on_window_resize)

    def on_window_resize(self, new_size):
        self.layout()

    def on_destroy(self):
        window.unregister_size_change_listener(self)

    def layout(self):
        super().layout()
        for c in self.content:
            if isinstance(c, ButtonList):
                c.x = -.5 # Magic Numbers for Ada
        print(self.x, self.percentage_x, self.percentage_x is not None)
        print(percentage_to_x_coordinate(self.percentage_x))
        self.x = percentage_to_x_coordinate(self.percentage_x) if self.percentage_x is not None else self.x 
        print(self.x)
        self.x += window.aspect_ratio * (self.world_scale_x / 36) / 2
        print(self.x)
        self.y = percentage_to_y_coordinate(self.percentage_y) if self.percentage_y is not None else self.y
        #print (self.x)

