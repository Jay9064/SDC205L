from datetime import datetime

# Replace this with your own student ID.
student_id = "Jasgut7158"

# Each key is a menu number, and each value is that option's description.
menu_options = {
    "1": "Input Data",
    "2": "View Current Data",
    "3": "Generate Report"
}

# Display the application name first, including the student's ID.
print(f"{student_id}'s Spreadsheet Automation Menu")
print("Choose a number from the following options")

# Each option_number is a menu key, and description is its text label.
for option_number, description in menu_options.items():
    print(option_number, description)

# Read the user's selection as text so it can be checked against the menu keys.
choice = input()

if choice in menu_options:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"You selected {choice} at {current_time}")
else:
    print("Error: Invalid choice selected.")
