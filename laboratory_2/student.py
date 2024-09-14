# instituto/estudiante.py

# Dictionary students matters.
student_matters = {
    "Daniel": ["Math", "Computing"],
    "Maria": ["Math", "Physics"],
    "Jonnathan": ["TICs", "Physics", "Computing"],
}

def get_matters_by_student_name(name: str):
    try:
        return student_matters[name]
    except KeyError:
        raise KeyError(f"The student  {name} not found.")
