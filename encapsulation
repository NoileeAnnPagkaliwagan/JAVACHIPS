# Encapsulation (Private attributes with getters and setters)
class Patient:
    def __init__(self, id_number, name, address, age, total_cost):
        self.__id_number = id_number  # Private attribute
        self.__name = name            # Private attribute
        self.__address = address      # Private attribute
        self.__age = age              # Private attribute
        self.__total_cost = total_cost # Private attribute

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
