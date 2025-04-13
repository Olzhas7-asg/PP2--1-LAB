import psycopg2
import csv

# Connect to the PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            host='localhost',  # Update with your parameters
            port=5432,
            database='phonebook_db',
            user='postgres',
            password='admin'
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Connection error: {e}")
        return None

# Create the PhoneBook table
def create_table():
    conn = connect_to_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PhoneBook (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                phone VARCHAR(15) NOT NULL
            );
        """)
        conn.commit()
        print("PhoneBook table created.")
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

# Insert data from a CSV file
def insert_data_from_csv(csv_file):
    conn = connect_to_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                cursor.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", row)
        conn.commit()
        print("Data from CSV successfully added.")
    except Exception as e:
        print(f"Error adding data from CSV: {e}")
    finally:
        conn.close()

# Insert data from console
def insert_data_from_console():
    conn = connect_to_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        username = input("Enter username: ")
        phone = input("Enter phone number: ")
        cursor.execute("INSERT INTO PhoneBook (username, phone) VALUES (%s, %s)", (username, phone))
        conn.commit()
        print("Data successfully added.")
    except Exception as e:
        print(f"Error adding data: {e}")
    finally:
        conn.close()

# Update data in the table
def update_data():
    conn = connect_to_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        username = input("Enter username to update: ")
        new_phone = input("Enter the new phone number: ")
        cursor.execute("UPDATE PhoneBook SET phone = %s WHERE username = %s", (new_phone, username))
        conn.commit()
        if cursor.rowcount > 0:
            print("Data successfully updated.")
        else:
            print("User not found.")
    except Exception as e:
        print(f"Error updating data: {e}")
    finally:
        conn.close()

# Query data from the table with filters
def query_data():
    conn = connect_to_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        filter_type = input("Filter by (username/phone): ").strip().lower()
        value = input(f"Enter value for {filter_type}: ")
        query = f"SELECT * FROM PhoneBook WHERE {filter_type} = %s"
        cursor.execute(query, (value,))
        results = cursor.fetchall()
        if results:
            print("Results:")
            for row in results:
                print(row)
        else:
            print("No records found.")
    except Exception as e:
        print(f"Error querying data: {e}")
    finally:
        conn.close()

# Delete data from the table
def delete_data():
    conn = connect_to_db()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        username = input("Enter username to delete: ")
        cursor.execute("DELETE FROM PhoneBook WHERE username = %s", (username,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Data successfully deleted.")
        else:
            print("User not found.")
    except Exception as e:
        print(f"Error deleting data: {e}")
    finally:
        conn.close()

# Main menu for interaction
def main_menu():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Add data from CSV")
        print("2. Add data from console")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            csv_file = input("Enter the path to the CSV file: ")
            insert_data_from_csv(csv_file)
        elif choice == '2':
            insert_data_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

# Program entry point
if __name__ == "__main__":
    main_menu()
