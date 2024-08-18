from ursina import *
from request import Request 
from screens import AestheticScreen, CompositionScreen, SubmitScreen

class HUD(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)
        Request.register_listener(self.process_request_event)
        self.screen = AestheticScreen(parent=self)
        self.order_panel = {}
        self.request_dict = {}
        self.request_list = ButtonList(self.request_dict, x=-.85, font='VeraMono.ttf', button_height=1.5, popup=0, clear_selected_on_enable=False)


    def display_request(self, request):
        self.request_list.disable()
        Request.active_request = request
        Text(text=f'Order:\n{request.order_id}\nDetails:\n{request.description}',
             x=window.left.x+.05, y=.45, wordwrap=50, origin=(-.5,.5))
        # DO we want to switch to the aesthetic screen here?
        # Do we want a way to go back to the list of requests?

    def process_request_event(self, *args):
        event = args[0]
        if event == "new_request":
            request = args[1]
            #DO STUFF WITH THE REQUEST
            self.request_dict[request.short_id()] = Func(self.display_request,request) # Do something on click later
            self.request_list.button_dict = self.request_dict
    def close_screen(self):
        if type(self.screen) == AestheticScreen:
            self.screen.disable() #No going back we lose track of aesthetics. TODO fix that please
            self.screen = CompositionScreen(parent=self)
        elif type(self.screen) == CompositionScreen:
            self.screen.disable() 
            self.screen = SubmitScreen(parent=self)