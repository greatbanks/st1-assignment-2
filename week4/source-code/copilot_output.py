#!/usr/bin/env python3

# Simple Appointment Booking System

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    print("\nAppointments:")
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']}, "
            f"Practitioner: {appointment['practitioner']}, "
            f"Time: {appointment['time']}"
        )

# Sample data
#
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 11:30 AM')
book_appointment('Bob Johnson', 'Dr. John Doe', '2024-07-20 11:30 AM')

# Display all appointments
display_appointments()
