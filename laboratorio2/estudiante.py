# instituto/estudiante.py

from typing import List, Dict

# Diccionario de estudiantes y materias
estudiantes_materias: Dict[str, List[str]] = {
    "Daniel": ["Matematica", "Computacion"],
    "Maria": ["Matematica", "Fisica"],
}

def devolver_materias(nombre: str) -> List[str]:
    """Devuelve la lista de materias de un estudiante.

    Args:
        nombre (str): Nombre del estudiante.

    Returns:
        List[str]: Lista de materias en las que está inscrito el estudiante.

    Raises:
        KeyError: Si el estudiante no está en el diccionario.
    """
    try:
        return estudiantes_materias[nombre]
    except KeyError:
        raise KeyError(f"El estudiante {nombre} no está registrado.")
