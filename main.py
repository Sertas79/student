class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.finished_courses
                and course in lecturer.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def aver_grade(self):
        result = 0
        count = 0
        for key in self.grades:
            result += sum(self.grades[key])
            count += len(self.grades[key])
        return result / count


    def __str__(self):
        return(f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.aver_grade()}\n'
               f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {','.join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def aver_grade(self):
        result = 0
        count = 0
        for key in self.grades:
            result += sum(self.grades[key])
            count += len(self.grades[key])
        return result / count

    def __str__(self):
        return(f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}'
               f'Средняя оценка за лекции: {self.aver_grade()}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return(f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}')



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

very_bests_student = Student('Иван', 'Иванов', 'муж.')
very_bests_student.courses_in_progress += ['Фронтенд-разработчик. ЯндексПрактикум']
very_bests_student.finished_courses += ['Python-разработчик. ЯндексПрактикум']

reviewer = Reviewer('Аркадий ', 'Волож')
reviewer.courses_attached += ['Фронтенд-разработчик. ЯндексПрактикум']
reviewer.courses_attached += ['Python-разработчик. ЯндексПрактикум']

very_bad_reviewer = Reviewer('Лена', 'Головач')
very_bad_reviewer.courses_attached += ['Python']
very_bad_reviewer.courses_attached += ['Git']

reviewer.rate_hw(best_student, 'Фронтенд-разработчик. ЯндексПрактикум', 10)
reviewer.rate_hw(best_student, 'Python-разработчик. ЯндексПрактикум', 10)
very_bad_reviewer.rate_hw(best_student, 'Git', 10)
very_bad_reviewer.rate_hw(best_student, 'Git', 10)


print(best_student.courses_in_progress)
print(very_bests_student.courses_in_progress)


