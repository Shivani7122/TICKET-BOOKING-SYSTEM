# Constants for the dimensions of the theater
ROWS = 5
SEATS_PER_ROW = 10

# Initialize the seats array with all seats available
seats = [[True for _ in range(SEATS_PER_ROW)] for _ in range(ROWS)]

# Function to display available seats
def display_seats():
    print("Available seats:")
    for row in range(ROWS):
        row_display = ""
        for seat in range(SEATS_PER_ROW):
            if seats[row][seat]:
                row_display += "O "  # O indicates available
            else:
                row_display += "X "  # X indicates booked
        print(f"Row {row + 1}: {row_display}")

# Function to book a seat
def book_seat(row_number, seat_number):
    if row_number < 1 or row_number > ROWS or seat_number < 1 or seat_number > SEATS_PER_ROW:
        print("Invalid seat number.")
        return

    if seats[row_number - 1][seat_number - 1]:
        seats[row_number - 1][seat_number - 1] = False
        print(f"Seat {seat_number} in Row {row_number} has been successfully booked.")
    else:
        print(f"Seat {seat_number} in Row {row_number} is already booked.")

# Function to cancel a booking
def cancel_booking(row_number, seat_number):
    if row_number < 1 or row_number > ROWS or seat_number < 1 or seat_number > SEATS_PER_ROW:
        print("Invalid seat number.")
        return

    if not seats[row_number - 1][seat_number - 1]:
        seats[row_number - 1][seat_number - 1] = True
        print(f"Seat {seat_number} in Row {row_number} has been successfully cancelled.")
    else:
        print(f"Seat {seat_number} in Row {row_number} is already available.")

# Main function to run the movie ticket booking system
def main():
    while True:
        print("\nMovie Ticket Booking System")
        print("1. Display available seats")
        print("2. Book a seat")
        print("3. Cancel a booking")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            display_seats()
        elif choice == 2:
            try:
                row_number = int(input("Enter row number to book: "))
                seat_number = int(input("Enter seat number to book: "))
                book_seat(row_number, seat_number)
            except ValueError:
                print("Invalid input. Please enter valid row and seat numbers.")
        elif choice == 3:
            try:
                row_number = int(input("Enter row number to cancel: "))
                seat_number = int(input("Enter seat number to cancel: "))
                cancel_booking(row_number, seat_number)
            except ValueError:
                print("Invalid input. Please enter valid row and seat numbers.")
        elif choice == 4:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main function
if __name__ == "__main__":
    main()
