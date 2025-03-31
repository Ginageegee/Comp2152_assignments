
from assignment02.character import Character


class Hero(Character):

    #constructor
    def __init__(self):
        # Call the parent class constructor to initialize shared properties
        super().__init__(role="hero")

    # Hero's Attack Function
    def hero_attacks(self, m_health_points):
        ascii_image = """
                                    @@   @@ 
                                    @    @  
                                    @   @   
                   @@@@@@          @@  @    
                @@       @@        @ @@     
               @%         @     @@@ @       
                @        @@     @@@@@     
                   @@@@@        @@       
                   @    @@@@                
              @@@ @@                        
           @@     @                         
       @@*       @                          
       @        @@                          
               @@                                                    
             @   @@@@@@@                    
            @            @                  
          @              @                  

      """
        print(ascii_image)
        print("    |    Player's weapon (" + str(self.combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
        if self.combat_strength >= m_health_points:
            # Player was strong enough to kill monster in one blow
            m_health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            m_health_points -= self.combat_strength

            print("    |    You have reduced the monster's health to: " + str(m_health_points))
        return m_health_points

    # Destructor
    def __del__(self):
        # Call parent destructor
        super().__del__()


