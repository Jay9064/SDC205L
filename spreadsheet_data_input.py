from datetime import datetime

student_id = "Jasgut7158"

# Set this to the spreadsheet you chose: "Temperature", "Weight", or "Rain Amount".
SPREADSHEET_TYPE = "Temperature"

menu_options = {
    "1": "Input Data",
    "2": "View Current Data",
    "3": "Generate Report"
}


def convertData(data):
    """Convert one numeric value for the selected spreadsheet; return the converted value."""
    if SPREADSHEET_TYPE == "Temperature":
        # Convert Fahrenheit to Celsius.
        return (data - 32) * 5 / 9
    elif SPREADSHEET_TYPE == "Weight":
        # Convert pounds to kilograms.
        return data / 2.205
    elif SPREADSHEET_TYPE == "Rain Amount":
        # Convert inches to centimeters.
        return data * 2.54
    else:
        raise ValueError("SPREADSHEET_TYPE must be Temperature, Weight, or Rain Amount.")


def getInput():
    """Collect dated values, convert them, and display each saved record."""
    while True:
        try:
            entry_count = int(input("How many entries are you inputting?\n"))
            if entry_count < 0:
                print("Please enter zero or a positive whole number.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    records = []

    for _ in range(entry_count):
        entry_date = input("Enter a date: ")

        if SPREADSHEET_TYPE == "Temperature":
            prompt = "Enter the highest temp for the inputted date: "
        elif SPREADSHEET_TYPE == "Weight":
            prompt = "Enter the weight in pounds for the inputted date: "
        else:
            prompt = "Enter the rain amount in inches for the inputted date: "

        while True:
            try:
                value = float(input(prompt))
                break
            except ValueError:
                print("Please enter a numeric value.")

        # Function: convertData; argument: the entered numeric value (float);
        # expected return: the converted numeric value (float).
        converted_value = convertData(value)
        records.append((entry_date, value, converted_value))

        print(
            f"The following was saved at {datetime.now()} : "
            f"{entry_date},{value},{converted_value}"
        )

    return records


# Keep the application title as the first line printed by the program.
print(f"{student_id}'s Spreadsheet Automation Menu")
print("Choose a number from the following options")

# Each option_number is the menu key; description is its corresponding label.
for option_number, description in menu_options.items():
    print(option_number, description)

choice = input()

if choice in menu_options:
    print(f"You selected {choice} at {datetime.now()}")
    if choice == "1":
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")
else:
    print("Error: Invalid choice selected.")
