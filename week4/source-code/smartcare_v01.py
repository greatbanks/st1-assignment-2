import sys # emacs will hang if I don't include this when using .sys functions, leaving here for debugging

# Declare active_booking as empty string, while loop populates it with input, append it to a list for storing bookings
active_booking: string = ""
previous_bookings = []

# Booking inputs for user to fill
patient_name: string = input("Enter the patient's name: ")
gp_name: string = input("Enter the name of the GP the patient will see: ")
booking_time: string = input("Enter the time of the booking [Format: DD-MM-YY HH:MM]: ")

# Typecast all inputs to strings
patient_name = str(patient_name)
gp_name = str(gp_name)
booking_time = str(booking_time)

# Formatted display for the user to confirm the booking
print(f"Patient: {patient_name} | GP: {gp_name} | Booking time: {booking_time}")

# Storing the booking as a variable
active_booking: string = patient_name + "," + gp_name + "," + booking_time

# Appending the active booking to the end of the list
previous_bookings.append(active_booking)

# Displaying all the currently stored bookings
for booking in previous_bookings:
    print(booking)
