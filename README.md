# Blood Bank Management System

A **menu-driven Blood Bank Management System built using Python**. The application allows users to register and manage blood donors, record blood donations, manage available blood stock, and handle blood requests through a command-line interface.

## Features

* Add new blood donors
* Automatically generate unique donor IDs
* View all registered donors
* Search for a donor using their donor ID
* Update donor information
* Delete donor records
* Record blood donations
* Track the number of donations made by each donor
* Maintain blood group-wise stock
* Request blood based on blood group and required quantity
* Check available blood stock
* View donation records
* Menu-driven command-line interface

## Blood Groups Supported

The system supports the following blood groups:

* A+
* A-
* B+
* B-
* AB+
* AB-
* O+
* O-

## Technologies Used

* **Python**
* Object-Oriented Programming (OOP)
* Lists
* Dictionaries
* Classes and Objects
* Functions
* Loops
* Conditional Statements
* Command-Line Interface (CLI)

## Project Structure

```text
BloodBankManagement/
│
├── bloodbank.py
└── README.md
```

## How the System Works

The application provides a menu with the following operations:

```text
1. Add Donor
2. View Donors
3. Search Donor
4. Update Donor
5. Delete Donor
6. Donate Blood
7. Request Blood
8. View Blood Stock
9. View Donations
10. Exit
```

### Donor Management

Each donor is represented using a `Donor` class containing:

* Donor ID
* Name
* Age
* Blood Group
* Phone Number
* City

Donor records are stored in a Python list while the program is running.

### Blood Donation

When a registered donor donates blood:

* The donor's donation count is updated.
* The corresponding blood group's stock is increased by one packet.
* The donation is recorded using the donor ID.

### Blood Requests

Users can request a specific number of blood packets by entering a blood group.

The system checks the available stock before dispatching the requested quantity. If sufficient stock is unavailable, the request is rejected.

### Blood Stock

The system maintains blood stock using a Python dictionary, with the blood group as the key and the available number of packets as the value.

### Donation Records

The system maintains the number of donations made by each donor using their donor ID.

## How to Run

Make sure Python is installed on your system.

Run the program using:

```bash
python bloodbank.py
```

The program will display the Blood Bank Management menu in the terminal.

## Data Storage

This project **does not use a database or external data storage system**.

Donor information, blood stock, and donation records are stored in Python data structures while the program is running. The data will be lost when the program is closed.

## Purpose

This project was developed to practice Python programming and demonstrate the use of:

* Object-Oriented Programming
* Classes and Objects
* Lists and Dictionaries
* Functions
* Loops and Conditional Statements
* User Input Handling
* Menu-Driven Programming
* Basic Record Management
