# Hotel Room Allotment System using Basic Python

rooms = [
    {"room": 101, "type": "Single", "price": 1500, "status": "Available"},
    {"room": 102, "type": "Single", "price": 1500, "status": "Available"},
    {"room": 201, "type": "Double", "price": 2500, "status": "Available"},
    {"room": 202, "type": "Double", "price": 2500, "status": "Available"},
    {"room": 301, "type": "Deluxe", "price": 3500, "status": "Available"}
]
bookings = []       # stores every active booking as a dictionary
booking_counter = 1  # used to generate Booking IDs like B001, B002..
def view():
    print("\n{:<8}{:<10}{:<10}{:<10}".format("Room", "Type", "Price", "Status"))
    print("-" * 40)
    for room in rooms:
        print("{:<8}{:<10}{:<10}{:<10}".format(
            room["room"], room["type"], room["price"], room["status"]
        ))

def available():
    for room in rooms:
        if room["status"] == "Available":
            print(f"Room {room['room']} is available")
        else:
            print(f"Room {room['room']} is already booked")
def find_room(room_number):
    """Return the room dict matching room_number, or None if not found."""
    for room in rooms:
        if room["room"] == room_number:
            return room
    return None
def find_booking(booking_id):
    """Return the booking dict matching booking_id, or None if not found."""
    for booking in bookings:
        if booking["id"] == booking_id:
            return booking
    return None
def book_room():
    global booking_counter
    room_number = int(input("Enter Room Number: "))
    room = find_room(room_number)
    if room["status"] == "Booked":
        print(f"❌ Room {room_number} is already occupied. Please select another room.")
        return
 
    print(f"\nRoom {room['room']}")
    print(f"Type: {room['type']}")
    print(f"Price: ₹{room['price']}/night")
    print(f"Status: {room['status']}")
 
    confirm = input("Confirm booking? Y/N: ").strip().upper()
    if confirm != "Y":
        print("Booking cancelled by user.")
        return
 
    name = input("Enter Guest Name: ")
    age = int(input("Enter Age: "))
    phone = input("Enter Phone Number: ")
    guests = int(input("Enter Number of Guests: "))
 
    booking_id = "B" + str(booking_counter).zfill(3)
    booking_counter += 1
 
    booking = {
        "id": booking_id,
        "name": name,
        "age": age,
        "phone": phone,
        "guests": guests,
        "room": room["room"],
        "type": room["type"],
        "price": room["price"],
    }
 
    bookings.append(booking)
    room["status"] = "Booked"
 
    print("\n================================")
    print("       BOOKING CONFIRMED")
    print("================================")
    print(f"Booking ID : {booking['id']}")
    print(f"Guest      : {booking['name']}")
    print(f"Room       : {booking['room']}")
    print(f"Room Type  : {booking['type']}")
    print(f"Price      : ₹{booking['price']}/night")
    print(f"Status     : Booked")
    print("================================")

def view_booking_details():
    booking_id = input("Enter Booking ID: ").strip().upper()
    booking = find_booking(booking_id)
 
    if booking is None:
        print("❌ Booking not found.")
        return
 
    print("\nBooking Details:")
    for key, value in booking.items():
        print(f"{key.capitalize()}: {value}")
def search_guest():
    name = input("Enter Guest Name: ").strip().lower()
    found = False
 
    for booking in bookings:
        if booking["name"].lower() == name:
            print("\nGuest Found!")
            print(f"Booking ID : {booking['id']}")
            print(f"Room       : {booking['room']}")
            print(f"Room Type  : {booking['type']}")
            print(f"Status     : Booked")
            found = True
 
    if not found:
        print("❌ No booking found for this guest.")
def cancel_booking():
    booking_id = input("Enter Booking ID: ").strip().upper()
    booking = find_booking(booking_id)
 
    if booking is None:
        print("❌ Booking not found.")
        return
 
    print(f"\nGuest: {booking['name']}")
    print(f"Room: {booking['room']}")
    confirm = input("Cancel booking? Y/N: ").strip().upper()
 
    if confirm == "Y":
        room = find_room(booking["room"])
        if room:
            room["status"] = "Available"
        bookings.remove(booking)
        print("Booking cancelled successfully.")
        print(f"Room {booking['room']} -> Available")
    else:
        print("No changes made.")
def check_out():
    booking_id = input("Enter Booking ID: ").strip().upper()
    booking = find_booking(booking_id)
 
    if booking is None:
        print("❌ Booking not found.")
        return
 
    print(f"\nGuest: {booking['name']}")
    print(f"Room: {booking['room']}")
    print(f"Price: ₹{booking['price']}/night")
 
    try:
        nights = int(input("Number of nights: "))
    except ValueError:
        print("❌ Invalid number of nights.")
        return
 
    total = nights * booking["price"]
    print(f"\nTotal = ₹{total}")
 
    room = find_room(booking["room"])
    if room:
        room["status"] = "Available"
    bookings.remove(booking)
 
    print("Checkout successful.")
    print(f"Room {booking['room']} is now available.")
def hotel_summary():
    total_rooms = len(rooms)
    available = sum(1 for r in rooms if r["status"] == "Available")
    booked = total_rooms - available
 
    single = sum(1 for r in rooms if r["type"] == "Single")
    double = sum(1 for r in rooms if r["type"] == "Double")
    deluxe = sum(1 for r in rooms if r["type"] == "Deluxe")
 
    print("\n================================")
    print("         HOTEL SUMMARY")
    print("================================")
    print(f"Total Rooms      : {total_rooms}")
    print(f"Available Rooms  : {available}")
    print(f"Booked Rooms     : {booked}")
    print()
    print(f"Single Rooms     : {single}")
    print(f"Double Rooms     : {double}")
    print(f"Deluxe Rooms     : {deluxe}")
    print("================================")
 
 
# ------------------ MAIN MENU ------------------
 
def main():
    while True:
        print("\n========================================")
        print("       HOTEL ROOM ALLOTMENT SYSTEM")
        print("========================================")
        print("1. View All Rooms")
        print("2. View Available Rooms")
        print("3. Book a Room")
        print("4. View Booking Details")
        print("5. Search Guest")
        print("6. Cancel Booking")
        print("7. Check Out")
        print("8. Hotel Summary")
        print("9. Exit")
 
        choice = input("\nEnter your choice: ").strip()
 
        if choice == "1":
            view()
        elif choice == "2":
            available()
        elif choice == "3":
            book_room()
        elif choice == "4":
            view_booking_details()
        elif choice == "5":
            search_guest()
        elif choice == "6":
            cancel_booking()
        elif choice == "7":
            check_out()
        elif choice == "8":
            hotel_summary()
        elif choice == "9":
            print("Thank you for using the Hotel Room Allotment System!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-9.")
 
 
if __name__ == "__main__":
    main()
