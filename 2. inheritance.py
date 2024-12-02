# Inheriting from Patient to add a method for generating the PDF
class DentalPatient(Patient):
    def __init__(self, id_number, name, address, age, total_cost):
        # Call the constructor of the base class
        super().__init__(id_number, name, address, age, total_cost)

    # Method to generate and save PDF receipt (Polymorphism in action)
    def generate_pdf_receipt(self):
        filename = f"patient_{self.get_id_number()}_receipt.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        
        # Receipt details
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, f"Patient ID: {self.get_id_number()}")
        c.drawString(100, 730, f"Name: {self.get_name()}")
        c.drawString(100, 710, f"Address: {self.get_address()}")
        c.drawString(100, 690, f"Age: {self.get_age()}")
        c.drawString(100, 670, f"Total Cost: ${self.get_total_cost():.2f}")
        
        c.save()
        print(f"PDF receipt saved as {filename}")
        return filename

explanation
Inheritance is used to create a subclass (DentalPatient) from the base class (Patient). 
The subclass inherits the attributes and methods of the parent class and can also add new functionality.
