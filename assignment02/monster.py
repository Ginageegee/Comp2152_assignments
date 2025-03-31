import character
import random
from assignment02.character import Character
from assignment02.hero import Hero


class Monster(Character):
    def __init__(self):
        # Call the parent class constructor to initialize shared properties
        super().__init__(role="monster")


    # Monster's Attack Function
    def monster_attacks(self, health_points):
        ascii_image2 = """                                                                 
               @@@@ @                           
          (     @*&@  ,                         
        @               %                       
         &#(@(@%@@@@@*   /                      
          @@@@@.                                
                   @       /                    
                    %         @                 
                ,(@(*/           %              
                   @ (  .@#                 @   
                              @           .@@. @
                       @         ,              
                          @       @ .@          
                                 @              
                              *(*  *      
                 """
        print(ascii_image2)
        print("    |    Monster's Claw (" + str(self.combat_strength) + ") ---> Player (" + str(health_points) + ")")
        if self.combat_strength >= health_points:
            # Monster was strong enough to kill player in one blow
            health_points = 0
            print("    |    Player is dead")
        else:
            # Monster only damaged the player
            health_points -= self.combat_strength
            print("    |    The monster has reduced Player's health to: " + str(health_points))
        return health_points

    def __del__(self):
        # Call parent destructor
        super().__del__()