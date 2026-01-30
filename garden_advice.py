# global variables for storing user input and advice strings
season = ""
plant_type = ""
season_advice_str = ""
plant_advice_str = ""


def get_user_input():  # no input parameters
    '''
    Get user input for the current season and plant type.
    1. Prompt the user to enter the current season (summer/winter).
    2. Prompt the user to enter the type of plant (flower/vegetable).
    3. Store the inputs in the global variables season and plant_type.
    4. Return the season and plant_type.
    '''
    # use global variables to store user input
    global season, plant_type
    season += input("Enter the current season (summer/winter): ")
    plant_type += input("Enter the type of plant (flower/vegetable): ")

    return season, plant_type


def season_advice(season):  # takes season as input
    '''
    Determine gardening advice based on the season.
    1. If the season is summer, advise to water plants regularly and provide
        shade.
    2. If the season is winter, advise to protect plants from frost with
        covers.
    3. If the season is neither, indicate no advice is available.
    4. Append the advice to the global variable season_advice_str.
    5. Return the season_advice_str.
    '''
    # use global variable to store advice
    global season_advice_str
    if season == "summer":
        season_advice_str += "Water your plants regularly and provide shade.\n"
    elif season == "winter":
        season_advice_str += "Protect your plants from frost with covers.\n"
    else:
        season_advice_str += "No advice for this season.\n"
    return season_advice_str


def plant_advice(plant_type):  # takes plant_type as input
    '''
    Provide gardening advice based on the type of plant.
    1. If the plant type is flower, advise to use fertiliser to encourage
        blooms
    2. If the plant type is vegetable, advise to watch for pests
    3. If the plant type is neither, indicate no advice is available
    4. Append the advice to the global variable plant_advice_str.
    5. Return the plant_advice_str.
    '''
    # use global variable to store advice
    global plant_advice_str
    if plant_type == "flower":
        plant_advice_str += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        plant_advice_str += "Keep an eye out for pests!"
    else:
        plant_advice_str += "No advice for this type of plant."

    return plant_advice_str


def main():  # no input parameters
    '''
    Main function to run the garden advice program.
    1. Call get_user_input to get the season and plant type.
    2. Call season_advice and plant_advice to get the respective advice.
    3. Print the combined advice to the user.
    '''
    get_user_input()
    print(season_advice(season) + plant_advice(plant_type))


if __name__ == "__main__":
    main()


# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
