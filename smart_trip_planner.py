"""
Smart Trip Planner (without API)

The Smart Trip Planner uses user input to provide the user with suggested items to take on their trip of choice

1. Prompts the user for current temperature in Fahrenheit.
2. Prompts the user for trip t ipe (e.g., Hiking, Jeep).
3. Generates a list of suggested items

I took out the requirment for the API due to it not being reliable and providing 404 errors due to the site not always connecting, this provided a bad UX.
"""



def prompt_for_temperature():
    """Asks the user to input current temperature in Fahrenheit."""
    print("\nPlease enter the current temperature:")
    while True:
        try:
            temp_input = input("  - Temperature (°F): ").strip()
            temperature = float(temp_input)
            return temperature
        except ValueError:
            print("    Invalid input. Please enter a number for the temperature.")

def prompt_user_for_trip_type():
    """Asks the user to input the type of trip."""
    known_trip_types = ["Hiking", "Jeep", "Camping", "Fishing"]
    print(f"\nEnter trip type (e.g., {', '.join(known_trip_types)}):")
    while True:
        trip_type = input("> ").strip().capitalize()
        if trip_type:
            return trip_type
        else:
            print("    Please enter a trip type.")

def suggest_checklist_items(trip_type, temperature):
    """Suggests a basic list of items based on trip type and temperature."""
    suggestions = []

    suggestions.extend(["Water Bottle", "Snacks", "First-Aid Kit", "Phone", "Pocket Knife"])

    if trip_type == "Hiking":
        suggestions.extend(["Hiking Boots", "Backpack", "Map/Compass"])
    elif trip_type == "Jeep":
        suggestions.extend(["Recovery Strap", "Basic Tools", "Tire Pressure Gauge", "Air Compressor", "Navigation Device"])
    elif trip_type == "Camping":
        suggestions.extend(["Tent", "Sleeping Bag", "Camp Stove", "Headlamp/Flashlight"])
    elif trip_type == "Fishing":
        suggestions.extend(["Fishing Rod/Reel", "Tackle Box", "Fishing License", "Cooler"])

    if temperature is not None:
        if temperature < 40:
            suggestions.extend(["Warm Hat", "Gloves", "Insulated Jacket"])
        elif temperature < 60:
            suggestions.extend(["Light Jacket", "Long Sleeves"])
        elif temperature > 80:
            suggestions.extend(["Sun Hat", "Sunscreen", "Extra Water", "Sunglasses"])
        elif temperature > 70:
            suggestions.append("Sunglasses")

    unique_suggestions = list(dict.fromkeys(suggestions))

    print(f"\nSuggested items for your {trip_type} trip (Temp: {temperature}°F):")
    for item in unique_suggestions:
        print(f"- {item}")

    return unique_suggestions

# --- Main Execution Block ---

print("\n--- Starting Trip Planner ---")

temperature = prompt_for_temperature()
trip_type = prompt_user_for_trip_type()
suggested_list = suggest_checklist_items(trip_type, temperature)

print("\n--- Enjoy your Trip! ---")

# --- pytest Execution Block ---
#    print("\n--- Starting Trip Planner ---")

#    temperature = prompt_for_temperature()
#    trip_type = prompt_user_for_trip_type()
#    suggested_list = suggest_checklist_items(trip_type, temperature)

#    print("\n--- Enjoy your Trip! ---")