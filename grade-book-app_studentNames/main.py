#!usr/bin/python3

class Student:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.courses_registered = []
        self.grades = {}
        self.GPA = 0.0

    def register_for_course(self, course):
        self.courses_registered.append(course)

    def add_grade(self, course, grade):
        self.grades[course.name] = grade
        self.calculate_GPA()

    def calculate_GPA(self):
        if self.grades:
            total_points = sum(self.grades.values())
            self.GPA = total_points / len(self.grades)
        else:
            self.GPA = 0.0

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, name):
        student = Student(email, name)
        self.student_list.append(student)
        print(f"⭐ Student {name} added successfully! ⭐")
        return student

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        print(f"🌸 Course {name} added successfully! 🌸")
        return course

    def register_student_for_course(self, student, course):
        student.register_for_course(course)
        print(f"⭐ {student.name} registered for course {course.name} successfully! ⭐")

    def add_grade(self, student, course, grade):
        student.add_grade(course, grade)
        print(f"🌸 Grade {grade} added for {student.name} in course {course.name}! 🌸")

    def calculate_ranking(self):
        ranking = sorted(self.student_list, key=lambda s: s.GPA, reverse=True)
        print("⭐ Student Ranking by GPA ⭐")
        for idx, student in enumerate(ranking, 1):
            print(f"{idx}. {student.name} (GPA: {student.GPA:.2f})")
        return ranking

    def search_by_grade(self, grade):
        students_with_grade = [student for student in self.student_list if grade in student.grades.values()]
        print(f"🌸 Students with grade {grade}: 🌸")
        for student in students_with_grade:
            print(f"{student.name} ({student.email})")
        return students_with_grade

    def generate_transcript(self, student):
        transcript = f"⭐ Transcript for {student.name} ({student.email}): ⭐\n"
        for course_name, grade in student.grades.items():
            transcript += f"{course_name}: {grade}\n"
        transcript += f"GPA: {student.GPA:.2f}"
        print(transcript)
        return transcript

def display_menu():
    print("🌸" * 8 + " GRADEBOOK MANAGEMENT SYSTEM " + "🌸" * 8)
    print("1. ⭐ Add Student")
    print("2. 🌸 Add Course")
    print("3. ⭐ Register Student for Course")
    print("4. 🌸 Calculate GPA")
    print("5. ⭐ Calculate Ranking")
    print("6. 🌸 Search by Grade")
    print("7. ⭐ Generate Transcript")
    print("8. ❌ Exit")
    print("🌸" * 50)

def main():
    gradebook = GradeBook()

    while True:
        display_menu()
        action = input("Select an option (1-8): ").strip()

        if action == "1":
            email = input("Enter student email: ")
            name = input("Enter student name: ")
            gradebook.add_student(email, name)
        elif action == "2":
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        elif action == "3":
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            student = next((s for s in gradebook.student_list if s.email == email), None)
            course = next((c for c in gradebook.course_list if c.name == course_name), None)
            if student and course:
                gradebook.register_student_for_course(student, course)
            else:
                print("Student or course not found.")
        elif action == "4":
            email = input("Enter student email: ")
            student = next((s for s in gradebook.student_list if s.email == email), None)
            if student:
                student.calculate_GPA()
                print(f"{student.name}'s GPA is {student.GPA:.2f}")
            else:
                print("Student not found.")
        elif action == "5":
            gradebook.calculate_ranking()
        elif action == "6":
            grade = float(input("Enter grade to search for: "))
            gradebook.search_by_grade(grade)
        elif action == "7":
            email = input("Enter student email: ")
            student = next((s for s in gradebook.student_list if s.email == email), None)
            if student:
                gradebook.generate_transcript(student)
            else:
                print("Student not found.")
        elif action == "8":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

