

class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name 
        self.age = age
        self.myCourses = {}

    def enroll_in_class(self, class_id):
            if class_id not in self.myCourses:
                self.myCourses[class_id] = []
                print(f"successfully added {class_id}")
            else:
                return "You are alreadr enrolled"
        

    def list_classes(self):
            return [i for i in self.myCourses]
        
    def add_grade(self, class_id, grade):
            if class_id in self.myCourses:
                self.myCourses[class_id].append(grade)


    def get_average_grade(self):
        sm = 0
        count = 0
        for i, j in self.myCourses.items():
            if j:
                sm+= sum(j)
                count += len(j)
        if count == 0:
             return 0
        return f'You age is: {sm / count}'
    

    def set_student(self, new_data):
        self.name = new_data.name
        self.age = new_data.age

    



class Class:
    def __init__(self, class_id, name, instructor):
        self.class_id = class_id
        self.name = name 
        self.instructor = instructor
        self.StudentsId = {}

    
    def list_students(self):
        return [i for i in self.StudentsId]
    

    def add_student(self, student_id):
        if student_id not in self.StudentsId:
            self.StudentsId[student_id] = []
            return f'{student_id} was added successsfully to{self.name}'

    
    def add_grade(self, student_id, grade):
        self.StudentsId[student_id].append(grade)
        return f'{grade} was added to {student_id} successfully'

    def get_name(self):
        return self.name 
    
    def set_class(self, new_data):
        self.name = new_data.name
        self.instructor = new_data.instructor

    
    def get_average(self):
        sm = 0
        count = 0
        for _, value in self.StudentsId.items():
            sm+=sum(value)
            count+=len(value)
        return sm/count
   


class SalymbekovUniversity:
    def __init__(self):
       self.allStudents = []
       self.allClasses = []
    
    def add_student(self, student):
        if student not in self.allStudents:
            self.allStudents.append(student)

    def add_class(self, university_class):
        if university_class not in self.allClasses:
            self.allClasses.append(university_class)


    def enroll_student(self, student_id, class_id):
        for student in self.allStudents:
            if student.student_id == student_id:
                for cla in self.allClasses:
                    if cla.class_id == class_id:
                        student.enroll_in_class(class_id)
                        cla.add_student(student_id)
            
    def search_student(self, student_id):
        for student in self.allStudents:
            if student.student_id == student_id:
                return f'{student.student_id}, {student.name}, {student.age}'
            

    def search(self, student_id):
        for classs in self.allClasses:
            if classs.class_id == student_id:
                return classs.class_id, classs.name, classs.instructor
            
    
    
    def update_student(self, student_id, new_data):
        for student in self.allStudents:
            if student.student_id == student_id:
                student.set_student(new_data)

    
    def update_class(self, class_id, new_data):
        for classs in self.allClasses:
            if classs.class_id == class_id:
                classs.set_class(new_data)

    
    def total_students(self):
        return len(self.allStudents)
    
    def total_classes(self):
        return len(self.allClasses)
    

    def students_in_class(self, class_id):
        for clas in self.allClasses:
            if clas.class_id == class_id:
                return clas.list_students()
            
    
    def classes_for_student(self, student_id):
        for student in self.allStudents:
            if student.student_id == student_id:
                return student.list_classes()
            
    
    def average_grade_for_student(self, student_id):
        for student in self.allStudents:
            if student.student_id == student_id:
                return student.get_average_grade()

    def average_grade_for_class(self, class_id):
        for clss in self.allClasses:
            if clss.class_id == class_id:
                return clss.get_average()


