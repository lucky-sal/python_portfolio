from data import MENU, resources

machine_state = 'on'

money = 0
money_inserted = 0
water_current = resources['water']
milk_current = resources['milk']
coffee_current = resources['coffee']
resources_ready = False


def payment():
    print('Please insert coins.')
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickels = int(input('how many nickels?: '))
    pennies = int(input('how many pennies?: '))
    money_calc = (quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)
    return money_calc


# def resources_transaction():

while machine_state == 'on':
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 3. Print report.
    if user_selection == 'report':
        print(f'Water: {water_current}ml')
        print(f'Milk: {milk_current}ml')
        print(f'Coffee: {coffee_current}g')
        print(f'Money: ${money}')

    # TODO: 4. Check resources sufficient?
    elif user_selection == 'espresso':
        if (water_current >= MENU['espresso']['ingredients']['water']
                and coffee_current >= MENU['espresso']['ingredients']['coffee']):
            resources_ready = True
        else:
            print('not enough resources')

    elif user_selection == 'latte':
        if (water_current >= MENU['latte']['ingredients']['water']
                and milk_current >= MENU['latte']['ingredients']['milk']
                and coffee_current >= MENU['latte']['ingredients']['coffee']):

            resources_ready = True
        else:
            print('not enough resources')

    elif user_selection == 'cappuccino':
        if (water_current >= MENU['cappuccino']['ingredients']['water']
                and milk_current >= MENU['cappuccino']['ingredients']['milk']
                and coffee_current >= MENU['cappuccino']['ingredients']['coffee']):

            resources_ready = True
        else:
            print('not enough resources')

    # TODO: 5. Process coins.
    if resources_ready:
        money_inserted = payment()
        # TODO: 6. Check transaction successful?
        if money_inserted >= MENU[user_selection]['cost']:
            change = round(money_inserted - MENU[user_selection]['cost'], 2)
            print(f'Here is your change: {change}')

            # TODO: 7. Make Coffee.
            print(f'Here is your {user_selection} ☕. Enjoy!')

            water_current -= MENU[user_selection]['ingredients']['water']
            if user_selection != 'espresso':
                milk_current -= MENU[user_selection]['ingredients']['milk']
            coffee_current -= MENU[user_selection]['ingredients']['coffee']
            money += MENU[user_selection]['cost']

            money_inserted = 0
            resources_ready = False

        else:
            print(f"Sorry that's not enough money. Money refunded.")
            money_inserted = 0
            resources_ready = False

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_selection == 'off':
        machine_state = 'off'
