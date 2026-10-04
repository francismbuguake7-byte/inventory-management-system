import cli_actions

def print_menu():
    print('\n=== Inventory Management CLI ===')
    print('1. View inventory')
    print('2. Add item')
    print('3. Update item')
    print('4. Delete item')
    print('5. Search OpenFoodFacts')
    print('6. Import product from OpenFoodFacts')
    print('7. Exit')

def handle_choice(choice):
    if choice == '1':
        cli_actions.view_inventory()
    elif choice == '2':
        cli_actions.add_item()
    elif choice == '3':
        cli_actions.update_item()
    elif choice == '4':
        cli_actions.delete_item()
    elif choice == '5':
        cli_actions.search_api()
    elif choice == '6':
        cli_actions.import_api()
    elif choice == '7':
        print('Goodbye!')
        return False
    else:
        print('Invalid choice, please try again.')
    return True

def main():
    running = True
    while running:
        print_menu()
        choice = input('Choose an option (1-7): ')
        running = handle_choice(choice)
if __name__ == '__main__':
    main()
