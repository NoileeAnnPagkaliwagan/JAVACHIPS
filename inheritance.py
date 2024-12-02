# Inheritance (DentalPatient inherits from Patient)
class DentalPatient(Patient):
    def __init__(self, id_number, name, address, age, total_cost):
        super().__init__(id_number, name, address, age, total_cost)  # Inherit from Patient class

    # Additional method to generate PDF receipt
    def generate_pdf_receipt(self):
        filename = f"patient_{self.get_id_number()}_receipt.pdf"
        # Code to generate PDF receipt (using reportlab library)
        print(f"PDF receipt generated and saved as {filename}")
