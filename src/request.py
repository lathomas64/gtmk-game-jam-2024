import random
import uuid
class Request:
    queue = []
    listeners = []
    aesthetics = ["sphere", "cube", "cone"]
    aesthetic_descriptions = {
        "sphere": ["A silent echo of curvature where every point is both beginning and end.",
                   "A paradoxical line made of countless directions, curving toward unity without yielding any corners.",
                   "A tension of curves pulling in all directions until no edges are left to grasp."],
        "cube": ["A shadowy hex of equal but opposing forces, all in balanced contradiction.",
                 "A collection of flat edges trying to meet in hidden corners, holding invisible space.",
                 "A frozen thought, structured by the equal distance from everywhere, yet stuck between planes."],
        "cone": ["A spiraling descent from a broad horizon, narrowing into an unreachable apex.",
                 "A shape where every angle reaches inward yet remains spread apart in widening contradiction.",
                 "A gradual squeeze from openness to precision, where the broad becomes infinitesimally small."]
    }
    diets = ["meat", "plants", "dead", "minerals", "mana"]
    diet_descriptions = {
        "meat": ["A garden of motion, brimming with trembling sustenance waiting to be silenced.",
                 "A living banquet, teeming with restless forms waiting to surrender to sharper wills.",
                 "A sphere of fleeting warmth wrapped in layers of delectable frailty."],
        "plants": ["A realm where the green breathes freely, offering itself in quiet abundance to those who listen.",
                   "A field of quiet persistence, where the sun feeds the silent symphony of gentle growth.",
                   "A sheltering embrace of still life, where the world ripens slowly, awaiting soft grazes."],
        "dead": ["A haven where the quiet surrender of matter whispers its secrets to those who listen closely.",
                 "A world where life’s remnants linger, inviting the embrace of time’s final dance.",
                 "A domain where the forgotten and the fallen transform into the sweetest essence of life."],
        "minerals": ["A world where the bones of the earth pulse with silent, nourishing density.",
                     "A domain where the hardened veins of the planet stretch in nourishing silence beneath the soil.",
                     "A sphere where the buried echoes of creation offer sustenance in jagged form and sharp purity."],
        "mana": ["A cradle of pure resonance, where the streams of life’s essence flow through invisible channels.",
                 "A sanctuary where the aether shivers with latent vibrations, overflowing with the taste of potential.",
                 "A realm where the air hums with unseen threads of boundless potential, ripe for the taking."]
    }
    def __init__(self):
        self.aesthetic = random.choice(Request.aesthetics)
        self.diet = random.choice(Request.diets)
        sentences = []
        sentences.append(random.choice(Request.aesthetic_descriptions[self.aesthetic]))
        sentences.append(random.choice(Request.diet_descriptions[self.diet]))
        random.shuffle(sentences)
        self.description = " ".join(sentences)
        self.order_id = uuid.uuid4() 
        Request.queue.append(self)
        Request.fire_event("new_request", self)
    
    def short_id(self):
        return hex(self.order_id.node)[2:].zfill(12)

    @classmethod
    def fire_event(cls, event, *args):
        for listener in cls.listeners:
            listener(event, *args)

    @classmethod
    def register_listener(cls, callback):
        cls.listeners.append(callback)