# ACTIVITY TRACKER MAIN SYSTEM
# Controls menu and user actions

from tracker import start_activity, stop_activity
from storage import load_entries

# Display menu options
def show_menu():
    print("\n========================")
    print("   ACTIVITY TRACKER")
    print("========================")
    print("1. Start Activity")
    print("2. Stop Activity")
    print("3. View History")
    print("4. Exit")

#infinite loop
while True:
    show_menu()
    choice = input("\nEnter choice: ")

    if choice == "1":
        name = input("Enter activity name: ")
        print(start_activity(name))

    elif choice == "2":
        print(stop_activity())

    elif choice == "3":
        print("\n--- HISTORY ---")
        entries = load_entries()

        if not entries:
            print("No data yet.")
        else:
            for e in entries:
                print("-", e)

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")