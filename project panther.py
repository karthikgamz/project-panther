print("Hello")
print("Welcome to Project Panther")
print("Press 1 to access calculator")
print("Press 2 to use weather")
print("Press 3 to use story generator")
print("Press 4 to use number guesser")
print("Press 5 to use currency converter")
print("Press 6 to use dice roll")
print("Press 7 to learn about")

choice = input("Enter your choice (1/2/3/4/5/6/7): ")

if choice == "1":
    # Code to open the calculator
    print("You chose to access the calculator.")
    
    # Add your calculator code here
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    while True:
        print("Select operation.")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter choice (1/2/3/4): ")

        if operation in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operation == '4':
                result = divide(num1, num2)
                if result == "Cannot divide by zero":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid input")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != "yes":
            break

elif choice == "2":
    # Code to use the weather feature
    print("You chose to use the weather feature.")
    
    # Add your weather code here
    import requests
    
    city = input("Enter Your City: ")
    Api_Key = "Your-API-Key-Here"
    final_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_Key}"
    
    response = requests.get(final_URL)
    data = response.json()
    
    if data['cod'] == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        print(f"Temperature: {temperature}K")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
    else:
        print("City not found")

elif choice == "3":
    # Code to use the story generator
    print("You chose to use the story generator.")
    
    # Add your story generator code here
    def get_input(word_type):
        user_input = input(f"Enter a {word_type}: ")
        return user_input

    noun1 = get_input("noun")
    adjective1 = get_input("adjective")
    verb1 = get_input("verb")
    noun2 = get_input("noun")
    verb2 = get_input("verb")

    story = f"""
    Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} all day.

    One day, {noun2} walked into the room and caught the {noun1} in the act.

    {noun2}: "What are you doing?"
    {noun1}: "I'm just {verb1}ing, what's the big deal?"
    {noun2}: "Well, it's not every day that you see a {noun1} {verb1}ing in the middle of the day."
    {noun1}: "I guess you're right. Maybe I should take a break."
    {noun2}: "That's probably a good idea. Why don't we go {verb2} instead?"
    {noun1}: "Sure, that sounds like fun!"

    And so, {noun2} and the {noun1} went off to {verb2} and had a great time.
    The end.
    """
    
    print(story)

elif choice == "4":
    # Code for the number guesser
    print("You chose to use the number guesser.")
    
    # Add your number guesser code here
    import random
    
    def guess_the_number():
        number_to_guess = random.randint(1, 100)
        attempts = 0
    
        while True:
            user_guess = int(input("Guess the number (1-100): "))
            attempts += 1
    
            if user_guess < number_to_guess:
                print("Try higher!")
            elif user_guess > number_to_guess:
                print("Try lower!")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break

    guess_the_number()

elif choice == "5":
    # Code for the currency converter
    print("You chose to use the currency converter.")
    
    # Add your currency converter code here
    # You can use exchange rate data to convert currencies

elif choice == "6":
    # Code for dice roll
    print("You chose to use the dice roll.")
    
    # Add your dice roll code here
    import random
    
    def roll_dice():
        return random.randint(1, 6)
    
    result = roll_dice()
    print(f"You rolled a {result}")

elif choice == "7":
    # Code to provide information about Project Panther
    print("You chose to learn about Project Panther.")
    
    # Add your information about Project Panther here
    print("Project Panther is an amazing project created by Python enthusiasts.")
    print("It offers various fun and useful features for users to enjoy.")
    print("Feel free to explore and use the different functionalities!")

else:

    print("Invalid choice. Please enter a valid option (1-7).")
