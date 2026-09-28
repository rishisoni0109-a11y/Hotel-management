# Hotel Room Allotment System

## 1. Problem Statement

Hotels need to manage room availability and guest bookings efficiently. Manual room allocation can result in difficulties such as identifying available rooms, maintaining guest records, preventing double booking, and calculating checkout bills.

The Hotel Room Allotment System aims to provide a simple command-line solution for managing these basic hotel operations using Python.

The system allows users to view rooms, check availability, allot rooms, store guest information, search bookings, cancel bookings, check out guests, calculate bills, and view a hotel summary.

The system prevents an occupied room from being allotted to another guest and provides basic validation for incorrect inputs.

---

## 2. Scope

The project is limited to a command-line environment and focuses on basic hotel room management.

The scope includes:

* Room information management
* Room availability checking
* Room allotment
* Guest information management
* Booking identification
* Guest search
* Booking cancellation
* Checkout
* Basic bill calculation
* Hotel occupancy summary
* Input validation

The project does not include database systems, online services, payment gateways, authentication systems, or graphical interfaces.

---

## 3. Target Users

The intended users are:

* Small hotel staff
* Reception desk operators
* Students learning programming
* Academic evaluators

The current implementation is primarily an educational prototype demonstrating Python programming concepts.

---

## 4. High-Level Features

### Room Management

The system stores room number, room type, price, and availability status.

### Room Availability

The system identifies whether a room is available or already booked.

### Room Booking

Users can allot an available room to a guest.

### Guest Management

Guest details such as name, age, phone number, and number of guests are stored with the booking.

### Booking Search

Users can search for a booking using a booking ID or search for a guest by name.

### Cancellation

An active booking can be cancelled and the associated room becomes available again.

### Checkout

The system calculates the bill according to the room price and number of nights.

### Reporting

The system displays total, available, and booked rooms along with room-type statistics.

---

## 5. Core Constraint

A room whose status is `Booked` cannot be allotted to another guest until its existing booking is cancelled or checked out.

This is the primary business rule of the system.
