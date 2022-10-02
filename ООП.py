class School:
    def average(self):
        overall_sum = 0
        overall_len = 0
        for el in self.grades.values():
            overall_sum += sum(el)
            overall_len += len(el)
        if (overall_len or overall_sum) == 0:
            return 0
        else:
            return overall_sum / overall_len

    def __lt__(self, other):
        if not isinstance(other, (Student,Lecturer)):
            return "В сравнении нет студентов или лекторов"    
        return self.average() < other.average()

    def __eq__(self, other):
        if not isinstance(other, (Student,Lecturer)):
            return "В сравнении нет студентов или лекторов"
        return self.average() == other.average()


class Student(School):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    

    def put_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in (self.courses_in_progress or self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


    def __str__(self):
        output = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n"
        return output


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    

class Lecturer(Mentor,School):
    def __str__(self):
        output = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}\n"
        return output
    
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    

    def __str__(self):
        output = f"Имя: {self.name}\nФамилия: {self.surname}\n"
        return output


def average_gr_student(students, course):
    amount_st_in_course = 0
    amount_gr = []
    for student in students:
        for el in student.grades:
            if el == course:
                amount_gr.append(*student.grades[el])
                amount_st_in_course += 1
    if amount_st_in_course == 0:
        return 0
    else: 
        return sum(amount_gr) / amount_st_in_course


def average_gr_lecturers(lecturers, course):
    amount_lec_in_course = 0
    amount_gr = []
    for lecturer in lecturers:
        for el in lecturer.grades:
            if el == course:
                amount_gr.append(*lecturer.grades[el])
                amount_lec_in_course += 1
    if amount_lec_in_course == 0:
        return 0
    else: 
        return sum(amount_gr) / amount_lec_in_course



peter = Student("David", "Mosunov", "male")
polya = Student("Polya", "Davidova", "female")
students_list = [peter,polya]
livsi = Lecturer("Kolos", "Livsi")
pontiph = Lecturer("Pontiphiy", "Pilatovich")
lecturers_list = [livsi, pontiph]
petrovich = Reviewer("Alex", "Petrovich")
ivan = Reviewer("Ivan", "Ivanov")
peter.add_courses("Введение в программирование") 
peter.add_courses("Git")
peter.courses_in_progress += ["Python"]
peter.courses_in_progress += ["C++"]
polya.courses_in_progress += ["Python"]
livsi.courses_attached += ["Python"]
livsi.courses_attached += ["C++"]
peter.put_grade(livsi,"Python",8)
peter.put_grade(livsi,"C++",10)
petrovich.courses_attached += ["Python"]
petrovich.courses_attached += ["С++"]
petrovich.rate_hw(peter, "Python", 9)
petrovich.rate_hw(polya, "Python", 8)
petrovich.rate_hw(peter, "С++", 10)
print(livsi.grades)
print(peter.grades)
print(livsi.average())
print(peter.average())
print(peter == livsi)
print(polya > livsi)
print(polya == livsi)
print(polya < livsi)
print()
print(peter)
print(polya)
print(livsi)
print(pontiph)
print(petrovich)
print(ivan)
print(average_gr_student(students_list, "Python"))
print(average_gr_lecturers(lecturers_list, "Python" ))
