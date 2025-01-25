import random

# Dice options and weapons list
diceOptions = [1, 2, 3, 4, 5, 6]
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Hero's base combat strength and health
heroCombatStrength = 10
heroHealth = 50

# Monster's combat strength and health
monsterCombatStrength = 8
monsterHealth = 40

# Rolling for the hero's weapon
weaponRoll = random.choice(diceOptions)
print(f"Weapon Roll: {weaponRoll}")
heroWeapon = weapons[weaponRoll - 1]
print(f"The hero's weapon is: {heroWeapon}")

# Add the weapon roll to hero's combat strength
heroCombatStrength += weaponRoll
print(f"Hero's combat strength after weapon roll: {heroCombatStrength}")

# Rolling for the monster's health and combat strength
monsterHealthRoll = random.choice(diceOptions)
monsterCombatStrength += monsterHealthRoll
print(f"Monster's combat strength: {monsterCombatStrength}")

# Battle logic
if heroCombatStrength > monsterCombatStrength:
    print("The hero defeats the monster!")
    # Add healing potion roll
    healingPotionRoll = random.choice(diceOptions)
    print(f"Healing potion roll: {healingPotionRoll}")
    if healingPotionRoll > 3:
        heroHealth += healingPotionRoll
        print(f"Hero heals and now has {heroHealth} health.")
    else:
        print("Healing potion had no effect.")
else:
    print("The monster defeats the hero!")
    heroHealth -= monsterCombatStrength
    print(f"Hero's health after battle: {heroHealth}")

# Logical operators test
print("\nLogical Operators Test:")
print(f"Is the hero alive? {'Yes' if heroHealth > 0 else 'No'}")
print(f"Did the monster survive? {'Yes' if monsterHealth > 0 else 'No'}")
print(f"Did the hero defeat the monster and survive? {'Yes' if heroCombatStrength > monsterCombatStrength and heroHealth > 0 else 'No'}")
print(f"Is the hero's health critical (below 20)? {'Yes' if heroHealth < 20 else 'No'}")
