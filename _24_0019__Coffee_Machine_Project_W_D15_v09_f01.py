
#logo?

#start here:
penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

#money cost (* 100)
espresso_cost_per_serving = 150
latte_cost_per_serving = 250
cappuccino_cost_per_serving = 300


#General Starting resources: (in ml, ml, and g grams)
Water_starting_resources = 300
Milk_starting_resources = 200
Coffee_starting_resources = 100

#Espresso resource usage
water_resource_usage_amount_for_espresso = 50
coffee_resource_usage_amount_for_espresso = 18
# enough_espresso_resources = ""    #why is this here?? not needed for the code to work, necessarily

#Latte resource usage
water_resource_usage_amount_for_latte = 200
milk_resource_usage_amount_for_latte = 150
coffee_resource_usage_amount_for_latte = 24

#Cappuccino resource usage
water_resource_usage_amount_for_cappuccino = 250
milk_resource_usage_amount_for_cappuccino = 100
coffee_resource_usage_amount_for_cappuccino = 24

current_water_resource_level = Water_starting_resources
current_milk_resource_level = Milk_starting_resources
current_coffee_resource_level = Coffee_starting_resources


def start_up_the_coffee_machine():

    while True:
        global current_water_resource_level, current_milk_resource_level, current_coffee_resource_level
        print("Hello, welcome to Drinky Smort!\n")

        if water_resource_usage_amount_for_espresso <= current_water_resource_level and coffee_resource_usage_amount_for_espresso <= current_coffee_resource_level:
            print(f"We can make you an espresso. Press e to order an espresso")
            if water_resource_usage_amount_for_latte <= current_water_resource_level and milk_resource_usage_amount_for_latte <= current_milk_resource_level and coffee_resource_usage_amount_for_latte <= current_coffee_resource_level:
                print(f"We can make you a latte. Press l to order a latte")
                if water_resource_usage_amount_for_latte <= current_water_resource_level and milk_resource_usage_amount_for_latte <= current_milk_resource_level and coffee_resource_usage_amount_for_latte <= current_coffee_resource_level:
                    print(f"We can make you a cappuccino. Press c to order a cappuccino\n")
        else:
            print("Sorry, we are Out of Stock. Please stop by again later.")
            break

        user_drink_selection = input(f"What would you like to order, from the above selection? (Type the letter selection or type REPORT for updated inventory Report): ").lower()


        def check_inventory_levels_espresso():

            global Water_starting_resources, Milk_starting_resources, Coffee_starting_resources

            if water_resource_usage_amount_for_espresso < current_water_resource_level and coffee_resource_usage_amount_for_espresso < current_coffee_resource_level:
                # print(f"Sure! We have enough resources for you.")
                return True
            else:
                # print("Sorry, we are Out of Stock at this time. Please swing by again later.")
                return True #return False??


        def check_inventory_levels_latte():

            global Water_starting_resources, Milk_starting_resources, Coffee_starting_resources, current_water_resource_level, current_water_resource_level, current_coffee_resource_level
            # print(f"The current inventory levels:\nWater is at: {Water_starting_resources} ml\nMilk is at: {Milk_starting_resources} ml\nCoffee is at: {Coffee_starting_resources} g")
            current_water_resource_level = Water_starting_resources #minus other math...
            current_milk_resource_level = Milk_starting_resources #minus other math...
            current_coffee_resource_level = Coffee_starting_resources #minus other math...

            if water_resource_usage_amount_for_latte < current_water_resource_level and coffee_resource_usage_amount_for_latte < current_coffee_resource_level:
                # print("Sure! We have enough resources for you.")
                return True
            else:
                print("Sorry, not enough resources for this item")
                return False

        def check_inventory_levels_cappuccino():

            global Water_starting_resources, Milk_starting_resources, Coffee_starting_resources
            # print(f"The current inventory levels:\nWater is at: {Water_starting_resources} ml\nMilk is at: {Milk_starting_resources} ml\nCoffee is at: {Coffee_starting_resources} g")
            current_water_resource_level = Water_starting_resources #minus other math...
            current_milk_resource_level = Milk_starting_resources #minus other math...
            current_coffee_resource_level = Coffee_starting_resources #minus other math...

            if water_resource_usage_amount_for_cappuccino < current_water_resource_level and milk_resource_usage_amount_for_cappuccino < current_milk_resource_level and coffee_resource_usage_amount_for_cappuccino < current_coffee_resource_level:
                # print("Sure! We have enough resources for you.")
                return True
            else:
                print("Sorry, not enough resources for this item")
                return play_again_option

        if user_drink_selection == "e":
            check_inventory_levels_espresso()

        elif user_drink_selection == "l":
            check_inventory_levels_latte()

        elif user_drink_selection == "c":
            check_inventory_levels_cappuccino()

#####################################################################################

# Drink and Money transaction
        if user_drink_selection == "e":
            print(f"That will cost ${espresso_cost_per_serving / 100:.2f}")
            print(f"Please insert coins:")
            pennies_entered_for_espresso = int(input(f"Quantity of pennies you will place in the machine: "))     #YOU NEEDED INT AND * 100 in certain areas, to get the math to work.
            nickels_entered_for_espresso = int(input(f"Quantity of nickels you will place in the machine: "))
            dimes_entered_for_espresso = int(input(f"Quantity of dimes you will place in the machine: "))
            quarters_entered_for_espresso = int(input(f"Quantity of quarters you will place in the machine: "))

            total_in_pennies = pennies_entered_for_espresso * penny # * 100
            print(f"${total_in_pennies:.2f} in pennies.")                                          #this gives you 2 decimal points  :.2f}")
            total_in_nickels = nickels_entered_for_espresso * nickel # * 100
            print(f"${total_in_nickels:.2f} in nickels.")
            total_in_dimes = dimes_entered_for_espresso * dime # * 100
            print(f"${total_in_dimes:.2f} in dimes.")
            total_in_quarters = quarters_entered_for_espresso * quarter # * 100
            print(f"${total_in_quarters:.2f} in quarters.")

            total_of_all_inserted_coins = ((total_in_pennies + total_in_nickels + total_in_dimes + total_in_quarters))
            print(f"The total you entered was ${total_of_all_inserted_coins:.2f}")

            print(f"The total for the drink costs ${espresso_cost_per_serving / 100:.2f}")
            change_difference_math = total_of_all_inserted_coins - (espresso_cost_per_serving/100)
            if change_difference_math < 0:
                print(f"Sorry, you don't have enough change to pay for this right now. You have been refunded ${total_of_all_inserted_coins:.2f}")
            elif change_difference_math > 0 and check_inventory_levels_espresso() == True:
                print(f"Enjoy your drink and your ${change_difference_math:.2f}!")
                current_water_resource_level -= water_resource_usage_amount_for_espresso # minus other math...
                # doesn't use milk - current_milk_resource_level = Milk_starting_resources #minus other math...
                current_coffee_resource_level -= coffee_resource_usage_amount_for_espresso  # minus other math...

        # else:
        # check to see if we have enough coffee resources


# elif for latte
        elif user_drink_selection == "l":
            print(f"That will cost ${latte_cost_per_serving / 100:.2f}")
            print(f"Please insert coins:")
            pennies_entered_for_latte = int(input(f"Quantity of pennies you will place in the machine: "))     #YOU NEEDED INT AND * 100 in certain areas, to get the math to work.
            nickels_entered_for_latte = int(input(f"Quantity of nickels you will place in the machine: "))
            dimes_entered_for_latte = int(input(f"Quantity of dimes you will place in the machine: "))
            quarters_entered_for_latte = int(input(f"Quantity of quarters you will place in the machine: "))

            total_in_pennies = pennies_entered_for_latte * penny # * 100
            print(f"${total_in_pennies:.2f} in pennies.")                                          #this gives you 2 decimal points  :.2f}")
            total_in_nickels = nickels_entered_for_latte * nickel # * 100
            print(f"${total_in_nickels:.2f} in nickels.")
            total_in_dimes = dimes_entered_for_latte * dime # * 100
            print(f"${total_in_dimes:.2f} in dimes.")
            total_in_quarters = quarters_entered_for_latte * quarter # * 100
            print(f"${total_in_quarters:.2f} in quarters.")

            total_of_all_inserted_coins = ((total_in_pennies + total_in_nickels + total_in_dimes + total_in_quarters))
            print(f"The total you entered was ${total_of_all_inserted_coins:.2f}")

            print(f"The total for the drink costs ${latte_cost_per_serving / 100:.2f}")
            change_difference_math = total_of_all_inserted_coins - (latte_cost_per_serving/100)
            if change_difference_math < 0:
                print(f"Sorry, you don't have enough change to pay for this right now. You have been refunded ${total_of_all_inserted_coins:.2f}")
            elif change_difference_math > 0 and check_inventory_levels_latte() == True:
                print(f"Enjoy your drink and your ${change_difference_math:.2f}!")
                current_water_resource_level -= water_resource_usage_amount_for_latte  # minus other math...
                current_milk_resource_level -= milk_resource_usage_amount_for_latte #minus other math...
                current_coffee_resource_level -= coffee_resource_usage_amount_for_latte  # minus other math...

# elif for cappuccino
        elif user_drink_selection == "c":
            print(f"That will cost ${cappuccino_cost_per_serving / 100:.2f}")
            print(f"Please insert coins:")
            pennies_entered_for_cappuccino = int(input(f"Quantity of pennies you will place in the machine: "))     #YOU NEEDED INT AND * 100 in certain areas, to get the math to work.
            nickels_entered_for_cappuccino = int(input(f"Quantity of nickels you will place in the machine: "))
            dimes_entered_for_cappuccino = int(input(f"Quantity of dimes you will place in the machine: "))
            quarters_entered_for_cappuccino = int(input(f"Quantity of quarters you will place in the machine: "))

            total_in_pennies = pennies_entered_for_cappuccino * penny # * 100
            print(f"${total_in_pennies:.2f} in pennies.")                                          #this gives you 2 decimal points  :.2f}")
            total_in_nickels = nickels_entered_for_cappuccino * nickel # * 100
            print(f"${total_in_nickels:.2f} in nickels.")
            total_in_dimes = dimes_entered_for_cappuccino * dime # * 100
            print(f"${total_in_dimes:.2f} in dimes.")
            total_in_quarters = quarters_entered_for_cappuccino * quarter # * 100
            print(f"${total_in_quarters:.2f} in quarters.")

            total_of_all_inserted_coins = ((total_in_pennies + total_in_nickels + total_in_dimes + total_in_quarters))
            print(f"The total you entered was ${total_of_all_inserted_coins:.2f}")

            print(f"The total for the drink costs ${cappuccino_cost_per_serving / 100:.2f}")
            change_difference_math = total_of_all_inserted_coins - (cappuccino_cost_per_serving/100)
            if change_difference_math < 0:
                print(f"Sorry, you don't have enough change to pay for this right now. You have been refunded ${total_of_all_inserted_coins:.2f}")
            elif change_difference_math > 0 and check_inventory_levels_cappuccino() == True:
                print(f"Enjoy your drink and your ${change_difference_math:.2f}!")
                current_water_resource_level -= water_resource_usage_amount_for_cappuccino  # minus other math...
                current_milk_resource_level -= water_resource_usage_amount_for_cappuccino  # minus other math...
                current_coffee_resource_level -= water_resource_usage_amount_for_cappuccino  # minus other math...

        elif user_drink_selection == "report":
            print(
                f"The current inventory levels are {current_water_resource_level} ml of water, {current_milk_resource_level} ml of milk, and {current_coffee_resource_level} g of coffee.")


# TODO Program Requirements: # 1. Be able to Print a report (report what it has left inside the machine, resource-wise)

# TODO Program Requirements: # 2. Check if there’s sufficient resources.

# TODO Program Requirements: # 3. Process coins.

# TODO Program Requirements: # 4. Check if transaction successful. (enough money to cover the transaction)

# TODO Program Requirements: # 5. If successful, make coffee (deduct the resources)




        play_again_option = input(f"Do you want to play again? (Y or N): ").upper()
        if play_again_option != "Y":
            break

start_up_the_coffee_machine()