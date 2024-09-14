# instituto/clase.py

from student import get_matters_by_student_name

def student_registered_in_matter(name: str, matter: str) -> bool:
    try:
        matters = get_matters_by_student_name(name)
        return matter in matters
    except KeyError as e:
        return False
