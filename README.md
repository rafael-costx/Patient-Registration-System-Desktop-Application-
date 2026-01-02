# Patient Registration System (Desktop Application)
This project is a Patient Registration System developed to simulate a basic hospital or clinic management environment. The application provides a simple and intuitive desktop interface that allows users to manage patient records efficiently, focusing on data organization, validation, and persistence.

The system was designed to demonstrate core concepts of desktop application development, database integration, and CRUD operations using Python.


## Features

- Add new patients with data validation
- Display a dynamic list of all registered patients
- Delete selected patient records safely
- Store data locally using a relational database
- User-friendly graphical interface
- Technologies Used
- Python – main programming language
- Tkinter – graphical user interface (GUI)
- SQLite – lightweight relational database
- SQL – database structure and queries
- CRUD operations – Create, Read, and Delete


## System Architecture and Processes

- Relational database schema creation and management
- Input validation to ensure data consistency
- Event-driven programming for GUI interactions
- Separation of application logic and interface components
- Local data persistence using SQLite


## Database Structure
The system uses a SQLite database with the following table:
- patients
- id (INTEGER, Primary Key, Auto Increment)
- name (TEXT, Not Null)
- age (INTEGER)
- phone (TEXT)
- case_description (TEXT)

## How to Run the Project
- Make sure Python 3 is installed on your system
- Clone this repository
- Navigate to the project directory
- Run the application:
- python sistema.py
- The database file (hospital.db) will be created automatically on the first run.


## Future Improvements
- Update and edit patient records
- User authentication and access control
- Search and filtering functionality
- Migration to a client-server architecture
- Improved UI design and usability


## Purpose of the Project

This project was created for learning and portfolio purposes, aiming to strengthen skills in Python, GUI development, and database integration. It serves as a solid foundation for more advanced healthcare management systems.
