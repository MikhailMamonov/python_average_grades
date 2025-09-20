class Student:
 
    def __init__(self, student_name, grades = []):
        if(not all(isinstance(grade, int) for grade in grades)):
            raise TypeError
        self.student_name = student_name    # имя студента
        self.grades = grades        # возраст человека

    def addGrade(self, grade):
        if type(grade) is not int:
            raise TypeError    
        self.grades.append(grade)

    def calculate_average(self):  
        if not self.grades:  
            return 0  
        return sum(self.grades) / len(self.grades)