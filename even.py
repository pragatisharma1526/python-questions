'''Question 1'''

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in original_list if num % 2 == 0]
print(even_numbers)




'''Question 4'''

string_list = ['apple', 'banana', 'cherry', 'date']
sorted_list = sorted(string_list, key=lambda x: len(x))
print(sorted_list)






'''Question 2'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


person1 = Person("Pragati Sharma", 20, "female")
print(person1)






'''Question 5'''
class Vehicle:
    def drive(self):
        print("Driving a vehicle.")

class Car(Vehicle):
    def drive(self):
        print("Driving a car.")

class Truck(Vehicle):
    def drive(self):
        print("Driving a truck.")

class Motorcycle(Vehicle):
    def drive(self):
        print("Riding a motorcycle.")

vehicle = Vehicle()
car = Car()
truck = Truck()
motorcycle = Motorcycle()

vehicle.drive()    
car.drive()        
truck.drive()      
motorcycle.drive() 


