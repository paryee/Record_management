import json

# Function to load records from a JSON file
def load_records():
    try:
        with open("records.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save records to a JSON file
def save_records(records):
    with open("records.json", "w") as file:
        json.dump(records, file)

# Function to add a new record
def add_record(records):
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email address: ")

    records[username] = {
        "password": password,
        "email": email
    }

    save_records(records)
    print("Record added successfully.")

# Function to retrieve a record
def retrieve_record(records):
    username = input("Enter username: ")

    if username in records:
        record = records[username]
        print(f"Username: {username}")
        print(f"Password: {record['password']}")
        print(f"Email: {record['email']}")
    else:
        print("Record not found.")

# Function to update a record
def update_record(records):
    username = input("Enter username: ")

    if username in records:
        record = records[username]
        password = input("Enter new password (leave blank to keep existing): ")
        email = input("Enter new email address (leave blank to keep existing): ")

        if password:
            record['password'] = password
        if email:
            record['email'] = email

        save_records(records)
        print("Record updated successfully.")
    else:
        print("Record not found.")

# Function to delete a record
def delete_record(records):
    username = input("Enter username: ")

    if username in records:
        del records[username]
        save_records(records)
        print("Record deleted successfully.")
    else:
        print("Record not found.")

# Main program loop
def main():
    records = load_records()

    while True:
        print("\nPersonal Record Management System")
        print("1. Add Record")
        print("2. Retrieve Record")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            retrieve_record(records)
        elif choice == "3":
            update_record(records)
        elif choice == "4":
            delete_record(records)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()