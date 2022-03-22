import math


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    # выставляем оценку лектору
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    #подсчёт средней оценки для студента
    def mid_grade1(self): 
        new = []
        for i in self.grades.values():
            new.append(sum(i) / len(i))
        mid_grades = round(sum(new) / len(new), 1)
        return mid_grades
    
    # средний бал
    def mid_grade(self):
        new = []
        if len(self.grades.values()) < 1:
            return f'{self.name} {self.surname} has no ratings.'
        else:
            for i in self.grades.values():
                new += i
            mid_grades = round(sum(new) / len(new), 1)
            return mid_grades
    
    # список студентов         
    def add_in_lis(self):
        lis_student = []
        if isinstance(self, Student):
            lis_student.append(self)
        else:
            return 'invalid class'
            
    # выводим информацию про студента
    def __str__(self):
          return(f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние работы: {self.mid_grade()} \n Курсы в процессе изучения: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses}')
       


class Mentor:
    def __init__(self, name, surname, courses_attached=[]):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached
    def __str__(self, name, surname):
          return(f'Имя: {name} \n Фамилия: {surname} \n ')
        


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)
        self.grades = {}
    
    # средняя оценка лектора
    def mid_grade(self):
        new = []
        if len(self.grades.values()) < 1:
            return f'{self.name} {self.surname} has no ratings.'
        else:
            for i in self.grades.values():
                new += i
            mid_grades = round(sum(new) / len(new), 1)
            return mid_grades      
    
    # список лекторов
    def add_in_lis(self):
        lis_lectur = []
        if isinstance(self, Lecturer):
            lis_lectur.append(self)
        else:
            return 'invalid class'
    def __str__(self):
        return(f'Имя: {self.name} \n Фамилия {self.surname} \n Средняя оценка за лекции: {self.mid_grade}')    
        
class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)       
    
    # выставляем оценку студенту
    def rate_hw(self, student, course, grade):
        print('raiting')
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    # вывод информации о проверяющем
    def __str__(self, name, surname):
      return(f'Имя: {name} \n Фамилия: {surname} \n ')

# сравниваем успеваемость студентов
def perform_comparison(person1, person2): 
    if isinstance(person1, Student) and isinstance(person2, Student):
        if person1.mid_grade() > person2.mid_grade():
            return f'Успеваемость студента {person1.name} лучше. Средний бал {person1.mid_grade()}'
        else:
            return f'Успеваемость студента {person2.name} лучше. Средний бал {person2.mid_grade()}'
    else:
        return 'Ошибка'
# вопросы по доработке: 
# Как сделать сравнение успевамости, если студентов больше чем двое? Тоже самое про лекторов. 
# Прописать вызов всех функций    
student_1 = Student('Ivan', 'Petrov', 'M')
student_1.courses_in_progress = ['Python', 'SQL']
student_1.finished_courses = ['Pascal', 'Basic']
print(student_1)

student_2 = Student('Vasili', 'Nikolaev', 'M')
student_2.courses_in_progress = ['Python', 'SQL']
student_2.finished_courses = ['Pascal', 'Basic']

student_3 = Student('Alexandr', 'Sidorov', 'M')
student_3.courses_in_progress = ['Python', 'SQL']
student_3.finished_courses = ['Pascal', 'Basic']

lecturer_1 = Lecturer('Nikolai', 'Bragin', ['Python', 'Basic'])
lecturer_2 = Lecturer('Olga', 'Krupskaya', ['Python', 'SQL'])

reviewer_2 = Reviewer('Voroshilov', 'Stepan', ['SQL', 'Basic'])
reviewer_1 = Reviewer('Svetlana', 'Makarova', ['Python', 'Basic',])
print('student_1 before rating:', student_1.grades)
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_2.rate_hw(student_1, 'SQL', 5)
reviewer_2.rate_hw(student_3, 'SQL', 3)
reviewer_2.rate_hw(student_2, 'Basic', 3)

print('student_1 after rating:', student_1.grades)
print('student_2 after rating:', student_2.grades)
print('student_3 after rating:', student_3.grades)

student_1.rate_lecturer(lecturer_1, 'Python', 4)
student_1.rate_lecturer(lecturer_1, 'Python', 5)
student_1.rate_lecturer(lecturer_2, 'Python', 3)
student_1.rate_lecturer(lecturer_2, 'SQL', 2)

print('lecturer_1 after rating:', lecturer_1.grades)
print('lecturer_2 after rating:', lecturer_2.grades)

print(student_1.mid_grade())
print(lecturer_1.mid_grade())

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_reviewer = Reviewer('Some', 'Buddy', [])
# print(cool_reviewer)
# cool_reviewer.courses_attached += ['Python']
# cool_reviewer.rate_hw(best_student, 'Python', 10)
# # cool_reviewer.rate_hw(best_student, 'Python', 10)
# # cool_reviewer.rate_hw(best_student, 'Python', 10)
# # print(best_student.grades)
