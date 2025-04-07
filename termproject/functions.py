# Import the random library to use for the dice later
import random

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")


# Lab 4: Question 4
def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


# Lab 4: Question 3
def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt

#group assignment feature Treasure Hunt (Regina)
def treasure_hunt(health_points, belt):

    #possible treasures
    treasures = [("Golden Apple", 5), ("Magic Elixir", 10), ("Ancient Relic", -5), ("Cursed Dagger", -10)]

    # The lower the health, the higher the chance of finding treasure
    find_treasure = random.choices([True, False], weights=[max(1, 30 - health_points), health_points], k=1)[0]

    #If treasure was found...
    if find_treasure:
        found_treasure = random.choice(treasures)

        # Nested loops with list comprehension to process treasure effects
        treasure_effects = [
            effect_message #creates a list that stores the resulting message for each treasure effect
            for name, effect in [found_treasure]
            for effect_message in [
                #possible effects the treasure can have
                f"You found a {name}! It heals you!" if effect > 0 and health_points <= 10 else
                f"You found a {name}, but your health is too high to benefit from it!" if effect > 0 else
                f"You found a {name}! It curses you!" if effect < 0 and health_points >= 15 else
                f"You found a {name}, but your health is too low to take the curse!"
            ]
        ]

        # Apply the effect to health points
        health_points += sum(effect for _, effect in [found_treasure]
                             if (effect > 0 and health_points <= 10) or (effect < 0 and health_points >= 15))

        # Print the effects
        print("\n".join([f"    |    {effect}" for effect in treasure_effects]))

        # Add treasure to belt if it's beneficial (healing treasure only)
        if found_treasure[1] > 0:  # Only add healing treasures to the belt
            belt.append(found_treasure[0])

    else:
        print("    |    No treasure was found this time.")

    return belt, health_points

# Function for casting a spell during the fight sequence (Cast-A-Spell feature)
def cast_spell(available_spells, m_health_points, weather_types, health_points):

    # List comprehension for getting the different weather types


    # Displaying available spells
    print("    |    Choose a spell to cast:")
    for x, spell in enumerate(available_spells):
        if "hp_boost" in spell:
            print(f"    |    {spell['name']} - Element: {spell['element_type']} - Healing: {spell['hp_boost']}")
        else:
            print(f"    |    {spell['name']} - Element: {spell['element_type']} - Attack: {spell.get('attack_power', 0)}")

    # Get the hero's spell choice
    while True:
        try:
            spell_choice = int(input("    |    Enter spell number:"))

            # Checking if choice is valid (within range of available spells)
            if 0 < spell_choice <= len(available_spells):
                selected_spell = next((s for s in available_spells if s['name'].startswith(f"{spell_choice}")), None)
                if selected_spell:
                    break;
                else:
                    print("    |    You don't know that spell!")
            else:
                print("    |    Invalid spell Number.")
        except ValueError:
            print("    |    Please enter a valid number.")

    # Getting the values from the spells dictionary
    spell_element = selected_spell['element_type']
    attack_power = selected_spell.get('attack_power', 0)
    hp_boost = selected_spell.get('hp_boost', 0)
    spell_effectiveness = 1.0 # default multiplier for spell effectiveness

    # Nested conditionals for weather effects on spell casting
    if "Rain" in weather_types:
        if spell_element == "fire":
            print("    |    Oh no! Your fire spell fizzles in the rain! No effect.")
            spell_effectiveness = 0
        elif spell_element == "water":
            print("    |    Your water spell is boosted by the rain!")
            spell_effectiveness = 2.0
    elif "Sunny" in weather_types:
        if spell_element == "fire":
            print("    |    Your fire spell is empowered by the sun!")
            spell_effectiveness = 1.5
        elif spell_element == "ice":
            print("    |    Oh no! Your ice spell was melted by the sun! No effect.")
            spell_effectiveness = 0
    elif "Snow" in weather_types:
        if spell_element == "ice":
            print("    |    Your ice spell is stronger in the snow!")
            spell_effectiveness = 2.0
        elif spell_element == "fire":
            print("    |    Your fire spell was weakened by the snow!")
            spell_effectiveness = 0.5
    elif "Thunderstorm" in weather_types:
        if spell_element == "electricity":
            print("    |    Your electric spell is supercharged by the storm!")
            spell_effectiveness = 2.5

    # Nested conditionals for applying spell effects
    if "hp_boost" in selected_spell:
        print(f"    |    You cast a {selected_spell['name']} spell and heal yourself for {hp_boost} health points!")
        return health_points + hp_boost, m_health_points
    else:
        actual_damage = int(attack_power * spell_effectiveness)
        if spell_effectiveness > 0:
            print(f"    |    You cast a {selected_spell['name']} spell for {actual_damage} damage!")
            return health_points, m_health_points - actual_damage
        else:
            print(f"    |    Your spell failed to have any effect!")
            return health_points, m_health_points


# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
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
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength

        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
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
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Lab 5: Question 7
# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Base Case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case
    else:
        # inception_dream(5)
        # 1 + inception_dream(4)
        # 1 + 1 + inception_dream(3)
        # 1 + 1 + 1 + inception_dream(2)
        # 1 + 1 + 1 + 1 + inception_dream(1)
        # 1 + 1 + 1 + 1 + 2
        return 1 + int(inception_dream(num_dream_lvls - 1))

