
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}! Welcome to Vend-a-car!")

def get_age():
    return input("Please enter your age: ")

def show_menu():
    print("How can I help you today?")
    print("1. Browse available cars")
    print("2. Learn about financing options")
    print("3. Trade in your car")
    print("4. Contact customer support")
    print("5. Exit")

def main():
    user_name = get_user_name()
    greet_user(user_name)
    age = get_age()
    print(f"Age {age} recorded.\n")

    while True:
        show_menu()
        choice = input("Please choose an option (1-5): ")
        if choice == "1":
            print("Showing available cars...\n")
        elif choice == "2":
            print("Explaining financing options...\n")
        elif choice == "3":
            print("Starting trade-in process...\n")
        elif choice == "4":
            print("Connecting you to customer support...\n")
        elif choice == "5":
            print(f"Goodbye {user_name}, thanks for visiting Vend-a-car!")
            break
        else:
            print("Invalid choice. Please pick a number 1-5.\n")

if __name__ == "__main__":
    main()
