class Student:
 
    def __init__(self, student_name, grades):
        self.student_name = student_name    # имя студента
        self.grades = grades        # возраст человека

    def addGrade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):  
        if not self.grades:  
            return 0  
        return sum(self.grades) / len(self.grades)  