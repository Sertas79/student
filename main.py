class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0

    def rete_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_teach):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calc_aver(self):
        result = []
        for value in self.grades.values():
            for i in value:
                result.append(i)
        if len(result) == 0:
            self.average_score = 0
        else:
            self.average_score = round(sum(result) / len(result), 1)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_score == other.average_score
        return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_score < other.average_score
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_score > other.average_score
        return False


    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задания: {self.average_score}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_teach = []
        self.grades = {}
        self.average_score = 0

    def calc_aver(self):
        result = []
        for value in self.grades.values():
            for i in value:
                result.append(i)
        if len(result) == 0:
            self.average_score = 0
        else:
            self.average_score = round(sum(result) / len(result), 1)

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score == other.average_score
        return False

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score < other.average_score
        return False

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_score > other.average_score
        return False

    def __str__(self):
        self.calc_aver()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_score}')


class Reviewer(Mentor):
    def rete_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')



# Reviewer
cool_reviewer = Reviewer('Some', 'Bobby')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

# Student
#first student
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
cool_reviewer.rete_hw(best_student, 'Python', 10)
cool_reviewer.rete_hw(best_student, 'Python', 5)
cool_reviewer.rete_hw(best_student, 'Python', 10)
best_student.calc_aver()
# second student
second_student = Student('Jack', 'Vorobei', 'your_gender')
second_student.finished_courses += ['SQL']
second_student.courses_in_progress += ['Git']
cool_reviewer.rete_hw(second_student, 'Git', 9)
cool_reviewer.rete_hw(second_student, 'Git', 5)
cool_reviewer.rete_hw(second_student, 'Git', 10)
second_student.calc_aver()
# comparison students
print(best_student == second_student)
print(best_student > second_student)
print(best_student < second_student)


# Lecturer
# first lecturer
cool_lecturer = Lecturer('Bill', 'Voland')
cool_lecturer.courses_teach += ['Python']
best_student.rete_hw(cool_lecturer, 'Python', 10)
best_student.rete_hw(cool_lecturer, 'Python', 9)
best_student.rete_hw(cool_lecturer, 'Python', 10)
#second lecturer
second_lecturer = Lecturer('Ivan', 'Ivanov')
second_lecturer.courses_teach += ['Git']
second_student.rete_hw(second_lecturer, 'Git', 6)
second_student.rete_hw(second_lecturer, 'Git', 9)
second_student.rete_hw(second_lecturer, 'Git', 7)
# comparison lecturer
print(cool_lecturer == second_lecturer)
print(cool_lecturer > second_lecturer)
print(cool_lecturer < second_lecturer)


def course_aver_student(other, course): # среднее по курсу для студентов

    for obj in other:
        if isinstance(obj, Student) and course in obj.courses_in_progress:
            return round(sum(obj.grades[course]) / len(obj.grades[course]),1)
        else:
            continue
    return 'Ошибка'

def course_aver_lecturer(other, course): # среднее по курсу для лекторов
    for obj in other:
        if isinstance(obj, Lecturer) and course in obj.courses_teach:
            return round(sum(obj.grades[course]) / len(obj.grades[course]),1)
        else:
            continue
    return 'Ошибка'

student_list = [best_student,second_student]
print(course_aver_student(student_list, 'Git'))

lecturer_list = [cool_lecturer,second_lecturer]
print(course_aver_lecturer(lecturer_list, 'Git'))