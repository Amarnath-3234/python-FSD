# for i in range(10):
#     print("hello good morning")


#i=1
#while i <=10:
    #print("hello good morning")
    #i+=1
#############function#####################
#def greet():
   # print("hello teacher")
    #print("welcome to python class")
#greet()



###############function with parameters#####################
# def add(a,b):
#     result = a+b
#     print(result)
# add(10,20)
# add(50,30)

#################list####################

# student = ["amba","kiran","pavan","rrrr","priya"]
# print(student)

# student.append("sai")
# print(student)
# student.remove("kiran")
# print(student)
# student.insert(1,"kiran")
# print(student)

################tuple####################
# student_details = ("pavan", 22, 89,90.7, True)

# print(student_details) 

##################dictionary####################
 
# student = {
#     "name": "pavan",
#     "age": 22,
#     "marks": 89,
#     "USN": 31,  
#     "college": "sri chaitanya"
# }
# student["course"] = "python"
# student["marks"] = 90
# print(student["name"], student["age"], student["USN"], student["college"])
# print(student["course"])
# print(student["marks"])

########################oops####################

# class Student:
#     def display(self):
#         print("hello teacher")
#         print("welcome to python class")

# s1 = Student()
# s1.display()

###################constructor####################
# class Student:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print("name:", self.name)
#         print("age:", self.age)
#         print("marks:", self.marks)

# s1 = Student("pavan",22,89)
# s2 = Student("kiran",23,45)
# s1.display()
# s2.display() 

####################encapsulation####################

# class student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         self.__marks = marks

#     def show_marks(self):
#         print("student marks:", self.__marks)

# s1 = student()
# s1.set_marks(89)
# s1.show_marks()

#####################inheritance####################
 

# class father:
#     def house(self):
#         print("father has a house")

# class son(father):   
#     def car(self):
#         print("son has a car")

# class daughter(father):
#     def bike(self):
#         print("daughter has a bike")

# s = son()
# d = daughter()
# s.house()
# s.car()
# d.house()
# d.bike()

###########################abstract class####################

# from abc import ABC, abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class upi(payment):
#     def pay(self, amount):
#         print(f"paid {amount} using UPI")

# class card(payment):
#     def pay(self, amount):
#         print(f"paid {amount} using card")

# p1 = upi()
# p2 = card()
# p1.pay(1000)
# p2.pay(2000)