class Flight:
    def __init__(self,flight_number,destination, max_passengers):
        self.flight_number = flight_number
        self.destination = destination
        self.max_passengers = max_passengers
        self.passengers = []




    def add_passenger(self,name,passport,age):
        if self.is_full():
            print(f"There is no available seats on this flight.")
        elif age < 0:
            print(f"Age can't be an negative number")
        else:
            for passenger in self.passengers:
                if passenger[1] == passport:
                    print(f"A passenger with this passport number is already registered.")
                    return
            
        
        self.passengers.append([name,passport,age])
        print(f"Passenger is succesfuly added to passengers list.")




    def remove_passenger(self,passport):
        for passenger in self.passengers:
            if passenger[1] == passport:
                self.passengers.remove(passenger)
                print(f"The {passenger} is deleted from passengers list.")
                return
            
        print(f"Number is not found.")




    def show_passengers(self):
        numb = 0
        many = len(self.passengers)
        print(f"The number of passengers is {many}.")
        for passenger in self.passengers:
            print(f"Passenger {numb}: {passenger[0]}, {passenger[1]}, {passenger[2]}")
            numb += 1




    def show_flight_info(self):
        many = len(self.passengers)
        print(f"Flight: {self.flight_number}")
        print(f"Destination: {self.destination}")
        print(f"Passengers: {many}/{self.max_passengers}")

    
    
    
    def find_passenger(self,passport):
        for passenger in self.passengers:
            if passenger[1] == passport:
                print(f"The passenger: {passenger[0]}, {passenger[1]}, {passenger[2]}")
                return
            
        print(f"Passenger is not found.")



    def count_adults(self):
        count = 0
        for passenger in self.passengers:
            if passenger[2] >= 18:
                count += 1
        return count
    


    def count_children(self):
        count = 0
        for passenger in self.passengers:
            if passenger[2] < 18:
                count += 1
        return count
    

    def is_full(self):
        return len(self.passengers) == self.max_passengers
    




flight = Flight("AZ101", "Istanbul", 5)
flight.show_flight_info()


flight.add_passenger("Anna", "A123", 23)
flight.add_passenger("Mark", "B456", 17)
flight.add_passenger("Kate", "C789", 30)
flight.add_passenger("John", "D111", 12)

flight.show_passengers()

flight.find_passenger("B456")
flight.find_passenger("X999")

print(flight.count_adults())
print(flight.count_children())

flight.remove_passenger("C789")

flight.show_flight_info()
flight.show_passengers()