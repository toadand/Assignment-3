
# Prints the menu, where a menu is a dictionary
def print_menu(menu):
    for k, v in menu.items():
        print(f'{k}: {v}')

# Returns an integer corresponding to the user's selection from a dictionary
def get_selection(_dict):
    while True:
        try:
            print_menu(_dict)
            first_key = list(_dict)[0]
            last_key = list(_dict)[-1]
            selection = int(input(f'Enter selection ({first_key}-{last_key}): '))
            if selection in _dict.keys():
                print(_dict.get(selection), 'selected.\n')
                return selection
            else:
                print(f'Invalid selection. Please enter a number between {first_key} and {last_key}.\n')
        except:
            print(f'Invalid selection. Please enter a number between {first_key} and {last_key}.\n')

# Get Int
# Prompts the user to enter an int until one is entered
# Optional int range
def get_int(prompt, min_val = None, max_val = None):
    while True:
        try:
            user_input = int(input(prompt))
            if min_val is not None and user_input < min_val:
                print(f'Invalid input. Please enter a number greater than {min_val}.')
                continue
            if max_val is not None and user_input > max_val:
                print(f'Invalid input. Please enter a number less than {max_val}.')
                continue
            return user_input
        except:
            if min_val is not None and max_val is not None:
                print(f'Invalid input. Please enter a number between {min_val} and {max_val}.')
            elif min_val is not None:
                print(f'Invalid input. Please enter a number greater than {min_val}.')
            elif max_val is not None:
                print(f'Invalid input. Please enter a number less than {max_val}.')
            else:
                print('Invalid input. Please enter a number.')

# List to string
# Joins each value from a list into a single string
def list_to_string(array, separator=''):
    string = separator.join(map(str, array))
    return string
