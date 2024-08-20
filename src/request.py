import random
import uuid
from planet import Planet
class Request:
    queue = []
    listeners = []
    active_request = None
    criteria = {
        "aesthetic": {
            "sphere": ["A silent echo of curvature where every point is both beginning and end.",
                   "A paradoxical line made of countless directions, curving toward unity without yielding any corners.",
                   "A tension of curves pulling in all directions until no edges are left to grasp."],
            "cube": ["A shadowy hex of equal but opposing forces, all in balanced contradiction.",
                 "A collection of flat edges trying to meet in hidden corners, holding invisible space.",
                 "A frozen thought, structured by the equal distance from everywhere, yet stuck between planes."],
            "cone":["A spiraling descent from a broad horizon, narrowing into an unreachable apex.",
                 "A shape where every angle reaches inward yet remains spread apart in widening contradiction.",
                 "A gradual squeeze from openness to precision, where the broad becomes infinitesimally small."],
        },
        "diet": {
            "meat": ["A garden of motion, brimming with trembling sustenance waiting to be silenced.",
                 "A living banquet, teeming with restless forms waiting to surrender to sharper wills.",
                 "A sphere of fleeting warmth wrapped in layers of delectable frailty."],
            "plants":["A realm where the green breathes freely, offering itself in quiet abundance to those who listen.",
                   "A field of quiet persistence, where the sun feeds the silent symphony of gentle growth.",
                   "A sheltering embrace of still life, where the world ripens slowly, awaiting soft grazes."],
            "dead":["A haven where the quiet surrender of matter whispers its secrets to those who listen closely.",
                 "A world where life’s remnants linger, inviting the embrace of time’s final dance.",
                 "A domain where the forgotten and the fallen transform into the sweetest essence of life."],
            "minerals":["A world where the bones of the earth pulse with silent, nourishing density.",
                     "A domain where the hardened veins of the planet stretch in nourishing silence beneath the soil.",
                     "A sphere where the buried echoes of creation offer sustenance in jagged form and sharp purity."],
            "mana":["A cradle of pure resonance, where the streams of life’s essence flow through invisible channels.",
                 "A sanctuary where the aether shivers with latent vibrations, overflowing with the taste of potential.",
                 "A realm where the air hums with unseen threads of boundless potential, ripe for the taking."]
        },
        "leisure": {
            "beach": ["A space for glittering edifices overlooking vast planes of aquamarine."]
        }
    }
    def __init__(self, criteria_count = 2):
        self.order_criteria = random.sample(list(Request.criteria), criteria_count)        
        for criterion in self.order_criteria:
            self.add_criteria(criterion)
        self.generate_description()
        self.order_id = uuid.uuid4() 
        Request.queue.append(self)
        Request.fire_event("new_request", self)
    
    def add_criteria(self, criterion):
        setattr(self, criterion, random.choice(list(Request.criteria[criterion])))
    
    def get_sentence(self, criterion, value):
        return random.choice(Request.criteria[criterion][value])
    
    def generate_description(self):
        sentences = []
        for criterion in self.order_criteria:
            sentence = self.get_sentence(criterion, getattr(self, criterion))
            sentences.append(sentence)
        random.shuffle(sentences)
        self.description = " ".join(sentences)

    def short_id(self):
        return hex(self.order_id.node)[2:].zfill(12)

    def evaluate_planet(self):
        score = 0
        for criterion in self.order_criteria:
            value = getattr(self, criterion) #meat, plants, cone, cube
            score += self.evaluate_criteria(criterion, value)
        score /= len(self.order_criteria) # flat average should this be weighted?
        Request.active_request = None
        Request.fire_event("request_fullfilled", self, score)
        return score
    
    def evaluate_criteria(self, criterion, value):
        # Planet.get_planet() why pass it in?
        planet = Planet.get_planet()
        match criterion:
            case "aesthetic":
                if value == planet.shape:
                    return 100
                else:
                    return 0
            case "diet":
                match value:
                    case "meat":
                        return min(100, planet.biomass/100)
                    case "plants":
                        return min(100, planet.biomass/10)
                    case "dead":
                        return min(100, planet.biomass/100)
                    case "minerals":
                        return 50 #Not sure what to do here?
                    case "mana":
                        return min(100, planet.composition["Esoteric materials"] * planet.aether/1000)
            case _:
                return 50

    @classmethod
    def fire_event(cls, event, *args):
        for listener in cls.listeners:
            listener(event, *args)

    @classmethod
    def register_listener(cls, callback):
        cls.listeners.append(callback)