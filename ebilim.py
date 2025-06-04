from collections import defaultdict
class Ebilim:
    def __init__(self):
        self.students = []

    def addStudent(self, name, surname, grade):
        student = Student(name, surname, grade)
        self.students.append(student)

    def putMark(self, student, subject, grade):
        for i in self.students:
            if i.name == student:
                i.add_grade(subject, grade)

    def get_marks(self, name):
        for i in self.students:
            if i.name == name:
                return i.see_grades()
            
    def get_average(self, student):
        for i in self.students:
            if i.name == student:
                return i.average()



class Student:
    def __init__(self, name, surname, grade):
        self.name = name 
        self.surname = surname
        self.grade = grade
        self.grades = defaultdict(list)
    

    def add_grade(self, subject, grade):
        self.grades[subject].append(grade)


    def see_grades(self):
        return dict(self.grades)
    
    def average(self):
        if not self.grades:  # Check if there are any grades
            return 0
            
        total_sum = 0
        total_count = 0
        
        # Calculate the average for each subject then the overall average
        for subject in self.grades:
            subject_grades = self.grades[subject]
            total_sum += sum(subject_grades)
            total_count += len(subject_grades)
        
        return total_sum / total_count

    

dnevnik = Ebilim()
dnevnik.addStudent("yntymak", "almazbek uulu", 5)
dnevnik.putMark("yntymak", "math", 5)
dnevnik.putMark("yntymak", "english", 4)
dnevnik.putMark("yntymak", "math",6)
print(dnevnik.get_marks("yntymak"))
print(dnevnik.get_average("yntymak"))





