# interactive-sandwich-order.py
# Description: An interactive script that allows users to build their sandwich by selecting ingredients, adding extras,
# choosing the quantity, and calculating the total cost. Offers choices for bread, protein, cheese, extras, and payment method.

import pyinputplus as pyip

# Price list for each ingredient
price_list = {
    'Wheat': '2.4', 'White': '3.2', 'Sourdough': '3',
    'Chicken': '5.5', 'Turkey': '3.5', 'Ham': '4.2', 'Tofu': '4.9',
    'Cheddar': '2.4', 'Swiss': '4.1', 'Mozzarella': '3.9',
    'Mayo': '1.9', 'Mustard': '1.9', 'Lettuce': '1.5', 'Tomato': '1.4'
}

total_cost = 0

# Prompt the user to choose bread type and calculate cost
selected_bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], prompt='Choose your bread type:\n', numbered=True)
total_cost += float(price_list[selected_bread])
print(f'Total cost so far: {total_cost}$\n')

# Prompt for protein choice
selected_protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt='Choose your protein:\n', numbered=True)
total_cost += float(price_list[selected_protein])
print(f'Total cost so far: {total_cost}$\n')

# Ask for cheese and extras options
if pyip.inputYesNo(prompt='Do you want cheese?\n') == 'yes':
    selected_cheese = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt='Choose your cheese:\n', numbered=True)
    total_cost += float(price_list[selected_cheese])
    if pyip.inputYesNo(prompt='Do you want extra cheese?\n') == 'yes':
        total_cost += float(price_list[selected_cheese])  # Add extra cheese cost
    print(f'Total cost so far: {total_cost}$')

# Option for additional extras
if pyip.inputYesNo(prompt='Do you want any extras?\n') == 'yes':
    while True:
        selected_extras = pyip.inputMenu(['Mayo', 'Mustard', 'Lettuce', 'Tomato'], prompt='Choose your extras:\n', numbered=True)
        total_cost += float(price_list[selected_extras])
        print(f'Total cost so far: {total_cost}$')
        if pyip.inputYesNo(prompt='Do you want any more extras?\n') != 'yes':
            break

# Specify the number of sandwiches
number_of_sandwiches = pyip.inputInt(prompt='How many sandwiches do you want?\n', min=1, max=20)
total_cost *= number_of_sandwiches
print(f'Total order cost: {total_cost}$\n')

# Payment method choice
payment_method = pyip.inputChoice(['card', 'cash'], prompt='Payment by card or cash?\n')
print(f'You chose to pay by {payment_method}.')

# Final order summary
print('Thank you for your order. Enjoy your sandwich!')
