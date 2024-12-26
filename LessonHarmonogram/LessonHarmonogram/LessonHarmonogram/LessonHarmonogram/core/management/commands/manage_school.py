import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LessonHarmonogram.settings')
django.setup()

from django.core.management.base import BaseCommand
from datetime import datetime
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
                confirm_exit = input("Are you sure you want to exit? (yes/no): ").strip().lower()
                if confirm_exit == 'yes':
                    break
            else:
                print("Invalid choice. Try again.")

    def add_subject(self):
        name = input("Enter subject name: ").strip()
        description = input("Enter subject description: ").strip()

        if Subject.objects.filter(name=name).exists():
            print("Subject already exists.")
        else:
            Subject.objects.create(name=name, description=description)
            print("Subject added successfully.")

    def add_teacher(self):
        first_name = input("Enter teacher's first name: ").strip()
        last_name = input("Enter teacher's last name: ").strip()
        subject_name = input("Enter subject name: ").strip()

        try:
            subject = Subject.objects.get(name=subject_name)
            Teacher.objects.create(first_name=first_name, last_name=last_name, subject=subject)
            print("Teacher added successfully.")
        except Subject.DoesNotExist:
            print("Subject does not exist. Add the subject first.")

    def add_class(self):
        name = input("Enter class name: ").strip()
        year = input("Enter class year: ").strip()

        if Class.objects.filter(name=name, year=year).exists():
            print("Class already exists.")
        else:
            Class.objects.create(name=name, year=year)
            print("Class added successfully.")

    def add_student(self):
        first_name = input("Enter student's first name: ").strip()
        last_name = input("Enter student's last name: ").strip()
        class_name = input("Enter class name: ").strip()

        try:
            student_class = Class.objects.get(name=class_name)
            Student.objects.create(first_name=first_name, last_name=last_name, student_class=student_class)
            print("Student added successfully.")
        except Class.DoesNotExist:
            print("Class does not exist. Add the class first.")

    def add_schedule(self):
        day = input("Enter day of week (MON/TUE/WED/THU/FRI): ").strip().upper()
        start_time = input("Enter start time (HH:MM): ").strip()
        subject_name = input("Enter subject name: ").strip()
        class_name = input("Enter class name: ").strip()
        teacher_name = input("Enter teacher's name (First Last): ").strip()

        try:
            subject = Subject.objects.get(name=subject_name)
            student_class = Class.objects.get(name=class_name)
            teacher_first, teacher_last = teacher_name.split()
            teacher = Teacher.objects.get(first_name=teacher_first, last_name=teacher_last)
            Schedule.objects.create(day_of_week=day, start_time=start_time, subject=subject, class_assigned=student_class, teacher=teacher)
            print("Schedule added successfully.")
        except Subject.DoesNotExist:
            print("Subject does not exist.")
        except Class.DoesNotExist:
            print("Class does not exist.")
        except Teacher.DoesNotExist:
            print("Teacher does not exist.")
        except ValueError:
            print("Invalid teacher name format. Use 'First Last'.")

    def add_grade(self):
        student_name = input("Enter student's name (First Last): ").strip()
        subject_name = input("Enter subject name: ").strip()
        grade = input("Enter grade: ").strip()
        date_input = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            student_first, student_last = student_name.split()
            student = Student.objects.get(first_name=student_first, last_name=student_last)
            subject = Subject.objects.get(name=subject_name)
            date = datetime.strptime(date_input, '%Y-%m-%d').date()
            Grade.objects.create(student=student, subject=subject, grade=grade, date=date)
            print("Grade added successfully.")
        except Student.DoesNotExist:
            print("Student does not exist.")
        except Subject.DoesNotExist:
            print("Subject does not exist.")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
