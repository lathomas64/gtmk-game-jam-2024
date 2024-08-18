from ursina import *
from request import Request 
from screens import AestheticScreen, CompositionScreen, SubmitScreen
import random

class HUD(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)
        Request.register_listener(self.process_request_event)
        self.screen = AestheticScreen(parent=self)
        self.order_panel = {}
        self.request_dict = {}
        self.total_score = 0 # can we do something with this?
        self.request_list = ButtonList(self.request_dict, x=-.85, font='VeraMono.ttf', button_height=1.5, popup=0, clear_selected_on_enable=False)

    def input(self, key):
        if key == "r": # for us to reset without resetting the game
            self.screen.disable()
            self.screen = AestheticScreen(parent=self)

    def display_request(self, request):
        self.request_list.disable()
        Request.active_request = request
        # TODO use preexisting text element if it exists instead of creating a new one
        self.request_detail = Text(text=f'Order:\n{request.order_id}\nDetails:\n{request.description}',
             x=window.left.x+.05, y=.45, wordwrap=50, origin=(-.5,.5))
        # DO we want to switch to the aesthetic screen here?

    def process_request_event(self, *args):
        event = args[0]
        if event == "new_request":
            request = args[1]
            #DO STUFF WITH THE REQUEST
            self.request_dict[request.short_id()] = Func(self.display_request,request) # Do something on click later
            self.request_list.button_dict = self.request_dict
        if event == "request_fullfilled":
            request = args[1]
            score = args[2]
            self.total_score += score
            for _ in range(random.randint(1,3)):
                Request(random.randint(1,3))
            del self.request_dict[request.short_id()]
            self.request_list.button_dict = self.request_dict
            self.request_detail.disable()
            self.request_list.enable()
    def close_screen(self):
        if type(self.screen) == AestheticScreen:
            self.screen.disable() #No going back we lose track of aesthetics. TODO fix that please
            self.screen = CompositionScreen(parent=self)
        elif type(self.screen) == CompositionScreen:
            self.screen.disable() 
            self.screen = SubmitScreen(parent=self)