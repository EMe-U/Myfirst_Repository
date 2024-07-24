#!/usr/bin/env python3

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
            return self.GPA
        total_credits = sum(course['credits'] for course in self.courses_registered)
        total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
        self.GPA = total_points / total_credits if total_credits > 0 else 0.0
        return self.GPA

    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})


class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self):
        email = input("Enter student email: ")
        names = input("Enter student names: ")
        new_student = Student(email, names)
        self.student_list.append(new_student)
        print(f"Student {names} added successfully!")

    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = int(input("Enter course credits: "))
        new_course = Course(name, trimester, credits)
        self.course_list.append(new_course)
        print(f"Course {name} added successfully!")

    def register_student_for_course(self):
        student_email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        grade = float(input("Enter grade received: "))

        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)

        if student and course:
            student.register_for_course(course, grade)
            print(f"Student {student.names} registered for course {course.name} successfully!")
        else:
            print("Student or course not found!")

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()
            print(f"{student.names}'s GPA: {student.GPA:.2f}")

    def calculate_ranking(self):
        self.calculate_GPA()
        self.student_list.sort(key=lambda student: student.GPA, reverse=True)
        for student in self.student_list:
            print(f"Student Email: {student.email}, GPA: {student.GPA:.2f}")
        print("Ranking calculated successfully!")

    def search_by_grade(self):
        min_grade = float(input("Enter minimum grade: "))
        max_grade = float(input("Enter maximum grade: "))

        filtered_students = [student for student in self.student_list if min_grade <= student.GPA <= max_grade]
        for student in filtered_students:
            print(f"Student Email: {student.email}, GPA: {student.GPA:.2f}")
        print("Search by grade completed successfully!")

    def generate_transcript(self):
        for student in self.student_list:
            print(f"Transcript for {student.names} ({student.email}):")
            for course in student.courses_registered:
                print(f"Course: {course['course'].name}, Grade: {course['grade']}, Credits: {course['credits']}")
            print(f"GPA: {student.GPA:.2f}\n")
        print("Transcripts generated successfully!")


def main():
    grade_book = GradeBook()

    print("Welcome to the Gradebook Application")

    while True:
        print("\nGrade Book Menu:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for course")
        print("4. Calculate GPA")
        print("5. Calculate ranking")
        print("6. Search by grade")
        print("7. Generate transcript")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            grade_book.add_student()
        elif choice == '2':
            grade_book.add_course()
        elif choice == '3':
            grade_book.register_student_for_course()
        elif choice == '4':
            grade_book.calculate_GPA()
        elif choice == '5':
            grade_book.calculate_ranking()
        elif choice == '6':
            grade_book.search_by_grade()
        elif choice == '7':
            grade_book.generate_transcript()
        elif choice == '8':
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
