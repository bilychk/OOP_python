class Flight:
    def __init__(self,name,passport,age):
        self.name = name
        self.passport = passport
        self.age = age
        self.passengers = []


    def add_passenger(self,name,passport,age):
        if self.name != str:
            print(f"Passenger name is written uncorrectly.")
        elif len.self.passport < 6:
            print(f"Passport number is too short.")
        elif self.age <= 0 or self.age >= 105:
            print(f"Age is uncorrect")
        
        self.passengers.append([name,passport,age])
        print(f"Passenger is succesfuly added to passengers list.")

    def remove_passenger(self,passport):

        number = input(print(f"Print here Passenger passport number you wish to delete from passengers list:"))
        for number in self.passengers:
            if number[1] == passport:
                self.passengers.remove(number)
                print(f"The {number} is deleted from passengers list.")
                return
            
        print(f"Number is not found.")

    def show_passengers(self):
        if len.self.passengers < 0:
            print(f"Passengers list is empty.")
        else:
            numb = 0
            many = len.self.passengers
            print(f"The number of passengers is {many}.")
            for name in self.name:
                print(f"Passenger {numb}: {name[0]}")
                numb += 1

