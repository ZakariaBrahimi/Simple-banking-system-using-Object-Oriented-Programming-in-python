# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_grade(self):
#         return self.grade

# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

# s1 = Student("zaki", 20, 99)
# s2 = Student("abdou", 23, 50)
# s3 = Student("ayoube", 14, 100)

# course = Course('Science', 2)
# course.add_student(s1)
# course.add_student(s2)
# # students = [("zaki", 20, 99), ("abdou", 23, 50)]
# print(course.students[1].age)

# # if __name__ == "__main__":
# #     x = 5
#     # help(x)


class test:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def test_method(self, grade):
        self.grade = grade
    
t1 = test("zaki", 20)
print(t1.test_method(50).grade)