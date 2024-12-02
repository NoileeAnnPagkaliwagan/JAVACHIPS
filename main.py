ito yung buo


import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Base class for Patient (Encapsulation and Data Hiding)
class Patient:
    def __init__(self, id_number, name, address, age, total_cost):
        self.__id_number = id_number
        self.__name = name
        self.__address = address
        self.__age = age
        self.__total_cost = total_cost

    # Getters
    def get_id_number(self):
        return self.__id_number
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_total_cost(self):
        return self.__total_cost

    # Setters
    def set_id_number(self, id_number):
        if isinstance(id_number, int) and id_number > 0:
            self.__id_number = id_number
        else:
            raise ValueError("ID number must be a positive integer")
    
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Name cannot be empty and must be a string")
    
    def set_address(self, address):
        self.__address = address
    
    def set_age(self, age):
        if isinstance(age, int) and 0 < age < 120:
            self.__age = age
        else:
            raise ValueError("Age must be a positive integer between 1 and 120")
    
    def set_total_cost(self, total_cost):
        if isinstance(total_cost, float) and total_cost >= 0:
            self.__total_cost = total_cost
        else:
            raise ValueError("Total cost must be a positive number")

# Inheriting from Patient to add a method for generating the PDF
class DentalPatient(Patient):
    def __init__(self, id_number, name, address, age, total_cost):
        super().__init__(id_number, name, address, age, total_cost)

    # Method to generate and save PDF receipt
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

# Function to handle the app functionality
class DentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dental Patient Receipt Generator")
        self.root.geometry("400x350")
        
        # Labels and Entry fields for user inputs
        self.label_id = tk.Label(root, text="ID Number:")
        self.label_id.pack(pady=5)
        self.entry_id = tk.Entry(root)
        self.entry_id.pack(pady=5)
        
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.pack(pady=5)
        self.entry_name = tk.Entry(root)
        self.entry_name.pack(pady=5)
        
        self.label_address = tk.Label(root, text="Address:")
        self.label_address.pack(pady=5)
        self.entry_address = tk.Entry(root)
        self.entry_address.pack(pady=5)
        
        self.label_age = tk.Label(root, text="Age:")
        self.label_age.pack(pady=5)
        self.entry_age = tk.Entry(root)
        self.entry_age.pack(pady=5)
        
        self.label_total_cost = tk.Label(root, text="Total Cost:")
        self.label_total_cost.pack(pady=5)
        self.entry_total_cost = tk.Entry(root)
        self.entry_total_cost.pack(pady=5)
        
        # Submit Button
        self.submit_button = tk.Button(root, text="Generate Receipt", command=self.generate_receipt)
        self.submit_button.pack(pady=20)
    
    def generate_receipt(self):
        try:
            # Get user input
            id_number = int(self.entry_id.get())
            name = self.entry_name.get()
            address = self.entry_address.get()
            age = int(self.entry_age.get())
            total_cost = float(self.entry_total_cost.get())

            # Create DentalPatient instance
            patient = DentalPatient(id_number, name, address, age, total_cost)

            # Generate PDF and show success message
            receipt_filename = patient.generate_pdf_receipt()
            messagebox.showinfo("Success", f"Receipt generated and saved as {receipt_filename}")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = DentalApp(root)
    root.mainloop()
