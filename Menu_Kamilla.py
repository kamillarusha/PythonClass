# Defining the 'menu' dictionary with items and their prices
menu = {
    'Hamburger': {'calories': 600, 'price': 5},
    'Cheese Burger': {'calories': 750, 'price': 6},
    'Veggie Burger': {'calories': 400, 'price': 5},
    'Vegan Burger': {'calories': 350, 'price': 5},
    'Sweet Potatoes': {'calories': 230, 'price': 3},
    'Salad': {'calories': 15, 'price': 4},
    'Iced Tea': {'calories': 70, 'price': 1},
    'Lemonade': {'calories': 90, 'price': 2},
}

# Defining the 'combos' dictionary with combo items
combos = {
    "Cheesy Combo": ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo": ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo": ["Vegan Burger", "Salad", "Lemonade"],
}

# Initializing a list to store selected items
selected_items = []

# Initializing variables for total calorie count and total cost
total_calories = 0
total_cost = 0

# Creating a loop to input meal options
while True:
    order_item = input("Enter a meal or combo from the menu (or 'done' to finish): ").strip()
    
    # Checking if the user wants to exit the loop
    if order_item.lower() == 'done':
        break
    
    # Checking if the entered item is a combo or a valid meal
    if order_item in combos:
        combo_items = combos[order_item]
        selected_items.extend(combo_items)
        print(f"Added '{order_item}' to the order.")
    elif order_item in menu:
        selected_items.append(order_item)
        print(f"Added '{order_item}' to the order.")
    else:
        print(f"'{order_item}' not found in the menu.")
        
# Calculating the total calorie count and total cost for the selected options
for item in selected_items:
    if item in menu:
        total_calories += menu[item]['calories']
        total_cost += menu[item]['price']

# Displaying selected items, total calorie count, and total cost
if selected_items:
    print("\nSelected items in the order:")
    for item in selected_items:
        print(f"{item}: {menu.get(item, {}).get('calories', 'Calorie info not found')} calories - ${menu.get(item, {}).get('price', 'Price info not found')}")
    print(f"\nTotal calorie count for the order: {total_calories} calories")
    print(f"Total cost of the order: ${total_cost:.2f}")
else:
    print("No items selected.")
    
