tables = [
    {'number': 1, 'seats': 2},
    {'number': 2, 'seats': 6},
    {'number': 3, 'seats': 2},
    {'number': 4, 'seats': 4},
    {'number': 5, 'seats': 8},
]

class Reservation:
    reserved = []

    def __init__(self, name, party_size, contact):
        self.name = name
        self.party_size = party_size
        self.contact = contact

    @classmethod
    def make_reservation(cls, name, party_size, contact):
        for table in tables:
            if table['seats'] >= party_size and table['number'] not in [r['table_number'] for r in cls.reserved]:
                reservation_det = {
                    "name": name,
                    "party_size": party_size,
                    "contact": contact,
                    "table_number": table['number']
                }
                cls.reserved.append(reservation_det)
                print(f"Table number {table['number']} reserved for {name}")
                return
        print("No available table for the given party size")

    @classmethod
    def view_reservations(cls):
        if not cls.reserved:
            print("No reservations found.")
            return
        print("Current reservations:")
        for r in cls.reserved:
            print(f"Table {r['table_number']} reserved for {r['name']} (Party size: {r['party_size']}, Contact: {r['contact']})")

    @classmethod
    def cancel_reservation(cls, name, table_number):
        for r in cls.reserved:
            if r['name'] == name and r['table_number'] == table_number:
                cls.reserved.remove(r)
                print(f"Reservation for table {table_number} made by {name} cancelled")
                return
        print(f"No reservation found for {name} at table {table_number}")

def main_menu():
    while True:
        print("\n1. Make Reservation\n2. View Reservations\n3. Cancel Reservation\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            try:
                party_size = int(input("Enter party size: "))
            except ValueError:
                print("Invalid input for party size. Please enter an integer.")
                continue
            contact = input("Enter contact number: ")
            Reservation.make_reservation(name, party_size, contact)
        elif choice == '2':
            Reservation.view_reservations()
        elif choice == '3':
            name = input("Enter your name: ")
            try:
                table_number = int(input("Enter table number: "))
            except ValueError:
                print("Invalid input for table number. Please enter an integer.")
                continue
            Reservation.cancel_reservation(name, table_number)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the reservation system
main_menu()
