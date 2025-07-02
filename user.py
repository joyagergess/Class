class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def get_info(self):
        return f"Name: {self.__name}, Email: {self.__email}"

    def set_email(self, new_email):
        self.__email = new_email


class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__enrolled_courses = []

    def enroll(self, course_name):
        self.__enrolled_courses.append(course_name)

    def get_enrolled_courses(self):
        return self.__enrolled_courses

