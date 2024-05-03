# List to store user information
user_data = []

# Function to get user input and store it
def get_user_input():
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    sports_equipment = input("Enter the name of sports equipment: ")
    sap_id = input("Enter your SAP ID: ")
    return {"Name": name, "Phone Number": phone_number, "Sports Equipment": sports_equipment, "SAP ID": sap_id}

# Function to display all stored user information
def display_user_data():
    print("\nUser Information:")
    for user in user_data:
        print("Name:", user["Name"])
        print("Phone Number:", user["Phone Number"])
        print("Sports Equipment:", user["Sports Equipment"])
        print("SAP ID:", user["SAP ID"])
        print()

# Function to search for a user by name
def search_user_by_name(name):
    found = False
    for user in user_data:
        if user["Name"].lower() == name.lower():
            print("\nUser Information for", name + ":")
            print("Name:", user["Name"])
            print("Phone Number:", user["Phone Number"])
            print("Sports Equipment:", user["Sports Equipment"])
            print("SAP ID:", user["SAP ID"])
            found = True
            break
    if not found:
        print("\nUser", name, "not found.")

# Function to search for a user by SAP ID
def search_user_by_sap_id(sap_id):
    found = False
    for user in user_data:
        if user["SAP ID"] == sap_id:
            print("\nUser Information for SAP ID", sap_id + ":")
            print("Name:", user["Name"])
            print("Phone Number:", user["Phone Number"])
            print("Sports Equipment:", user["Sports Equipment"])
            print("SAP ID:", user["SAP ID"])
            found = True
            break
    if not found:
        print("\nUser with SAP ID", sap_id, "not found.")

# Function to search for a user by sports equipment
def search_user_by_sports_equipment(equipment):
    found = False
    for user in user_data:
        if user["Sports Equipment"].lower() == equipment.lower():
            print("\nUser Information for", equipment + ":")
            print("Name:", user["Name"])
            print("Phone Number:", user["Phone Number"])
            print("Sports Equipment:", user["Sports Equipment"])
            print("SAP ID:", user["SAP ID"])
            found = True
    if not found:
        print("\nNo user found with the sports equipment", equipment)

# Function to write user data to a file
def write_to_file(user_data):
    with open("user_data.txt", "a") as file:
        for user in user_data:
            file.write(f"Name: {user['Name']}, Phone Number: {user['Phone Number']}, Sports Equipment: {user['Sports Equipment']}, SAP ID: {user['SAP ID']}\n")

# Function to read user data from the file
def read_from_file():
    with open("user_data.txt", "r") as file:
        print(file.read())

# Main function
def main():
    # Get user input
    while True:
        user_input = get_user_input()
        user_data.append(user_input)
        display_user_data()
        continue_input = input("Do you want to continue entering data? (yes/no): ")
        if continue_input.lower() != "yes":
            break

    # Write user data to file
    write_to_file(user_data)

    # After entering all data, allow the user to search for a specific user
    while True:
        search_choice = input("\nEnter the type of search you want to perform (name/sap_id/sports_equipment): ")
        if search_choice.lower() == "name":
            search_name = input("Enter the name of the user you want to search for: ")
            search_user_by_name(search_name)
        elif search_choice.lower() == "sap_id":
            search_sap_id = input("Enter the SAP ID of the user you want to search for: ")
            search_user_by_sap_id(search_sap_id)
        elif search_choice.lower() == "sports_equipment":
            search_equipment = input("Enter the sports equipment you want to search for: ")
            search_user_by_sports_equipment(search_equipment)
        else:
            print("Invalid search type. Please enter 'name', 'sap_id', or 'sports_equipment'.")

        continue_search = input("Do you want to perform another search? (yes/no): ")
        if continue_search.lower() != "yes":
            break

if __name__ == "__main__":
    main()
