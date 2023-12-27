from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

machine_state = 'on'

while machine_state == 'on':
    options = menu.get_items()
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input(f'What would you like? ({options}):')

# 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == 'off':
        machine_state = 'off'

# 3. Print report.
    elif choice == 'report':
        coffe_maker.report()
        money_machine.report()

# 4. Check resources sufficient?
    # 5. Process coins.
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
