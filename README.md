# Hotel Room Allotment System Using Python

## 1. Project Overview

The Hotel Room Allotment System is a command-line based Python application designed to simplify basic hotel room management.

The system allows a hotel staff member to view rooms, check room availability, allot rooms to guests, maintain booking information, search for guests, cancel bookings, check out guests, calculate bills, and view a basic hotel summary.

The project is designed using fundamental Python programming concepts such as lists, dictionaries, functions, loops, conditional statements, strings, input/output operations, type conversion, and basic exception handling.

The project does not require a database, graphical interface, external API, or internet connection.

---

## 2. Problem Statement

Managing hotel room allocation manually can result in problems such as difficulty tracking room availability, accidental double booking, inefficient guest record searching, and errors during checkout and bill calculation.

The objective of this project is to develop a simple command-line Hotel Room Allotment System using Python that provides a structured way to manage room availability and guest bookings.

The system maintains room and booking information using Python data structures and provides functions for room viewing, availability checking, booking, guest searching, cancellation, checkout, billing, and hotel summary generation.

The system must ensure that an already booked room cannot be allotted to another guest and that invalid user inputs are handled appropriately.

---

## 3. Objectives

The main objectives are:

1. To develop a basic hotel room management application using Python.
2. To maintain room information using lists and dictionaries.
3. To check room availability before allotment.
4. To prevent double booking of rooms.
5. To store and retrieve guest booking information.
6. To provide booking cancellation functionality.
7. To calculate the total bill during checkout.
8. To provide a basic hotel occupancy summary.
9. To demonstrate modular programming using multiple Python files.
10. To apply input validation and basic error handling.

---

## 4. Features

### Room Management

* View all rooms
* View available rooms
* Search for a room
* Check room status
* Display room type and price

### Booking Management

* Book a room
* Generate a unique booking ID
* Store guest information
* Prevent double booking
* View booking details
* Cancel booking

### Guest Management

* Search guest by name
* Display guest booking information

### Billing

* Enter number of nights
* Calculate total amount
* Complete checkout
* Release the room after checkout

### Reporting

* Total number of rooms
* Available rooms
* Booked rooms
* Room-type statistics

### Validation

* Invalid menu choice handling
* Invalid room handling
* Invalid booking ID handling
* Basic numeric input validation
* Prevention of booking occupied rooms

---

## 5. Technologies Used

* Python 3
* Git
* GitHub
* Command Line / Terminal

### Python Concepts Used

* Variables
* Data types
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* String operations
* Type conversion
* Exception handling
* Modules and imports

---

## 6. Project Structure

```text
Hotel-Room-Allotment-System/
│
├── README.md
├── statement.md
├── requirements.txt
├── main.py
│
├── modules/
│   ├── __init__.py
│   ├── room_manager.py
│   ├── booking_manager.py
│   ├── guest_manager.py
│   ├── billing.py
│   └── reports.py
│
├── data/
│   ├── rooms.py
│   └── bookings.py
│
├── tests/
│   └── test_hotel.py
│
└── docs/
    ├── architecture.md
    ├── workflow.md
    └── diagrams.md
```

---

## 7. Requirements

Python 3.8 or later is recommended.

The project uses only Python's standard functionality and does not require external packages.

---

## 8. Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/AvikamGupta/Hotel-Room-Allotment-System.git
```

### Step 2: Open the project directory

```bash
cd Hotel-Room-Allotment-System
```

### Step 3: Verify Python installation

```bash
python --version
```

If your system uses `python3`:

```bash
python3 --version
```

### Step 4: Install dependencies

The project does not require third-party packages.

If a requirements file is provided:

```bash
pip install -r requirements.txt
```

---

## 9. Running the Project

From the project root directory:

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

The main menu will appear in the terminal.

---

## 10. Main Menu

```text
========================================
       HOTEL ROOM ALLOTMENT SYSTEM
========================================

1. View All Rooms
2. View Available Rooms
3. Book a Room
4. View Booking Details
5. Search Guest
6. Cancel Booking
7. Check Out
8. Hotel Summary
9. Exit
```

---

## 11. Example Workflow

### Booking a Room

```text
Enter Room Number: 201

Room 201
Type: Double
Price: ₹2500/night
Status: Available

Confirm booking? Y/N: Y

Enter Guest Name: Avikam
Enter Age: 18
Enter Phone Number: 9876543210
Enter Number of Guests: 2
```

The system generates a booking ID such as:

```text
B001
```

and changes the room status from:

```text
Available
```

to:

```text
Booked
```

---

## 12. Double Booking Prevention

If Room 201 is already booked:

```text
Enter Room Number: 201

Room 201 is already occupied.
Please select another room.
```

The system will not create another booking for the same room.

---

## 13. Checkout

During checkout, the system asks for the number of nights.

For example:

```text
Room price = ₹2500/night
Number of nights = 3

Total = ₹7500
```

After successful checkout, the room status changes back to:

```text
Available
```

---

## 14. Testing

Basic validation tests are included in the `tests` directory.

The project should be tested for:

* Valid room booking
* Already booked room
* Invalid room number
* Invalid booking ID
* Guest search
* Booking cancellation
* Checkout
* Invalid number of nights
* Room availability after cancellation
* Room availability after checkout

---

## 15. Limitations

The current version is intentionally designed as a first-semester Python project.

It does not include:

* SQL/database storage
* Online booking
* Login/authentication
* Payment gateway
* Email/SMS services
* Graphical user interface
* Cloud deployment
* External APIs

The application stores information during the current program execution.

---

## 16. Future Enhancements

Possible future improvements include:

* Database integration
* Graphical user interface
* Persistent booking records
* User authentication
* Online booking
* Payment integration
* Date-based check-in/check-out
* Advanced reporting

These enhancements are outside the scope of the current implementation.

---

## 17. Author

**Rishi Soni**

Branch: B.Tech AI/ML
Registration Number: 26BAI11014

---

## 18. License

This project is developed as an academic project for educational purposes.
