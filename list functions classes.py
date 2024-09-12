# Author: Joshua Begley
# Teacher: Cindy N. Zhou
# Class: SDEV using python
# Date: 09/09/2024
# Assignment: m03

# this program asks for vehicle information from the user and displays it
# in a readable format for the user.

# Superclass: Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass: Automobile inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Method to display vehicle information
    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# Main application
def main():
    # Asking for vehicle type
    vehicle_type = input("Enter the vehicle type (car, truck, plane, boat, broomstick): ").lower()

    if vehicle_type == "car" "truck":
        year = input("Enter the year of the car: ")
        make = input("Enter the make of the car: ")
        model = input("Enter the model of the car: ")
        doors = input("Enter the number of doors (two or four): ").lower()
        roof = input("Enter the type of roof (solid or sunroof): ").lower()

        car = Automobile(vehicle_type, year, make, model, doors, roof)

        # Output the vehicle information
        print("\nCar Details:")
        car.display_info()
    else:
        print(f"Vehicle type '{vehicle_type}' is not handled in this program.")

# Run the application
if __name__ == "__main__":
    main()