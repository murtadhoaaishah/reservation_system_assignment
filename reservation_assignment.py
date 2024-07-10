tables = [
    {'number': 1, 'seats': 2},
    {'number': 2, 'seats': 6},
    {'number': 3, 'seats': 2},
    {'number': 4, 'seats': 4},
    {'number': 5, 'seats': 8},
]

class Reservation:

    reservations_list = []

    def __init__(self, name, party_size, contact):
        self.name = name
        self.party_size = party_size
        self.contact = contact


    def make_reservation(self):
        for table in tables:
            if table['seats'] >= self.party_size and table['number'] not in [table['table_number'] for table in Reservation.reservations_list]: # loops through the tables list to see if the available seats specified in the tables that can accomodate the perty size and table number does not readily exist in reservations_list list
                reservation_det = {
                    "name": self.name,
                    "party_size": self.party_size,
                    "contact": self.contact,
                    "table_number": table['number']
                    } #details required to save reservation to the rserved list
                reservation_det['table_number'] = table['number'] #it should add  a key called table_number and set it the table number that suits the party size to it
                print(f"table number {table['number']} has been reserved for {self.name}")
                Reservation.reservations_list.append(reservation_det) #it should save it to the reservations_list 
                return
        print("No available table for the given party size")

    


    @classmethod
    def view_reservations(cls):
        reserved_table = [reservation['table_number'] for reservation in cls.reservations_list] #it should loop through the reservations_list list, create a list of all table numbers reserved and save it in reserved table
        print(f"{'Table number' if len(reserved_table) < 2 else 'Table numbers'}: {reserved_table}")

    @classmethod
    def cancel_reservation(cls, name, table_number):
        # if name and table_number:
            for reservation in cls.reservations_list:
                if reservation['name'] == name and reservation['table_number'] == table_number: # it should check if the name and number cancelling the reservation exists on the reservations_list
                    cls.reservations_list.remove(reservation) #if it does, it should remove it from the list



    @classmethod
    def modify_reservation(cls, name, table_number, new_party_size):
        for reservation in cls.reservations_list:
            if reservation['name'] == name and reservation['table_number'] == table_number:
                for table in tables: 
                    if table['seats'] >= new_party_size and table['number'] not in [reservation['table_number'] for reservation in cls.reservations_list]:
                        reservation['party_size'] = new_party_size
                        reservation['table_number'] = table['number']
                        print(f"Reservation for {name} has been changed from table number {table_number} to table number {reservation['table_number']}")
                        return
                print('no table available')
                return

        print(f'no reservation made with the name {name}')

                


# print(Reservation.reservations_list)
# reservation2 = Reservation('John', 2, '07012345678')
# reservation2.make_reservation()

# reservation3 = Reservation('Emily', 4, '08098765432')
# reservation3.make_reservation()




def menu():
    while True:
        print("\n1. Make Reservation\n2. View Reservations\n3. Cancel Reservation\n4. Exit")
        menu = input("Enter your choice: ")

        if menu == '1':
            name= input('Enter your name: ')
            party_size = int(input('Enter your party size: '))
            contact_number = int(input('Enter your contact number: '))

            reservation = Reservation(name, party_size, contact_number)
            reservation.make_reservation()

        elif menu == '2':
            Reservation.view_reservations()

        elif menu == '3':
            name = input('Enter your name: ')
            table_number = int(input('Enter your table number: '))

            Reservation.cancel_reservation(name, table_number)    

        elif menu == '4':
            name = input('Enter your name: ')
            table_number = int(input('Enter your table number: '))
            new_party_size = int(input('Enter your new party size: '))

            Reservation.modify_reservation(name, table_number, new_party_size)

        elif  menu == '5':
            break

        else:
            print('Choose a valid option on the menu list')

menu()
