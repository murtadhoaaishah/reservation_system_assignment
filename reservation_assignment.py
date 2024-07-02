tables =[
    {
    'number': 1, 'seats': 2,
},
{
    'number': 2, 'seats': 6,
},
{
    'number': 3, 'seats': 2,
},
{
    'number': 4, 'seats': 4,
},
{
    'number': 5, 'seats': 8,
}
]

class Reservation:

    reserved = []

    def __init__(self, name, party_size, contact):
        self.name = name
        self.party_size = party_size
        self.contact = contact



    def make_reservation(self):
        for table in tables:
            if table['seats'] >= self.party_size and table['number'] not in [table['table_number'] for table in Reservation.reserved]: # loops through the tables list to see if the available seats specified in the tables that can accomodate the perty size and table number does not readily exist in reserved list
                reservation_det = {
                    "name": self.name,
                    "party_size": self.party_size,
                    "contact": self.contact
                    } #details required to save reservation to the rserved list
                reservation_det['table_number'] = table['number'] #it should add  a key called table_number and set it the table number that suits the party size to it
                print(f"table number {table['number']} reserved for {self.name}")
                Reservation.reserved.append(reservation_det) #it should save it to the reserved list
                return
        print(f"table not available")

    def view_reservations(self):
        reserved_table = [reservation['table_number'] for reservation in Reservation.reserved] #it should loop through the reserved list, create a list of all table numbers reserved and save it in reserved table
        print(f"{'Table number' if len(reserved_table) < 2 else 'Table numbers'}: {reserved_table}")

    def cancel_reservation(self, name, table_number):
        # if name and table_number:
            for reservation in Reservation.reserved:
                if reservation['name'] == name and reservation['table_number'] == table_number: # it should check if the name and number cancelling the reservation exists on the reserved list
                    Reservation.reserved.remove(reservation) #if it does, it should remove it from the list

                    print(f"Reservation for table {reservation['table_number']} made by {reservation['name']} cancelled")
                    return
            print(f"No reservation made for {name}") #else it should print this


reservation1 = Reservation('Aaishah', 8, '08023269533')
reservation1.make_reservation()
# print(Reservation.reserved)
reservation2 = Reservation('John', 2, '07012345678')
reservation2.make_reservation()

reservation3 = Reservation('Emily', 4, '08098765432')
reservation3.make_reservation()

reservation1.cancel_reservation('Aaishah', 5)    
print(Reservation.reserved)  