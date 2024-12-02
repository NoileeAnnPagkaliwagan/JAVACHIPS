# Polymorphism (Method overriding)
class DentalPatient(Patient):
    def __init__(self, id_number, name, address, age, total_cost):
        super().__init__(id_number, name, address, age, total_cost)

    # Overriding the 'print_details' method
    def print_details(self):
        print(f"Name: {self.get_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Total Cost: ${self.get_total_cost():.2f}")
