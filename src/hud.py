from ursina import *
from request import Request 
from screens import AestheticScreen

class HUD(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)
        Request.register_listener(self.process_request_event)
        self.screen = AestheticScreen()
        self.order_panel = {}
        self.request_dict = {}
        self.request_list = ButtonList(self.request_dict, x=-.85, font='VeraMono.ttf', button_height=1.5, popup=0, clear_selected_on_enable=False)


    def display_request(self, request):
        self.request_list.disable()
        a = Text(text=f'Order:\n{request.order_id}\nDetails:\n{request.description}',
             x=window.left.x+.05, y=.45, wordwrap=50, origin=(-.5,.5))

    def process_request_event(self, *args):
        event = args[0]
        if event == "new_request":
            request = args[1]
            #DO STUFF WITH THE REQUEST
            self.request_dict[request.short_id()] = Func(self.display_request,request) # Do something on click later
            self.request_list.button_dict = self.request_dict
            print(self.request_dict)
            print(self.request_list.button_dict)