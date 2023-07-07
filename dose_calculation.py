# Author: Mirsadra Molaei
# Date created: 2023-05-18
# Python version: 3.10.11
# Description: Dose calculation of liquid dosage forms based on the Hungarian Pharmacopoeia (Hg. Ph.)


def get_user_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Please enter a valid number.")


def calculate_quantity(usr_api_gram, usr_solvent_gram, usr_spoon_gram, usr_density, usr_max_single, usr_max_daily, usr_max_intake):
    table_sp = 15
    child_sp = 10
    tea_sp = 5

    spoon_mapping = {1: table_sp, 2: child_sp, 3: tea_sp}
    usr_spoon_gram = spoon_mapping.get(usr_spoon_gram)

    density_mapping = {1: 1, 2: 1.3}
    usr_density = density_mapping.get(usr_density)

    result_single = (usr_api_gram * 1000 * usr_spoon_gram * usr_density) / usr_solvent_gram
    result_daily = result_single * usr_max_intake

    print(f"The ordered quantity in one spoon is {result_single} mg.")
    print(f"The ordered quantity in one day is {result_daily} mg.")

    if result_single > usr_max_single:
        print(f"The ordered quantity in one spoon is more than the maximum single dose of {usr_max_single} mg.")

    if result_daily > usr_max_daily:
        print(f"The ordered quantity in one day is more than the maximum daily dose of {usr_max_daily} mg.")

    if usr_max_single * usr_max_intake < usr_max_daily:
        x = (usr_max_single * usr_solvent_gram) / (usr_spoon_gram * usr_density)
        print(f"The corrected quantity in one spoon is {round(x / 1000, 3)} g.")
        y = x * usr_max_intake
        print(f"The corrected quantity in one day is {round(y / 1000, 3)} g.")
    else:
        x = (usr_max_daily * usr_solvent_gram) / (usr_max_intake * usr_spoon_gram * usr_density)
        print(f"The corrected quantity in one spoon is {round(x / 1000, 3)} g.")
        y = x * usr_max_intake
        print(f"The corrected quantity in one day is {round(y / 1000, 3)} g.")


def main():
    usr_api_gram = get_user_input("Enter the amount of active agent weighted in grams: ", float)
    usr_solvent_gram = get_user_input("Enter the amount of solvent weighted in grams: ", float)
    usr_spoon_gram = get_user_input("Enter the spoon size (1 = table spoon, 2 = child spoon, 3 = tea spoon): ", int)
    usr_density = get_user_input("Enter the density of the active agent (1 = aqueous, 2 = syrup): ", int)
    usr_max_single = get_user_input("Enter the maximum single dose, defined by Hg. Ph., in mg: ", int)
    usr_max_daily = get_user_input("Enter the maximum daily dose, defined by Hg. Ph., in mg: ", int)
    usr_max_intake = get_user_input("How many times a day does the medicine need to be taken? ", int)

    calculate_quantity(usr_api_gram, usr_solvent_gram, usr_spoon_gram, usr_density, usr_max_single, usr_max_daily, usr_max_intake)


if __name__ == "__main__":
    main()
