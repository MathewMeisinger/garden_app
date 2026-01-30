# variables for storing user input
season = ""
plant_type = ""
season_advice_str = ""
plant_advice_str = ""


def get_user_input():
    global season, plant_type
    season += input("Enter the current season (summer/winter): ")
    plant_type += input("Enter the type of plant (flower/vegetable): ")

    return season, plant_type


def season_advice(season):
    # Determine advice based on the season
    global season_advice_str
    if season == "summer":
        season_advice_str += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        season_advice_str += "Protect your plants from frost with covers.\n"
    else:
        season_advice_str += "No advice for this season.\n"
    return season_advice_str


def plant_advice(plant_type):
    # Determine advice based on the plant type
    global plant_advice_str
    if plant_type == "flower":
        plant_advice_str += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        plant_advice_str += "Keep an eye out for pests!"
    else:
        plant_advice_str += "No advice for this type of plant."

    return plant_advice_str


def main():
    # Print the generated advice
    get_user_input()
    print(season_advice(season) + plant_advice(plant_type))


if __name__ == "__main__":
    main()


# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
