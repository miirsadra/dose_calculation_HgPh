# Author: Mirsadra Molaei
# Date created: 2023-05-18
# Python version: 3.10.11
# Description: Dose calculation of liquid dosage forms based on the Hungarian Pharmacopoeia (Hg. Ph.)


usr_api_gram = None
while True:
    try:
        api = float(input("Enter the amount of active agent weighted in grams: "))
        if api.is_integer():
            usr_api_gram = int(api)
        else:
            usr_api_gram = api
        break
    except ValueError:
        print("Please enter a valid number.")

usr_solvent_gram = None
while True:
    try:
        solvent = float(input("Enter the amount of solvent weighted in grams: "))
        if solvent.is_integer():
            usr_solvent_gram = int(solvent)
        else:
            usr_solvent_gram = solvent
        break
    except ValueError:
        print("Please enter a valid number.")

table_sp = 15
child_sp = 10
tea_sp = 5

while True:
    try:
        usr_spoon_gram = int(input("Enter the spoon size (1 = table spoon, 2 = child spoon, 3 = tea spoon): "))
        if usr_spoon_gram == 1:
            usr_spoon_gram = table_sp
            break
        elif usr_spoon_gram == 2:
            usr_spoon_gram = child_sp
            break
        elif usr_spoon_gram == 3:
            usr_spoon_gram = tea_sp
            break
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

aq_den = 1
syrup_den = 1.3

while True:
    try:
        usr_density = int(input("Enter the density of the active agent (1 = aqueous, 2 = syrup): "))
        if usr_density == 1:
            usr_density = aq_den
            break
        elif usr_density == 2:
            usr_density = syrup_den
            break
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

usr_max_single = int(input("Enter the maximum single dose, defined by Hg. Ph., in mg: "))
usr_max_daily = int(input("Enter the maximum daily dose, defined by Hg. Ph., in mg: "))
usr_max_intake = (int(input("How many times a day do the medicine need to be taken? ")))

result_single = (usr_api_gram * 1000 * usr_spoon_gram * usr_density) / usr_solvent_gram
result_daily = result_single * usr_max_intake

if result_single > usr_max_single:
    print(f"The ordered quantity in one spoon is {result_single} mg, which is more than the maximum single dose of {usr_max_single} mg.")
else:
    print(f"The ordered quantity in one spoon is {result_single} mg, which is less than the maximum single dose of {usr_max_single} mg.")

if result_daily > usr_max_daily:
    print(f"The ordered quantity in one day is {result_daily} mg, which is more than the maximum daily dose of {usr_max_daily} mg.")
else:
    print(f"The ordered quantity in one day is {result_daily} mg, which is less than the maximum daily dose of {usr_max_daily} mg.")

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
