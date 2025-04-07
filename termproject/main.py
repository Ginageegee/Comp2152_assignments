# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions

# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Defining the spells (Cast-A-Spell feature)
spell_options = [
    {"name": "1. Fire Balls", "element_type": "fire", "attack_power": 3, "skill_lvl_required": 5},
    {"name": "2. Basic Healing", "element_type": "none", "hp_boost": 2, "skill_lvl_required": 3},
    {"name": "3. Flying Icicle", "element_type": "ice", "attack_power": 4, "skill_lvl_required": 10},
    {"name": "4. Twisting Vines", "element_type": "earth", "attack_power": 1, "skill_lvl_required": 3},
    {"name": "5. Fire Sword", "element_type": "fire", "attack_power": 4, "skill_lvl_required": 10},
    {"name": "6. Electric Shock", "element_type": "electricity", "attack_power": 5, "skill_lvl_required": 10},
    {"name": "7. Freeze Ray", "element_type": "ice", "attack_power": 4, "skill_lvl_required": 8},
    {"name": "8. Mud Goblins Summoning", "element_type": "earth", "attack_power": 3, "skill_lvl_required": 6},
    {"name": "9. Poisonous Mushroom Cloud", "element_type": "earth", "attack_power": 5, "skill_lvl_required": 18},
    {"name": "10. Invisibility", "element_type": "none", "attack_power": 3, "skill_lvl_required": 14},
    {"name": "11. Tidal Wave", "element_type": "water", "attack_power": 4, "skill_lvl_required": 16},
    {"name": "12. Super Healing", "element_type": "none", "hp_boost": 10, "skill_lvl_required": 20}
]

# Defining the hero's skill level (Cast-A-Spell feature)
skill_lvl = 0

# Defining the hero's available spells based on their skill level (Cast-A-Spell feature)
available_spells = []

# Define the weather
weather_effects = [
    {"type": "Sunny", "effects": {"hero_hp_boost": 10, "monster_attack_debuff": -4}},
    {"type": "Rain", "effects": {"hero_hp_boost": -3, "hero_attack_debuff": 10}},
    {"type": "Foggy", "effects": {"hero_attack_debuff": -5, "monster_hp_boost": 7}},
    {"type": "Darkness", "effects": {"monster_attack_debuff": 10}},
    {"type": "Thunderstorm", "effects": {"both_damage": -7, "paralyzed": True}},
    {"type": "Snow", "effects": {"skip_turn": "random"}}
]



# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- But thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Roll for hero's spell skill level (Cast-A-Spell feature)
    print("    |", end="    ")
    input("Roll the dice for your spell-casting skill level (Press enter)")
    skill_lvl = random.choice(big_dice_options)
    print("    |    Player rolled " + str(skill_lvl) + " for their skill level")


    # Filtering the available spells based on the hero's skill level (Cast-A-Spell feature)
    available_spells = [spell for spell in spell_options if spell["skill_lvl_required"] <= skill_lvl]
    print("    |    Here are the spells you can cast based on your skill level:")
    if available_spells:
        for spell in available_spells:
            if "hp_boost" in spell:
                print(f"    |    {spell['name']} - Element: {spell['element_type']} - Healing: {spell['hp_boost']}")
            else:
                print(f"    |    {spell['name']} - Element: {spell['element_type']} - Attack: {spell.get('attack_power', 0)}")
    else:
        print("    |    You don't know any spells yet! You skill level is too low.")
    print("    |    Hopefully these spells will come in handy during a fight...")



    # Collect Loot
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    # Collect Loot First time
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    # Collect Loot Second time
    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    # Use Loot
    belt, health_points = functions.use_loot(belt, health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    # Compare Player vs Monster's strength
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))

    # Check the Player's overall strength and health
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))


    # Trigger a treasure hunt
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Go on a treasure hunt (Press enter)")

    belt, health_points = functions.treasure_hunt(health_points, belt)
    print(f"    |    Updated health points: {health_points}")
    print(f"    |    Updated belt: {belt}")




    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                        
             &                          
      @      .                          

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster’s combat strength by its power
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        m_combat_strength) + " using the " + power_roll + " magic power")

    # Call Recursive function

    print("    |", end="    ")

    while True:  # Loop indefinitely until valid input is received
        num_dream_lvls = input("How many dream levels do you want to go down? ").strip()  # Remove extra spaces

        if num_dream_lvls.isdigit():  # Check if input is numeric
            num_dream_lvls = int(num_dream_lvls)  # Convert to integer
            break  # Exit the loop once valid input is given
        else:
            print("    |    Invalid input! Please enter a valid number.")

    if num_dream_lvls != 0:
        health_points -= 1
        crazy_level = functions.inception_dream(num_dream_lvls)
        combat_strength += crazy_level
        print("combat strength: " + str(combat_strength))
        print("health points: " + str(health_points))

    # Display Hero and Monster Stats Before Battle
    print("    ------------------------UPDATED STATS------------------------------")
    print(f"    |    Hero Stats -> Health: {health_points}, Combat Strength: {combat_strength}")
    print(f"    |    Monster Stats -> Health: {m_health_points}, Combat Strength: {m_combat_strength}")
    print("    ------------------------------------------------------------------")



    # Loop while the monster and the player are alive.
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:


        # Select active weather effects
        active_effects = [weather["effects"] for weather in weather_effects if random.random() < 0.2]  #20% chances of activating each type so
        # battle is more dynamic

        # Prints Type and its respective effect
        print(
            f"Active Weather Effects: {[weather['type'] for weather in weather_effects if weather['effects'] in active_effects]}")
        print("\n \U0001F327\U0000FE0F The following weather types have been activated:")
        for weather in weather_effects:
            if weather["effects"] in active_effects:
                print(f"- {weather['type']}: {weather['effects']}")

        # Apply active weather effects
        health_points += sum(effect.get("hero_hp_boost", 0) for effect in active_effects)
        m_health_points += sum(effect.get("monster_hp_boost", 0) for effect in active_effects)
        m_combat_strength += sum(effect.get("monster_attack_debuff", 0) for effect in active_effects)
        combat_strength += sum(effect.get("hero_attack_debuff", 0) for effect in active_effects)
        m_health_points += sum(effect.get("both_damage", 0) for effect in active_effects)
        health_points += sum(effect.get("both_damage", 0) for effect in active_effects)

        # Make sure that health goes below 0 during the weather sequence and keep the combat strength at least to 1 so the battle keeps going
        health_points = max(health_points, 0)
        m_health_points = max(m_health_points, 0)
        combat_strength = max(combat_strength, 1)
        m_combat_strength = max(m_combat_strength, 1)

        print(
            "    ----------------------STATS AFTER WEATHER EFFECT--------------------")
        print(f"    |    Hero Stats -> Health: {health_points}, Combat Strength: {combat_strength}")
        print(f"    |    Monster Stats -> Health: {m_health_points}, Combat Strength: {m_combat_strength}")
        print("    ------------------------------------------------------------------")
        input("Press Enter to continue...")

        hero_paralyzed = any(effect.get("paralyzed", False) for effect in active_effects)
        monster_paralyzed = any(effect.get("paralyzed", False) for effect in active_effects)

        # Determine if a turn is skipped
        skipped_turn = None
        for effect in active_effects:
            if "skip_turn" in effect:
                skipped_turn = random.choice(["Hero", "Monster"])
                print(f"\u2744\ufe0f {skipped_turn} loses a turn due to Snow!")

        # Hero turn
        if hero_paralyzed:
            print("\u26A1 Hero is paralyzed and skips this turn!")
            hero_paralyzed = False  # Recovers next round
        elif skipped_turn == "Hero":
            print("\u2744\ufe0f Hero loses a turn due to Snow!")
            skipped_turn = None  # Only lose 1 turn
        else:
            if random.choice([True, False]):
                print("Hero attacks!")

                # Cast-A-Spell feature1

                casting_spell = input("Do you want to cast a spell? (y/n): ")
                if casting_spell.lower() == "y":
                    if available_spells:
                        active_weather_types = [weather["type"] for weather in weather_effects if weather["effects"] in active_effects]

                        health_points, m_health_points = functions.cast_spell(available_spells, m_health_points, active_weather_types, health_points)
                    else:
                        print("Uh oh, you don't know any spells!")
                else:
                    print("Casting spell option skipped.")
                    m_health_points = functions.hero_attacks(combat_strength, m_health_points)
                if m_health_points <= 0:
                    num_stars = 3
                    break

        # Monster turn
        if monster_paralyzed:
            print("\u26A1 Monster is paralyzed and skips this turn!")
            monster_paralyzed = False  # Recovers next round
        elif skipped_turn == "Monster":
            print("	\u2744\ufe0f Monster loses a turn due to Snow!")
            skipped_turn = None  # Only lose 1 turn
        else:
            print("Monster attacks!")
            health_points = functions.monster_attacks(m_combat_strength, health_points)
            if health_points <= 0:
                num_stars = 1
                break
            else:
                num_stars = 2

    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")

        hero_name = input("Enter your Hero's name (in two words)")
        name = hero_name.split()
        if len(name) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        else:
            if not name[0].isalpha() or not name[1].isalpha():
                print("    |    Please enter an alphabetical name")
                tries += 1
            else:
                short_name = name[0][0:2:1] + name[1][0:1:1]
                print("    |    I'm going to call you " + short_name + " for short")
                input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")

