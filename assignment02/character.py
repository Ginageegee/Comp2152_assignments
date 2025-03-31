import random

class Character:

    #constructor
    def __init__(self,role):
        # shared properties that are inherited by monster and hero
        self._combat_strength = random.randint(1, 7)
        self._health_points = random.randint(1, 20)
        self.role = role

    #getter for combat_strength
    @property
    def combat_strength(self):
        return self._combat_strength

    #setter for combat_strength
    @combat_strength.setter
    def combat_strength(self, value):
        if value >= 0:
            self._combat_strength = value


    #getter for health_points
    @property
    def health_points(self):
        return self._health_points

    #setter for health_points
    @health_points.setter
    def health_points(self, value):
        if value >= 0:
            self._health_points = value

    #destructor
    def __del__(self):
        print(f"The {self.role} object is being destroyed by the garbage collector")
