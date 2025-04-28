def main_menu():
    print("1. Add Student")
    print("2. Show Student Details")
    print("3. Save Students to File")
    print("4. Load Students from File")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice
def get_student_details():
    name = input("Enter student name:")
    roll_no = input("Enter student roll number:")
    marks={}
    while True:
        subject = input("Enter subject name (or 'done' to finish):")
        if subject.lower()=="done":
            break
        mark = input(f"Enter marks for {subject}:")
        marks[subject] = mark
    return name, roll_no, marks

def search_student():
    name = input("Name of student to show:")
    return name
