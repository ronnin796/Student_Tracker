import src.view as v
from src.models import Student_Model as sm

model = sm
model.load()
model.show_all_students()