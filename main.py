import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

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

# Inheriting from Patient to add a method for displaying patient details
class DentalPatient(Patient):
    def __init__(self, id_number, name, address, age, total_cost):
        super().__init__(id_number, name, address, age, total_cost)

    # Method to display patient details
    def display_patient_details(self):
        details = (
            f"Patient ID: {self.get_id_number()}\n"
            f"Name: {self.get_name()}\n"
            f"Address: {self.get_address()}\n"
            f"Age: {self.get_age()}\n"
            f"Total Cost: {self.get_total_cost():.2f}"
        )
        return details

# Function to handle the app functionality
class DentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dental Patient Receipt")
        
        # Set the background color of the main window to sky blue
        self.root.geometry("800x600")  # Width = 800px, Height = 600px
        self.root.configure(bg="sky blue")  # Background color set to sky blue
        
        # Labels and Entry fields for user inputs with adjusted padding and alignment
        self.label_id = tk.Label(root, text="ID Number:", font=("Helvetica", 12), bg="sky blue")
        self.label_id.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_id = tk.Entry(root, font=("Helvetica", 12))
        self.entry_id.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_name = tk.Label(root, text="Name:", font=("Helvetica", 12), bg="sky blue")
        self.label_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = tk.Entry(root, font=("Helvetica", 12))
        self.entry_name.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        self.label_address = tk.Label(root, text="Address:", font=("Helvetica", 12), bg="sky blue")
        self.label_address.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_address = tk.Entry(root, font=("Helvetica", 12))
        self.entry_address.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_age = tk.Label(root, text="Age:", font=("Helvetica", 12), bg="sky blue")
        self.label_age.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_age = tk.Entry(root, font=("Helvetica", 12))
        self.entry_age.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.label_total_cost = tk.Label(root, text="Total Cost:", font=("Helvetica", 12), bg="sky blue")
        self.label_total_cost.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_total_cost = tk.Entry(root, font=("Helvetica", 12))
        self.entry_total_cost.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Submit Button with smaller width and height
        self.submit_button = tk.Button(root, text="Generate Receipt", font=("Helvetica", 10), width=30, height=3, command=self.generate_receipt)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

        # Update Button with smaller width and height
        self.update_button = tk.Button(root, text="Update Patient Details", font=("Helvetica", 10), width=30, height=3, command=self.update_patient)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # Allow rows and columns to expand
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Create Treeview for the receipt
        self.treeview = ttk.Treeview(root, columns=("Information", "Value"), show="headings", height=10)
        self.treeview.grid(row=0, column=2, rowspan=6, pady=10, padx=20, sticky="nsew")

        # Define columns and set headings
        self.treeview.heading("Information", text="Information", anchor="w")
        self.treeview.heading("Value", text="Value", anchor="w")
        
        # Set column widths
        self.treeview.column("Information", width=150, anchor="w")
        self.treeview.column("Value", width=300, anchor="w")

        # Set column styles
        self.treeview.tag_configure("information", background="lightblue")
        self.treeview.tag_configure("value", background="white")

        self.current_patient = None  # Store the current patient instance

    def generate_receipt(self):
        try:
            # Get user input
            id_number = int(self.entry_id.get())
            name = self.entry_name.get()
            address = self.entry_address.get()
            age = int(self.entry_age.get())
            total_cost = float(self.entry_total_cost.get())

            # Create DentalPatient instance
            self.current_patient = DentalPatient(id_number, name, address, age, total_cost)

            # Get patient details
            patient_details = self.current_patient.display_patient_details()

            # Clear previous entries in the Treeview
            for row in self.treeview.get_children():
                self.treeview.delete(row)

            # Insert new data into the Treeview
            self.treeview.insert("", "end", values=("Patient ID", str(self.current_patient.get_id_number())), tags=("information", "value"))
            self.treeview.insert("", "end", values=("Name", self.current_patient.get_name()), tags=("information", "value"))
            self.treeview.insert("", "end", values=("Address", self.current_patient.get_address()), tags=("information", "value"))
            self.treeview.insert("", "end", values=("Age", str(self.current_patient.get_age())), tags=("information", "value"))
            self.treeview.insert("", "end", values=("Total Cost", f"${self.current_patient.get_total_cost():.2f}"), tags=("information", "value"))

            # Open the save dialog and save to the chosen file path
            self.save_to_file(patient_details)

        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def save_to_file(self, patient_details):
        # Ask the user for a file location using file dialog
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        
        if file_path:
            try:
                # Save the receipt to the file
                with open(file_path, "w") as file:
                    file.write(patient_details)
                messagebox.showinfo("Receipt Generated", f"Receipt saved to {file_path}")

            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {str(e)}")

    def update_patient(self):
        if self.current_patient:
            try:
                # Get updated user input
                self.current_patient.set_id_number(int(self.entry_id.get()))
                self.current_patient.set_name(self.entry_name.get())
                self.current_patient.set_address(self.entry_address.get())
                self.current_patient.set_age(int(self.entry_age.get()))
                self.current_patient.set_total_cost(float(self.entry_total_cost.get()))

                # Refresh the Treeview to show updated data
                self.generate_receipt()
                messagebox.showinfo("Patient Updated", "Patient details have been successfully updated.")
            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e))
        else:
            messagebox.showwarning("No Patient", "Please generate a receipt first before updating.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DentalApp(root)
    root.mainloop()
