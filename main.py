import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import ttk
import json  #json module

# Class for Patient (Encapsulation and Data Hiding)
class Patient:
    def __init__(self, id_number, name, address, age, total_cost):
        self.__id_number = id_number
        self.__name = name
        self.__address = address
        self.__age = age
        self.__total_cost = total_cost

    # GETTERS
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

    # SETTERS
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

# INHERITANCE
class DentalPatient(Patient):
    def __init__(self, id_number, name, address, age, total_cost):
        super().__init__(id_number, name, address, age, total_cost)

# POLYMORPHISM
    def display_patient_details(self):
        details = (
            f"Patient ID: {self.get_id_number()}\n"
            f"Name: {self.get_name()}\n"
            f"Address: {self.get_address()}\n"
            f"Age: {self.get_age()}\n"
            f"Total Cost: {self.get_total_cost():.2f}"
        )
        return details

# FUNCTION AND DESIGN
class DentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dental Patient Receipt")
        self.root.geometry("800x650")  
        self.root.configure(bg="sky blue") 
        
        # Label and entry fields
        self.label_id = tk.Label(root, text="ID Number:", font=("Helvetica", 12), bg="sky blue")
        self.label_id.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_id = tk.Entry(root, font=("Helvetica", 12), width=30)  
        self.entry_id.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_name = tk.Label(root, text="Name:", font=("Helvetica", 12), bg="sky blue")
        self.label_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = tk.Entry(root, font=("Helvetica", 12), width=30)  
        self.entry_name.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        self.label_address = tk.Label(root, text="Address:", font=("Helvetica", 12), bg="sky blue")
        self.label_address.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_address = tk.Entry(root, font=("Helvetica", 12), width=30)  
        self.entry_address.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_age = tk.Label(root, text="Age:", font=("Helvetica", 12), bg="sky blue")
        self.label_age.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_age = tk.Entry(root, font=("Helvetica", 12), width=30)  
        self.entry_age.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.label_cost = tk.Label(root, text="Total Cost:", font=("Helvetica", 12), bg="sky blue")
        self.label_cost.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_cost = tk.Entry(root, font=("Helvetica", 12), width=30)  
        self.entry_cost.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Buttons for saving, updating, and generating receipt
        self.button_save = tk.Button(root, text="Save Patient", command=self.save_patient, font=("Helvetica", 12))
        self.button_save.grid(row=5, column=0, columnspan=2, pady=20)

        self.button_generate_receipt = tk.Button(root, text="Generate Receipt", command=self.generate_receipt, font=("Helvetica", 12))
        self.button_generate_receipt.grid(row=5, column=2, padx=10, pady=10)  

        self.button_update = tk.Button(root, text="Update Patient", command=self.update_patient, font=("Helvetica", 12))
        self.button_update.grid(row=6, column=0, columnspan=2, pady=20)

        # Table (Treeview) for displaying patient data
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Address", "Age", "Total Cost"), show="headings", height=10)
        self.tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
        
        # headings and column widths
        self.tree.heading("ID", text="ID Number")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Total Cost", text="Total Cost")
        
        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Name", width=150)
        self.tree.column("Address", width=200)
        self.tree.column("Age", width=50, anchor="center")
        self.tree.column("Total Cost", width=100, anchor="e")

        self.patients = []  # List patient objects

    def save_patient(self):
        try:
            id_number = int(self.entry_id.get())
            name = self.entry_name.get()
            address = self.entry_address.get()
            age = int(self.entry_age.get())
            total_cost = float(self.entry_cost.get())

            patient = DentalPatient(id_number, name, address, age, total_cost)
            self.patients.append(patient)

            self.save_to_json()  # the function to save data to JSON
            self.refresh_table()  # Refresh the table to show the new data
            messagebox.showinfo("Success", "Patient data saved successfully!")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def save_to_json(self):
        # Convert patient data to a list
        patients_data = [
            {
                "id_number": patient.get_id_number(),
                "name": patient.get_name(),
                "address": patient.get_address(),
                "age": patient.get_age(),
                "total_cost": patient.get_total_cost()
            }
            for patient in self.patients
        ]

        # Write the data to patients.json
        with open("patients.json", "w") as json_file:
            json.dump(patients_data, json_file, indent=4)

    def update_patient(self):
        try:
            patient_id = int(self.entry_id.get())
            patient_to_update = None
            for patient in self.patients:
                if patient.get_id_number() == patient_id:
                    patient_to_update = patient
                    break
            
            if patient_to_update:
                # Ask for new values for all fields
                new_id = simpledialog.askinteger("Update ID", "Enter new ID:", initialvalue=patient_to_update.get_id_number())
                new_name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=patient_to_update.get_name())
                new_address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=patient_to_update.get_address())
                new_age = simpledialog.askinteger("Update Age", "Enter new age:", minvalue=1, maxvalue=120, initialvalue=patient_to_update.get_age())
                new_total_cost = simpledialog.askfloat("Update Cost", "Enter new total cost:", initialvalue=patient_to_update.get_total_cost())

                # Update the patient information
                patient_to_update.set_id_number(new_id)
                patient_to_update.set_name(new_name)
                patient_to_update.set_address(new_address)
                patient_to_update.set_age(new_age)
                patient_to_update.set_total_cost(new_total_cost)

                self.save_to_json()  # Update the JSON file
                self.refresh_table()  # Refresh the table to show updated data
                messagebox.showinfo("Success", "Patient data updated successfully!")
            else:
                messagebox.showerror("Error", "Patient ID not found.")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def refresh_table(self):
        # Clear existing data in the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Add patients to the table
        for patient in self.patients:
            self.tree.insert("", "end", values=(
                patient.get_id_number(),
                patient.get_name(),
                patient.get_address(),
                patient.get_age(),
                f"{patient.get_total_cost():.2f}"
            ))

    def generate_receipt(self):
        # Get the selected patient
        selected_item = self.tree.focus()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            patient_id = values[0]
            name = values[1]
            address = values[2]
            age = values[3]
            total_cost = values[4]

            # Generate receipt content
            receipt_text = (
                f"--- Dental Patient Receipt ---\n"
                f"Patient ID: {patient_id}\n"
                f"Name: {name}\n"
                f"Address: {address}\n"
                f"Age: {age}\n"
                f"Total Cost: {total_cost}\n"
                f"----------------------------\n"
                f"Thank you"
            )

            # Open file dialog to choose where to save the receipt
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(receipt_text)
                messagebox.showinfo("Success", f"Receipt saved at {file_path}")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = DentalApp(root)
    root.mainloop()
