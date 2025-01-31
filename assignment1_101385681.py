"""
Author: Punar
Assignment: #1
"""
# String
gym_member = "Alex Alliton"
# Float
preferred_weight_kg = 20.5
# Integer
highest_reps = 25
# Boolean
membership_active = True
# Dictionary with string keys and tuple values
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 15),
    "Taylor": (40, 35, 25)
}
for friend, activities in workout_stats.items():
    total_minutes = sum(activities)
    workout_stats[f"{friend}_Total"] = total_minutes
# Nested list
workout_list = [list(activities) for friend, activities in workout_stats.items() if "_Total" not in friend]
# Yoga and running minutes for all friends
yoga_and_running = [row[:2] for row in workout_list]
print("Yoga and running minutes:", yoga_and_running)

# Weightlifting minutes for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for the last two friends:", weightlifting_last_two)
for friend, total_minutes in workout_stats.items():
    if isinstance(total_minutes, int) and total_minutes >= 120:
        print(f"Great job staying active, {friend}!")
friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    print(f"{friend_name}'s workout minutes: {workout_stats[friend_name]}")
    print(f"Total: {workout_stats[f'{friend_name}_Total']}")
else:
    print(f"Friend {friend_name} not found in the records.")
totals = {friend: minutes for friend, minutes in workout_stats.items() if "_Total" in friend}
most_active = max(totals, key=totals.get)
least_active = min(totals, key=totals.get)
print(f"Most active: {most_active}, minutes: {totals[most_active]}")
print(f"Least active: {least_active}, minutes: {totals[least_active]}")

