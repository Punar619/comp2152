import random

# Step 1: Define the weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]


# Step 2: Roll the dice (1-6)
weaponRoll = random.randint(1, 6)  # Simulate dice roll


# Step 3: Add the roll to the hero's combat strength
hero_combat_strength = 10  # Base combat strength
final_combat_strength = hero_combat_strength + weaponRoll


# Step 4: Select the weapon based on the roll
selected_weapon = weapons[weaponRoll - 1]  # Subtract 1 because list indices start at 0


# Step 5: Print the weapon and apply conditions
print(f"Weapon Roll: {weaponRoll}")
print(f"Selected Weapon: {selected_weapon}")
print(f"Hero's Final Combat Strength: {final_combat_strength}")


# Step 6: Weapon strength evaluation
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if selected_weapon != "Fist":
    print("Thank goodness you didn’t roll the Fist...")

    # Step 7: Error handling (optional for dice rolls and inputs)
    # Validate that weaponRoll is between 1 and 6 (already ensured by randint in this case)
    if not (1 <= weaponRoll <= 6):
        print("Error: Dice roll must be between 1 and 6!")