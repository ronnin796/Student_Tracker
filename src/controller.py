from re import search
from src.models import Student_Model
import src.student as student
from src.view import main_menu, get_student_details , search_student
from src.student import Student
class Controller:
    def __init__(self):
        self.model = Student_Model()
    def run(self):
        while True:
            ch = main_menu()
            match ch:
                case '1':
                        name, roll_number , marks = get_student_details()
                        student= Student(name, roll_number, marks)
                        self.model.add_students(student)
                        print("Student added successfully!")
                case '2':
                    name = search_student()
                    self.model.show_student_details(name)
                case '3':
                    self.model.save()
                    print("Students saved to file successfully!")
                case '4':
                    self.model.load()
                    print("Loaded students from file successfully!")    
                    
                case '5':
                    print("Exiting...")
                    break
                
                case _:
                    print("Invalid choice!")
        
if __name__ == "__main__":
    controller = Controller()
    controller.run()
#         controller.run()
        
