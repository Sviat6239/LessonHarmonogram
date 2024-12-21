from django.core.management.base import BaseCommand
from LessonHarmonogram.core.models import Subject, Teacher, Class, Student, Schedule, Grade


class Command(BaseCommand):
    help = 'Manage school data'

    def handle(self, *args, **kwargs):
        while True:
            print("\n--- School Management System ---")
            print("1. Add Subject")
            print("2. Add Teacher")
            print("3. Add Class")
            print("4. Add Student")
            print("5. Add Schedule")
            print("6. Add Grade")
            print("0. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                self.add_subject()
            elif choice == '2':
                self.add_teacher()
            elif choice == '3':
                self.add_class()
            elif choice == '4':
                self.add_student()
            elif choice == '5':
                self.add_schedule()
            elif choice == '6':
                self.add_grade()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Try again.")

    def add_subject(self):
        name = input("Enter subject name: ")
        description = input("Enter subject description: ")

        if Subject.objects.filter(name=name).exists():
            print("Subject already exists.")
        else:
            Subject.objects.create(name=name, description=description)
            print("Subject added successfully.")

    def add_teacher(self):
        first_name = input("Enter teacher's first name: ")
        last_name = input("Enter teacher's last name: ")
        subject_name = input("Enter subject name: ")

        try:
            subject = Subject.objects.get(name=subject_name)
            Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)
            print("Teacher added successfully.")
        except Subject.DoesNotExist:
            print("Subject does not exist. Add the subject first.")

    def add_class(self):
        name = input("Enter class name: ")
        year = input("Enter class year: ")

        if Class.objects.filter(name=name, year=year).exists():
            print("Class already exists.")
        else:
            Class.objects.create(name=name, year=year)
            print("Class added successfully.")

    def add_student(self):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        class_name = input("Enter class name: ")

        try:
            student_class = Class.objects.get(name=class_name)
            Student.objects.create(first_name=first_name, last_name=last_name, student_class=student_class)
            print("Student added successfully.")
        except Class.DoesNotExist:
            print("Class does not exist. Add the class first.")

    def add_schedule(self):
        day = input("Enter day of week (MON/TUE/WED/THU/FRI): ")
        start_time = input("Enter start time (HH:MM): ")
        subject_name = input("Enter subject name: ")
        class_name = input("Enter class name: ")
        teacher_name = input("Enter teacher's name: ")

        try:
            subject = Subject.objects.get(name=subject_name)
            student_class = Class.objects.get(name=class_name)
            teacher = Teacher.objects.get(first_name=teacher_name.split()[0], last_name=teacher_name.split()[1])
            Schedule.objects.create(day_of_week=day, start_time=start_time, subject=subject, class_assigned=student_class, teacher=teacher)
            print("Schedule added successfully.")
        except (Subject.DoesNotExist, Class.DoesNotExist, Teacher.DoesNotExist):
            print("Invalid data. Make sure all related entities exist.")

    def add_grade(self):
        student_name = input("Enter student's name: ")
        subject_name = input("Enter subject name: ")
        grade = input("Enter grade: ")
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            student = Student.objects.get(first_name=student_name.split()[0], last_name=student_name.split()[1])
            subject = Subject.objects.get(name=subject_name)
            Grade.objects.create(student=student, subject=subject, grade=grade, date=date)
            print("Grade added successfully.")
        except (Student.DoesNotExist, Subject.DoesNotExist):
            print("Invalid data. Make sure all related entities exist.")
