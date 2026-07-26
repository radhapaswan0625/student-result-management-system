class Student:
    def __init__(self, name, roll, english, math, science):
        self.name = name
        self.roll = roll
        self.english = english
        self.math = math
        self.science = science

    def calculate_total(self):
        total = self.english+self.math+self.science
        return total 

    def calculate_percentage(self):
        total = self.calculate_total()
        percentage = total/3
        return percentage
    
    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B+"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        else:
            return "F"
    def display_student(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("english:", self.english)
        print("math:", self.math)
        print("science:", self.science)
        print("Total:", self.calculate_total())
        print("Percentage:", self.calculate_percentage())
        print("Grade:", self.calculate_grade())

    def to_dict(self): 
        return{
            "name": self.name, 
            "roll": self.roll,
            "english": self.english, 
            "math": self.math,
            "science": self.science

        }    


