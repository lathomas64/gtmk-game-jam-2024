from ursina import *
from UrsinaExts.extended_panel import ExtendedPanel as WindowPanel
from planet import Planet
from request import Request
from ursina.prefabs.slider import ThinSlider
#from UrsinaExts.extended_panel import ExtendedPanel

# accept shape, change planet shape
class AestheticScreen(Entity):
    def __init__(self, parent):
        super().__init__(parent=parent)
        left = Button(text="<--", x=-.2, scale=.125, parent=self, on_click=self.scroll_left)
        left.text_entity.use_tags = False
        left.text = "<--"
        Button(text="-->", x=.2, scale=.125, parent=self, on_click=self.scroll_right)
        Button(text="accept",y=-.2, scale=.125, color=color.green, parent=self, on_click=parent.close_screen)
        self.planet_index = Planet.shapes.index(Planet.get_planet().shape)
    def scroll_left(self):
        self.planet_index -= 1
        if self.planet_index == -1:
            self.planet_index = len(Planet.shapes) - 1
        Planet.get_planet().set_shape(Planet.shapes[self.planet_index])
    def scroll_right(self):
        self.planet_index += 1
        if self.planet_index == len(Planet.shapes):
            self.planet_index = 0
        Planet.get_planet().set_shape(Planet.shapes[self.planet_index])
    def on_enable(self):
        Planet.get_planet().enable()
    def on_disable(self):
        Planet.get_planet().disable()

class CompositionScreen(Entity):
    def input(self, key):
        if key == "space":
            self.alkali_metals.value = 50
    
    def slider_changed(self, index):
        total = 0
        unchanged_total = 0
        unchanged_sliders = []
        for second_index in range(len(self.sliders)):
            slider = self.sliders[second_index]
            total += slider.value
            if second_index != index:
                unchanged_total += slider.value 
                unchanged_sliders.append(slider)
        if total > 100:
            changed_slider = self.sliders[index]
            remaining = 100 - changed_slider.value
            for slider in unchanged_sliders:
                slider.value = max(((slider.value * remaining) / unchanged_total)-1, 0)
    
    def __init__(self, parent):
        super().__init__(parent=parent)
        elemental_blocks = ["Alkali metals", "Transition metals", "Esoteric materials", "Non-metals", "Halogens", "Metalloids", "Noble Gases"]
        self.sliders = []
        for index in range(len(elemental_blocks)):
            slider = ThinSlider(0,100,parent=self,step=1,y=(index-1) * .07,text=elemental_blocks[index], dynamic=True, on_value_changed=Func(self.slider_changed, index))
            self.sliders.append(slider)
        Button(text="accept",y=-.2, scale=.125, color=color.green, parent=self, on_click=self.finalize)

    def finalize(self):
        planet = Planet.get_planet()
        composition = {}
        for slider in self.sliders:
            composition[slider.label.text] = slider.value
        planet.composition = composition
        self.parent.close_screen() 
    def on_enable(self):
        pass 
    def on_disable(self):
        pass

class BuildScreen(Entity):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.planet = Planet.get_planet()
        self.tool_dict = {
            "Atmosphere Generator": Func(self.planet.add_building, "atmosphere_generator"),
            "Aetheric Condensor": Func(self.planet.add_building, "aetheric_condensor"),
            "Primordial Cauldron": Func(self.planet.add_building, "primordial_cauldron")
        }
        self.tool_list = ButtonList(self.tool_dict,font='VeraMono.ttf',origin=(-.5,0), button_height=1.5, popup=0, clear_selected_on_enable=False)
        print("tool list position:", self.tool_list.position)
        self.tool_list.x = -1
        print("tool list position:", self.tool_list.position)
        self.tool_panel = WindowPanel(
            title="Tools",height=0.25, percentage_y=0, percentage_x=70,
            content=(
                self.tool_list,
            )
        )
        self.tool_panel.panel.scale_y = 5
        print("tool_panel bounds:", self.tool_panel.getTightBounds())
        self.inspector_panel = WindowPanel(
            title="Inspector", percentage_y=50, height=.25, percentage_x=70,
            content=(
                [Text(text="Inspection Details here...")]
            )
        )

    def on_enable(self):
        planet = Planet.get_planet()
        planet.enable()


class SubmitScreen(Entity):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.shipit = Button(text="Ship it!",y=-.2, scale=.125, color=color.red, parent=self, on_click=self.evaluate_planet)
        self.newplanet = Button(text="New Planet",y=-.2, scale=.125, parent=self, on_click=self.parent.close_screen, enabled=False)
        self.score_text = Text(y=.2, parent=self, enabled=False)
    
    def update(self):
        if self.newplanet.enabled or Request.active_request == None:
            self.shipit.disable()
        else:
            self.shipit.enable()
    
    def evaluate_planet(self):
        score = Request.active_request.evaluate_planet()
        self.score_text.text = f'Customer rating of your planet: {score}'
        self.score_text.enable()
        # IDEA: color text based on score value?
        self.newplanet.enable()

    def on_enable(self):
        Planet.get_planet().enable()
    def on_disable(self):
        Planet.get_planet().disable()
