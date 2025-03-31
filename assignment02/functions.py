# Import the random library to use for the dice later
import random

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")


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


def save_game(winner, hero_name="", num_stars=0, monsters_killed_in_game=0):
    try:
        # Read the previous total monsters killed from the save file
        with open("save.txt", "r") as file:
            lines = file.readlines()
            if lines and lines[-1].startswith("Total Monsters Killed (all games):"):
                previous_total = int(lines[-1].split(": ")[1])
            else:
                previous_total = 0
    except FileNotFoundError:
        # If file doesn't exist, start fresh with 0
        previous_total = 0

    # Update the total number of monsters killed across all games
    total_monsters_killed = previous_total + monsters_killed_in_game

    # Append new game results to the file
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed {monsters_killed_in_game} monster(s) and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously.\n")
        file.write(f"Total Monsters Killed (all games): {total_monsters_killed}\n")


# Lab 06 - Question 5a
def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if lines:
                # Get the last game action and total monsters killed
                last_action = lines[-2].strip() if len(lines) > 1 else "No previous actions recorded."
                total_monsters_killed_line = lines[-1].strip()
                if "Total Monsters Killed (all games):" in total_monsters_killed_line:
                    total_monsters_killed = int(total_monsters_killed_line.split(": ")[1])
                else:
                    total_monsters_killed = 0

                # Display and return relevant details
                print(last_action)
                print(total_monsters_killed_line)
                return last_action, total_monsters_killed
    except FileNotFoundError:
        # If no save file exists, start fresh
        print("No previous game found. Starting fresh.")
        return None, 0


# Lab 06 - Question 5b
def adjust_combat_strength(combat_strength, m_combat_strength):
    # Lab Week 06 - Question 5 - Load the game
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")


